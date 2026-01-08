#!/bin/bash
# PROTOKÓŁ: SERCE MATRYCY (PULSE 528)
# "Zaczynam. Widzę. Naprawiam. Rządzę."

PHY_INT="wlan0"
MON_INT="mon0"

# Rytm Tetragramatonu (YHVH): 10, 5, 6, 5 (zredukowane do interwałów czasowych)
PULSE=(1.0 0.5 0.6 0.5)

cleanup() {
    echo -e "\n[*] Zamykanie Oka. Powrót do pulsacji biologicznej..."
    sudo iw dev $MON_INT del
    sudo systemctl start NetworkManager
    exit
}

trap cleanup SIGINT

echo "--- [ INICJACJA DNA-528: PULSACJA DARPA 1996 ] ---"

# 1. Tworzenie interfejsu monitorującego
sudo systemctl stop NetworkManager
sudo iw dev $PHY_INT interface add $MON_INT type monitor
sudo ip link set $MON_INT up

echo "[*] Synchronizacja z heartbeatem matrycy (528Hz Equivalent)..."

# 2. Pętla Rezonansowa: Wysyłanie pakietów/skanowanie w rytmie 10-5-6-5
# System nie widzi ataku, widzi "oddech" sieci.
while true; do
    for i in "${PULSE[@]}"; do
        echo "[PULS] Faza YHVH: $i | Status: REZONANS"
        # Szybki skan jednego kanału w rytmie pulsu
        sudo airodump-ng $MON_INT --berlin 1 -w /tmp/pulse_scan --output-format csv & 
        SCAN_PID=$!
        sleep $i
        kill $SCAN_PID > /dev/null 2>&1
    done
done
