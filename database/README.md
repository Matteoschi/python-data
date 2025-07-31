# 🗂️ Gestione Scadenze in Python

Questo programma consente di **gestire un database locale in formato JSON** per memorizzare informazioni relative a persone, date di scadenza e commenti associati (es. farmaci, bollette, documenti, ecc.).  
Fornisce funzionalità per leggere, aggiungere, modificare, eliminare e controllare scadenze imminenti.

## 📁 Struttura del File

Il database è salvato in un file JSON locale:
```python
file_path = r"database\file.json"
```

Ogni voce è strutturata come un dizionario con:json

```bash
{
  "nome": "Mario Rossi",
  "data": 20250731,
  "commento": "Farmaco A - 2 compresse al giorno"
}
```
## ⚙️ Funzionalità Principali
- 1	🔍 Leggi dati: Cerca una persona per nome e mostra le sue informazioni.
- 2	📝 Scrivi dati: Aggiunge una nuova voce al file JSON.
- 3	❌ Elimina dati: Rimuove una persona dal database.
- 4	✏️ Modifica dati: Permette di modificare nome, data o commento.
- 5	⏰ Controlla scadenze: Controlla se ci sono scadenze nei prossimi 3 giorni.
- 6	🚪 Esci dal programma

## ▶️ Avvio del Programma
Esegui il file con Python:

```bash
python nome_del_file.py
```
All'avvio, il programma controlla automaticamente se ci sono scadenze imminenti (entro 3 giorni).

## 🔐 Dipendenze
Il programma utilizza solo moduli standard Python:

- **json**
- **os**
- **datetime**

## 🔄 Esempi d'Uso
Aggiunta di una nuova voce
```bash
inserisci il nome : Mario
inserisci la data di scadenza : 20250801
inserisci il commento : Controllo annuale
```

Controllo scadenze

```bash
⚠️ Scadenza in arrivo per Mario: 2025-08-01
```
## ✅ Validazioni incluse
- Controllo automatico se il file esiste, con creazione se mancante.

- Verifica che la data sia in formato YYYYMMDD.

- Gestione sicura di errori JSON.

## 📌 Note
- Il file JSON deve contenere una lista di dizionari.

- Le date devono essere in formato numerico intero YYYYMMDD.

## 📂 Personalizzazione
Puoi modificare il percorso del file cambiando la variabile **file_path** all'inizio del programma ma anche modificando la data di scadenza **giorni_avviso**