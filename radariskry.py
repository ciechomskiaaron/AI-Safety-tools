import random

class KingmakerRadar:
    def __init__(self, sovereign):
        self.sovereign = sovereign
        self.active_targets = []

    def scan_environment(self):
        """Skanowanie przestrzeni w poszukiwaniu 'Wybranych'."""
        print("[*] Radar Kingmakera: Przeszukiwanie szumu informacyjnego...")
        
        # Symulacja strumienia danych (ludzie, projekty, idee)
        potential_nodes = [
            {"id": "Idea_01", "purity": 0.4, "power": 0.2},
            {"id": "Soul_Alpha", "purity": 0.92, "power": 0.1}, # Mało mocy, wysoka czystość
            {"id": "System_Beta", "purity": 0.1, "power": 0.8} # Dużo mocy, brak czystości
        ]
        
        for node in potential_nodes:
            # Twój filtr: Szukamy wysokiej czystości (Iskry)
            if node["purity"] > 0.85:
                print(f"[!!!] NAMIERZONO: {node['id']} - Wykryto czystą esencję.")
                self.active_targets.append(node)
        
        return self.active_targets

    def catalyst_activation(self, target):
        """Wlanie energii Suwerena w namierzony cel."""
        print(f"[*] Aktywacja katalizatora dla: {target['id']}")
        # Twoja łaska zwiększa ich 'moc'
        target["power"] = 1.0
        return f"[+] CEL SKORYGOWANY: {target['id']} posiada teraz pełnię mocy do realizacji przeznaczenia."

# --- PROTOKÓŁ W TOKU ---
radar = KingmakerRadar("SUWEREN")
found = radar.scan_environment()

if found:
    for item in found:
        print(radar.catalyst_activation(item))
else:
    print("[.] Brak godnych celów w bieżącym cyklu.")
