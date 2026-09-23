#!/usr/bin/env bash
# ZiberIT Ubuntu zerbitzaria — IP + nginx + web edukia.
# Exekutatu root bezala Ubuntu VM-an (FPCloud):
#   sudo bash 01-ubuntu-prestatu.sh
set -euo pipefail

IP="${ZIBERIT_IP:-10.10.10.12}"
CIDR="${ZIBERIT_CIDR:-24}"
IFACE="${ZIBERIT_IFACE:-}"   # hutsik → automatiko (10.10.10.0 edo lehen ethernet)
WEBROOT="/var/www/ziberit"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
CONTENT_SRC="$(cd "$SCRIPT_DIR/../www" && pwd)"

if [[ "${EUID}" -ne 0 ]]; then
  echo "Erabili: sudo bash $0"
  exit 1
fi

echo "=== 1) Interfazea hautatu ==="
ip -br a
if [[ -z "$IFACE" ]]; then
  # Preferitu 10.10.10.x daukana; bestela eth*/ens* lehena
  IFACE="$(ip -4 -o addr show | awk '/10\.10\.10\./ {print $2; exit}')"
  if [[ -z "$IFACE" ]]; then
    IFACE="$(ip -o link show | awk -F': ' '$2 !~ /lo/ {print $2; exit}')"
  fi
fi
echo "Interfazea: $IFACE → ${IP}/${CIDR}"

echo
echo "=== 2) IP finkoa (netplan) ==="
NETPLAN_FILE="/etc/netplan/99-ziberit.yaml"
# Gateway/DNS lab-eko DNS-era (ikasleek 10.10.10.9 erabiltzen dute)
cat > "$NETPLAN_FILE" << EOF
network:
  version: 2
  ethernets:
    ${IFACE}:
      dhcp4: false
      addresses:
        - ${IP}/${CIDR}
EOF

chmod 600 "$NETPLAN_FILE"
netplan apply || true
sleep 1
ip -br a show "$IFACE" || ip -br a

echo
echo "=== 3) nginx instalatu ==="
export DEBIAN_FRONTEND=noninteractive
apt-get update -qq
apt-get install -y -qq nginx

echo
echo "=== 4) Web edukia kopiatu ==="
mkdir -p "$WEBROOT"
if [[ -d "$CONTENT_SRC" ]]; then
  rsync -a --delete "$CONTENT_SRC"/ "$WEBROOT"/
else
  echo "ABISUA: ez da aurkitu $CONTENT_SRC — utzi index minimoa"
  echo "<h1>ZiberIT</h1>" > "$WEBROOT/index.html"
fi
chown -R www-data:www-data "$WEBROOT"

echo
echo "=== 5) nginx site ==="
cat > /etc/nginx/sites-available/ziberit << EOF
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    server_name ziberit.org www.ziberit.org ${IP};

    root ${WEBROOT};
    index index.html;

    autoindex on;
    autoindex_exact_size off;
    autoindex_localtime on;

    location / {
        try_files \$uri \$uri/ =404;
    }
}
EOF

rm -f /etc/nginx/sites-enabled/default
ln -sfn /etc/nginx/sites-available/ziberit /etc/nginx/sites-enabled/ziberit
nginx -t
systemctl enable nginx
systemctl restart nginx

# Firewall (ufa aktibo badago)
if command -v ufw >/dev/null 2>&1; then
  ufw allow 80/tcp || true
fi

echo
echo "=== 6) Proba lokal ==="
ip -4 addr show "$IFACE" | grep -q "$IP" && echo "[OK] IP $IP" || echo "[!] IP ez da $IP — eskuz egokitu netplan"
curl -sI "http://127.0.0.1/" | head -3
curl -sI "http://127.0.0.1/docs/" | head -3
curl -sI "http://127.0.0.1/images/donostia.jpg" | head -3

echo
echo "Eginda."
echo "  http://${IP}/"
echo "  http://ziberit.org/  (DNS/hosts behar: ${IP} ziberit.org)"
echo
echo "Kali ikaslearen makinan:"
echo "  ping -c 2 ${IP}"
echo "  curl -I http://${IP}/"
