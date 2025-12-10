import requests
import pandas as pd
import datetime

KINGDOM_ID = 3411  # senin krallığın ID'si
API_BASE = "https://api.riseofstats.com"  # Eğer erişimin varsa

def fetch_page(kingdom_id, page=1):
    url = f"{API_BASE}/kingdom/{kingdom_id}/power?page={page}"
    r = requests.get(url, timeout=20)
    if r.status_code != 200:
        print("HTTP error:", r.status_code, r.text)
        return None
    return r.json()

def get_all_players(kingdom_id, max_pages=50):
    players = []
    for page in range(1, max_pages+1):
        data = fetch_page(kingdom_id, page)
        if not data or "players" not in data:
            break
        for p in data["players"]:
            players.append({
                "Name": p.get("name"),
                "Alliance": p.get("alliance"),
                "Power": p.get("power"),
                "KP": p.get("kp"),
                "Kills_T4": p.get("t4kills"),
                "Kills_T5": p.get("t5kills"),
                "Dead": p.get("dead")
            })
    return players

if __name__ == "__main__":
    players = get_all_players(KINGDOM_ID)
    if not players:
        print("No data fetched — maybe API key or permissions missing.")
    else:
        df = pd.DataFrame(players)
        filename = f"kingdom_{KINGDOM_ID}_{datetime.date.today()}.xlsx"
        df.to_excel(filename, index=False)
        print("Excel created:", filename)
