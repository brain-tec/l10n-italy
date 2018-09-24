[![Build Status](https://travis-ci.org/Odoo-Italia-Associazione/l10n-italy.svg?branch=8.0)](https://travis-ci.org/Odoo-Italia-Associazione/l10n-italy)
[![license agpl](https://img.shields.io/badge/licence-AGPL--3-blue.svg)](http://www.gnu.org/licenses/agpl-3.0.html)
[![Coverage Status](https://coveralls.io/repos/github/Odoo-Italia-Associazione/l10n-italy/badge.svg?branch=8.0)](https://coveralls.io/github/Odoo-Italia-Associazione/l10n-italy?branch=8.0)
[![codecov](https://codecov.io/gh/Odoo-Italia-Associazione/l10n-italy/branch/8.0/graph/badge.svg)](https://codecov.io/gh/Odoo-Italia-Associazione/l10n-italy/branch/8.0)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-8.svg)](https://erp8.zeroincombenze.it)


[![en](https://github.com/zeroincombenze/grymb/blob/master/flags/en_US.png)](https://www.facebook.com/groups/openerp.italia/)

   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
================================================================
   :alt: License: AGPL-3

Account Fiscal Year Closing - Chiusura e riapertura fiscale
===========================================================


Generalization of l10n_es_fiscal_year_closing.

This module replaces the default Odoo end of year wizards
(from account module)
with a more advanced all-in-one wizard that will let the users:
  - Check for unbalanced moves, moves with invalid dates
    or period or draft moves on the fiscal year to be closed.
  - Create the Loss and Profit entry.
  - Create the Net Loss and Profit entry.
  - Create the Closing entry.
  - Create the Opening entry.

Installation
------------

























Configuration
-------------

























Usage
-----









































=====

To use this module, you need to:

#. Create new journal entries
#. Create specific accounts in chart of account
#. Execute: accounting -> Periodic processing -> End of period -> Chiudi anno fiscale
#. Check for all values in form
#. Confirm all account operations



[![it](https://github.com/zeroincombenze/grymb/blob/master/flags/it_IT.png)](https://www.facebook.com/groups/openerp.italia/)

Variante del modulo l10n_es_fiscal_year_closing
===============================================

Questo modulo sostituisce il modulo standard di apertura di Odoo con alcune
specificità legate alla contabilità italiana:
  - Controllo movimenti sbilanciati o con date non valide
  - Crea il movimento di rilevazione profitti e perdite
  - Crea il movimento di chiusura contabile
  - Crea il movimento di apertura contabile dei soli conti patrimoniali


Uso
===

Per utilizzare questo modulo:

#. Creare nuovi sezionali specifici
#. Creare conti specifici per la chiusura e riapertura
#. Eseguire: Contabilità -> Elaborazione periodica -> Fine del periodo -> Chiudi anno fiscale
#. Controllare i valori risultanti
#. Confermare definitivamente tutte le operazioni



For further information, please visit:

* http://www.odoo-italia.org/

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/122/8.0

Installation
------------

























Configuration
-------------

























Usage
-----









































Known issues / Roadmap
----------------------

























Bug Tracker
-----------

























Credits
-------





















































### Contributors


























* Borja López Soilán <borja@kami.es>
* Lorenzo Battistini <lorenzo.battistini@agilebg.com>
* Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>

### Funders
### Maintainer



















































.. image:: http://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: http://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose mission is to support the collaborative development of Odoo features and promote its widespread use.

To contribute to this module, please visit http://odoo-community.org.

[//]: # (copyright)

----

**Odoo** is a trademark of [Odoo S.A.](https://www.odoo.com/) (formerly OpenERP, formerly TinyERP)

**OCA**, or the [Odoo Community Association](http://odoo-community.org/), is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

**Odoo Italia Associazione**, or the [Associazione Odoo Italia](https://www.odoo-italia.org/)
is the nonprofit Italian Community Association whose mission
is to support the collaborative development of Odoo designed for Italian law and markeplace.
Since 2017 Odoo Italia Associazione issues modules for Italian localization not developed by OCA
or available only with Odoo Proprietary License.
Odoo Italia Associazione distributes code under [AGPL](https://www.gnu.org/licenses/agpl-3.0.html) or [LGPL](https://www.gnu.org/licenses/lgpl.html) free license.

[Odoo Italia Associazione](https://www.odoo-italia.org/) è un'Associazione senza fine di lucro
che dal 2017 rilascia moduli per la localizzazione italiana non sviluppati da OCA
o disponibili solo con [Odoo Proprietary License](https://www.odoo.com/documentation/user/9.0/legal/licenses/licenses.html).

Odoo Italia Associazione distribuisce il codice esclusivamente con licenza [AGPL](https://www.gnu.org/licenses/agpl-3.0.html) o [LGPL](https://www.gnu.org/licenses/lgpl.html)

[//]: # (end copyright)


[//]: # (addons)

[//]: # (end addons)


