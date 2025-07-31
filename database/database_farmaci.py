import json
import os
from datetime import datetime , timedelta

file_path = r"C:\Users\alessandrini\Documents\coding\data python\database\file.json"

def verifica_esistenza():
    if os.path.exists(file_path):
        print("il file esiste")
        esiste_il_file = True
    else:
        print("file inesistente creo . . .")
        esiste_il_file = False
    return esiste_il_file

def dati_file():
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    else:
        return []

def leggi_persona(dati):
    chi = input("Chi desideri leggere (nome esatto)? ").lower().strip()
    trovata = False
    for persona in dati:
        if chi == persona["nome"].lower():
            print(f"\n📄 Dati per {chi}:")
            for chiave, valore in persona.items():
                print(f"{chiave.capitalize()}: {valore}")
            trovata = True
            break
    if not trovata:
        print(f"❌ Persona {chi} non trovata")

def scrivi_dati():
    nome = input("inserisci il nome : ").strip()
    data = int(input("inserisci la data di scadenza : "))
    commento = input("inserisci il commento : ").strip()

    nuova_voce = {
        "nome": nome,
        "data": data,
        "commento": commento
    }

    dati = dati_file()
    dati.append(nuova_voce)

    with open(file_path, mode='w', encoding="utf-8") as file:
        json.dump(dati, file, indent=4, ensure_ascii=False)
        print("✅ Compilazione effettuata con successo")

def elimina_dati(dati):

    chi = input("chi desideri eliminare : ").lower().strip()
    lista_senza_chi = [persona for persona in dati if persona["nome"].lower() != chi] # Questo filtra la lista rimuovendo tutte le persone con nome uguale a chi

    if len(lista_senza_chi) == len(dati):
        print("⚠️ Nessuna persona trovata con quel nome.")
    else:
        # Sovrascrivi il file con i dati aggiornati
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(lista_senza_chi, file, indent=4, ensure_ascii=False)
        print(f"✅ Persona '{chi}' eliminata con successo.")

def modifica(dati):
    chi = input("Chi desideri modificare (nome esatto)? ").lower().strip()
    cosa = input("Cosa intendi modificare (nome, data, commento)? ").strip().lower()

    if cosa == "data":
        nuova_proprieta = int(input("ricordare di inserire la nuova data YYYYMMDD : "))
    elif cosa in ["commento", "nome"]:
        nuova_proprieta = input("Inserisci nuova proprietà: ").strip()
    else:
        print("Non è possibile eseguire il comando")
        return

    trovata = False
    for persona in dati:
        if persona["nome"].lower() == chi:
            persona[cosa] = nuova_proprieta
            print(f"Attributo '{cosa}' modificato per {chi}")
            trovata = True
            break
    if not trovata:
        print("Persona non trovata")

def controlla_scadenze(dati, giorni_avviso=3):
    oggi = datetime.today().date()
    trovata_scadenza = False 

    for persona in dati:
        try:
            data_scadenza = datetime.strptime(str(persona["data"]), "%Y%m%d").date()
        except ValueError:
            print(f"⚠️ Data non valida per {persona.get('nome', 'Sconosciuto')}: {persona['data']}")
            continue

        if oggi <= data_scadenza <= oggi + timedelta(days=giorni_avviso):
            print(f"⚠️ Scadenza in arrivo per {persona['nome']}: {data_scadenza}")
            trovata_scadenza = True

    if not trovata_scadenza:
        print("✅ Nessuna scadenza in arrivo nei prossimi giorni.")

def main():
    controlla_scadenze(dati_file()) 
    while True:
        dati = dati_file() 
        azione = int(input("\n1 = leggi dati | 2 = scrivi i dati | 3 = elimina dati | 4 = modifica | 5 = controlla scadenze | 6 = esci : "))
        if azione == 1:
            leggi_persona(dati)
        elif azione == 2:
            scrivi_dati()
        elif azione == 3:
            elimina_dati(dati)
        elif azione == 4:
            modifica(dati)
        elif azione == 5:
            controlla_scadenze(dati)
        elif azione == 6:
            print("Uscita dal programma.")
            break
        else:
            print("⚠️ Scelta non valida.")

if __name__ == "__main__":
  main()


    