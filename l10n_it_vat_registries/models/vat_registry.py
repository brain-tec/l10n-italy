# -*- coding: utf-8 -*-
# Copyright 2016-2017 Lorenzo Battistini - Agile Business Group
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models
from odoo.tools.misc import formatLang
from odoo.tools.translate import _
from odoo.exceptions import Warning as UserError

import time


class ReportRegistroIva(models.AbstractModel):
    _name = 'report.l10n_it_vat_registries.report_registro_iva'

    @api.model
    def render_html(self, docids, data=None):
        # docids required by caller but not used
        # see addons/account/report/account_balance.py

        date_format = data['form']['date_format']

        docargs = {
            'doc_ids': data['ids'],
            'doc_model': self.env['account.move'],
            'data': data['form'],
            'docs': self.env['account.move'].browse(data['ids']),
            'get_move': self._get_move,
            'tax_lines': self._get_tax_lines,
            'format_date': self._format_date,
            'from_date': self._format_date(
                data['form']['from_date'], date_format),
            'to_date': self._format_date(
                data['form']['to_date'], date_format),
            'registry_type': data['form']['registry_type'],
            'invoice_total': self._get_move_total,
            'tax_registry_name': data['form']['tax_registry_name'],
            'env': self.env,
            'formatLang': formatLang,
            'compute_totals_tax': self._compute_totals_tax,
            'l10n_it_count_fiscal_page_base': data['form']['fiscal_page_base'],
            'only_totals': data['form']['only_totals'],
            'date_format': date_format
        }

        return self.env['report'].render(
            'l10n_it_vat_registries.report_registro_iva', docargs)

    def _get_move(self, move_ids):
        move_list = self.env['account.move'].browse(move_ids)
        return move_list

    def _format_date(self, my_date, date_format):
        formatted_date = time.strftime(date_format,
                                       time.strptime(my_date, '%Y-%m-%d'))
        return formatted_date or ''

    def _get_invoice_from_move(self, move):
        return self.env['account.invoice'].search([
            ('move_id', '=', move.id)])

    def _get_move_line(self, move, data):
        return [move_line for move_line in move.line_ids]

    def _tax_amounts_by_tax_id(self, move, move_lines, registry_type,
                               split_payment=None):

        def _parse_tax(tax, move_line, registry_type, res):
            set_cee_absolute_value = False
            tax_id = tax.id
            if not move_line.tax_line_id and \
                    tax.parent_tax_ids and \
                    len(tax.parent_tax_ids) == 1:
                # we group by main tax
                tax = tax.parent_tax_ids[0]
            if tax.exclude_from_registries:
                return 0.0, tax.id, tax.exclude_from_registries
            if ((registry_type == 'customer' and tax.cee_type == 'sale') or
                (registry_type == 'supplier' and
                    tax.cee_type == 'purchase')):
                set_cee_absolute_value = True
            elif tax.cee_type:
                return 0.0, tax.id, tax.exclude_from_registries
            tax_amount = move_line.debit - move_line.credit
            if set_cee_absolute_value:
                tax_amount = abs(tax_amount)
            if 'receivable' in move.move_type:
                tax_amount = -tax_amount
            return tax_amount, tax_id, tax.exclude_from_registries

        res = {}
        split_payment = split_payment or {}
        if split_payment:
            res[split_payment['sp_tax_id'].id] = {
                'name': split_payment['sp_tax_id'].name,
                'base': 0,
                'tax': 0,
            }

        for move_line in move_lines:
            if not(move_line.tax_line_id or move_line.tax_ids):
                continue
            if move_line.tax_line_id:
                tax = move_line.tax_line_id
                tax_amount, tax_id, exclude = _parse_tax(tax,
                                                         move_line,
                                                         registry_type,
                                                         res)
                if exclude:
                    continue
                if tax_id not in res:
                    res[tax.id] = {
                        'name': tax.name,
                        'base': 0,
                        'tax': 0,
                    }
                res[tax.id]['tax'] += tax_amount
                if split_payment:
                    res[split_payment['sp_tax_id'].id]['tax'] -= tax_amount
            else:
                is_base = True
                for move_line_tax in (move_line.tax_ids):
                    tax = move_line_tax
                    tax_amount, tax_id, exclude = _parse_tax(tax,
                                                             move_line,
                                                             registry_type,
                                                             res)
                    if exclude:
                        continue
                    if tax_id not in res:
                        res[tax.id] = {
                            'name': tax.name,
                            'base': 0,
                            'tax': 0,
                        }
                    if is_base:
                        res[tax.id]['base'] += tax_amount
                        is_base = False
        return res

    def _get_tax_lines(self, move, data):
        """
        Args:
            move: the account.move representing the invoice

        Returns:
            A tuple of lists: (INVOICE_TAXES, TAXES_USED)
            where INVOICE_TAXES is a list of dict
            and TAXES_USED a recordset of account.tax

        """
        inv_taxes = []
        used_taxes = self.env['account.tax']

        # index è usato per non ripetere la stampa dei dati fattura quando ci
        # sono più codici IVA
        index = 0
        invoice = self._get_invoice_from_move(move)
        if 'refund' in invoice.type:
            invoice_type = "NC"
        else:
            invoice_type = "FT"
        if (invoice.fiscal_position_id and
                invoice.fiscal_position_id.split_payment):
            if not invoice.company_id.sp_account_id:
                raise UserError(
                    _("Please set 'Split Payment Write-off Account' field in"
                      " accounting configuration"))
            if not invoice.company_id.sp_tax_id:
                raise UserError(
                    _("Please set 'Split Payment Write-off Tax' field in"
                      " accounting configuration"))
            split_payment_params = {
                'sp_account_id': invoice.company_id.sp_account_id,
                'sp_tax_id': invoice.company_id.sp_tax_id,
            }
        else:
            split_payment_params = {}

        move_lines = self._get_move_line(move, data)

        amounts_by_tax_id = self._tax_amounts_by_tax_id(
            move,
            move_lines,
            data['registry_type'],
            split_payment=split_payment_params)

        for tax_id in amounts_by_tax_id:
            tax = self.env['account.tax'].browse(tax_id)
            tax_item = {
                # 'tax_code_name': tax._get_tax_name(),
                'tax_code_name': amounts_by_tax_id[tax_id]['name'],
                'base': amounts_by_tax_id[tax_id]['base'],
                'tax': amounts_by_tax_id[tax_id]['tax'],
                'index': index,
                'invoice_type': invoice_type,
                'invoice_date': (
                    invoice and invoice.date_invoice or move.date or ''),
                'reference': (
                    invoice and invoice.reference or ''),
            }
            inv_taxes.append(tax_item)
            index += 1
            used_taxes |= tax

        return inv_taxes, used_taxes

    def _get_move_total(self, move):
        total = 0.0
        receivable_payable_found = False
        for move_line in move.line_ids:
            if move_line.account_id.internal_type == 'receivable':
                total += move_line.debit or (- move_line.credit)
                receivable_payable_found = True
            elif move_line.account_id.internal_type == 'payable':
                total += (- move_line.debit) or move_line.credit
                receivable_payable_found = True
        if receivable_payable_found:
            total = abs(total)
        else:
            total = abs(move.amount)
        if 'refund' in move.move_type:
            total = -total
        return total

    def _compute_totals_tax(self, tax, data):
        """
        Returns:
            A tuple: (tax_name, base, tax, deductible, undeductible)

        """
        return tax._compute_totals_tax(data)
