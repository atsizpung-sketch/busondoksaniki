import pandas as pd
import datetime

# Örnek oyuncu verisi
players = [
    {"Name": "Player1", "Power": 5000000, "Kills": 1000, "Kill_T4": 500, "Kill_T5": 200, "Dead": 50, "Alliance": "Alpha", "KP": 1500},
    {"Name": "Player2", "Power": 3000000, "Kills": 800, "Kill_T4": 300, "Kill_T5": 100, "Dead": 20, "Alliance": "Beta", "KP": 1200},
    {"Name": "Player3", "Power": 7000000, "Kills": 1500, "Kill_T4": 700, "Kill_T5": 400, "Dead": 100, "Alliance": "Gamma", "KP": 2100}
]

# Excel oluştur
df = pd.DataFrame(players)
filename = f"kingdom_test_{datetime.date.today()}.xlsx"
df.to_excel(filename, index=False)

print("Excel created:", filename)
