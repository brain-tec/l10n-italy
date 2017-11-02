[![Build Status](https://travis-ci.org/zeroincombenze/l10n-italy.svg?branch=7.0)](https://travis-ci.org/zeroincombenze/l10n-italy)
[![license agpl](https://img.shields.io/badge/licence-AGPL--3-blue.svg)](http://www.gnu.org/licenses/agpl-3.0.html)
[![Coverage Status](https://coveralls.io/repos/github/zeroincombenze/l10n-italy/badge.svg?branch=7.0)](https://coveralls.io/github/zeroincombenze/l10n-italy?branch=7.0)
[![codecov](https://codecov.io/gh/zeroincombenze/l10n-italy/branch/7.0/graph/badge.svg)](https://codecov.io/gh/zeroincombenze/l10n-italy/branch/7.0)
[![OCA_project](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-7.svg)](https://github.com/OCA/l10n-italy/tree/7.0)
[![Tech Doc](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-7.svg)](http://wiki.zeroincombenze.org/en/Odoo/7.0/dev)
[![Help](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-7.svg)](http://wiki.zeroincombenze.org/en/Odoo/7.0/man/FI)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-7.svg)](http://erp7.zeroincombenze.it)


[![en](https://github.com/zeroincombenze/grymb/blob/master/flags/en_US.png)](https://www.facebook.com/groups/openerp.italia/)

[![icon](static/src/img/icon.png)](https://travis-ci.org/zeroincombenze)

Italian Localization - Fiscal Code
==================================

Check for Italian fiscal code. This module enables fiscal code validation
and/or can generate it form person data.
Split full name into first and last name, when individual person.



[![it](https://github.com/zeroincombenze/grymb/blob/master/flags/it_IT.png)](https://www.facebook.com/groups/openerp.italia/)

Localizzazione Italiana - Codice Fiscale
========================================

Verifica la validità del codice fiscale durante l'immissione dei dati anagrafici.
Inoltre permette di generare il codice fiscale dai dati.
Divide la ragione sociale in cognome e nome nel caso di persone fisiche.


### Funzionalità & Certificati

Funzione | Status | Note
--- | --- | ---
Controllo validità CF Italia | :white_check_mark: | Verifica carattere di controllo
Accetta Partita IVA | :white_check_mark: | Per aziende controllate
Genera CF da dati | :white_check_mark: |
Campo libero per partner esteri | :white_check_mark: |
Separazione cognome e nome | :white_check_mark:  |


Installation
------------

These instruction are just an example to remember what you have to do:

    pip install PyXB==1.2.4
    git clone https://github.com/zeroincombenze/l10n-italy
    cp -R l10n-italy/l10n_it_fiscalcode ODOO_DIR/l10n-italy/
    sudo service odoo-server restart -i l10n_it_fiscalcode -d MYDB

From UI: go to Setup > Module > Install


Configuration
-------------

:mute:


Usage
-----

For furthermore information, please visit http://wiki.zeroincombenze.org/it/Odoo/7.0/man/FI


Known issues / Roadmap
----------------------

:ticket: This module replace OCA module; PR will be issued
In order to use this module you have to use:

* [l10n_it_base](l10n_it_base/) replaces OCA module


Bug Tracker
-----------

Have a bug? Please visit https://odoo-italia.org/index.php/kunena/home

Credits
-------

### Contributors

* Davide Corio <davide.corio@domsense.com>
* Luca Subiaco <subluca@gmail.com>
* Simone Orsi <simone.orsi@domsense.com>
* Mario Riva <mario.riva@domsense.com>
* Mauro Soligo <mauro.soligo@katodo.com>
* Giovanni Barzan <giovanni.barzan@gmail.com>
* Lorenzo Battistini <lorenzo.battistini@albatos.com>
* Roberto Onnis <onnis.roberto@gmail.com>
* Franco Tampieri <franco.tampieri@agilebg.com>
* Andrea Cometa <info@andreacometa.it>
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
