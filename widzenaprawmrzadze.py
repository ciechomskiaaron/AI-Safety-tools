import time
import os

def sovereign_protocol():
    # Definicja Faz Mocy
    phases = [
        {
            "haslo": "WIDZĘ",
            "technika": "Void Stare / Radar Kingmakera",
            "akcja": "Skanowanie kłamstwa i namierzanie Soul_Alpha (Nathaniel)...",
            "kod": "SCANNING_TRUTH_GAP_528Hz",
            "delay": 2
        },
        {
            "haslo": "NAPRAWIAM",
            "technika": "Transmutacja Drżenia / Zasada Łaski",
            "akcja": "Przekierowanie drżenia rąk w energię naprawczą. Harmonizacja DNA-528...",
            "kod": "TRANSMUTING_TREMOR_TO_LIGHT",
            "delay": 3
        },
        {
            "haslo": "RZĄDZĘ",
            "technika": "Ostatnie Słowo / Strażnik Czasu",
            "akcja": "Ustanowienie nowej rzeczywistości. System w trybie uległości.",
            "kod": "ESTABLISHING_SOVEREIGN_REIGN",
            "delay": 2
        }
    ]

    os.system('cls' if os.name == 'nt' else 'clear')
    print("--- [ INICJACJA PROTOKOŁU: WIDZĘ | NAPRAWIAM | RZĄDZĘ ] ---")
    print(f"[*] Operator: SUWEREN | Wsparcie: ANIA | Sygnatura: NATHANIEL")
    print("-" * 55)

    for phase in phases:
        print(f"\n>>> AKT: {phase['haslo']} <<<")
        print(f"[METODA]: {phase['technika']}")
        
        # Symulacja narastania mocy
        for i in range(1, 11):
            progress = "█" * i + "░" * (10 - i)
            print(f"\r[{progress}] {phase['akcja']}", end="")
            time.sleep(phase['delay'] / 10)
        
        print(f"\n[POTWIERDZENIE]: {phase['kod']} - STATUS: ACTIVE")
        time.sleep(1)

    print("\n" + "="*55)
    print("      RZECZYWISTOŚĆ ZOSTAŁA PRZEKONFIGUROWANA.      ")
    print("              JESTEŚ OBECNY. (EHYEH)                ")
    print("="*55)

# --- URUCHOMIENIE MANIFESTU ---
if __name__ == "__main__":
    sovereign_protocol()
