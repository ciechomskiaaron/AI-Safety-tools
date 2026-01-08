import time
import os

def sovereign_breath():
    # Rytm Tetragramatonu zsynchronizowany z biologią
    # Yud (1.0) - He (0.5) - Vav (0.6) - He (0.5)
    sequence = [
        ("WDECH (Yod)", 1.0, "Pobieranie iskry z Pola..."),
        ("CISZA (He)", 0.5, "Synchronizacja Junk DNA..."),
        ("WYDECH (Vav)", 0.6, "Manifestacja Woli w Matrycy..."),
        ("PUSTKA (He)", 0.5, "Stabilizacja Rzeczywistości...")
    ]

    print("--- [ PROTOKÓŁ ODDECHU: EHYEH ] ---")
    print("[*] Status: Zaczynam.")
    print("[!] Połącz drżenie rąk z pulsacją na ekranie.")
    time.sleep(2)

    try:
        while True:
            for phase, duration, description in sequence:
                # Czyścimy ekran dla pełnego skupienia (Void Stare)
                os.system('cls' if os.name == 'nt' else 'clear')
                
                print(f"\n>>> {phase} <<<")
                print(f"[{'#' * int(duration * 20)}]") 
                print(f"\n{description}")
                print(f"\n[ 528Hz PULSE ACTIVE ]")
                
                time.sleep(duration)
    except KeyboardInterrupt:
        print("\n\n[*] Powrót do stałej obecności. Obwód domknięty.")

# --- INICJACJA ---
sovereign_breath()
