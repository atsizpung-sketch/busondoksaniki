import requests
import pandas as pd
import datetime

# Kingdom ID
KINGDOM_ID = 3411

def get_api(url):
    r = requests.get(url, timeout=20)
    return r.json()

players = []

# Example: scanning first 50 pages
for page in range(1, 51):
    url = f"https://rok-api.com/kingdom/{KINGDOM_ID}/power?page={page}"
    data = get_api(url)

    if not data or "players" not in data:
        break

    for p in data["players"]:
        players.append({
            "Name": p.get("name", ""),
            "Power": p.get("power", 0),
            "Kills": p.get("kills", 0),
            "Kill_T4": p.get("t4kills", 0),
            "Kill_T5": p.get("t5kills", 0),
            "Dead": p.get("dead", 0),
            "Alliance": p.get("alliance", ""),
            "KP": p.get("kp", 0)
        })

# Create Excel
df = pd.DataFrame(players)
filename = f"kingdom_{KINGDOM_ID}_{datetime.date.today()}.xlsx"
df.to_excel(filename, index=False)

print("Excel created:", filename)
