|Maturity| |Build Status| |license gpl| |Coverage Status| |Codecov Status| |OCA project| |Tech Doc| |Help| |Try Me|

.. |icon| image:: /l10n_it_split_payment/static/description/icon.png

====================
|icon| Split Payment
====================


|en|


.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=
Italian Localization - split payment
=====================================

Law: http://goo.gl/1riAwt (Articolo 17 ter)

Module to generate Split Payment accounting entries

Configuration
==============

To configure this module, you need to:

* go to Settings, Configuration, Accounting and configure
'Split Payment Write-off account' (like 'IVA n/debito sospesa SP').
Write-off account should be different from standard debit VAT,
in order to separately add it in VAT statement.
* configure the fiscal position used for split payment, setting 'Split Payment'
flag. In fiscal position, map standard VAT with SP VAT, like the following:

.. image:: /l10n_it_split_payment/static/fiscal_position.png


-

22SPL is configured like the following:


.. image:: /l10n_it_split_payment/static/SP.png

Credits
========

Contributors
-------------

* Davide Corio <davide.corio@abstract.it>
* Lorenzo Battistini <lorenzo.battistini@agilebg.com>

Maintainer
-----------

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit http://odoo-community.org.



|it|



|en|


Installation
=============

These instruction are just an example to remember what you have to do.
Deployment is ODOO_DIR/REPOSITORY_DIR/MODULE_DIR where:

ODOO_DIR is root Odoo directory, i.e. /opt/odoo/7.0

REPOSITORY_DIR is downloaded git repository directory, currently is: l10n-italy

MODULE_DIR is module directory, currently is: l10n_it_split_payment

MYDB is the database name


``cd $HOME``

``git clone https://github.com/zeroincombenze/tools.git``

``cd $HOME``

``./install_tools.sh -p``

``export PATH=~/dev:$PATH``

``odoo_install_repository l10n-italy -b 7.0 -O zero``


From UI: go to:
*  admin > About > Activate Developer mode

* Setting > Modules > Update Modules List

* Setting > Local Modules > Select l10n_it_split_payment > Install

Warning: if your Odoo instance crashes, you can do following instruction
to recover installation:

``run_odoo_debug.sh 7.0 -um l10n_it_split_payment -s -d MYDB``












Credits
========

Authors
~~~~~~~

* `SHS-AV s.r.l. <https://www.zeroincombenze.it/>`__


Contributors
~~~~~~~~~~~~

* Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>


Maintainers
~~~~~~~~~~~

|Odoo Italia Associazione|

Odoo Italia is a nonprofit organization whose develops Italian
Localization on Odoo.

To contribute to this module, please visit https://odoo-italia.org/.




**Odoo** is a trademark of `Odoo S.A. <https://www.odoo.com/>`__
(formerly OpenERP, formerly TinyERP)

**OCA**, or the `Odoo Community Association <http://odoo-community.org/>`__,
is a nonprofit organization whose mission is to support
the collaborative development of Odoo features and promote its widespread use.

**zeroincombenze®** is a trademark of `SHS-AV s.r.l. <http://www.shs-av.com/>`__
which distributes and promotes **Odoo** ready-to-use on own cloud infrastructure.
`Zeroincombenze® distribution <http://wiki.zeroincombenze.org/en/Odoo>`__
is mainly designed for Italian law and markeplace.
Users can download from `Zeroincombenze® distribution <https://github.com/zeroincombenze/OCB>`__
and deploy on local server.



.. |Maturity| image:: https://img.shields.io/badge/maturity-Alfa-red.png
    :target: https://odoo-community.org/page/development-status
    :alt: Alfa
.. |Build Status| image:: https://travis-ci.org/zeroincombenze/l10n-italy.svg?branch=7.0
    :target: https://travis-ci.org/zeroincombenze/l10n-italy
    :alt: github.com
.. |license gpl| image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |Coverage Status| image:: https://coveralls.io/repos/github/zeroincombenze/l10n-italy/badge.svg?branch=7.0
    :target: https://coveralls.io/github/zeroincombenze/l10n-italy?branch=7.0
    :alt: Coverage
.. |Codecov Status| image:: https://codecov.io/gh/zeroincombenze/l10n-italy/branch/7.0/graph/badge.svg
    :target: https://codecov.io/gh/zeroincombenze/l10n-italy/branch/7.0
    :alt: Codecov
.. |OCA project| image:: http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-7.svg
    :target: https://github.com/OCA/l10n-italy/tree/7.0
    :alt: OCA
.. |Tech Doc| image:: http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-7.svg
    :target: http://wiki.zeroincombenze.org/en/Odoo/7.0/dev
    :alt: Technical Documentation
.. |Help| image:: http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-7.svg
    :target: http://wiki.zeroincombenze.org/it/Odoo/7.0/man
    :alt: Technical Documentation
.. |Try Me| image:: http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-7.svg
    :target: https://erp7.zeroincombenze.it
    :alt: Try Me
.. |Odoo Italia Associazione| image:: https://www.odoo-italia.org/images/Immagini/Odoo%20Italia%20-%20126x56.png
   :target: https://odoo-italia.org
   :alt: Odoo Italia Associazione
.. |en| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/flags/en_US.png
   :target: https://www.facebook.com/groups/openerp.italia/
.. |it| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/flags/it_IT.png
   :target: https://www.facebook.com/groups/openerp.italia/
.. |br| raw:: html

    <br/>


