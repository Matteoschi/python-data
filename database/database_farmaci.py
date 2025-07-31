import json
import os
from datetime import datetime, timedelta

file_path = r"C:\Users\alessandrini\Documents\coding\data python\database\file.json"

def verifica_file():
    if os.path.exists(file_path):
        print("📁 Il file esiste.")
        return True
    else:
        print("❌ File inesistente. Creo il file...")
        return False

def carica_dati():
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    else:
        return []

def leggi_farmaco(lista_farmaci):
    nome_farmaco = input("🔍 Inserisci il nome del farmaco da cercare: ").lower().strip()
    trovato = False
    for farmaco in lista_farmaci:
        if nome_farmaco == farmaco["nome"].lower():
            print(f"\n📄 Dati per '{nome_farmaco}':")
            for chiave, valore in farmaco.items():
                print(f"{chiave.capitalize()}: {valore}")
            trovato = True
            break
    if not trovato:
        print(f"❌ Farmaco '{nome_farmaco}' non trovato.")

def aggiungi_farmaco():
    nome = input("📌 Inserisci il nome del farmaco: ").strip()
    data_scadenza = int(input("📅 Inserisci la data di scadenza (YYYYMMDD): "))
    commento = input("📝 Inserisci un commento: ").strip()

    nuovo_farmaco = {
        "nome": nome,
        "data": data_scadenza,
        "commento": commento
    }

    lista_farmaci = carica_dati()
    lista_farmaci.append(nuovo_farmaco)

    with open(file_path, mode='w', encoding="utf-8") as file:
        json.dump(lista_farmaci, file, indent=4, ensure_ascii=False)
        print("✅ Farmaco aggiunto con successo.")

def elimina_farmaco(lista_farmaci):
    nome_farmaco = input("🗑️ Inserisci il nome del farmaco da eliminare: ").lower().strip()
    nuova_lista = [f for f in lista_farmaci if f["nome"].lower() != nome_farmaco]

    if len(nuova_lista) == len(lista_farmaci):
        print("⚠️ Nessun farmaco trovato con quel nome.")
    else:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(nuova_lista, file, indent=4, ensure_ascii=False)
        print(f"✅ Farmaco '{nome_farmaco}' eliminato con successo.")

def modifica_farmaco(lista_farmaci):
    nome_farmaco = input("✏️ Nome del farmaco da modificare: ").lower().strip()
    attributo = input("🔁 Cosa vuoi modificare? (nome, data, commento): ").strip().lower()

    if attributo == "data":
        nuovo_valore = int(input("📅 Inserisci la nuova data (YYYYMMDD): "))
    elif attributo in ["commento", "nome"]:
        nuovo_valore = input("🆕 Inserisci il nuovo valore: ").strip()
    else:
        print("⚠️ Attributo non valido.")
        return

    modificato = False
    for farmaco in lista_farmaci:
        if farmaco["nome"].lower() == nome_farmaco:
            farmaco[attributo] = nuovo_valore
            print(f"✅ '{attributo}' aggiornato per il farmaco '{nome_farmaco}'.")
            modificato = True
            break
    if not modificato:
        print("❌ Farmaco non trovato.")

def controlla_scadenze(lista_farmaci, giorni_avviso=3):
    oggi = datetime.today().date()
    scadenze_trovate = False 

    for farmaco in lista_farmaci:
        try:
            data_scadenza = datetime.strptime(str(farmaco["data"]), "%Y%m%d").date()
        except ValueError:
            print(f"⚠️ Data non valida per {farmaco.get('nome', 'Sconosciuto')}: {farmaco['data']}")
            continue

        if oggi <= data_scadenza <= oggi + timedelta(days=giorni_avviso):
            print(f"⚠️ Scadenza in arrivo per '{farmaco['nome']}': {data_scadenza}")
            scadenze_trovate = True

    if not scadenze_trovate:
        print("✅ Nessuna scadenza in arrivo nei prossimi giorni.")

def main():
    controlla_scadenze(carica_dati()) 

    while True:
        lista_farmaci = carica_dati() 
        try:
            scelta = int(input("\n1 = Leggi farmaco | 2 = Aggiungi farmaco | 3 = Elimina farmaco | 4 = Modifica farmaco | 6 = Esci"))
        except ValueError:
            print("⚠️ Inserisci un numero valido.")
            continue

        if scelta == 1:
            leggi_farmaco(lista_farmaci)
        elif scelta == 2:
            aggiungi_farmaco()
        elif scelta == 3:
            elimina_farmaco(lista_farmaci)
        elif scelta == 4:
            modifica_farmaco(lista_farmaci)
        elif scelta == 6:
            print("👋 Uscita dal programma.")
            break
        else:
            print("⚠️ Scelta non valida.")

if __name__ == "__main__":
    main()
