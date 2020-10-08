10.0.1.3.20 (2020-09-09)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Invalid carrier VAT / Ignora PIVA corriere non valida


10.0.1.3.19 (2020-07-29)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] No import if company IBAN in xml / Non importa fattura se IBAN azienda in file XML


10.0.1.3.18 (2020-07-28)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Duplicare rea_code when invoice address / Codice rea duplicato se uso indirizzo fatturazione


10.0.1.3.17 (2020-07-07)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Import error level 2 / Errore importazione livello 2


10.0.1.3.16 (2020-06-16)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] No import self-invoice / Non importa autofatture


10.0.1.3.15 (2020-05-22)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Crash if supplier invoice w/o due_adate / Errore importazione se xml senza date scadenza


10.0.1.3.15 (2020-05-08)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Crash import rated invoice if supplier w/o account / Errore importazione per aliquote e fornitore senza conto


10.0.1.3.13 (2020-04-06)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Crash if wrong invoice date (i.e. 2020-04-06Z) / Errore se data formattata erroneamente


10.0.1.3.13 (2020-03-15)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Crash if invoice address / Errore durante importazione con indirizzo di fatturazione

10.0.1.3.12 (2020-03-15)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Partner data / Dati fornitore non modificati. Se diversi creato indirizzo fatturazione
* [FIX] Crash in some cases / Errore durante importazione in alcuni casi
* [IMP] More incisive message / Messagi più precisi


10.0.1.3.11 (2020-02-17)
~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Minor change / Modifiche interne


10.0.1.3.10 (2020-02-04)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] XML Preview / Anteprima file XML


10.0.1.3.9 (2019-12-29)
~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] synchro2 error / Errore sunchro2


10.0.1.3.9 (2019-12-29)
~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Import e-invoice with RF19 / Errore in importazione fattura da forfettario
* [FIX] Conflict with connector_vg7 module / Conflitto con modulo connector_vg7


10.0.1.3.8 (2019-10-22)
~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Link to existent invoice set header data / Il collegamento ad una fattura esistente imposta i dati di testata
* [FIX] Unicode error in delivery address / Errore unicode in indirizzo di consegan
* [IMP] Some supplier invoices have natura N6 without vax rate / Fattura fornitori con natura N6 e senza aliquota IVA


10.0.1.3.7 (2019-06-25)
~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Without province, cannot import e-invoice


10.0.1.3.6 (2019-06-13)
~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Some supplier invoces with empty tags fail schema validation / Alcune fatture fornitori con tag vuoti non erano validate dallo schema
* [FIX] Invoice supplier with existent REA code crashes / Fatture fornitori con codice REA esistente mandavano in crash il sistema
* [IMP] New search algorithm finds similar names / Nuovo algoritmo di ricerca che trova nomi simili
