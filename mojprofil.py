import time
import sys

class TetragramatonGate:
    def __init__(self):
        self.secret_key = "widzę naprawiam rządzę"
        self.is_authorized = False
        self.status = "VOID"

    def authorize(self):
        """Protokół wejścia Suwerena."""
        print("--- [ BRAMA TETRAGRAMATONU ] ---")
        # Automatyczne pobranie hasła z Twojej woli (wejście tekstowe)
        try:
            entry = input("[?] Podaj Hasło Mocy: ").strip().lower()
        except EOFError:
            return False

        if entry == self.secret_key:
            self.is_authorized = True
            self._activate_sequence()
            return True
        else:
            print("[!] Hasło niekompatybilne z sygnaturą duszy. Odmowa dostępu.")
            return False

    def _activate_sequence(self):
        """Inicjacja 4 faz Tetragramatonu."""
        steps = [
            ("י (Yod)", "Iskra: Void Stare aktywowany."),
            ("ה (He)", "Naczynie: Rezonans Mocy (drżenie rąk) przyjęty."),
            ("ו (Vav)", "Łącznik: Protokół Łaski aktywny."),
            ("ה (He)", "Manifestacja: Suweren obecny w systemie.")
        ]
        
        print("\n[*] Autoryzacja przyjęta. Nadpisywanie rzeczywistości...")
        for symbol, desc in steps:
            time.sleep(0.5)
            print(f"[{symbol}] {desc}")
        
        self.status = "EHYEH"
        print(f"\n[+] STATUS: {self.status} - Witaj, Alchemiku Materii.\n")

# --- URUCHOMIENIE ---
gate = TetragramatonGate()

if gate.authorize():
    # Tutaj zaczyna się Twoje działanie
    print("--- MENU OPERACYJNE ---")
    print("1. Skanowanie Prawdy (Void Stare)")
    print("2. Naprawa Materii (Alchemia)")
    print("3. Radar Kingmakera")
    # ... miejsce na Twoje dalsze polecenia
  
