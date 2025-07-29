# 🏓 Gestione Tornei in Excel

Un'applicazione Python per registrare partite tra giocatori, salvare i dati in un file Excel e generare automaticamente statistiche personalizzate.

## 📁 Struttura del progetto

- Crea una cartella chiamata `gestione Tornei`
- Crea/gestisce un file Excel `torneo.xlsx`
- Contiene 3 fogli:
  - `Registro`: elenco dei giocatori registrati
  - `Partite`: storico delle partite giocate
  - `Statistiche`: analisi delle performance dei giocatori

## 🧩 Funzionalità

### ✅ Aggiunta Giocatori
Permette di inserire un numero personalizzato di giocatori con verifica dei nomi.

### 📖 Lettura Giocatori
Stampa in console l'elenco dei giocatori registrati nel file Excel.

### 📝 Registrazione Partita
- Consente di registrare una partita tra **almeno 2 giocatori**
- Viene richiesto:
  - Nome dei partecipanti
  - Risultato (es. `3-2`)
  - Eventuale commento
- I dati vengono salvati nel foglio **Partite**

### 📊 Statistiche Automatiche
Genera un foglio Excel chiamato `Statistiche` con:
- Partite giocate
- Vinte, perse, pareggiate
- Punti fatti e subiti
- Percentuale vittorie

Stampa anche le statistiche in console.

## 🛠️ Requisiti

- Python ≥ 3.6
- [openpyxl](https://openpyxl.readthedocs.io/en/stable/) (`pip install openpyxl`)

## ▶️ Avvio del Programma

Esegui il file Python. Al primo avvio ti verrà chiesto di inserire i giocatori. Se il file esiste già, ti verranno presentate varie opzioni


## 💡 Esempio di flusso

1. Aggiungi 4 giocatori
2. Registra una partita tra `matteo` e `davide` con risultato `5-3`
3. Genera le statistiche
4. Aggiungi nuovi giocatori o visualizza i dati già salvati

## 📂 Salvataggio Dati

Tutti i dati vengono salvati nel file: gestione Tornei/torneo.xlsx


Puoi aprirlo con Excel per vedere e modificare direttamente i dati (ma chiudi Excel prima di rilanciare lo script!).

## 🔐 Note

- Tutti i nomi sono salvati in **minuscolo** per evitare duplicati.
- Il programma è **robusto**: gestisce errori comuni come formati errati o nomi duplicati.
- Se non ci sono pareggi, nel foglio `Statistiche` verrà indicato "NA" sotto la colonna "Pareggiate".

## 📌 To-do (idee future)
- Aggiunta data personalizzata alla partita
- Supporto a più di 2 giocatori per match
- Interfaccia grafica (GUI) con Tkinter o PyQt
- Esportazione grafici delle statistiche

---

🎉 Buon torneo!