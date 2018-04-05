# -*- coding: utf-8 -*-
#
# Copyright 2008, Borja López Soilán <borja@kami.es> - (Pexego)
# Copyright 2008, ACYSOS S.L. (http://acysos.com)
#                 Pedro Tarrafeta <pedro@acysos.com>
# Copyright 2009, Zikzakmedia S.L. (http://zikzakmedia.com)
#                 Jordi Esteve <jesteve@zikzakmedia.com>
# Copyright 2011-2018, Associazione Odoo Italia <https://odoo-italia.org>
# Copyright 2012, Domsense srl (<http://www.domsense.com>)
# Copyright 2012, Agile Business Group sagl (<http://www.agilebg.com>)
# Copyright 2014-2018, Odoo Community Association (OCA)
# Copyright 2017-2018, Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
"""
Fiscal Year Closing
"""
import pdb

from datetime import datetime

from openerp.tools.translate import _

from openerp import netsvc
from openerp.osv import fields, orm, osv


# -------------------------------------------------------------------------
# Predeclaration of the FYC object
# -------------------------------------------------------------------------
class FiscalYearClosingInit(orm.Model):
    """
    Fiscal Year Closing Wizard
    """

    _name = "account_fiscal_year_closing.fyc"
    _description = "Fiscal Year Closing Wizard"

    _columns = {
        'name': fields.char('Description', size=60, required=True),
    }


FiscalYearClosingInit()


# -------------------------------------------------------------------------
# Account mapping objects (to be used on the fyc configuration)
# -------------------------------------------------------------------------
class FiscalYearClosingLpAccountMapping(orm.Model):
    """
    Loss & Profit Account Mapping
    """

    _name = "account_fiscal_year_closing.fyc_lp_account_map"
    _description = "SFYC Loss & Profit Account Mapping"

    _columns = {
        'name': fields.char('Description', size=60, required=False),

        # Parent eoy
        'fyc_id': fields.many2one(
            'account_fiscal_year_closing.fyc', 'Fiscal Year Closing',
            ondelete='cascade', required=True, select=1),

        # Accounts
        'source_account_id': fields.many2one(
            'account.account', 'Source account', required=True,
            ondelete='cascade'),
        'dest_account_id': fields.many2one(
            'account.account', 'Dest account', required=False,
            ondelete='cascade'),
    }


FiscalYearClosingLpAccountMapping()


class FiscalYearClosingNlpAccountMapping(orm.Model):
    """
    Net Loss & Profit Account Mapping
    """

    _name = "account_fiscal_year_closing.fyc_nlp_account_map"
    _description = "SFYC Net Loss & Profit Account Mapping"

    _columns = {
        'name': fields.char('Description', size=60, required=False),

        # Parent eoy
        'fyc_id': fields.many2one(
            'account_fiscal_year_closing.fyc', 'Fiscal Year Closing',
            ondelete='cascade', required=True, select=1),

        # Accounts
        'source_account_id': fields.many2one(
            'account.account', 'Source account', required=True,
            ondelete='cascade'),
        'dest_account_id': fields.many2one(
            'account.account', 'Dest account', required=False,
            ondelete='cascade'),
    }


FiscalYearClosingNlpAccountMapping()


class FiscalYearClosingCAccountMapping(orm.Model):
    """
    Closing Account Mapping
    """

    _name = "account_fiscal_year_closing.fyc_c_account_map"
    _description = "SFYC Closing Account Mapping"

    _columns = {
        'name': fields.char('Description', size=60, required=False),

        # Parent eoy
        'fyc_id': fields.many2one(
            'account_fiscal_year_closing.fyc', 'Fiscal Year Closing',
            ondelete='cascade', required=True, select=1),

        # Accounts
        'source_account_id': fields.many2one(
            'account.account', 'Account', required=True, ondelete='cascade'),
        'dest_account_id': fields.many2one(
            'account.account', 'Dest account', ondelete='cascade'),
    }


FiscalYearClosingCAccountMapping()

# -----------------------------------------------------------------------------
# Fiscal Year Closing Wizard
# -------------------------------------------------------------------------


class FiscalYearClosing(orm.Model):
    """
    Fiscal Year Closing Wizard
    """

    _inherit = "account_fiscal_year_closing.fyc"

    #
    # Fields ------------------------------------------------------------------
    #

    _columns = {
        # Company
        'company_id': fields.many2one(
            'res.company', 'Company', ondelete='cascade', readonly=True,
            required=True),

        # Fiscal years
        'closing_fiscalyear_id': fields.many2one(
            'account.fiscalyear', 'Fiscal year to close', required=True,
            ondelete='cascade', select=1),
        'opening_fiscalyear_id': fields.many2one(
            'account.fiscalyear', 'Fiscal year to open', required=True,
            ondelete='cascade', select=2),

        #
        # Operations (to do), and their account moves (when done)
        #
        'create_loss_and_profit': fields.boolean('Create Loss & Profit move'),
        'loss_and_profit_move_id': fields.many2one(
            'account.move', 'L&P Move', ondelete='set null', readonly=True),
        'create_net_loss_and_profit': fields.boolean(
            'Create Net Loss & Profit'),
        'net_loss_and_profit_move_id': fields.many2one(
            'account.move', 'Net L&P Move', ondelete='set null',
            readonly=True),
        'create_closing': fields.boolean('Close fiscal year'),
        'closing_move_id': fields.many2one(
            'account.move', 'Closing Move', ondelete='set null',
            readonly=True),
        'create_opening': fields.boolean('Open next fiscal year'),
        'opening_move_id': fields.many2one(
            'account.move', 'Opening Move', ondelete='set null',
            readonly=True),

        #
        # Extra operations
        #
        'check_invalid_period_moves': fields.boolean(
            'Check invalid period or date moves',
            help="Checks that there are no moves, on the fiscal year that is "
                 "being closed, with dates or periods outside that fiscal "
                 "year."),
        'check_draft_moves': fields.boolean(
            'Check draft moves',
            help="Checks that there are no draft moves on the fiscal year that"
                 " is being closed. Non-confirmed moves won't be taken in "
                 "account on the closing operations."),
        'check_unbalanced_moves': fields.boolean(
            'Check unbalanced moves',
            help="Checks that there are no unbalanced moves on the fiscal year"
                 " that is being closed."),

        # State
        'state': fields.selection([
                                  ('new', 'New'),
                                  ('draft', 'Draft'),
                                  ('in_progress', 'In Progress'),
                                  ('done', 'Done'),
                                  ('canceled', 'Canceled'),
                                  ], 'Status'),

        #
        # Loss and Profit options
        #
        'lp_description': fields.char('Description', size=60),
        'lp_journal_id': fields.many2one('account.journal', 'Journal'),
        'lp_period_id': fields.many2one('account.period', 'Period'),
        'lp_date': fields.date('Date'),
        'lp_account_mapping_ids': fields.one2many(
            'account_fiscal_year_closing.fyc_lp_account_map', 'fyc_id',
            'Account mappings'),

        #
        # Net Loss and Profit options
        #
        'nlp_description': fields.char('Description', size=60),
        'nlp_journal_id': fields.many2one('account.journal', 'Journal'),
        'nlp_period_id': fields.many2one('account.period', 'Period'),
        'nlp_date': fields.date('Date'),
        'nlp_account_mapping_ids': fields.one2many(
            'account_fiscal_year_closing.fyc_nlp_account_map', 'fyc_id',
            'Account mappings'),

        #
        # Closing options
        #
        'c_description': fields.char('Description', size=60),
        'c_journal_id': fields.many2one('account.journal', 'Journal'),
        'c_period_id': fields.many2one('account.period', 'Period'),
        'c_date': fields.date('Date'),
        'c_account_mapping_ids': fields.one2many(
            'account_fiscal_year_closing.fyc_c_account_map', 'fyc_id',
            'Accounts'),

        #
        # Opening options
        #
        'o_description': fields.char('Description', size=60),
        'o_journal_id': fields.many2one('account.journal', 'Journal'),
        'o_period_id': fields.many2one('account.period', 'Period'),
        'o_date': fields.date('Date'),
    }

    #
    # Default values ----------------------------------------------------------
    #
    def _get_last_date(self, cr, uid, context=None, company_id=None):
        fyc_ids = self.pool.get(
            'account.fiscalyear').search(
                cr, uid, [('company_id', '=', company_id)])
        str_date = '%s-06-01' % (datetime.now().year - 1)
        if fyc_ids:
            date_last = False
            for fyc_id in fyc_ids:
                fyc = self.pool.get('account.fiscalyear').browse(
                    cr, uid, fyc_id, context=context)
                if fyc.date_stop:
                    if not date_last or fyc.date_stop > date_last:
                        date_last = fyc.date_stop
            if date_last:
                str_date = date_last
        return str_date

    def _get_closing_fiscalyear_id(self, cr, uid,
                                   context=None, company_id=None):
        """
        Gets the last (previous) fiscal year
        """
        if not company_id:
            company_id = self.pool.get('res.users').browse(
                cr, uid, uid, context=context).company_id.id
        str_date = self._get_last_date(cr, uid, context=context,
                                       company_id=company_id)
        fiscalyear_ids = self.pool.get('account.fiscalyear').search(cr, uid, [
            ('company_id', '=', company_id),
            ('date_start', '<=', str_date),
            ('date_stop', '>=', str_date),
        ])
        if not fiscalyear_ids:
            fiscalyear_ids = self.pool.get('account.fiscalyear').search(
                cr, uid, [
                    ('company_id', '=', False),
                    ('date_start', '<=', str_date),
                    ('date_stop', '>=', str_date),
                ])
        return fiscalyear_ids and fiscalyear_ids[0]

    def _get_opening_fiscalyear_id(self, cr, uid,
                                   context=None, company_id=None):
        """
        Gets the current fiscal year
        """
        if not company_id:
            company_id = self.pool.get('res.users').browse(
                cr, uid, uid, context=context).company_id.id
        str_date = self._get_last_date(cr, uid, context=context,
                                       company_id=company_id)
        fiscalyear_ids = self.pool.get('account.fiscalyear').search(cr, uid, [
            ('company_id', '=', company_id),
            ('date_start', '<=', str_date),
            ('date_stop', '>=', str_date),
        ])
        if not fiscalyear_ids:
            fiscalyear_ids = self.pool.get('account.fiscalyear').search(
                cr, uid, [
                    ('company_id', '=', False),
                    ('date_start', '<=', str_date),
                    ('date_stop', '>=', str_date),
                ])
        return fiscalyear_ids and fiscalyear_ids[0]

    _defaults = {
        # Current company by default:
        'company_id': lambda self, cr, uid, context: self.pool.get(
            'res.users').browse(cr, uid, uid, context=context).company_id.id,

        # Draft state by default:
        'state': lambda *a: 'new',

        # Name
        'name': lambda self, cr, uid, context: _(
            "%s Fiscal Year Closing") % (datetime.now().year - 1),

        # Fiscal years
        'closing_fiscalyear_id': _get_closing_fiscalyear_id,
        'opening_fiscalyear_id': _get_opening_fiscalyear_id,
    }

    #
    # Workflow actions --------------------------------------------------------
    #

    def _get_journal_id(self, cr, uid, fyc, context=None, des=None):
        """
        Gets the journal to use.
        (It will search for a 'OPEJ' or 'General' journal)
        """
        assert fyc.company_id, "A company should have been selected"
        jcode = {
            'Loss & Profit': 'OLPJ',
            'Net Loss & Profit': 'OCLJ',
            'Fiscal Year Closing': 'OPCJ',
            'Fiscal Year Opening': 'OPEJ',
        }
        if des and des in jcode:
            codes = [jcode[des], 'OPEJ', 'MISC']
        else:
            codes = ['OPEJ', 'MISC']
        for code in codes:
            journal_ids = self.pool.get('account.journal').search(cr, uid, [
                ('company_id', '=', fyc.company_id.id),
                ('code', '=', code),
            ])
            if not journal_ids:
                journal_ids = self.pool.get(
                    'account.journal').search(
                        cr, uid, [('company_id', '=', False),
                                  ('code', '=', code), ]
                    )
            if journal_ids:
                break
        return journal_ids and journal_ids[0]

    def _get_lp_period_id(self, cr, uid, fyc, context=None):
        """
        Gets the period for the L&P entry
        (It searches for a "PG%" special period on the previous fiscal year)
        """
        period_ids = self.pool.get('account.period').search(cr, uid, [
            ('fiscalyear_id', '=',
             fyc.closing_fiscalyear_id.id),
            ('special', '=', True),
            ('date_start', '>=',
             fyc.closing_fiscalyear_id.date_stop),
            ('date_stop', '<=',
             fyc.closing_fiscalyear_id.date_stop),
        ])
        return period_ids and period_ids[0]

    def _get_c_period_id(self, cr, uid, fyc, context=None):
        """
        Gets the period for the Closing entry
        (It searches for a "C%" special period on the previous fiscal year)
        """
        period_ids = self.pool.get('account.period').search(cr, uid, [
            ('fiscalyear_id', '=',
             fyc.closing_fiscalyear_id.id),
            ('special', '=', True),
            ('date_start', '>=',
             fyc.closing_fiscalyear_id.date_stop),
            ('date_stop', '<=',
             fyc.closing_fiscalyear_id.date_stop),
        ])
        return period_ids and period_ids[0]

    def _get_o_period_id(self, cr, uid, fyc, context=None):
        """
        Gets the period for the Opening entry
        (It searches for a "A%" special period on the previous fiscal year)
        """
        period_ids = self.pool.get('account.period').search(cr, uid, [
            ('fiscalyear_id', '=',
             fyc.opening_fiscalyear_id.id),
            ('special', '=', True),
            ('date_start', '>=',
             fyc.opening_fiscalyear_id.date_start),
            ('date_stop', '<=',
             fyc.opening_fiscalyear_id.date_start),
        ])
        return period_ids and period_ids[0]

    def _get_account_mappings(self, cr, uid, fyc, mapping, context=None):
        """
        Transforms the mapping dictionary on a list of mapping lines.
        """
        account_mappings = []
        for source, dest, description in mapping:
            #
            # Find the source account
            #
            account_ids = self.pool.get('account.account').search(cr, uid, [
                ('company_id', '=', fyc.company_id.id),
                ('code', '=like', source),
            ])
            source_account_id = account_ids and account_ids[0] or None

            #
            # Find the dest account
            #
            account_ids = self.pool.get('account.account').search(cr, uid, [
                ('company_id', '=', fyc.company_id.id),
                ('code', '=like', dest),
                ('type', '!=', 'view'),
            ])
            dest_account_id = account_ids and account_ids[0] or None

            #
            # Use a default description if not provided
            #
            if not description:
                if source_account_id:
                    description = self.pool.get('account.account').read(
                        cr, uid, source_account_id, ['name'])['name']

            #
            # If the mapping is valid for this chart of accounts
            #
            if source_account_id:
                #
                # Make sure that the dest account is valid
                #
                if dest_account_id:
                    # Add the line to the result
                    account_mappings.append({
                        'name': description,
                        'source_account_id': source_account_id,
                        'dest_account_id': dest_account_id,
                    })
                else:
                    # Add the line to the result
                    account_mappings.append({
                        'name':
                            _(
                                'No destination account %s found for account '
                                '%s.'
                            ) % (dest, source),
                        'source_account_id': source_account_id,
                        'dest_account_id': None,
                    })

        return [(0, 0, acc_map) for acc_map in account_mappings]

    def on_change_company(self, cr, uid, ids, company_id, context=None):
        res = {'company_id': company_id}
        res['closing_fiscalyear_id'] = self._get_closing_fiscalyear_id(
            cr, uid, context=context, company_id=company_id)
        res['opening_fiscalyear_id'] = self._get_opening_fiscalyear_id(
            cr, uid, context=context, company_id=company_id)
        return res

    def action_draft(self, cr, uid, ids, context=None):
        """
        Called when the user clicks the confirm button.
        """
        pdb.set_trace()
        context = context or {}
        #
        # Make sure the lang is defined on the context
        #
        user = self.pool.get('res.users').browse(cr, uid, uid, context=context)
        context['lang'] = context.get('lang') or user.lang

        for fyc in self.browse(cr, uid, ids, context=context):
            #
            # Check for duplicated entries
            #
            fyc_ids = self.search(cr, uid, [('name', '=', fyc.name)])
            if len(fyc_ids) > 1:
                raise osv.except_osv(
                    _('Error'),
                    _('There is already a fiscal year closing with this name.')
                )                                            # pragma: no cover

            assert fyc.closing_fiscalyear_id and fyc.closing_fiscalyear_id.id
            fyc_ids = self.search(
                cr, uid,
                [('closing_fiscalyear_id', '=', fyc.closing_fiscalyear_id.id)])
            if len(fyc_ids) > 1:
                raise osv.except_osv(                        # pragma: no cover
                    _('Error'),
                    _('There is already a fiscal year closing for the fiscal '
                      'year to close.'))

            assert fyc.opening_fiscalyear_id and fyc.opening_fiscalyear_id.id
            fyc_ids = self.search(
                cr, uid,
                [('opening_fiscalyear_id', '=', fyc.opening_fiscalyear_id.id)])
            if len(fyc_ids) > 1:
                raise osv.except_osv(                        # pragma: no cover
                    _('Error'),
                    _('There is already a fiscal year closing for the fiscal '
                      'year to open.'))

            #
            # Check whether the default values of the fyc object have to be
            # computed
            # or they have already been computed (restarted workflow)
            #
            if fyc.c_account_mapping_ids:
                # Fyc wizard reverted to 'new' after canceled

                self.write(cr, uid, [fyc.id], {'state': 'draft'})
            else:
                # New fyc wizard object

                vals = {
                    #
                    # Perform all the operations by default
                    #
                    'create_loss_and_profit': True,
                    'create_net_loss_and_profit': False,
                    'create_closing': True,
                    'create_opening': True,

                    'check_invalid_period_moves': True,
                    'check_draft_moves': True,
                    'check_unbalanced_moves': True,

                    #
                    # L&P options
                    #
                    'lp_description': _("Loss & Profit"),
                    'lp_journal_id': self._get_journal_id(
                        cr, uid, fyc, context=context, des="Loss & Profit"),
                    'lp_date': fyc.closing_fiscalyear_id.date_stop,
                    'lp_period_id': self._get_lp_period_id(
                        cr, uid, fyc, context=context),
                    # 'lp_account_mapping_ids': self._get_account_mappings(
                    #     cr, uid, fyc, _LP_ACCOUNT_MAPPING, context),

                    #
                    # Net L&P options
                    #
                    'nlp_description': _("Net Loss & Profit"),
                    'nlp_journal_id': self._get_journal_id(
                        cr, uid, fyc,
                        context=context, des="Net Loss & Profit"),
                    'nlp_period_id': self._get_lp_period_id(
                        cr, uid, fyc, context=context),
                    'nlp_date': fyc.closing_fiscalyear_id.date_stop,
                    # 'nlp_account_mapping_ids': self._get_account_mappings(
                    #     cr, uid, fyc, _NLP_ACCOUNT_MAPPING, context),

                    #
                    # Closing options
                    #
                    'c_description': _("Fiscal Year Closing"),
                    'c_journal_id': self._get_journal_id(
                        cr, uid, fyc,
                        context=context, des="Fiscal Year Closing"),
                    'c_period_id': self._get_c_period_id(
                        cr, uid, fyc, context=context),
                    'c_date': fyc.closing_fiscalyear_id.date_stop,
                    # 'c_account_mapping_ids': self._get_account_mappings(
                    #    cr, uid, fyc, _C_ACCOUNT_MAPPING, context),

                    #
                    # Opening options
                    #
                    'o_description': _("Fiscal Year Opening"),
                    'o_journal_id': self._get_journal_id(
                        cr, uid, fyc,
                        context=context, des="Fiscal Year Opening"),
                    'o_period_id': self._get_o_period_id(
                        cr, uid, fyc, context=context),
                    'o_date': fyc.opening_fiscalyear_id.date_start,

                    # *** New state ***
                    'state': 'draft',
                }
                self.write(cr, uid, [fyc.id], vals)
        return True

    def action_run(self, cr, uid, ids, context=None):
        """
        Called when the create entries button is used.
        """
        # Note: Just change the state,
        # everything else is done on the run wizard
        #       *before* this action is called.
        self.write(cr, uid, ids, {'state': 'in_progress'})
        return True

    def action_confirm(self, cr, uid, ids, context=None):
        """
        Called when the user clicks the confirm button.
        """
        context = {} if context is None else context
        #
        # Make sure the lang is defined on the context
        #
        user = self.pool.get('res.users').browse(cr, uid, uid, context=context)
        context['lang'] = context.get('lang') or user.lang

        for fyc in self.browse(cr, uid, ids, context=context):
            #
            # Require the L&P, closing, and opening moves to exist
            # (NL&P is optional)
            #
            if not fyc.loss_and_profit_move_id:
                raise osv.except_osv(                        # pragma: no cover
                    _("Not all the operations have been performed!"),
                    _("The Loss & Profit move is required"))
            if not fyc.closing_move_id:
                raise osv.except_osv(                        # pragma: no cover
                    _("Not all the operations have been performed!"),
                    _("The Closing move is required"))
            if not fyc.opening_move_id:
                raise osv.except_osv(                        # pragma: no cover
                    _("Not all the operations have been performed!"),
                    _("The Opening move is required"))

        # Done
        self.write(cr, uid, ids, {'state': 'done'})
        return True

    def action_cancel(self, cr, uid, ids, context=None):
        """
        Called when the user clicks the cancel button.
        """
        context = {} if context is None else context
        #
        # Make sure the lang is defined on the context
        #
        user = self.pool.get('res.users').browse(cr, uid, uid, context=context)
        context['lang'] = context.get('lang') or user.lang

        #
        # Uncheck all the operations
        #
        self.pool.get('account_fiscal_year_closing.fyc').write(cr, uid, ids, {
            'create_loss_and_profit': False,
            'create_net_loss_and_profit': False,
            'create_closing': False,
            'create_opening': False,
            'check_invalid_period_moves': False,
            'check_draft_moves': False,
            'check_unbalanced_moves': False,
        }, context=context)

        for fyc in self.browse(cr, uid, ids, context=context):
            if fyc.loss_and_profit_move_id:
                fyc.loss_and_profit_move_id.unlink()
            if fyc.net_loss_and_profit_move_id:
                fyc.net_loss_and_profit_move_id.unlink()
            if fyc.closing_move_id:
                fyc.closing_move_id.unlink()
            if fyc.opening_move_id:
                fyc.opening_move_id.unlink()

        # Canceled
        self.write(cr, uid, ids, {'state': 'canceled'})
        return True

    def action_recover(self, cr, uid, ids, context=None):
        """
        Called when the user clicks the draft button to create
        a new workflow instance.
        """
        self.write(cr, uid, ids, {'state': 'new'})
        wf_service = netsvc.LocalService("workflow")
        for item_id in ids:
            wf_service.trg_create(
                uid, 'account_fiscal_year_closing.fyc', item_id, cr)
        return True


FiscalYearClosing()
