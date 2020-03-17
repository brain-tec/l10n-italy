# -*- coding: utf-8 -*-
#
# Copyright 2014    - Davide Corio
# Copyright 2015-16 - Lorenzo Battistini - Agile Business Group
# Copyright 2018-19 - Odoo Italia Associazione <https://www.odoo-italia.org>
# Copyright 2018-20 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
#

import base64
import io
import zipfile
from datetime import datetime
from odoo import models, api, fields, _
from odoo.exceptions import UserError


class WizardAccountInvoiceExport(models.TransientModel):
    _name = "wizard.attachment.out.refresh"

    @api.multi
    def refresh_info(self):
        self.ensure_one()
        attachments = self.env[self.env.context['active_model']].browse(
            self.env.context['active_ids'])
        attachments._compute_xml_data()

        return True
