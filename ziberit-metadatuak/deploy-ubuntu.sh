#!/bin/bash
# Ubuntu ziberit-en exekutatu: nginx webroot laborategia instalatu
# Erabilera:
#   cd /tmp && tar xzf ziberit-webroot.tar.gz
#   sudo bash deploy-ubuntu.sh /tmp/webroot

set -euo pipefail

SRC="${1:-./webroot}"
DEST="/var/www/html"

if [[ ! -d "$SRC" ]]; then
  echo "Errorea: ez da aurkitu $SRC"
  echo "Erabili: sudo bash $0 /bidea/webroot"
  exit 1
fi

export DEBIAN_FRONTEND=noninteractive
apt-get update -qq
apt-get install -y -qq nginx >/dev/null

# Apache badago 80ean, utzi (nginx nahi dugu jarduera honetarako)
if systemctl is-active --quiet apache2 2>/dev/null; then
  systemctl stop apache2
  systemctl disable apache2
fi

rm -f "$DEST/index.nginx-debian.html"
rsync -a --delete "$SRC"/ "$DEST"/
chown -R www-data:www-data "$DEST"

# DNS lokala (bind9 badago, aukerakoa): ziberit.org -> 10.10.10.12
# Ikasleek /etc/hosts edo 10.10.10.9 nameserver erabiliko dute.

nginx -t
systemctl enable --now nginx
systemctl reload nginx

echo "OK: http://10.10.10.12/ prestatuta"
echo "Direktorioak: images/ docs/ download/"
ls -la "$DEST"
