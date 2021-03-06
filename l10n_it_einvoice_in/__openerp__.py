# -*- coding: utf-8 -*-
# Copyright 2015 AgileBG SAGL <http://www.agilebg.com>
# Copyright 2015 innoviu Srl <http://www.innoviu.com>
# Copyright 2018 Lorenzo Battistini
# Copyright 2018 Gianmarco Conte, Marco Calcagni - Dinamiche Aziendali srl
# Copyright 2018 Sergio Corato

{
    'name': 'Italian Localization - Fattura elettronica - Ricezione',
    'version': '8.0.1.0.2',
    'development_status': 'Beta',
    'category': 'Localization/Italy',
    'summary': 'Electronic invoices reception',
    'author': 'Agile Business Group, Innoviu, '
              'Odoo Community Association (OCA)',
    'website': 'http://www.agilebg.com',
    'license': 'LGPL-3',
    'depends': [
        'account',
        'l10n_it_einvoice_base',
        'l10n_it_fiscal_ipa',
        'l10n_it_causali_pagamento',
        # 'l10n_it_withholding_tax_causali',
        ],
    'data': [
        # 'views/account_view.xml',
        'views/partner_view.xml',
        'wizard/wizard_import_fatturapa_view.xml',
        'security/ir.model.access.csv',
        'wizard/link_to_existing_invoice.xml',
        'views/company_view.xml',
    ],
    'installable': False
}
