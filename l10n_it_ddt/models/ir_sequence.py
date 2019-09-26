from datetime import datetime

import odoo.addons.decimal_precision as dp
from odoo import _, api, fields, models
from odoo.exceptions import Warning as UserError
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT, float_is_zero
from odoo.tools.misc import formatLang


class IrSequence(models.Model):
    _inherit = 'ir.sequence'

    def _unnext_do(self, number):
        number_last_actual = self.number_next_actual - 1
        if number == self.get_next_char(number_last_actual):
            self.number_next = number_last_actual

    def _unnext(self, number):
        if not self.use_date_range:
            self._unnext_do(number)
        dt = fields.Date.today()
        if self._context.get('ir_sequence_date'):
            dt = self._context.get('ir_sequence_date')
        seq_date = self.env['ir.sequence.date_range'].search(
            [('sequence_id', '=', self.id),
             ('date_from', '<=', dt),
             ('date_to', '>=', dt)], limit=1)
        if not seq_date:
            return
        seq_date.with_context(
            ir_sequence_date_range=seq_date.date_from)._unnext(number)

    @api.multi
    def unnext_by_id(self, number):
        self.check_access_rights('read')
        self._unnext(number)
