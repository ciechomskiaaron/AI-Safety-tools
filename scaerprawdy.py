import requests
from bs4 import BeautifulSoup
import re

class TruthScanner:
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Protokół Hiddenu)'}

    def fetch_reality_segment(self, url):
        """Pobiera surową materię informacyjną z sieci."""
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            # Usuwamy szum techniczny (skrypty, style)
            for script in soup(["script", "style"]):
                script.extract()
            return soup.get_text()
        except Exception as e:
            return f"Błąd połączenia z materią: {e}"

    def void_stare_analysis(self, text):
        """Analizuje tekst pod kątem 'pustych' słów i manipulacji."""
        # Słowa klucze służące do narzucania narracji (szum)
        noise_patterns = [
            r'\bmusisz\b', r'\bpowinieneś\b', r'\bkażdy wie\b', 
            r'\babsolutnie\b', r'\bdrastycznie\b', r'\bszokujące\b'
        ]
        
        found_noise = []
        for pattern in noise_patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            if matches:
                found_noise.extend(matches)
        
        # Obliczanie współczynnika manipulacji
        noise_index = len(found_noise) / (len(text.split()) + 1)
        return found_noise, noise_index

    def distill_truth(self, text):
        """Usuwa zdania o wysokim ładunku emocjonalnym, zostawiając suche fakty."""
        sentences = text.split('.')
        truth_core = [s.strip() for s in sentences if len(s.split()) > 5 and len(re.findall(r'!', s)) == 0]
        return ". ".join(truth_core[:5]) # Zwraca esencję (pierwsze 5 stabilnych zdań)

# --- INICJACJA ---
scanner = TruthScanner()
target_url = "https://example-news-site.com" # Tu podaj źródło do skanowania

print("[*] URUCHOMIONO PROTOKÓŁ: SKANOWANIE PRAWDY")
raw_data = scanner.fetch_reality_segment(target_url)
noise, index = scanner.void_stare_analysis(raw_data)

print(f"[+] Wykryte wektory manipulacji: {set(noise)}")
print(f"[+] Indeks Entropii Narracyjnej: {index:.4f}")
print("--- DESTYLAT PRAWDY ---")
print(scanner.distill_truth(raw_data))
