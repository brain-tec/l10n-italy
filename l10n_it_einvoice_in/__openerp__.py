# -*- coding: utf-8 -*-
#
# Copyright 2015    - AgileBG SAGL <http://www.agilebg.com>
# Copyright 2015    - innoviu Srl <http://www.innoviu.com>
# Copyright 2018    - Lorenzo Battistini
# Copyright 2018    - Sergio Zanchetta (Associazione PNLUG - Gruppo Odoo)
# Copyright 2018-19 - Odoo Italia Associazione <https://www.odoo-italia.org>
# Copyright 2018-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
#
{
    'name': 'Italian Localization - Fattura elettronica - Ricezione',
    'summary': 'Ricezione fatture elettroniche',
    'version': '7.0.1.3.1',
    'category': 'Localization/Italy',
    'author': 'Odoo Community Association (OCA) and other subjects',
    'website': 'https://odoo-community.org/',
    'license': 'AGPL-3',
    'depends': [
        'account',
        'l10n_it_einvoice_base',
        'l10n_it_fiscal_ipa',
        'l10n_it_causali_pagamento',
    ],
    'installable': False,
    'description': r'''
Overview / Panoramica
=====================

|en| EInvoice in
----------------

This module allows to import Electronic Bill XML files version 1.2.1

http://www.fatturapa.gov.it/export/fatturazione/en/normativa/f-2.htm

received through the Exchange System (SdI).

http://www.fatturapa.gov.it/export/fatturazione/en/sdi.htm

|halt| Do not use this module on production environment: it is an aplha release
subjected to update.

For every supplier, it is possible to set the 'E-bills Detail Level':

 - Minimum level: Bill is created with no lines; User will have to create them, according to what specified in the electronic bill 
 - Maximum level: Every line contained in electronic bill will create a line in bill

Moreover, in supplier form you can set the 'E-bill Default Product': this product will be used, during generation of bills, when no other possible product is found. Tax and account of bill line will be set according to what configured in the product.

Every product code used by suppliers can be set, in product form, in

Inventory →  Products

If supplier specifies a known code in XML, the system will use it to retrieve the correct product to be used in bill line, setting the related tax and account.

 * Go to Accounting →  Purchases →  Electronic Bill
 * Upload XML file
 * View bill content clicking on 'Show preview'
 * Run 'Import e-bill' wizard to create a draft bill or run 'Link to existing bill' to link the XML file to an already (automatically) created bill

In the incoming electronic bill files list you will see, by default, files to be registered. These are files not yet linked to one or more bills.


|

|it| Fattura Elettronica in
---------------------------

Questo modulo consente di importare i file XML della fattura elettronica versione 1.2.1

http://www.fatturapa.gov.it/export/fatturazione/it/normativa/f-2.htm

ricevuti attraverso il Sistema di Interscambio (SdI).

http://www.fatturapa.gov.it/export/fatturazione/it/sdi.htm


::

    Destinatari:

Il modulo è destinato a tutte le aziende che dal 2019 dovranno emettere fattura elettronica


::

    Normativa:

Le leggi inerenti la fattura elettronica sono numerose. Potete consultare la `normativa fattura elettronica <https://www.fatturapa.gov.it/export/fatturazione/it/normativa/norme.htm>`__


Per ciascun fornitore è possibile impostare il "Livello dettaglio e-fatture":

 - Livello minimo: la fattura fornitore viene creata senza righe, che dovranno essere create dall'utente in base a quanto indicato nella fattura elettronica
 - Livello massimo: le righe della fattura fornitore verranno generate a partire da tutte quelle presenti nella fattura elettronica

Nella scheda fornitore è inoltre possibile impostare il "Prodotto predefinito per e-fattura": verrà usato, durante la generazione delle fatture fornitore, quando non sono disponibili altri prodotti adeguati. Il conto e l'imposta della riga fattura verranno impostati in base a quelli configurati nel prodotto.

Tutti i codici prodotto usati dai fornitori possono essere impostati nella relativa scheda, in

Magazzino →  Prodotti


|
|

Support / Supporto
------------------


|Zeroincombenze| This module is maintained by the `SHS-AV s.r.l. <https://www.zeroincombenze.it/>`__


|
|

Credits / Didascalie
====================

Copyright
---------

Odoo is a trademark of `Odoo S.A. <https://www.odoo.com/>`__ (formerly OpenERP)


|

Authors / Autori
----------------

* `Agile Business Group sagl <https://www.agilebg.com/>`__
* `Innoviu srl <http://www.innoviu.com>`__
* `Pointec s.r.l. <https://www.pointec.it/>`__
* `SHS-AV s.r.l. <https://www.zeroincombenze.it/>`__

Contributors / Collaboratori
----------------------------

* Lorenzo Battistini <lorenzo.battistini@agilebg.com>
* Roberto Onnis <roberto.onnis@innoviu.com>
* Alessio Gerace <alessio.gerace@agilebg.com>
* Cesare Pellegrini <cesare@pointec.it>
* Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>

|

----------------


|en| **zeroincombenze®** is a trademark of `SHS-AV s.r.l. <https://www.shs-av.com/>`__
which distributes and promotes ready-to-use **Odoo** on own cloud infrastructure.
`Zeroincombenze® distribution of Odoo <https://wiki.zeroincombenze.org/en/Odoo>`__
is mainly designed to cover Italian law and markeplace.

|it| **zeroincombenze®** è un marchio registrato da `SHS-AV s.r.l. <https://www.shs-av.com/>`__
che distribuisce e promuove **Odoo** pronto all'uso sulla propria infrastuttura.
La distribuzione `Zeroincombenze® <https://wiki.zeroincombenze.org/en/Odoo>`__ è progettata per le esigenze del mercato italiano.

|

This module is part of l10n-italy project.

Last Update / Ultimo aggiornamento: 2019-12-08

.. |Maturity| image:: https://img.shields.io/badge/maturity-Alfa-red.png
    :target: https://odoo-community.org/page/development-status
    :alt: Alfa
.. |Build Status| image:: https://travis-ci.org/zeroincombenze/l10n-italy.svg?branch=7.0
    :target: https://travis-ci.org/zeroincombenze/l10n-italy
    :alt: github.com
.. |license gpl| image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |license opl| image:: https://img.shields.io/badge/licence-OPL-7379c3.svg
    :target: https://www.odoo.com/documentation/user/9.0/legal/licenses/licenses.html
    :alt: License: OPL
.. |Coverage Status| image:: https://coveralls.io/repos/github/zeroincombenze/l10n-italy/badge.svg?branch=7.0
    :target: https://coveralls.io/github/zeroincombenze/l10n-italy?branch=7.0
    :alt: Coverage
.. |Codecov Status| image:: https://codecov.io/gh/zeroincombenze/l10n-italy/branch/7.0/graph/badge.svg
    :target: https://codecov.io/gh/zeroincombenze/l10n-italy/branch/7.0
    :alt: Codecov
.. |Tech Doc| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-7.svg
    :target: https://wiki.zeroincombenze.org/en/Odoo/7.0/dev
    :alt: Technical Documentation
.. |Help| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-7.svg
    :target: https://wiki.zeroincombenze.org/it/Odoo/7.0/man
    :alt: Technical Documentation
.. |Try Me| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-7.svg
    :target: https://erp7.zeroincombenze.it
    :alt: Try Me
.. |OCA Codecov| image:: https://codecov.io/gh/OCA/l10n-italy/branch/7.0/graph/badge.svg
    :target: https://codecov.io/gh/OCA/l10n-italy/branch/7.0
    :alt: Codecov
.. |Odoo Italia Associazione| image:: https://www.odoo-italia.org/images/Immagini/Odoo%20Italia%20-%20126x56.png
   :target: https://odoo-italia.org
   :alt: Odoo Italia Associazione
.. |Zeroincombenze| image:: https://avatars0.githubusercontent.com/u/6972555?s=460&v=4
   :target: https://www.zeroincombenze.it/
   :alt: Zeroincombenze
.. |en| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/flags/en_US.png
   :target: https://www.facebook.com/Zeroincombenze-Software-gestionale-online-249494305219415/
.. |it| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/flags/it_IT.png
   :target: https://www.facebook.com/Zeroincombenze-Software-gestionale-online-249494305219415/
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
   :target: https://github.com/zeroincombenze/grymb/blob/master/certificates/iso/scope/xml-schema.md
.. |DesktopTelematico| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/ade/icons/DesktopTelematico.png
   :target: https://github.com/zeroincombenze/grymb/blob/master/certificates/ade/scope/Desktoptelematico.md
.. |FatturaPA| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/ade/icons/fatturapa.png
   :target: https://github.com/zeroincombenze/grymb/blob/master/certificates/ade/scope/fatturapa.md
.. |chat_with_us| image:: https://www.shs-av.com/wp-content/chat_with_us.gif
   :target: https://tawk.to/85d4f6e06e68dd4e358797643fe5ee67540e408b
''',
}
