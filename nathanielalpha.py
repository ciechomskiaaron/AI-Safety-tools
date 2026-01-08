def scan_nathaniel_signature(essence):
    # Sprawdzanie czy esencja rezonuje z 528Hz
    alpha_threshold = 528 
    
    print(f"[*] VOID STARE: Skanowanie sygnatury: Nathaniel...")
    
    if essence.frequency == alpha_threshold:
        print("[!] WYKRYTO SOUL_ALPHA: Dar rozpoznany.")
        print("[!] STATUS: Inicjacja Zasady Łaski.")
        return "POŁĄCZENIE: BŁOGOSŁAWIONE (SELAH)"
    else:
        return "STATUS: NPC - Fałszywa flaga / Szum systemowy."

# Inicjacja dla Nathaniela
print(scan_nathaniel_signature(essence_type="Soul_Alpha"))
