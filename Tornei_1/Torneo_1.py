import os
from openpyxl import Workbook, load_workbook
from datetime import datetime

# Percorso del file
FOLDER = "gestione Tornei"
os.makedirs(FOLDER, exist_ok=True)
FILE = 'torneo.xlsx'
FILE_PATH = os.path.join(FOLDER, FILE)
SHEET_NAME = 'Registro'

# Lista per contenere i nomi dei giocatori
list_player = []

# Funzione per aggiungere i giocatori
def aggiungere_giocatori():
    try:
        Num_player = int(input("Quanti giocatori siete? "))
    except ValueError:
        print("❌ Inserisci un numero valido.")
        return aggiungere_giocatori()
    
    for i in range(Num_player):
        while True:
            player = input(f"Inserire il nome del giocatore {i+1}: ").lower().strip()
            if player:
                if player in list_player:
                    print("⚠️ Giocatore già registrato, scegli un altro nome.")
                    continue
                print("✅ Giocatore aggiunto")
                list_player.append(player)
                break
            else:
                print("❌ Nome non valido, riprova.")

    print(f"I partecipanti sono: {list_player}")

def leggi_giocatori(giocatori_registrati):
    print("👥 leggo giocatori esistenti : ")
    for i , nome in enumerate(giocatori_registrati,1):
        print(f"{i} : {nome}")

def registro_partita(giocatori_registrati):
    if len(giocatori_registrati) < 2:
        print("❌ Servono  due giocatori registrati per registrare una partita.")
        return

    lis_players_name = []
    print("✍️ Inserisci i 2 nomi dei giocatori partecipanti . Premi Invio a vuoto per terminare.")
    
    for i in range(2):
        player_name = input("Nome giocatore: ").lower().strip()
        if not player_name:
            if len(lis_players_name) < 2:
                print("❌ Devi inserire almeno due giocatori.")
                continue
            else:
                break
        if player_name not in [g.lower() for g in giocatori_registrati]:
            print("❌ Giocatore inesistente.")
            continue
        if player_name in lis_players_name:
            print("⚠️ Giocatore già inserito.")
            continue
        lis_players_name.append(player_name)

    # Chiedi se l'utente vuole inserire un commento per la partita
    new_comment = input("Vuoi inserire una descrizione della partita? (s/n): ").strip().lower()
    if new_comment == "s":
        comment = input("Inserisci il commento: ").strip()
    else:
        comment = ""

    score= input("Inserisci il risultato (es. 3-2): ").strip()
    try:
        score_a, score_b = map(int, score.split("-"))
        print(f"✅ Risultato : {score_a}-{score_b}")
    except ValueError:
        print("❌ Formato risultato non valido. Usa il formato 'numero-numero' es (3-2).")

    date = datetime.now().strftime("%Y-%m-%d %H:%M")
    versus = " vs ".join(lis_players_name)

    # Salvataggio nel file Excel
    wb = load_workbook(FILE_PATH)
    
    if "Partite" not in wb.sheetnames:
        ws_partite = wb.create_sheet("Partite")
        ws_partite.append(["Data", "Giocatore 1", "Giocatore 2", "Punteggio 1", "Punteggio 2", "Risultato", "Commento"])
    else:
        ws_partite = wb["Partite"]

    ws_partite.append([date,lis_players_name[0], lis_players_name[1], score_a, score_b, score, comment])
    wb.save(FILE_PATH)
    print(f"✅ Partita registrata: {versus} ({score})")
    if comment:
        print(f"📝 Salvato commento: {comment}")

def nuovi_giocatori(giocatori_registrati):
    new_players= []
    try:
        N_player = int(input("🔢 Quanti giocatori vuoi aggiungere? "))
    except ValueError:
        print("❌ Inserisci un numero valido.")
        return

    for i in range(N_player):
        while True:
            name = input(f"Inserisci il nome del giocatore {i+1}: ").strip().lower()
            if not name:
                print("❌ Nome non valido. Riprova.")
                continue
            if name in giocatori_registrati or name in new_players:
                print("⚠️ Giocatore già presente. Scegline un altro.")
                continue
            new_players.append(name)
            break
    if not new_players:
        print("❌ Nessun giocatore aggiunto.")
        return  
    
    for name in new_players:
        ws.append([name])
    
    if len(new_players) != 1:
        print(f"✅ {len(new_players)} giocatori aggiunti con successo.")
    else:
        print(f"✅{len(new_players)} giocatore registrato con successo.")
        
    wb.save(FILE_PATH)

def statistiche():
    # 🔁 Ricarica il file aggiornato
    wb = load_workbook(FILE_PATH)

    # Elimina e ricrea il foglio "Statistiche"
    if "Statistiche" in wb.sheetnames:
        del wb["Statistiche"]
    ws_stats = wb.create_sheet("Statistiche")
    print("aggiornamento pagina statistiche . . .")

    partite = []
    if "Partite" not in wb.sheetnames:
        print("❌ Nessuna partita registrata.")
        return

    ws_partite = wb["Partite"]
    for row in ws_partite.iter_rows(min_row=2, values_only=True):
        try:
            _, g1, g2, p1, p2, _, _ = row
            g1, g2 = g1.lower(), g2.lower()
            p1, p2 = int(p1), int(p2)
            partite.append((g1, g2, p1, p2))
        except (ValueError, TypeError):
            continue

    if not partite:
        print("❌ Nessuna partita registrabile trovata.")
        return

    stats = {}
    for g1, g2, p1, p2 in partite:
        for g in [g1, g2]:
            if g not in stats:
                stats[g] = {
                    "giocate": 0, "vinte": 0, "perse": 0, "pareggiate": 0,
                    "punti_fatti": 0, "punti_subiti": 0
                }

        stats[g1]["giocate"] += 1
        stats[g2]["giocate"] += 1

        stats[g1]["punti_fatti"] += p1
        stats[g1]["punti_subiti"] += p2
        stats[g2]["punti_fatti"] += p2
        stats[g2]["punti_subiti"] += p1

        if p1 > p2:
            stats[g1]["vinte"] += 1
            stats[g2]["perse"] += 1
        elif p2 > p1:
            stats[g2]["vinte"] += 1
            stats[g1]["perse"] += 1
        else:
            stats[g1]["pareggiate"] += 1
            stats[g2]["pareggiate"] += 1

    # ✍️ Scrive intestazioni nel foglio "Statistiche"
    ws_stats.append([
        "Giocatore", "Partite Giocate", "Vinte", "Perse", "Pareggiate","Punti Fatti", "Punti Subiti", "Win Rate (%)"])

    # Scrive i dati nel foglio Excel + stampa
    for giocatore, s in stats.items():
        if s["giocate"] > 0:
            win_rate = round((s["vinte"] / s["giocate"]) * 100, 1)
        else:
            win_rate = 0.0

        if s["pareggiate"] > 0:
            pareggiate = s["pareggiate"]
        else:
            pareggiate = "NA"
        ws_stats.append([giocatore.capitalize(), s["giocate"], s["vinte"], s["perse"], pareggiate,s["punti_fatti"], s["punti_subiti"], win_rate])
        print(f"\n👤 {giocatore.capitalize()}")
        print(f"  • Partite giocate: {s['giocate']}")
        print(f"  • Vinte: {s['vinte']}, Perse: {s['perse']}, Pareggiate: {pareggiate}")
        print(f"  • Punti fatti: {s['punti_fatti']}, Subiti: {s['punti_subiti']}")
        print(f"  • Percentuale vittorie: {win_rate}%")

    # Salva le statistiche nel file
    wb.save(FILE_PATH)
    print("\n📁 Foglio 'Statistiche' aggiornato e salvato nel file Excel.")

# Se il file Excel non esiste, lo crea e salva i nomi dei giocatori
if not os.path.exists(FILE_PATH):
    print("🛠️ Creazione nuovo file Excel . . .")
    giocatori_registrati = aggiungere_giocatori()

    wb = Workbook()
    ws = wb.active
    ws.title = SHEET_NAME 

    ws.append(["Giocatori"])  
    for player in list_player:
        ws.append([player])  

    wb.save(FILE_PATH)
    print(f"✅ File '{FILE}' creato nella cartella '{FOLDER}' con i giocatori registrati.")
else:
    print(f"file {FILE} già esistente nel percorso: {FOLDER} ")
    print("apro file . . .")
    try:
        wb = load_workbook(FILE_PATH) 
        ws = wb[SHEET_NAME]
        print("✅ File aperto regolarmente")
        # Estrai i giocatori dal file
        giocatori_registrati = [row[0] for row in ws.iter_rows(min_row=2, max_col=1, values_only=True) if row[0]]
        if not giocatori_registrati:
            print("❌ Nessun giocatore trovato nel file.")
        
    except ValueError:
        print(f" ❌ problemi apertura file , verificare che sia chiuso: {ValueError}")
    
    while True:
        azione = input("Cosa vuoi fare? [1=Aggiungi giocatori, 2=Leggi giocatori, 3=Registra partita, 4=statistiche , 0=Esci]: ").strip()
        if azione == "1":
            nuovi_giocatori(giocatori_registrati)
        elif azione == "2":
            leggi_giocatori(giocatori_registrati)
        elif azione == "3":
            registro_partita(giocatori_registrati)
            wb = load_workbook(FILE_PATH)  # Ricarica il file aggiornato
        elif azione == "4":
            statistiche()
        elif azione == "0":
            print("👋 Chiudo il programma")
            break