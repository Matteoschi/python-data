import os
from openpyxl import Workbook, load_workbook
from datetime import datetime

# File path and sheet name
FOLDER = "tournament_manager"
os.makedirs(FOLDER, exist_ok=True)
FILE = 'tournament.xlsx'
FILE_PATH = os.path.join(FOLDER, FILE)
SHEET_NAME = 'Players'

# List to store player names
player_list = []

def add_players():
    try:
        num_players = int(input("How many players are there? "))
    except ValueError:
        print("❌ Please enter a valid number.")
        return add_players()
    
    for i in range(num_players):
        while True:
            player = input(f"Enter name of player {i+1}: ").lower().strip()
            if player:
                if player in player_list:
                    print("⚠️ Player already registered. Choose a different name.")
                    continue
                print("✅ Player added.")
                player_list.append(player)
                break
            else:
                print("❌ Invalid name. Try again.")

    print(f"Registered players: {player_list}")

def read_players(registered_players):
    print("👥 Registered players:")
    for i, name in enumerate(registered_players, 1):
        print(f"{i}: {name}")

def register_match(registered_players):
    if len(registered_players) < 2:
        print("❌ At least two registered players are required to record a match.")
        return

    match_players = []
    print("✍️ Enter names of 2 players. Press Enter to stop.")

    for i in range(2):
        player_name = input("Player name: ").lower().strip()
        if not player_name:
            if len(match_players) < 2:
                print("❌ You must enter two players.")
                continue
            else:
                break
        if player_name not in [p.lower() for p in registered_players]:
            print("❌ Player not found.")
            continue
        if player_name in match_players:
            print("⚠️ Player already entered.")
            continue
        match_players.append(player_name)

    comment = ""
    if input("Do you want to add a match description? (y/n): ").strip().lower() == "y":
        comment = input("Enter comment: ").strip()

    score = input("Enter the result (e.g. 3-2): ").strip()
    try:
        score_a, score_b = map(int, score.split("-"))
        print(f"✅ Result: {score_a}-{score_b}")
    except ValueError:
        print("❌ Invalid score format. Use 'number-number' (e.g. 3-2).")

    date = datetime.now().strftime("%Y-%m-%d %H:%M")
    versus = " vs ".join(match_players)

    wb = load_workbook(FILE_PATH)

    if "Matches" not in wb.sheetnames:
        ws_matches = wb.create_sheet("Matches")
        ws_matches.append(["Date", "Player 1", "Player 2", "Score 1", "Score 2", "Score", "Comment"])
    else:
        ws_matches = wb["Matches"]

    ws_matches.append([date, match_players[0], match_players[1], score_a, score_b, score, comment])
    wb.save(FILE_PATH)
    print(f"✅ Match recorded: {versus} ({score})")
    if comment:
        print(f"📝 Comment saved: {comment}")

def add_new_players(registered_players):
    new_players = []
    try:
        n = int(input("🔢 How many new players do you want to add? "))
    except ValueError:
        print("❌ Please enter a valid number.")
        return

    for i in range(n):
        while True:
            name = input(f"Enter name for player {i+1}: ").strip().lower()
            if not name:
                print("❌ Invalid name. Try again.")
                continue
            if name in registered_players or name in new_players:
                print("⚠️ Player already exists. Choose another.")
                continue
            new_players.append(name)
            break

    if not new_players:
        print("❌ No players added.")
        return

    for name in new_players:
        ws.append([name])
    
    if len(new_players) > 1:
        print(f"✅ {len(new_players)} players added successfully.")
    else:
        print(f"✅ 1 player added successfully.")

    wb.save(FILE_PATH)

def update_statistics():
    wb = load_workbook(FILE_PATH)

    if "Statistics" in wb.sheetnames:
        del wb["Statistics"]
    ws_stats = wb.create_sheet("Statistics")
    print("Updating statistics sheet...")

    matches = []
    if "Matches" not in wb.sheetnames:
        print("❌ No matches recorded.")
        return

    ws_matches = wb["Matches"]
    for row in ws_matches.iter_rows(min_row=2, values_only=True):
        try:
            _, p1, p2, s1, s2, _, _ = row
            p1, p2 = p1.lower(), p2.lower()
            s1, s2 = int(s1), int(s2)
            matches.append((p1, p2, s1, s2))
        except (ValueError, TypeError):
            continue

    if not matches:
        print("❌ No valid matches found.")
        return

    stats = {}
    for p1, p2, s1, s2 in matches:
        for p in [p1, p2]:
            if p not in stats:
                stats[p] = {
                    "played": 0, "won": 0, "lost": 0, "drawn": 0,
                    "points_for": 0, "points_against": 0
                }

        stats[p1]["played"] += 1
        stats[p2]["played"] += 1

        stats[p1]["points_for"] += s1
        stats[p1]["points_against"] += s2
        stats[p2]["points_for"] += s2
        stats[p2]["points_against"] += s1

        if s1 > s2:
            stats[p1]["won"] += 1
            stats[p2]["lost"] += 1
        elif s2 > s1:
            stats[p2]["won"] += 1
            stats[p1]["lost"] += 1
        else:
            stats[p1]["drawn"] += 1
            stats[p2]["drawn"] += 1

    ws_stats.append([
        "Player", "Games Played", "Won", "Lost", "Drawn", "Points For", "Points Against", "Win Rate (%)"
    ])

    for player, s in stats.items():
        win_rate = round((s["won"] / s["played"]) * 100, 1) if s["played"] > 0 else 0.0
        drawn = s["drawn"] if s["drawn"] > 0 else "NA"
        ws_stats.append([
            player.capitalize(), s["played"], s["won"], s["lost"],
            drawn, s["points_for"], s["points_against"], win_rate
        ])
        print(f"\n👤 {player.capitalize()}")
        print(f"  • Games played: {s['played']}")
        print(f"  • Won: {s['won']}, Lost: {s['lost']}, Drawn: {drawn}")
        print(f"  • Points for: {s['points_for']}, Against: {s['points_against']}")
        print(f"  • Win rate: {win_rate}%")

    wb.save(FILE_PATH)
    print("\n📁 Statistics sheet updated and saved.")

# Main program
if not os.path.exists(FILE_PATH):
    print("🛠️ Creating new Excel file...")
    add_players()

    wb = Workbook()
    ws = wb.active
    ws.title = SHEET_NAME

    ws.append(["Players"])
    for player in player_list:
        ws.append([player])

    wb.save(FILE_PATH)
    print(f"✅ File '{FILE}' created in folder '{FOLDER}' with registered players.")
else:
    print(f"File '{FILE}' already exists in folder '{FOLDER}'.")
    print("Opening file...")
    try:
        wb = load_workbook(FILE_PATH)
        ws = wb[SHEET_NAME]
        print("✅ File opened successfully.")
        registered_players = [row[0] for row in ws.iter_rows(min_row=2, max_col=1, values_only=True) if row[0]]
        if not registered_players:
            print("❌ No players found in the file.")
    except ValueError:
        print(f"❌ Error opening file. Make sure it’s not open elsewhere: {ValueError}")

    while True:
        action = input("What do you want to do? [1=Add players, 2=List players, 3=Register match, 4=Statistics, 0=Exit]: ").strip()
        if action == "1":
            add_new_players(registered_players)
        elif action == "2":
            read_players(registered_players)
        elif action == "3":
            register_match(registered_players)
            wb = load_workbook(FILE_PATH)  # Reload updated file
        elif action == "4":
            update_statistics()
        elif action == "0":
            print("👋 Exiting program.")
            break