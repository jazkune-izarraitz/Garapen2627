#!/usr/bin/env bash
# DNS prestatu FPCloud Arp Kali-n (10.10.10.0 sarea).
# Exekutatu: sudo ./01-dns-prestatu.sh
set -euo pipefail

DNS_LAB="10.10.10.9"
HOST_IP="10.10.10.12"
HOST_NAME="ziberit.org"
RESOLV="/etc/resolv.conf"
HOSTS="/etc/hosts"

if [[ "${EUID}" -ne 0 ]]; then
  echo "Errorea: root behar da. Erabili: sudo $0"
  exit 1
fi

echo "[1/3] ${RESOLV} eguneratzen — lehen nameserver: ${DNS_LAB}"

# Gorde kopia
cp -a "${RESOLV}" "${RESOLV}.bak.$(date +%Y%m%d%H%M%S)" 2>/dev/null || true

tmp="$(mktemp)"
{
  echo "nameserver ${DNS_LAB}"
  # Mantendu beste nameserver-ak, lab-koa bikoiztu gabe
  if [[ -f "${RESOLV}" ]]; then
    grep -E '^\s*nameserver' "${RESOLV}" | grep -v "${DNS_LAB}" || true
  fi
  # Beste lerro erabilgarriak (search, options…)
  if [[ -f "${RESOLV}" ]]; then
    grep -Ev '^\s*(#|$)|^\s*nameserver' "${RESOLV}" || true
  fi
} > "${tmp}"
cp "${tmp}" "${RESOLV}"
rm -f "${tmp}"
chmod 644 "${RESOLV}"

echo "---- ${RESOLV} ----"
cat "${RESOLV}"
echo "-------------------"

echo
echo "[2/3] ping ${HOST_NAME} ..."
if ping -c 2 -W 3 "${HOST_NAME}"; then
  echo "[OK] DNS ondo dabil."
else
  echo "[!] DNS bidez ez dago erantzunik. ${HOSTS} eguneratzen..."
  if grep -qE "[[:space:]]${HOST_NAME}([[:space:]]|$)" "${HOSTS}"; then
    # Eguneratu IP baldin badago sarrera
    sed -i -E "s/^.*[[:space:]]${HOST_NAME}([[:space:]].*)?$/${HOST_IP} ${HOST_NAME}/" "${HOSTS}"
  else
    echo "${HOST_IP} ${HOST_NAME}" >> "${HOSTS}"
  fi
  echo "Gehitua/eguneratua: ${HOST_IP} ${HOST_NAME}"
  echo
  echo "[3/3] Berriro ping..."
  if ping -c 2 -W 3 "${HOST_NAME}"; then
    echo "[OK] hosts bidez iristen da."
  else
    echo "[ERROREA] Oraindik ez. Egiaztatu:"
    echo "  - Kali + ITE sarea konektatuta (eth1/eth2/… → 10.10.10.x)"
    echo "  - ip -br a  (adib. eth2 10.10.10.140/24 OK da)"
    echo "  - Helburua piztuta: ping ${HOST_IP}"
    exit 1
  fi
fi

echo
echo "Prest. Hurrengoa: ./02-gobuster-bilatu.sh"
