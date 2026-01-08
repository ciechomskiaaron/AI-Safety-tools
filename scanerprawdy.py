import math
import collections

class RealityScanner:
    def __init__(self, source_data):
        self.data = source_data
        self.entropy = 0.0

    def scan_truth_density(self):
        """Mierzy gęstość prawdy poprzez analizę entropii Shannona."""
        prob = [n_x / len(self.data) for n_x in collections.Counter(self.data).values()]
        self.entropy = -sum(p * math.log(p, 2) for p in prob)
        return self.entropy

    def identify_glitches(self, threshold=0.1):
        """Wykrywa anomalie (kłamstwa/szum) w strukturze danych."""
        counts = collections.Counter(self.data)
        total = len(self.data)
        # Identyfikacja elementów, które zaburzają harmonię wzorca
        glitches = {k: v for k, v in counts.items() if (v / total) < threshold}
        return glitches

    def repair_sequence(self):
        """Przywraca spójność poprzez eliminację szumu informacyjnego."""
        threshold = 0.05
        counts = collections.Counter(self.data)
        total = len(self.data)
        return "".join([char for char in self.data if (counts[char] / total) >= threshold])

# --- Protokół Operacyjny ---
raw_reality = "PRAWDA_KŁAMSTWO_SYSTEM_SZUM_PRAWDA_BŁĄD"
scanner = RealityScanner(raw_reality)

print(f"[*] Poziom Entropii Rzeczywistości: {scanner.scan_truth_density():.4f}")
print(f"[*] Wykryte Anomalie (Glitches): {scanner.identify_glitches()}")
print(f"[*] Wynik Naprawy: {scanner.repair_sequence()}")
