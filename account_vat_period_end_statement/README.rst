
===============================
|icon| Period End VAT Statement
===============================


.. |icon| image:: https://raw.githubusercontent.com/zeroincombenze/l10n-italy/8.0/account_vat_period_end_statement/static/description/icon.png

|Maturity| |Build Status| |Coverage Status| |Codecov Status| |license gpl| |Tech Doc| |Help| |Try Me|

.. contents::


Overview / Panoramica
=====================

|en| This module evaluates VAT to pay (or on credit) and generates the electronic
VAT closeout statement as VAT Authority
<http://www.agenziaentrate.gov.it/wps/content/nsilib/nsi/documentazione/
normativa+e+prassi/provvedimenti/2017/marzo+2017+provvedimenti/
provvedimento+27+marzo+2017+liquidazioni+periodiche+iva>

By default, amounts of debit and credit taxes are automatically loaded
from tax codes of selected periods.

Previous debit or credit is loaded from previous VAT statement, according
to its payments status.

https://www.zeroincombenze.it/liquidazione-iva-elettronica-ip17

|

|it| Questo modulo calcola l'IVA da pagare (o a credito) sia per i contribuenti
mensili che trimestrali e permette di generare il file della comunicazione
elettronica come da normativa del 2017 dell'Agenzia delle Entrate
http://www.agenziaentrate.gov.it/wps/content/nsilib/nsi/documentazione/normativa+e+prassi/provvedimenti/2017/marzo+2017+provvedimenti/provvedimento+27+marzo+2017+liquidazioni+periodiche+iva

La liquidazione è calcolata sommando i totali di periodo dei conti imposte.

L'utente può aggiungere l'eventuale credito/debito del periodo precedente e
calcolare gli interessi; può anche registrare l'utilizzo del credito in
compensazione.


https://www.zeroincombenze.it/liquidazione-iva-elettronica-ip17

|
|

Certifications / Certificazioni
-------------------------------

+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+--------------+----------------------------------------+
| Logo                  | Ente/Certificato                                                                                                                                                                        | Data inizio   | Da fine      | Note                                   |
+=======================+=========================================================================================================================================================================================+===============+==============+========================================+
| |xml\_schema|         | `ISO + Agenzia delle Entrate <http://www.agenziaentrate.gov.it/wps/content/Nsilib/Nsi/Strumenti/Specifiche+tecniche/Specifiche+tecniche+comunicazioni/Fatture+e+corrispettivi+ST/>`__   | 01-06-2017    | 31-12-2017   | Validazione contro schema xml          |
+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+--------------+----------------------------------------+
| |DesktopTelematico|   | `Agenzia delle Entrate <http://www.agenziaentrate.gov.it/wps/content/Nsilib/Nsi/Strumenti/Specifiche+tecniche/Specifiche+tecniche+comunicazioni/Fatture+e+corrispettivi+ST/>`__         | 01-06-2017    | 31-12-2017   | Controllo tramite Desktop telematico   |
+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+--------------+----------------------------------------+

|

OCA comparation / Confronto con OCA
-----------------------------------

|OCA project|

|
|

Getting started / Come iniziare
===============================

|Try Me|


Prerequisites / Prerequisiti
----------------------------


* python
* postgresql 9.2+

|

Installation / Installazione
----------------------------

+---------------------------------+------------------------------------------+
| |en|                            | |it|                                     |
+---------------------------------+------------------------------------------+
| These instruction are just an   | Istruzioni di esempio valide solo per    |
| example to remember what        | distribuzioni Linux CentOS 7, Ubuntu 14+ |
| you have to do on Linux.        | e Debian 8+                              |
|                                 |                                          |
| Installation is built with:     | L'installazione è costruita con:         |
+---------------------------------+------------------------------------------+
| `Zeroincombenze Tools <https://github.com/zeroincombenze/tools>`__         |
+---------------------------------+------------------------------------------+
| Suggested deployment is:        | Posizione suggerita per l'installazione: |
+---------------------------------+------------------------------------------+
| /opt/odoo/8.0/l10n-italy/                                                  |
+----------------------------------------------------------------------------+

::

    cd $HOME
    git clone https://github.com/zeroincombenze/tools.git
    cd ./tools
    ./install_tools.sh -p
    export PATH=$HOME/dev:$PATH
    odoo_install_repository l10n-italy -b 8.0 -O zero
    for pkg in os0 z0lib; do
        pip install $pkg -U
    done
    sudo manage_odoo requirements -b 8.0 -vsy -o /opt/odoo/8.0

From UI: go to:

* |menu| Setting > Modules > Update Modules List
* |menu| Setting > Local Modules |right_do| Select **account_vat_period_end_statement** > Install

|

Upgrade / Aggiornamento
-----------------------

+---------------------------------+------------------------------------------+
| |en|                            | |it|                                     |
+---------------------------------+------------------------------------------+
| When you want upgrade and you   | Per aggiornare, se avete installato con  |
| installed using above           | le istruzioni di cui sopra:              |
| statements:                     |                                          |
+---------------------------------+------------------------------------------+

::

    odoo_install_repository l10n-italy -b 8.0 -O zero -U
    # Adjust following statements as per your system
    sudo systemctl restart odoo

From UI: go to:

* |menu| Setting > Modules > Update Modules List
* |menu| Setting > Local Modules |right_do| Select **account_vat_period_end_statement** > Update

|

Support / Supporto
------------------


|Zeroincombenze| This module is maintained by the `SHS-AV s.r.l. <https://www.zeroincombenze.it/>`__ and free support is supplied through `Odoo Italia Associazione Forum <https://odoo-italia.org/index.php/kunena/recente>`__


|
|

Get involved / Ci mettiamo in gioco
===================================

Bug reports are welcome! You can use the issue tracker to report bugs,
and/or submit pull requests on `GitHub Issues
<https://github.com/zeroincombenze/l10n-italy/issues>`_.

In case of trouble, please check there if your issue has already been reported.

Proposals for enhancement
-------------------------


|en| If you have a proposal to change this module, you may want to send an email to <cc@shs-av.com> for initial feedback.
An Enhancement Proposal may be submitted if your idea gains ground.

|it| Se hai proposte per migliorare questo modulo, puoi inviare una mail a <cc@shs-av.com> per un iniziale contatto.

|
|

Credits / Titoli di coda
========================

Copyright
---------

Odoo is a trademark of `Odoo S.A. <https://www.odoo.com/>`__ (formerly OpenERP)



|

Authors / Autori
----------------

* `Agile BG <https://www.agilebg.com/>`__
* `SHS-AV s.r.l. <https://www.zeroincombenze.it/>`__
* `Didotech srl <http://www.didotech.com>`__


Contributors / Collaboratori
----------------------------

*  Lorenzo Battistini lorenzo.battistini@agilebg.com
*  Marco Marchiori marcomarkiori@gmail.com
*  Sergio Corato sergiocorato@gmail.com
*  Andrei Levin andrei.levin@didotech.com
*  Antonio M. Vigliotti antoniomaria.vigliotti@gmail.com

|

----------------


|en| **zeroincombenze®** is a trademark of `SHS-AV s.r.l. <https://www.shs-av.com/>`__
which distributes and promotes ready-to-use **Odoo** on own cloud infrastructure.
`Zeroincombenze® distribution of Odoo <https://wiki.zeroincombenze.org/en/Odoo>`__
is mainly designed to cover Italian law and markeplace.

|it| **zeroincombenze®** è un marchio registrato di `SHS-AV s.r.l. <https://www.shs-av.com/>`__
che distribuisce e promuove **Odoo** pronto all'uso sullla propria infrastuttura.
La distribuzione `Zeroincombenze® è progettata per le esigenze del mercato italiano.


|chat_with_us|


|

Last Update / Ultimo aggiornamento: 2018-11-20

.. |Maturity| image:: https://img.shields.io/badge/maturity-Alfa-red.png
    :target: https://odoo-community.org/page/development-status
    :alt: Alfa
.. |Build Status| image:: https://travis-ci.org/zeroincombenze/l10n-italy.svg?branch=8.0
    :target: https://travis-ci.org/zeroincombenze/l10n-italy
    :alt: github.com
.. |license gpl| image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |license opl| image:: https://img.shields.io/badge/licence-OPL-7379c3.svg
    :target: https://www.odoo.com/documentation/user/9.0/legal/licenses/licenses.html
    :alt: License: OPL
.. |Coverage Status| image:: https://coveralls.io/repos/github/zeroincombenze/l10n-italy/badge.svg?branch=8.0
    :target: https://coveralls.io/github/zeroincombenze/l10n-italy?branch=8.0
    :alt: Coverage
.. |Codecov Status| image:: https://codecov.io/gh/zeroincombenze/l10n-italy/branch/8.0/graph/badge.svg
    :target: https://codecov.io/gh/zeroincombenze/l10n-italy/branch/8.0
    :alt: Codecov
.. |OCA project| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-8.svg
    :target: https://github.com/OCA/l10n-italy/tree/8.0
    :alt: OCA
.. |Tech Doc| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-8.svg
    :target: https://wiki.zeroincombenze.org/en/Odoo/8.0/dev
    :alt: Technical Documentation
.. |Help| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-8.svg
    :target: https://wiki.zeroincombenze.org/it/Odoo/8.0/man
    :alt: Technical Documentation
.. |Try Me| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-8.svg
    :target: https://erp8.zeroincombenze.it
    :alt: Try Me
.. |OCA Codecov Status| image:: Unknown badge-oca-codecov
    :target: Unknown oca-codecov-URL
    :alt: Codecov
.. |Odoo Italia Associazione| image:: https://www.odoo-italia.org/images/Immagini/Odoo%20Italia%20-%20126x56.png
   :target: https://odoo-italia.org
   :alt: Odoo Italia Associazione
.. |Zeroincombenze| image:: https://avatars0.githubusercontent.com/u/6972555?s=460&v=4
   :target: https://www.zeroincombenze.it/
   :alt: Zeroincombenze
.. |en| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/flags/en_US.png
   :target: https://www.facebook.com/groups/openerp.italia/
.. |it| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/flags/it_IT.png
   :target: https://www.facebook.com/groups/openerp.italia/
.. |check| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/check.png
.. |no_check| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/no_check.png
.. |menu| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/menu.png
.. |right_do| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/right_do.png
.. |exclamation| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/exclamation.png
.. |warning| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/warning.png
.. |same| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/same.png
.. |late| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/late.png
.. |halt| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/halt.png
.. |info| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/info.png
.. |xml_schema| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/iso/icons/xml-schema.png
   :target: https://raw.githubusercontent.com/zeroincombenze/grymbcertificates/iso/scope/xml-schema.md
.. |DesktopTelematico| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/ade/icons/DesktopTelematico.png
   :target: https://raw.githubusercontent.com/zeroincombenze/grymbcertificates/ade/scope/DesktopTelematico.md
.. |FatturaPA| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/ade/icons/fatturapa.png
   :target: https://raw.githubusercontent.com/zeroincombenze/grymbcertificates/ade/scope/fatturapa.md
.. |chat_with_us| image:: https://www.shs-av.com/wp-content/chat_with_us.gif
   :target: https://tawk.to/85d4f6e06e68dd4e358797643fe5ee67540e408b
