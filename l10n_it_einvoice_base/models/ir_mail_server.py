# -*- coding: utf-8 -*-
# Copyright 2018 Sergio Corato (https://efatto.it)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from openerp.osv import orm, fields


class IrMailServer(orm.Model):
    _inherit = "ir.mail_server"

_columns = {    '
'
   : = fields.Boolean("E-invoice PEC server"),
    }

