#!/usr/bin/env bash
# Direktorio-bilaketa gobuster-ekin http://ziberit.org gainean.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
WORDLIST="${WORDLIST:-$ROOT/hiztegiak/ziberit-dir.txt}"
TARGET="${TARGET:-http://ziberit.org}"
OUTDIR="${OUTDIR:-$ROOT/emaitzak}"
mkdir -p "${OUTDIR}"

OUT="${OUTDIR}/gobuster-dir.txt"

if ! command -v gobuster >/dev/null 2>&1; then
  echo "gobuster falta da. sudo apt install -y gobuster"
  exit 1
fi

if [[ ! -f "${WORDLIST}" ]]; then
  echo "Hiztegia ez da aurkitu: ${WORDLIST}"
  exit 1
fi

echo "Helburua:  ${TARGET}"
echo "Hiztegia:  ${WORDLIST}"
echo "Emaitza:   ${OUT}"
echo

# -q quiet progress; status codes interesgarriak gordetzen dira
gobuster dir \
  -u "${TARGET}" \
  -w "${WORDLIST}" \
  -t 30 \
  -q \
  -o "${OUT}" \
  ${GOBUSTER_EXTRA:-}

echo
echo "=== Aurkitutako path-ak ==="
if [[ -s "${OUT}" ]]; then
  cat "${OUT}"
  echo
  echo "Intereseko direktorioak (Status=200/301/302/403) atera:"
  awk '{print $1}' "${OUT}" | sed 's#^/##' | sort -u | tee "${OUTDIR}/direktorio-interesgarriak.txt"
else
  echo "(ez dago emaitzarik — handitu hiztegia edo begiratu DNS/konexioa)"
fi

echo
echo "Hurrengoa: editatu DIRS 03-wget-jeitsi.sh-n behar izanez gero, gero:"
echo "  ./03-wget-jeitsi.sh"
