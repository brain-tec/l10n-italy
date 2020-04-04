# -*- coding: utf-8 -*-

from odoo import models, api, fields, _
from odoo.exceptions import UserError


class WizardSetInvoiceCommyype(models.TransientModel):
    _name = "wizard.set.invoice.commtype"

    @api.multi
    def set_einvoice_commtype(self):
        self.ensure_one()
        invoices = self.env[self.env.context['active_model']].browse(
            self.env.context['active_ids'])
        return invoices.set_einvoice_commtype()
