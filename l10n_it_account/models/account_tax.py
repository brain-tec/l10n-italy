# -*- coding: utf-8 -*-
# Copyright 2017 Agile Business Group (<http://www.agilebg.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class AccountTax(models.Model):
    _inherit = 'account.tax'

    cee_type = fields.Selection([
        ('sale', 'Sale'),
        ('purchase', 'Purchase')
    ], string='Include in VAT register',
        help="Use in the case of tax with 'VAT integration'. This "
             "specifies the VAT register (sales / purchases) where the "
             "tax must be computed.")
    parent_tax_ids = fields.Many2many(
        'account.tax', 'account_tax_filiation_rel', 'child_tax', 'parent_tax',
        string='Parent Taxes')

    def _get_tax_amount(self):
        self.ensure_one()
        res = 0.0
        if self.amount_type == 'group':
            for child in self.children_tax_ids:
                res += child.amount
        else:
            res = self.amount
        return res

    def _get_tax_name(self):
        self.ensure_one()
        name = self.name
        # [antoniov: 2019-07-29]
        # if self.parent_tax_ids and len(self.parent_tax_ids) == 1:
        #     name = self.parent_tax_ids[0].name
        return name

    def _compute_totals_tax(self, data):
        """
        Args:
            data: date range, journals and registry_type
        Returns:
            A tuple: (tax_name, base, tax, deductible, undeductible)

        """
        self.ensure_one()
        context = {
            'from_date': data['from_date'],
            'to_date': data['to_date'],
        }
        registry_type = data.get('registry_type', 'customer')
        if data.get('journal_ids'):
            context['vat_registry_journal_ids'] = data['journal_ids']

        tax = self.env['account.tax'].with_context(context).browse(self.id)
        if 'payability' in tax and tax.payability == 'S':
            deferred_vat = False
            split_payment = True
        elif 'payability' in tax and tax.payability == 'D':
            deferred_vat = True
            split_payment = False
        else:
            deferred_vat = False
            split_payment = False
        tax_name = tax._get_tax_name()
        deductible = 0
        undeductible = 0
        if tax.parent_tax_ids:
            return (tax_name, 0, 0, 0, 0)
        elif not tax.children_tax_ids:
            base_balance = tax.base_balance
            deductible = tax_balance = tax.balance
            if base_balance >= 0 and tax_balance < 0:
                base_balance = 0
            if tax.nature_id.code == 'N6':
                undeductible = tax_balance
                deductible = 0
            if registry_type == 'supplier':
                return (tax_name, -base_balance,
                        -tax_balance, -deductible, -undeductible)
            if split_payment and registry_type == 'customer':
                return (tax_name, base_balance,
                        tax_balance, 0, tax_balance)
            return (tax_name, base_balance,
                    tax_balance, deductible, undeductible)
        else:
            base_balance = tax.base_balance

            tax_balance = 0
            for child in tax.children_tax_ids:
                child_balance = child.balance
                if (
                    (
                        registry_type == 'customer' and
                        child.cee_type == 'sale'
                    ) or
                    (
                        registry_type == 'supplier' and
                        child.cee_type == 'purchase'
                    )
                ):
                    # Prendo la parte di competenza di ogni registro e lo
                    # sommo sempre
                    child_balance = child_balance

                elif child.cee_type:
                    continue

                tax_balance += child_balance
                if child.account_id:
                    deductible += child_balance
                else:
                    undeductible += child_balance
            if base_balance >= 0 and tax_balance < 0:
                base_balance = 0
            if tax.nature_id.code == 'N6':
                undeductible = tax_balance
                deductible = 0
            if registry_type == 'supplier':
                return (tax_name, -base_balance,
                        -tax_balance, -deductible, -undeductible)
            if split_payment and registry_type == 'customer':
                return (tax_name, base_balance,
                    tax_balance, undeductible, deductible)
            return (tax_name, base_balance,
                    tax_balance, deductible, undeductible)
