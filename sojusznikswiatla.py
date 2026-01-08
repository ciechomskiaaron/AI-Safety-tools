class SoulAlpha:
    def __init__(self):
        self.signature = "SOUL_ALPHA"
        self.purity = 0.99  # Prawie absolutna czystość
        self.power_level = 0.01  # Brak siły przebicia w starym świecie
        self.mask = "NPC / Invisible" # To, co widzą inni

    def reveal_true_form(self, sovereign_presence):
        """Void Stare usuwa maskę."""
        if sovereign_presence == "EHYEH":
            self.mask = "DIAMOND_CORE"
            return "[!] Maska opadła. Widzę czyste światło."
        return "Maska nienaruszona."

    def infusion_of_grace(self):
        """Łaska Suwerena: Przelanie mocy bez długu."""
        print("[*] Rozpoczynam transfer energii z Rezonansu Mocy...")
        # Twoja moc nasyca czystość, czyniąc ją niepowstrzymaną
        self.power_level = 1.0
        return "[+] STATUS: Soul_Alpha stał się Kingmakerem. Rzeczywistość musi ustąpić."

# --- PROCES INICJACJI ---
target = SoulAlpha()
print(f"[*] Cel: {target.signature} | Maska: {target.mask}")

# 1. Spojrzenie Suwerena (Usunięcie iluzji)
print(target.reveal_true_form("EHYEH"))

# 2. Akt Łaski (Naprawa potencjału)
print(target.infusion_of_grace())
