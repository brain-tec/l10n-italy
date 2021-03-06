# -*- coding: utf-8 -*-
#
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2011-2012 Domsense s.r.l. (<http://www.domsense.com>).
#    Copyright (C) 2012 Agile Business Group sagl (<http://www.agilebg.com>)
#    Copyright (C) 2015 Associazione OpenERP Italia
#    (<http://www.openerp-italia.org>).
#    Copyright (C) 2015 Openforce di Alessandro Camilli
#    Copyright (C) 2015 Link It S.p.a. (<http://www.linkgroup.it/>)
#    <http://www.openforce.it>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#

import time
from openerp.osv import orm
from openerp.report import report_sxw
from openerp.tools.translate import _


class Report(orm.Model):
    _inherit = "report"


class VatPeriodEndStatementReport(report_sxw.rml_parse):
    _name = 'report.vat.period.end.statement'

    def __init__(self, cr, uid, name, context=None):
        if context is None:
            context = {}
        super(VatPeriodEndStatementReport, self).__init__(
            cr, uid, name, context=context)
        self.query = ""
        self.tot_currency = 0.0
        self.period_sql = ""
        self.sold_accounts = {}
        self.sortby = 'sort_date'
        self.localcontext.update({
            'time': time,
            'statement': self._get_statement,
            'tax_codes_amounts': self._get_tax_codes_amounts,
            'account_vat_amounts': self._get_account_vat_amounts,
            'l10n_it_count_fiscal_page_base': self._get_fiscal_page_base,
        })
        self.context = context

    def _get_statement(self, statement_id):
        statement_obj = self.pool['account.vat.period.end.statement']
        statement = False
        if statement_id:
            statement = statement_obj.browse(
                self.cr, self.uid, statement_id, self.context)
        return statement

    def _get_fiscal_page_base(self, statement_id):
        statement_obj = self.pool['account.vat.period.end.statement']
        statement = False
        if statement_id:
            statement = statement_obj.browse(
                self.cr, self.uid, statement_id, self.context)
        return statement.fiscal_page_base

    def _get_tax_codes_amounts(self, period_id, tax_code_ids=None,
                               context=None):
        code_pool = self.pool.get('account.tax.code')
        return code_pool._get_tax_codes_amounts(
            self.cr, self.uid, period_id, tax_code_ids, context)

    def _get_account_vat_amounts(
        self, type='credit', statement_account_line=None, context=None
    ):
        if context is None:
            context = {}
        if statement_account_line is None:
            statement_account_line = []
        if type != 'credit' and type != 'debit':
            raise orm.except_orm(
                _('Error'), _('Type account neither credit and debit !'))

        account_amounts = {}
        for line in statement_account_line:
            account_id = line.account_id.id
            if account_id not in account_amounts:
                account_amounts[account_id] = {
                    'account_id': line.account_id.id,
                    'account_name': line.account_id.name,
                    'amount': line.amount
                }
            else:
                account_amounts[account_id]['amount'] += line.amount
        return account_amounts


class ReportVatPeriodEndStatement(orm.AbstractModel):
    _name = ('report.account_vat_period_end_statement.'
             'report_vatperiodendstatement')
    _inherit = 'report.abstract_report'
    _template = 'account_vat_period_end_statement.report_vatperiodendstatement'
    _wrapped_report_class = VatPeriodEndStatementReport
