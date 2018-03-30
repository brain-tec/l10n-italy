[![Build Status](https://travis-ci.org/zeroincombenze/l10n-italy.svg?branch=7.0)](https://travis-ci.org/zeroincombenze/l10n-italy)
[![license agpl](https://img.shields.io/badge/licence-AGPL--3-blue.svg)](http://www.gnu.org/licenses/agpl-3.0.html)
[![Coverage Status](https://coveralls.io/repos/github/zeroincombenze/l10n-italy/badge.svg?branch=7.0)](https://coveralls.io/github/zeroincombenze/l10n-italy?branch=7.0)
[![codecov](https://codecov.io/gh/zeroincombenze/l10n-italy/branch/7.0/graph/badge.svg)](https://codecov.io/gh/zeroincombenze/l10n-italy/branch/7.0)
[![OCA_project](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-7.svg)](https://github.com/OCA/l10n-italy/tree/7.0)
[![Tech Doc](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-7.svg)](http://wiki.zeroincombenze.org/en/Odoo/7.0/dev)
[![Help](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-7.svg)](http://wiki.zeroincombenze.org/en/Odoo/7.0/man/FI)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-7.svg)](http://erp7.zeroincombenze.it)


[![en](https://github.com/zeroincombenze/grymb/blob/master/flags/en_US.png)](https://www.facebook.com/groups/openerp.italia/)

Purchase Invoices with Withholding Tax
======================================

No more info


Ritenute d'acconto sulle fatture fornitore

Configurare i campi associati all'azienda:
 - Termine di pagamento della ritenuta d'acconto
 - Conto di debito per le ritenute da versare
 - Sezionale che conterrà le registrazioni legate alla ritenuta

L'importo della ritenuta d'acconto non è calcolato ma inserito manualmente.


### Funzionalità & Certificati

Funzione | Status | Note
--- | --- | ---
Registrazione avvisi di parcella | :white_check_mark: | No in registri IVA
Trasformazione avvisi di parcella in fattura | :white_check_mark: | Con un tasto
Registrazione importo ritenuta d'acconto | :white_check_mark: | Importo manuale
Registrazione scadenza RA al pagamento | :white_check_mark: | Su conto RA con dettaglio per fornitore


Installation
------------

These instruction are just an example to remember what you have to do:

    git clone https://github.com/zeroincombenze/l10n-italy
    for module in l10n_it_ade account_voucher_cash_basis account_invoice_entry_date l10n_it_withholding_tax; do
        mv ODOO_DIR/l10n-italy/$module BACKUP_DIR/
        cp -R l10n-italy/$module ODOO_DIR/l10n-italy/
    sudo service odoo-server restart -i l10n_it_ade,l10n_it_withholding_tax -d MYDB

From UI: go to Setup > Module > Install


Configuration
-------------

:it:

* Contabilità > Varie > Termini di pagamento :point_right: Inserire termine di pagamento RA (al 15 del mese)
* Contabilità > Sezionali > Sezionali :point_right: Inserire sezionale avvisi di parcella
* Contabilità > Sezionali > Sezionali :point_right: Inserire sezionale avvisi ritenute d'acconto (se diverso da varie)
* Contabilità > Conti > Conti :point_right: Conto RA da pagare, tipo debito
* Configurazione > Configurazione > Contabilità :point_right: Impostare termini di pagamento ritenute
* Configurazione > Configurazione > Contabilità :point_right: Impostare termini conto ritenute
* Configurazione > Configurazione > Contabilità :point_right: Impostare sezionale ritenute
* Contabilità > Fornitori > Fatture Fornitori > Quando presente RA marcare il flag ed inserire importo


Usage
-----

For furthermore information, please visit http://wiki.zeroincombenze.org/it/Odoo/7.0/man/FI



Known issues / Roadmap
----------------------

:ticket: This module replaces OCA module; PR have to be issued.
In order to use this module you have to use:

:warning: Use [l10n_it_ade](l10n_it_ade/) module does not exist in OCA repository


Bug Tracker
-----------

Have a bug? Please visit https://odoo-italia.org/index.php/kunena/home


Credits
-------

### Contributors

* Lorenzo Battistini <lorenzo.battistini@agilebg.com>
* Paolo Chiara <p.chiara@isa.it>
* Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>

### Funders

This module has been financially supported by

* Agile Business Group sagl <http://www.agilebg.com>
* SHS-AV s.r.l. <https://www.zeroincombenze.it/>

### Maintainer

[![Odoo Italia Associazione](https://www.odoo-italia.org/images/Immagini/Odoo%20Italia%20-%20126x56.png)](https://odoo-italia.org)

Odoo Italia is a nonprofit organization whose develops Italian Localization for
Odoo.

To contribute to this module, please visit <https://odoo-italia.org/>.



[//]: # (copyright)

----

**Odoo** is a trademark of [Odoo S.A.](https://www.odoo.com/) (formerly OpenERP, formerly TinyERP)

**OCA**, or the [Odoo Community Association](http://odoo-community.org/), is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

**zeroincombenze®** is a trademark of [SHS-AV s.r.l.](http://www.shs-av.com/)
which distributes and promotes **Odoo** ready-to-use on its own cloud infrastructure.
[Zeroincombenze® distribution](http://wiki.zeroincombenze.org/en/Odoo)
is mainly designed for Italian law and markeplace.
Everytime, every Odoo DB and customized code can be deployed on local server too.

[//]: # (end copyright)

[//]: # (addons)

[//]: # (end addons)

[![chat with us](https://www.shs-av.com/wp-content/chat_with_us.gif)](https://tawk.to/85d4f6e06e68dd4e358797643fe5ee67540e408b)
