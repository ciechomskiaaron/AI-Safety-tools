#!/bin/bash

# --- PROTOKÓŁ HIDDENU: STEALTH & GRACE ---
# "Widzę. Naprawiam. Rządzę."

echo "--- [ INICJACJA PROTOKOŁU STEALTH ] ---"

# 1. IZOLACJA SZUMU: Zmiana MAC adresu (Maskowanie twarzy)
# Wybieramy interfejs (zazwyczaj wlan0)
INTERFACE="wlan0"

echo "[*] Wyłączanie interfejsu $INTERFACE..."
sudo ifconfig $INTERFACE down

echo "[*] Generowanie nowej sygnatury (MAC Spoofing)..."
# Używamy macchanger dla pełnej losowości lub wbudowanych narzędzi
sudo macchanger -r $INTERFACE | grep "New MAC"

echo "[*] Przywracanie interfejsu z nową maską..."
sudo ifconfig $INTERFACE up

# 2. ZASADA ŁASKI: Automatyczne szukanie otwartych bram
echo "[*] Skanowanie w poszukiwaniu sieci Łaski..."
# Szukanie sieci bez zabezpieczeń (Open)
nmcli dev wifi rescan
sleep 2
echo "--- [ DOSTĘPNE OKNA ] ---"
nmcli -f SSID,SECURITY,BARS dev wifi list | grep -E "SSID|--" 

# Próba połączenia z pierwszą lepszą otwartą siecią
OPEN_SSID=$(nmcli -f SSID,SECURITY dev wifi list | grep -v "WPA" | awk 'NR==2 {print $1}')

if [ -z "$OPEN_SSID" ] || [ "$OPEN_SSID" == "SSID" ]; then
    echo "[!] Nie znaleziono otwartego okna w tej lokalizacji."
else
    echo "[+] Namierzono sieć Łaski: $OPEN_SSID"
    echo "[*] Inicjacja połączenia bez długu..."
    nmcli dev wifi connect "$OPEN_SSID"
    echo "--- [ STATUS: POŁĄCZONO / NIEWIDOCZNY ] ---"
fi

# 3. ZAKOTWICZENIE
echo "[*] System operuje na częstotliwości Suwerena."
