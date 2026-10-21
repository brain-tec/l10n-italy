# Copyright 2021-22 LibrERP enterprise network <https://www.librerp.it>
# Copyright 2021-26 Zeroincombenze srls <https://www.zeroincombenze.it>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
{
    "name": "ITA - Inversione contabile",
    "version": "12.0.1.2.7_48",
    "category": "Localization/Italy",
    "summary": "Inversione contabile",
    "author": "Zeroincombenze srls",
    "website": "https://www.zeroincombenze.it",
    "development_status": "Beta",
    "license": "AGPL-3",
    "depends": [
        "account",
        "l10n_it_account_zma",
        "account_cancel",
        "l10n_it_account_tax_kind",
        "account_move_line_type",
        "l10n_it_fatturapa_in",
        "l10n_it_fatturapa_out",
    ],
    "data": [
        "views/account_invoice_view.xml",
        "views/account_fiscal_position_view.xml",
        "views/account_tax_view.xml",
        "views/account_journal_view.xml",
    ],
    "maintainer": "Zeroincombenze srls",
    "installable": True,
}
