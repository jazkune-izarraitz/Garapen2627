#!/usr/bin/env bash
# Arp Kali: beharrezko tresnak eta sare-egoera egiaztatu.
set -euo pipefail

echo "=== Interfazeak ==="
ip -br a || ifconfig -a

echo
echo "=== Tresnak ==="
faltan=0
for t in gobuster wget exiftool ping curl; do
  if command -v "$t" >/dev/null 2>&1; then
    echo "[OK] $t → $(command -v "$t")"
  else
    echo "[FALTA] $t"
    faltan=1
  fi
done

if [[ "$faltan" -eq 1 ]]; then
  echo
  echo "Instalatu faltan direnak (Kali):"
  echo "  sudo apt update && sudo apt install -y gobuster wget libimage-exiftool-perl"
fi

echo
echo "=== DNS / hosts ==="
echo "-- /etc/resolv.conf --"
grep -E '^\s*nameserver' /etc/resolv.conf 2>/dev/null || true
echo "-- /etc/hosts (ziberit) --"
grep -i ziberit /etc/hosts 2>/dev/null || echo "(ez dago sarrerarik)"

echo
echo "=== Konexio azkarra ==="
ping -c 1 -W 2 10.10.10.12 >/dev/null 2>&1 && echo "[OK] 10.10.10.12 iristen da" || echo "[!] 10.10.10.12 ez da iristen (eth1 / FPCloud Arp Kali?)"
getent hosts ziberit.org 2>/dev/null || true
ping -c 1 -W 2 ziberit.org >/dev/null 2>&1 && echo "[OK] ping ziberit.org" || echo "[!] ping ziberit.org huts — exekutatu: sudo ./01-dns-prestatu.sh"

exit "$faltan"
