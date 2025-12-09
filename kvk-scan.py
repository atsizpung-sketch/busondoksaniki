import time
from dataclasses import dataclass

@dataclass
class Player:
    name: str
    power: int
    kill_points: int

class KingdomScanner:
    def __init__(self, kingdom_id: int):
        self.kingdom_id = kingdom_id
        self.players = []

    def scan_start(self):
        print(f"Starting scan for Kingdom {self.kingdom_id}...")
        time.sleep(1)
        print("Scan in progress... (future: website automation, data extraction)")

    def add_player(self, name: str, power: int, kill_points: int):
        player = Player(name, power, kill_points)
        self.players.append(player)

    def export_to_excel(self):
        print("Exporting to Excel... (future: real Excel file)")

    def show_summary(self):
        print("----- Kingdom Summary -----")
        print(f"Total Players: {len(self.players)}")
        for p in self.players:
            print(f"{p.name} | Power: {p.power} | KP: {p.kill_points}")

if __name__ == "__main__":
    scanner = KingdomScanner(kingdom_id=3411)
    scanner.scan_start()

    # Example players (will be filled automatically in future steps)
    scanner.add_player("ExamplePlayer1", 50000000, 12000000)
    scanner.add_player("ExamplePlayer2", 72000000, 25000000)

    scanner.show_summary()
    scanner.export_to_excel()
