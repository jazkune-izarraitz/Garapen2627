#!/usr/bin/env bash
# Fluxu osoa Arp Kali-n (dns → gobuster → wget → exiftool).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "${ROOT}/scriptak"

chmod +x ./*.sh

echo "======== 0) Tresnak ========"
./00-tresnak-egiaztatu.sh || true

echo
echo "======== 1) DNS ========"
if [[ "${EUID}" -eq 0 ]]; then
  ./01-dns-prestatu.sh
else
  sudo ./01-dns-prestatu.sh
fi

echo
echo "======== 2) Gobuster ========"
./02-gobuster-bilatu.sh

echo
echo "======== 3) wget ========"
./03-wget-jeitsi.sh

echo
echo "======== 4) exiftool ========"
./04-exiftool-analisi.sh

echo
echo "Eginda. Igo emaitzak/ karpetako hiru fitxategi nagusiak."
