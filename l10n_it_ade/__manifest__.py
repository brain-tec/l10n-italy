# -*- coding: utf-8 -*-
#
# Copyright 2018-20 - SHS-AV s.r.l. <https://www.zeroincombenze.it/>
#
# Contributions to development, thanks to:
# * Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
{
    'name': 'Agenzia delle Entrate',
    'summary': 'Codice e definizioni come da Agenzia delle Entrate',
    'version': '10.0.0.1.14',
    'category': 'Localization/Italy',
    'author': 'Odoo Community Association (OCA), SHS-AV s.r.l.',
    'license': 'LGPL-3',
    'depends': ['account'],
    'external_dependencies': {'python': ['pyxb']},
    'data': [
        'security/ir.model.access.csv',
        'data/italy_ade_tax_nature.xml',
        'data/italy_ade_codice_carica.xml',
        'data/italy_ade_invoice_type.xml',
        'views/ir_ui_menu.xml',
        'views/account_tax_view.xml',
        'views/account_journal.xml',
        'views/codice_carica_view.xml',
        'views/tax_nature_view.xml',
        'views/invoice_type_view.xml',
    ],
    'installable': True,
    'maintainer': 'Odoo Community Association (OCA)',
    'development_status': 'Beta',
}
