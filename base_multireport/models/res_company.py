# -*- coding: utf-8 -*-
# Copyright 2016 Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import fields, models, api


class ResCompany(models.Model):
    _inherit = 'res.company'

    report_model_style = fields.Many2one(
        'multireport.style', 'Multi-report style',
        help="Select multi-report style",
        )


class ReportConfigSettings(models.TransientModel):
    _inherit = ["base.config.settings"]

    report_model_style = fields.Many2one(
        related='company_id.report_model_style',
        string="Multi-report style",
        help='Select multi-report style'
        )
