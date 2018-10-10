[![Build Status](https://travis-ci.org/zeroincombenze/tools.svg?branch=9.0)](https://travis-ci.org/zeroincombenze/tools)
[![license agpl](https://img.shields.io/badge/licence-AGPL--3-blue.svg)](http://www.gnu.org/licenses/agpl-3.0.html)
[![Coverage Status](https://coveralls.io/repos/github/zeroincombenze/tools/badge.svg?branch=9.0)](https://coveralls.io/github/zeroincombenze/tools?branch=9.0)
[![codecov](https://codecov.io/gh/zeroincombenze/tools/branch/9.0/graph/badge.svg)](https://codecov.io/gh/zeroincombenze/tools/branch/9.0)
[![OCA_project](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-9.svg)](https://github.com/OCA/tools/tree/9.0)
[![Tech Doc](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-9.svg)](http://wiki.zeroincombenze.org/en/Odoo/9.0/dev)
[![Help](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-9.svg)](http://wiki.zeroincombenze.org/en/Odoo/9.0/man/FI)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-9.svg)](https://erp9.zeroincombenze.it)














































[![en](https://github.com/zeroincombenze/grymb/blob/master/flags/en_US.png)](https://www.facebook.com/groups/openerp.italia/)

    :alt: License: AGPL-3

Period End VAT Statement
========================

This module helps to register the VAT statement of period end.

In order to load correct amount from tax code, the tax code has to be
associated to account involved in statement, through tax code form.

The 'VAT statement' object allows to specify every amount and relative account
used by the statement.
By default, amounts of debit and credit taxes are automatically loaded
from tax codes of selected periods.
Previous debit or credit is loaded from previous VAT statement, according
to its payments status.
Confirming the statement, the 'account.move' is created. If you select
a payment term, the due date(s) will be set.

The 'tax authority' tab contains information about payment(s).
You can see statement's result ('authority VAT amount') and residual
amount to pay ('Balance').
The statement can be paid like every other debit: by voucher or 'move.line'
reconciliation.

If you need to calculate interest, you can add default information in your
company data (percentage and account).

Specification:
http://wiki.odoo-italia.org/doku.php/moduli/vat_period_end_statement

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






* Lorenzo Battistini <lorenzo.battistini@agilebg.com>
* Elena Carlesso <ecarlesso@linkgroup.it>
* Marco Marchiori <marcomarkiori@gmail.com>
* Sergio Corato <sergiocorato@gmail.com>
* Andrea Gallina <a.gallina@apuliasoftware.it>
* Alex Comba <alex.comba@agilebg.com>
* Alessandro Camilli <camillialex@gmail.com>

### Funders

### Maintainer










.. image:: http://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: http://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit http://odoo-community.org.

[//]: # (copyright)

----

**Odoo** is a trademark of [Odoo S.A.](https://www.odoo.com/) (formerly OpenERP, formerly TinyERP)

**OCA**, or the [Odoo Community Association](http://odoo-community.org/), is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

**zeroincombenze®** is a trademark of [SHS-AV s.r.l.](http://www.shs-av.com/)
which distributes and promotes **Odoo** ready-to-use on own cloud infrastructure.
[Zeroincombenze® distribution of Odoo](http://wiki.zeroincombenze.org/en/Odoo)
is mainly designed for Italian law and markeplace.
Users can download from [Zeroincombenze® distribution](https://github.com/zeroincombenze/OCB) and deploy on local server.

[//]: # (end copyright)

[//]: # (addons)

[//]: # (end addons)


[![chat with us](https://www.shs-av.com/wp-content/chat_with_us.gif)](https://tawk.to/85d4f6e06e68dd4e358797643fe5ee67540e408b)
