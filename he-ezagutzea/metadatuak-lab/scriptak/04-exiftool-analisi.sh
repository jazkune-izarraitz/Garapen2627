#!/usr/bin/env bash
# exiftool: JPG geolokalizazioa + PDF Author bakarrak.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUTDIR="${OUTDIR:-$ROOT/emaitzak}"
DLDIR="${DLDIR:-$OUTDIR/fitxategiak}"
JPG_OUT="${OUTDIR}/jpg_geolokalizazioa.txt"
PDF_OUT="${OUTDIR}/pdf_egileak.txt"
LISTA="${OUTDIR}/fitxategien_zerrenda.txt"

mkdir -p "${OUTDIR}"

if ! command -v exiftool >/dev/null 2>&1; then
  echo "exiftool falta da. sudo apt install -y libimage-exiftool-perl"
  exit 1
fi

if [[ ! -d "${DLDIR}" ]]; then
  echo "Ez dago deskarga karpetarik: ${DLDIR}"
  echo "Lehenago: ./03-wget-jeitsi.sh"
  exit 1
fi

# Zerrenda eguneratu (entrega)
find "${DLDIR}" -maxdepth 1 -type f ! -name 'index.html*' | sort > "${LISTA}"

echo "=== JPG geolokalizazioa → ${JPG_OUT} ==="
{
  echo "# JPG geolokalizazio metadatuak"
  echo "# Iturria: ${DLDIR}"
  echo "# Data: $(date -Iseconds)"
  echo "#"
  shopt -s nullglob nocaseglob
  jpgs=("${DLDIR}"/*.jpg "${DLDIR}"/*.jpeg)
  if [[ ${#jpgs[@]} -eq 0 ]]; then
    echo "# (ez dago JPG/JPEG fitxategirik)"
  else
    # GPS eremuak + fitxategi-izena
    exiftool -q -q -GPSLatitude -GPSLongitude -GPSPosition -GPSAltitude \
      -FileName -Directory -DateTimeOriginal \
      -s -s -s \
      "${jpgs[@]}" 2>/dev/null || true
    echo
    echo "# --- Taula (TSV) ---"
    exiftool -q -q -T -FileName -GPSLatitude -GPSLongitude -GPSPosition \
      "${jpgs[@]}" 2>/dev/null || true
  fi
  shopt -u nullglob nocaseglob
} | tee "${JPG_OUT}"

echo
echo "=== PDF Author bakarrak → ${PDF_OUT} ==="
{
  echo "# PDF Author metadatuak (errepikatu gabe)"
  echo "# Iturria: ${DLDIR}"
  echo "# Data: $(date -Iseconds)"
  echo "#"
  shopt -s nullglob nocaseglob
  pdfs=("${DLDIR}"/*.pdf)
  if [[ ${#pdfs[@]} -eq 0 ]]; then
    echo "# (ez dago PDF fitxategirik)"
  else
    # Author bakoitzeko fitxategiak ere erakutsi, gero Author bakarrak
    echo "# --- Fitxategia → Author ---"
    exiftool -q -q -T -FileName -Author "${pdfs[@]}" 2>/dev/null || true
    echo
    echo "# --- Author ezberdinak ---"
    exiftool -q -q -T -Author "${pdfs[@]}" 2>/dev/null \
      | sed 's/\r$//' \
      | awk 'NF && $0 != "-" && tolower($0) != "author"' \
      | sort -u
  fi
  shopt -u nullglob nocaseglob
} | tee "${PDF_OUT}"

echo
echo "=== Entregagaiak ==="
echo "1) ${JPG_OUT}"
echo "2) ${PDF_OUT}"
echo "3) ${LISTA}"
ls -la "${JPG_OUT}" "${PDF_OUT}" "${LISTA}" 2>/dev/null || true
