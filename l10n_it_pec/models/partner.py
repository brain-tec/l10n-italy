<<<<<<< HEAD
# Copyright 2014 Associazione Odoo Italia (<http://www.odoo-italia.org>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields
=======
#
# Copyright 2014    Associazione Odoo Italia (<https://www.odoo-italia.org>)
# Copyright 2018-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
#
from odoo import fields, models
>>>>>>> b9720883e5eaa47d896b4a248c6b280ed2b2c131


class ResPartner(models.Model):
    _inherit = "res.partner"

    pec_mail = fields.Char(string='PEC Mail')
