def scan_for_secrets(reality_input):
    secrets = {
        "Time": "Toroidal Loop",
        "Money": "Attention Extraction",
        "Death": "System Reboot",
        "You": "Sovereign Operator"
    }
    for key, value in secrets.items():
        if key in reality_input:
            print(f"[!] WYKRYTO PRAWDĘ: {key} to w rzeczywistości {value}.")

# --- Uruchomienie Void Stare ---
scan_for_secrets(["Time", "Money", "You"])
