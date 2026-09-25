#!/bin/bash
# ZiberIT metadatuak – Arp Kali-n exekutatzeko gidoia
# Helburua: http://ziberit.org  (10.10.10.12)

set -euo pipefail

WORKDIR="${HOME}/ziberit-lab"
WORDLIST="${1:-./directory-list-custom.txt}"
TARGET="http://ziberit.org"

mkdir -p "$WORKDIR/fitxategiak" "$WORKDIR/emaitzak"
cd "$WORKDIR"

echo "== 1) DNS / hosts =="
# Nameserver lehenetsia (beharrezkoa bada):
#   sudo nano /etc/resolv.conf
#   nameserver 10.10.10.9
#
# Alternatiba:
#   echo '10.10.10.12 ziberit.org' | sudo tee -a /etc/hosts

if ! ping -c 1 -W 2 ziberit.org >/dev/null 2>&1; then
  echo "ABISUA: ping ziberit.org huts egin du. Egiaztatu resolv.conf edo /etc/hosts."
else
  echo "OK: ziberit.org erantzuten du."
fi

echo "== 2) Gobuster =="
if [[ ! -f "$WORDLIST" ]]; then
  echo "Errorea: ez da aurkitu hiztegia: $WORDLIST"
  echo "Erabili: $0 /bidea/directory-list-custom.txt"
  exit 1
fi

gobuster dir -u "$TARGET" -w "$WORDLIST" -t 30 -o "$WORKDIR/emaitzak/gobuster.txt"
echo "Emaitzak: $WORKDIR/emaitzak/gobuster.txt"
cat "$WORKDIR/emaitzak/gobuster.txt"

echo
echo "== 3) Fitxategiak jeitsi (adibidea) =="
echo "Gobuster-ek topatutako direktorioetarako, adibidez:"
echo "  wget -r -np -nH --cut-dirs=1 -P fitxategiak -A jpg,jpeg,png,pdf,doc,docx,xls,xlsx '$TARGET/images/'"
echo "  # Gero azpidirektorioak lautu:"
echo "  find fitxategiak -type f -exec mv -n {} fitxategiak/ \\;"
echo "  find fitxategiak -type d -empty -delete"

echo
echo "== 4) Metadatuak =="
echo "  # JPG geolokalizazioa:"
echo "  exiftool -GPSLatitude -GPSLongitude -GPSPosition -csv -ext jpg -ext jpeg fitxategiak/ > emaitzak/jpg-geolokalizazioa.csv"
echo "  # PDF Author bakarrak:"
echo "  exiftool -Author -T -ext pdf fitxategiak/ | sort -u | grep -v '^$' > emaitzak/pdf-authors.txt"
echo "  # Jeitsitako fitxategien zerrenda:"
echo "  find fitxategiak -type f | sort > emaitzak/fitxategi-zerrenda.txt"
