# -*- coding: utf-8 -*-
#
# Copyright 2019-20 - SHS-AV s.r.l. <https://www.zeroincombenze.it/>
#
# Contributions to development, thanks to:
# * Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#


import io
import base64
import zipfile
import re
# from datetime import datetime
from odoo import models, api, fields, _
from odoo.exceptions import UserError


class WizardAccountInvoiceImportZip(models.TransientModel):
    _name = "wizard.einvoice.import.zip"
    _description = "Import E-bill from zip"

    zip = fields.Binary('ZIP file')
    type = fields.Selection(
        [('purchase', 'Purchase Invoices'),
         ('sale', 'Sale Invoices')],
        'Invoice type',
        default='purchase')

    @api.multi
    def import_zip(self):
        if not zipfile.is_zipfile(io.BytesIO(base64.b64decode(self.zip))):
            raise UserError('Imported file is not a zip file')
        zf = zipfile.ZipFile(io.BytesIO(base64.b64decode(self.zip)))
        att_list = []
        ir_att_model = self.env['ir.attachment']
        if self.type == 'sale':
            model = 'fatturapa.attachment.out'
            att_model = self.env[model]
        else:
            model = 'fatturapa.attachment.in'
        att_model = self.env[model]
        rex = r'[A-Z]{2}[A-Za-z0-9]+_[A-Za-z0-9]{5}\.(xml|XML|xml.p7m|XML.P7m)'
        for xml_file in zf.namelist():
            if re.match(rex, xml_file):
                if att_model.search([('name', '=', xml_file)]):
                    continue
                try:
                    data = zf.read(xml_file)
                except KeyError:
                    raise UserError(
                        'Error extracting %s from zip file' % xml_file)
                vals = {
                    'name': xml_file,
                    'datas_fname': xml_file,
                    'datas': data.encode('base64'),
                    'type': 'binary',
                    'mimetype': 'text/xml',
                    'extension': '.xml',
                }
                try:
                    att_id = att_model.create(vals)
                    att_list.append(att_id.id)
                except BaseException:
                    raise UserError(
                        'Error extracting %s from zip file' % xml_file)
        return {
            'name': "Imported Attachment",
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': model,
            'type': 'ir.actions.act_window',
            'domain': [('id', 'in', att_list)],
            'view_id': False,
        }
