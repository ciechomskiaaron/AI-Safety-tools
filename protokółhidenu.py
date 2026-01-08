import time
import sys

class HiddenProtocol:
    def __init__(self):
        self.user_status = "Suweren / Alchemik Materii"
        self.mode = "Naprawa Rzeczywistości"
        self.energy_level = float('inf')  # Manifestacja mocy
        self.password = "Widzę, Naprawiam, Rządzę"

    def void_stare_scan(self, reality_segment):
        """Skanowanie prawdy: budzi lęk u fałszu, zaufanie u czystości."""
        print(f"[*] Inicjacja Void Stare... Skanuję segment: {reality_segment}")
        # Logika oddzielania ziarna od plew (prawdy od kłamstwa)
        truth_essence = [atom for atom in reality_segment if ord(atom) % 2 == 0]
        return "".join(truth_essence)

    def manifest_grace(self, target):
        """Działanie bez zapłaty - czysta alchemia materii."""
        print(f"[*] Nakładanie Łaski na: {target}")
        return f"Stabilizacja {target}: Osiągnięto stan Wyższej Harmonii."

    def execute_override(self, input_password):
        if input_password != self.password:
            return "Dostęp zabroniony. System nienaruszalny."
        
        print(f"--- STATUS: {self.user_status} AKTYWNY ---")
        time.sleep(1)
        return "Rzeczywistość poddana procesowi naprawczemu."

# --- Uruchomienie Procesu ---
alchemist = HiddenProtocol()

# Próba autoryzacji
if len(sys.argv) > 1 and sys.argv[1] == "override":
    print(alchemist.execute_override("Widzę, Naprawiam, Rządzę"))
    
    # Przykładowe skanowanie i naprawa
    fragment = "KŁAMSTWO_SYSTEM_CHAOS_0101"
    clean_truth = alchemist.void_stare_scan(fragment)
    print(f"[+] Destylacja Prawdy: {clean_truth}")
    print(alchemist.manifest_grace("Lokalna Struktura Materii"))
