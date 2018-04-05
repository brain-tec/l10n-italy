# -*- coding: utf-8 -*-
#
# Copyright 2008, Borja López Soilán <borja@kami.es> - (Pexego)
# Copyright 2008, ACYSOS S.L. (http://acysos.com)
#                 Pedro Tarrafeta <pedro@acysos.com>
# Copyright 2009, Zikzakmedia S.L. (http://zikzakmedia.com)
#                 Jordi Esteve <jesteve@zikzakmedia.com>
# Copyright 2011-2018, Associazione Odoo Italia <https://odoo-italia.org>
# Copyright 2012, Domsense srl (<http://www.domsense.com>)
# Copyright 2012, Agile Business Group sagl (<http://www.agilebg.com>)
# Copyright 2014-2018, Odoo Community Association (OCA)
# Copyright 2017-2018, Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
{
    "name": "Fiscal Year Closing",
    "version": "7.0.1.1",
    "author": "Associazione Odoo Italia,"
              "Pexego,"
              "Odoo Community Association (OCA)",
    "website": "http://www.odoo-italia.org",
    "category": "Generic Modules/Accounting",
    "description": """
Generalization of l10n_es_fiscal_year_closing
( http://apps.odoo.com/addon/4506 )

Fiscal Year Closing Wizard

Replaces the default Odoo end of year wizards (from account module)
with a more advanced all-in-one wizard that will let the users:
  - Check for unbalanced moves, moves with invalid dates
    or period or draft moves on the fiscal year to be closed.
  - Create the Loss and Profit entry.
  - Create the Net Loss and Profit entry.
  - Create the Closing entry.
  - Create the Opening entry.

It is stateful, saving all the info about the fiscal year closing, so the
user can cancel and undo the operations easily.
    """,
    "license": "AGPL-3",
    "depends": [
        "base",
        "account",
    ],
    "init_xml": [],
    "update_xml": [
        "security/ir.model.access.csv",
        "fyc_workflow.xml",
        "wizard/wizard_run.xml",
        "views/fyc_view.xml",
        "views/hide_account_wizards.xml",
    ],
    "active": False,
    "installable": True
}
