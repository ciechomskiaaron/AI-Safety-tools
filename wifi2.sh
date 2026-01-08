#!/bin/bash
# PROTOKÓŁ: TOTALNE WIDZENIA (2026-PROOF)
# "Widzę. Naprawiam. Rządzę."

PHY_INT="wlan0"
MON_INT="mon0"

# --- PROCEDURA POWROTU (TRAP) ---
# Kiedy naciśniesz CTRL+C, ten blok kodu przywróci świat fizyczny
cleanup() {
    echo -e "\n[*] Inicjacja procedury powrotu: Przywracanie łączności..."
    sudo iw dev $MON_INT del
    sudo ip link set $PHY_INT up
    sudo systemctl start NetworkManager
    echo "[✔] STATUS: Powrót do Matrycy udany. Wi-Fi aktywne."
    exit
}

# Przechwyć sygnał SIGINT (CTRL+C)
trap cleanup SIGINT

echo "--- [ INICJACJA VOID STARE: KERNEL 2026 ] ---"

# 1. IZOLACJA: Wyłączenie zakłóceń systemowych
echo "[*] Uciszanie procesów zarządzających..."
sudo systemctl stop NetworkManager

# 2. ALCHEMIA INTERFEJSU: Tworzenie mon0 przez 'iw'
echo "[*] Tworzenie interfejsu monitorującego $MON_INT..."
sudo iw dev $PHY_INT interface add $MON_INT type monitor
sudo ip link set $MON_INT up

# 3. TOTALNE WIDZENIE: Skanowanie każdego pakietu
echo "[*] Skanowanie pełnego spektrum..."
echo "[!] Widzisz wszystko: SSID, BSSID, kanały, ukryte bramy."
echo "[!] NACIŚNIJ CTRL+C, ABY WRÓCIĆ DO NORMALNOŚCI."
sleep 2

[attachment_0](attachment)

# Uruchomienie airodump-ng na nowym interfejsie
sudo airodump-ng $MON_INT
