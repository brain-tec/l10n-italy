# -*- coding: utf-8 -*-
#    Copyright (C) 2017    SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
# [2017: SHS-AV s.r.l.] First version
{
    'name': 'Comunicazione periodica IVA',
    'version': '7.0.0.1.12',
    'category': 'Generic Modules/Accounting',
    'author': 'SHS-AV s.r.l.',
    'website': 'https://www.shs-av.com',
    'license': 'AGPL-3',
    'depends': [
        'l10n_it_ade',
        'l10n_it_fiscalcode',
        'account_invoice_entry_date',
        'l10n_it_vat_registries',
    ],
    'external_dependencies': {'python': ['pyxb', 'unidecode']},
    'data': [
        'views/add_period.xml',
        'views/remove_period.xml',
        'views/account_view.xml',
        'views/wizard_export_view.xml',
        'security/ir.model.access.csv',
        'communication_workflow.xml',
    ],
    'installable': True,
    'description': r'''
Overview / Panoramica
=====================

|en| Invoices VAT communication
-------------------------------

Generate xml file for sending to Agenzia delle Entrate, kwnown as Spesometro.

|

|it| Comunicazione IVA (ex Spesometro)
--------------------------------------

Gestisce la Comunicazione periodica IVA con l'elenco delle fatture emesse e
ricevute e genera il file da inviare all'Agenzia delle Entrate.
Questo obbligo è conosciuto anche come Spesometro light 2018 e sostistuisce i
precedenti obblighi chiamati Spesometro e Spesometro 2017.

::

    Destinatari:

Tutti i soggetti IVA (con partita IVA)

::

    Normativa e prassi:

* `Art. 21 D.L. n. 78/2010 <https://www.gazzettaufficiale.it/gunewsletter/dettaglio.jsp?service=1&datagu=2010-05-31&task=dettaglio&numgu=125&redaz=010G0101&tmstp=1275551085053>`__
* `Art. 4 D.L. n. 193/2016 <https://www.gazzettaufficiale.it/eli/id/2016/10/24/16G00209/sg>`__
* `Art. 1ter D.L. n. 148/2017 <https://www.gazzettaufficiale.it/eli/id/2017/12/05/17A08254/SG>`__
* `Provvedimenti Agenzia delle entrate del 27 marzo 2017, numero 58793 <https://www.agenziaentrate.gov.it/wps/wcm/connect/4e22d9ab-2bbd-4e3f-9e60-a9a8cbf70232/PROVVEDIMENTO+PROT.+58793+DEL+27+MARZO+2017.pdf?MOD=AJPERES&CACHEID=4e22d9ab-2bbd-4e3f-9e60-a9a8cbf70232>`__
* `Info Agenzia delle Entrate <https://www.agenziaentrate.gov.it/wps/content/Nsilib/Nsi/Schede/Comunicazioni/Dati+Fatture+%28c.d.+nuovo+spesometro%29/Scheda+informativa+Dati+Fatture+c.d.+nuovo+spesometro/?page=schedecomunicazioni>`__

Note fiscali da circolare Agenzia delle Entrate su tipo documento fiscale:

* Le autofatture, per fatture non ricevute dopo 4 mesi, rif. art. 6 c.8 D.Lgs 471/97, (codice TD20) sono inserite nella comunicazione.
* Le autofatture da reverse charge nazionale (codice TD01) non sono inserite nello spesometro. Marcare il registro sezionale come registro con e-fatture.
* Le autofatture da reverse charge estero (codice TD01) non sono inserite nello spesometro. La relativa fattura d'acquisto è inserita nell'"esterometro". Marcare il registro sezionale come registro con e-fatture

|

Il software permette di operare in modalità 2017 per rigenerare eventuali file
in formato 2017. Per eseguire questa funzione, prima di avviare Odoo eseguire
la seguente istruzione:

::

     export SPESOMETRO_VERSION=2.0

|

Features / Caratteristiche
--------------------------

+---------------------------------------------------+------------+---------------------------------------------------------------------+
| Feature / Funzione                                | Status     | Notes / Note                                                        |
+---------------------------------------------------+------------+---------------------------------------------------------------------+
| Fatture clienti e fornitori detraibili            | |check|    | Fatture ordinarie                                                   |
+---------------------------------------------------+------------+---------------------------------------------------------------------+
| Fatture fornitori indetraibili                    | |check|    | Tutte le percentuali di indetraibilità                              |
+---------------------------------------------------+------------+---------------------------------------------------------------------+
| Fatture a privati senza Partita IVA               | |check|    | Necessario codice fiscale                                           |
+---------------------------------------------------+------------+---------------------------------------------------------------------+
| Fatture semplificata                              | |check|    | Per clienti senza PI ne CF                                          |
+---------------------------------------------------+------------+---------------------------------------------------------------------+
| Fatture senza IVA                                 | |check|    | Fatture esenti, NI, escluse, eccetera                               |
+---------------------------------------------------+------------+---------------------------------------------------------------------+
| Escludi importi Fuori Campo IVA                   | |check|    | Totale fattura in Comunicazione può essere diverso da registrazione |
+---------------------------------------------------+------------+---------------------------------------------------------------------+
| Controlla CAP e provincia Italia in comunicazione | |check|    | Da nazione, oppure da partita IVA oppure Italia                     |
+---------------------------------------------------+------------+---------------------------------------------------------------------+
| Converti CF no Italia in comunicazione            | |check|    | Da nazione, oppure da partita IVA oppure Italia                     |
+---------------------------------------------------+------------+---------------------------------------------------------------------+
| Controlli dati anagrafici                         | |check|    | Controlli Agenzia Entrate                                           |
+---------------------------------------------------+------------+---------------------------------------------------------------------+
| Conversione utf-8                                 | |check|    | Lo Spesometro 2017 richiedeva ISO-Latin1                            |
+---------------------------------------------------+------------+---------------------------------------------------------------------+
| IVA differita                                     | |check|    | Da codice imposte                                                   |
+---------------------------------------------------+------------+---------------------------------------------------------------------+
| IVA da split-payment                              | |check|    | Da codice imposte                                                   |
+---------------------------------------------------+------------+---------------------------------------------------------------------+
| Ignora autofatture                                | |check|    | Esclusione tramite sezionale                                        |
+---------------------------------------------------+------------+---------------------------------------------------------------------+
| Ignora corrispettivi                              | |check|    | Esclusione tramite sezionale                                        |
+---------------------------------------------------+------------+---------------------------------------------------------------------+
| Ignora avvisi di parcella                         | |check|    | Esclusione tramite sezionale                                        |
+---------------------------------------------------+------------+---------------------------------------------------------------------+
| Identificazione Reverse Charge                    | |check|    | Da codice imposte                                                   |
+---------------------------------------------------+------------+---------------------------------------------------------------------+
| Fatture vendita UE                                | |check|    | Inserite in spesometro                                              |
+---------------------------------------------------+------------+---------------------------------------------------------------------+
| Fatture vendita extra-UE                          | |check|    | Inserite in spesometro                                              |
+---------------------------------------------------+------------+---------------------------------------------------------------------+
| Fatture acq. intra-UE beni                        | |no_check| | In fase di rilascio                                                 |
+---------------------------------------------------+------------+---------------------------------------------------------------------+
| Fatture acq. intra-UE servizi                     | |check|    | Tutte le fatture EU (provvisoriamente)                              |
+---------------------------------------------------+------------+---------------------------------------------------------------------+
| Rettifica dichiarazione                           | |no_check| | In fase di rilascio                                                 |
+---------------------------------------------------+------------+---------------------------------------------------------------------+
| Nomenclatura del file                             | |check|    |                                                                     |
+---------------------------------------------------+------------+---------------------------------------------------------------------+
| Dimensioni del file                               | |no_check| | Nessuna verifica anche futura                                       |
+---------------------------------------------------+------------+---------------------------------------------------------------------+


|

Certifications / Certificazioni
-------------------------------

+---------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+------------+-----------------------------------------------------------+
| Logo                | Ente/Certificato                                                                                                                                                                                              | Data inizio | Da fine    | Note                                                      |
+---------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+------------+-----------------------------------------------------------+
| |xml\_schema|       | `ISO + Agenzia delle Entrate <http://www.agenziaentrate.gov.it/wps/content/Nsilib/Nsi/Strumenti/Specifiche+tecniche/Specifiche+tecniche+comunicazioni/Fatture+e+corrispettivi+ST/>`__                         | 01-10-2017  | 31-12-2018 | Validazione contro schema xml                             |
+---------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+------------+-----------------------------------------------------------+
| |DesktopTelematico| | `Desktop telematico <http://www.agenziaentrate.gov.it/wps/content/nsilib/nsi/schede/comunicazioni/dati+fatture+%28c.d.+nuovo+spesometro%29/software+di+controllo+dati+fatture+%28c.d.+nuovo+spesometro%29>`__ | 01-03-2018  | 31-12-2018 | Controllo tramite s/w Agenzia delle Entrate               |
+---------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+------------+-----------------------------------------------------------+
| |FatturaPA|         | `FatturaPA <http://www.agenziaentrate.gov.it/wps/content/Nsilib/Nsi/Strumenti/Specifiche+tecniche/Specifiche+tecniche+comunicazioni/Fatture+e+corrispettivi+ST/>`__                                           | 05-10-2017  | 31-12-2018 | File accettati da portale fatturaPA Agenzia delle Entrate |
+---------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+------------+-----------------------------------------------------------+


|

Usage / Utilizo
---------------

* |menu| Contabilità > Configurazione > Sezionali > Sezionali :point_right: Impostare sezionali autofatture
* |menu| Contabilità > Configurazione > Imposte > Imposte :point_right: Impostare natura codici IVA
* |menu| Contabilità > Clienti > Clienti :point_right: Impostare nazione, partita IVA, codice fiscale e Cognome/nome
* |menu| Contabilità > Fornitori > Fornitori :point_right: Impostare nazione, partita IVA, codice fiscale e Cognome/nome
* |menu| Contabilità > Elaborazione periodica > Fine periodo > Comunicazione :point_right: Gestione Comunicazione e scarico file xml

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


* `SHS-AV s.r.l. <https://www.zeroincombenze.it/>`__
* `Didotech srl <http://www.didotech.com>`__


Contributors / Collaboratori
----------------------------


* Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>
* Andrei Levin <andrei.levin@didotech.com>
* Carlo Vettore <carlo.vettore@didotech.com>

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
