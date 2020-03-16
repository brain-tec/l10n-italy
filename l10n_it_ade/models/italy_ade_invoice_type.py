# -*- coding: utf-8 -*-
#
# Copyright 2018-20 - SHS-AV s.r.l. <https://www.zeroincombenze.it/>
#
# Contributions to development, thanks to:
# * Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
from odoo import fields, models


class ItalyAdeInvoiceType(models.Model):
    _name = 'italy.ade.invoice.type'
    _description = 'Tipo Fattura Fiscale'

    _sql_constraints = [('code',
                         'unique(code)',
                         'Code already exists!')]

    code = fields.Char(string='Code', size=4,
                       help='Code assigned by Tax Authority')
    name = fields.Char(string='Name')
    help = fields.Text(string='Help')
    scope = fields.Char(string='Scope',
                        help='Reserved to specific scope')
    active = fields.Boolean(string='Active',
                            default=True)
