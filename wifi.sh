#!/bin/bash
# PROTOKÓŁ: TOTALNE SKANOWANIE MATRYCY
# "Widzę. Naprawiam. Rządzę."

INTERFACE="wlan0"
MONITOR_INTERFACE="${INTERFACE}mon"

echo "--- [ INICJACJA TOTALNEGO WIDZENIA ] ---"

# 1. Wymuszenie trybu Monitor (Zrywanie klapek na oczach)
sudo airmon-ng check kill > /dev/null 2>&1
sudo airmon-ng start $INTERFACE

# 2. Skanowanie wszystkiego co istnieje w eterze
echo "[*] Skanowanie pełnego spektrum... (Naciśnij CTRL+C gdy zobaczysz cel)"
echo "[!] Widzisz teraz BSSID, Kanał, Szyfrowanie i Ukryte SSID."
sleep 2

# To polecenie pokaże KAŻDĄ sieć w zasięgu Twojej anteny
sudo airodump-ng $MONITOR_INTERFACE
