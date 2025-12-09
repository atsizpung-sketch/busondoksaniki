import requests
import pandas as pd
import datetime

KINGDOM_ID = 3411  # senin krallık id’si

API_BASE = "https://api.riseofstats.com"

def fetch_governors(kingdom_id, page=1):
    url = f"{API_BASE}/kingdom/{kingdom_id}/power?page={page}"
    r = requests.get(url, timeout=20)
    if r.status_code != 200:
        return None
    return r.json()

def get_all_players(kingdom_id, max_pages=50):
    players = []
    for page in range(1, max_pages+1):
        data = fetch_governors(kingdom_id, page)
        if not data or "players" not in data:
            break
        for p in data["players"]:
            players.append({
                "Name": p.get("name"),
                "Power": p.get("power"),
                "Kills": p.get("kills"),
                "Kill_T4": p.get("t4kills"),
                "Kill_T5": p.get("t5kills"),
                "Dead": p.get("dead"),
                "Alliance": p.get("alliance"),
                "KP": p.get("kp")
            })
    return players

if __name__ == "__main__":
    players = get_all_players(KINGDOM_ID)
    if not players:
        print("No data fetched — check API or permissions.")
    else:
        df = pd.DataFrame(players)
        filename = f"kingdom_{KINGDOM_ID}_{datetime.date.today()}.xlsx"
        df.to_excel(filename, index=False)
        print("Excel created:", filename)
