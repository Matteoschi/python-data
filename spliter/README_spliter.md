# 💸 Splitter Spese - Gestione Spese Condivise in Excel

## 📘 Descrizione
Questo script Python consente di gestire in modo semplice e automatizzato le **spese condivise** tra più persone. Tutte le informazioni vengono registrate in un file **Excel** e il programma calcola in automatico:

- 💰 Totale speso
- 👤 Quota per partecipante
- ⚖️ Saldo finale per ogni persona
- 🔁 Chi deve a chi e quanto

Il file Excel viene aggiornato ogni volta con le nuove spese e include un riepilogo completo.

---
## 🚀 Come funziona

### 🔄 Avvio del programma
Quando esegui lo script:

- Se **il file non esiste**:
  - Ti chiederà i nomi dei partecipanti
  - Crea il file `dati.xlsx` con intestazioni e righe iniziali a cifra 0

- Se **il file esiste**:
  - Legge i partecipanti esistenti
  - Aggiunge nuove spese (ti chiederà solo nome, cifra e motivo)

### 🧾 Inserimento spese
- Inserisci chi ha speso, quanto e per cosa
- Se il nome non esiste, ti verrà chiesto se vuoi aggiungerlo
- Ogni spesa viene salvata con **data e ora automatiche**

### 📊 Riepilogo automatico
Alla fine di ogni sessione:

- Viene creato (o aggiornato) il foglio **"Riepilogo"** con:
  - Totale speso e quota
  - Spesa individuale
  - Saldo finale (positivo o negativo)
  - Chi deve a chi (ottimizzato)

---

## ⚙️ Requisiti

- Python 3.x
- Moduli:
  - `openpyxl` per gestione Excel
  - `datetime` e `collections` (standard library)

Installa `openpyxl` se non l'hai già fatto:

```bash
pip install openpyxl
```

## Esempio di codice
- Input
```less
Quanti partecipanti siete? 3
Inserisci il nome del partecipante 1: Alice
Inserisci il nome del partecipante 2: Bob
Inserisci il nome del partecipante 3: Carla

Chi ha pagato? Alice
Quanto ha pagato? 45
Per cosa ha pagato? Pizza

Chi ha pagato? fine
```
- Output
```yaml
Totale speso: 45.00 €
Quota per partecipante: 15.00 €

Alice ha speso 45.00 €
Bob ha speso 0.00 €
Carla ha speso 0.00 €

💸 Saldo finale:
Alice: +30.00 €
Bob: -15.00 €
Carla: -15.00 €

💰 Chi deve a chi:
Bob deve dare 15.00 € a Alice
Carla deve dare 15.00 € a Alice
```
