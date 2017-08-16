[![Build Status](https://travis-ci.org/zeroincombenze/account_vat_period_end_statement.svg?branch=7.0)](https://travis-ci.org/zeroincombenze/account_vat_period_end_statement)
[![license agpl](https://img.shields.io/badge/licence-AGPL--3-blue.svg)](http://www.gnu.org/licenses/agpl-3.0.html)
[![Coverage Status](https://coveralls.io/repos/github/zeroincombenze/account_vat_period_end_statement/badge.svg?branch=7.0)](https://coveralls.io/github/zeroincombenze/account_vat_period_end_statement?branch=7.0)
[![codecov](https://codecov.io/gh/zeroincombenze/account_vat_period_end_statement/branch/7.0/graph/badge.svg)](https://codecov.io/gh/zeroincombenze/account_vat_period_end_statement/branch/7.0)
[![OCA_project](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-7.svg)](https://github.com/OCA/account_vat_period_end_statement/tree/7.0)
[![Tech Doc](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-7.svg)](http://wiki.zeroincombenze.org/en/Odoo/dev/7.0)
[![Help](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-7.svg)](http://wiki.zeroincombenze.org/en/Odoo/7.0/l10n-italy)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-7.svg)](http://erp7.zeroincombenze.it)

[![en](http://www.shs-av.com/wp-content/en_US.png)](http://wiki.zeroincombenze.org/it/Odoo/7.0/man)

Period End VAT Statement
========================

This module evaluates VAT to pay (or on credit) and generates the electronic
VAT closeout statement as VAT Authority
http://www.agenziaentrate.gov.it/wps/content/nsilib/nsi/documentazione/normativa+e+prassi/provvedimenti/2017/marzo+2017+provvedimenti/provvedimento+27+marzo+2017+liquidazioni+periodiche+iva

By default, amounts of debit and credit taxes are automatically loaded
from tax codes of selected periods.

Previous debit or credit is loaded from previous VAT statement, according
to its payments status.

[How to use](https://www.zeroincombenze.it/liquidazione-iva-elettronica-ip17)



[![it](http://www.shs-av.com/wp-content/it_IT.png)](http://wiki.zeroincombenze.org/it/Odoo/7.0/man)

Liquidazione IVA periodica
==========================

Questo modulo calcola l'IVA da pagare (o a credito) sia per i contribuenti
mensili che trimestrali e permette di generare il file della comunicazione
elettronica come da normativa del 2017 dell'Agenzia delle Entrate
http://www.agenziaentrate.gov.it/wps/content/nsilib/nsi/documentazione/normativa+e+prassi/provvedimenti/2017/marzo+2017+provvedimenti/provvedimento+27+marzo+2017+liquidazioni+periodiche+iva

La liquidazione è calcolata sommando i totali di periodo dei conti imposte.

L'utente può aggiungere l'eventuale credito/debito del periodo precedente e
calcolare gli interessi; può anche registrare l'utilizzo del credito in
compensazione.

[Istruzioni di utilizzo](https://www.zeroincombenze.it/liquidazione-iva-elettronica-ip17)


Credits
=======

Contributors
------------

-   Lorenzo Battistini <lorenzo.battistini@agilebg.com>
-   Marco Marchiori <marcomarkiori@gmail.com>
-   Sergio Corato <sergiocorato@gmail.com>
-   Andrei Levin <andrei.levin@didotech.com>
-   Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>


Maintainer
----------

This module is maintained by Odoo Italia Associazione

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

[![chat with us](https://www.shs-av.com/wp-content/chat_with_us.gif)](https://tawk.to/85d4f6e06e68dd4e358797643fe5ee67540e408b)