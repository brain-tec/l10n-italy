# -*- coding: utf-8 -*-

from openerp import models, api, fields, _
from openerp.exceptions import Warning as UserError
from openerp.addons.l10n_it_ade.bindings import fatturapa_v_1_2


class WizardLinkToInvoice(models.TransientModel):
    _name = "wizard.link.to.invoice"
    _description = "Link to Supplier Invoice"
    invoice_id = fields.Many2one(
        'account.invoice', string="Invoice", required=True)

    def get_invoice_obj(self, fatturapa_attachment):
        xml_string = fatturapa_attachment.get_xml_string()
        return fatturapa_v_1_2.CreateFromDocument(xml_string)

    @api.multi
    def link(self):
        self.ensure_one()
        active_ids = self.env.context.get('active_ids')
        if len(active_ids) != 1:
            raise UserError(_("You can select only 1 XML file to link"))
        self.invoice_id.fatturapa_attachment_in_id = active_ids[0]
        # extract pdf if attached
        fatturapa_attachment_obj = self.env['fatturapa.attachment.in']
        for fatturapa_attachment_id in active_ids:
            fatturapa_attachment = fatturapa_attachment_obj.browse(
                fatturapa_attachment_id)
            fatt = self.get_invoice_obj(fatturapa_attachment)
            for FatturaBody in fatt.FatturaElettronicaBody:
                # 2.5
                AttachmentsData = FatturaBody.Allegati
                if AttachmentsData and self.invoice_id:
                    fatturapa_attachment_obj.extract_attachments(
                        AttachmentsData, self.invoice_id.id)
