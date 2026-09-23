#!/usr/bin/env bash
# Fitxategiak jeitsi wget-ekin, azpidirektoriorik gabe (flat).
# Gobuster-ek topatutako path-ak + erroa.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TARGET="${TARGET:-http://ziberit.org}"
OUTDIR="${OUTDIR:-$ROOT/emaitzak}"
DLDIR="${DLDIR:-$OUTDIR/fitxategiak}"
LISTA="${OUTDIR}/fitxategien_zerrenda.txt"
DIRS_FILE="${OUTDIR}/direktorio-interesgarriak.txt"

mkdir -p "${DLDIR}"

# Lehenetsitako direktorioak (gobuster emaitzarik ez badago ere)
DEFAULT_DIRS=("" "docs" "documents" "files" "download" "downloads" "images" "img" "fotos" "photos" "pdf" "uploads" "upload" "media" "assets")

DIRS=()
if [[ -f "${DIRS_FILE}" ]] && [[ -s "${DIRS_FILE}" ]]; then
  mapfile -t DIRS < "${DIRS_FILE}"
  echo "Gobuster path-ak erabiltzen (${#DIRS[@]}): ${DIRS[*]}"
else
  DIRS=("${DEFAULT_DIRS[@]}")
  echo "Hiztegi lehenetsia erabiltzen (gobuster emaitzarik ez). Path-ak: ${DIRS[*]}"
fi

# Erroko path hutsa beti sartu
has_root=0
for d in "${DIRS[@]}"; do
  [[ -z "$d" ]] && has_root=1
done
[[ "$has_root" -eq 0 ]] && DIRS=("" "${DIRS[@]}")

EXT="pdf,jpg,jpeg,png,doc,docx,xls,xlsx,ppt,pptx,gif,tif,tiff"

echo "Deskarga karpeta: ${DLDIR}"
echo "Extentsioak: ${EXT}"
echo

for d in "${DIRS[@]}"; do
  # Garbitu slash-ak
  d="${d#/}"
  d="${d%/}"
  if [[ -z "$d" ]]; then
    url="${TARGET}/"
  else
    url="${TARGET}/${d}/"
  fi
  echo ">>> wget: ${url}"
  # -r recursive, -l 2 depth, -nd flat (no directories), -np no parent,
  # -A accept extensions, -e robots=off, -nc no-clobber
  wget -r -l 2 -nd -np -nc \
    -A "${EXT}" \
    -e robots=off \
    -P "${DLDIR}" \
    "${url}" 2>&1 | tail -n 5 || true
  echo
done

echo "=== Fitxategien zerrenda ==="
find "${DLDIR}" -maxdepth 1 -type f ! -name 'index.html*' | sort | tee "${LISTA}"
count="$(grep -c . "${LISTA}" 2>/dev/null || echo 0)"
echo
echo "Guztira: ${count} fitxategi → ${LISTA}"
echo "Hurrengoa: ./04-exiftool-analisi.sh"
