# -*- coding: utf-8 -*-
#
# Copyright 2019-20 - SHS-AV s.r.l. <https://www.zeroincombenze.it/>
#
# Contributions to development, thanks to:
# * Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
from odoo import fields, models
import odoo.addons.decimal_precision as dp


class ItalyConaiProductCategory(models.Model):
    _name = 'italy.conai.product.category'
    _description = 'CONAI product category'

    _sql_constraints = [('code',
                         'unique(code)',
                         'Code already exists!')]

    code = fields.Char(string='Code', size=64, required=True,
                       help='Category code')
    name = fields.Char(string='Name', required=True)
    parent_id = fields.Many2one(
        'italy.conai.product.category', string='Parent Category',
        ondelete='set null')
    conai_price_unit = fields.Float(
        string='Unit Price',
        digits=dp.get_precision('Product Price'))
    conai_uom_id = fields.Many2one(
        'product.uom', string='Unit of Measure',
        ondelete='set null',
        default=lambda self: self.env.ref('product.product_uom_ton'))
    conai_percent = fields.Float(
        string='Applying percent', digits=dp.get_precision('Product Price'),
        default=100.0)
    type = fields.Selection([
        ('product', 'Product'),
        ('packing', 'Packing'),
    ], string='Type', required=True, default='packing',)
    start_date = fields.Date(string='Start Applying Date',
        copy = False)
    end_date = fields.Date(string='End Applying Date',
        copy = False)
    active = fields.Boolean(string='Active',
                            default=True)
    account_id = fields.Many2one(
        'account.account', string='Account')

