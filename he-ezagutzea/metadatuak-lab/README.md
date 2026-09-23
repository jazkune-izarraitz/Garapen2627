# Metadatuak — FPCloud Arp Kali prestaketa

Helburua: `http://ziberit.org` webgunetik fitxategiak lortu eta metadatuak aztertzea (JPG geolokalizazioa, PDF Author).

> **Irakaslea:** helburuko Ubuntu VM-a prestatzeko ikus `ziberit-zerbitzaria/` (IP `10.10.10.12` + nginx + edukia).
>
> **Ikasleak:** script hauek **FPCloud Kali**-n korritu (`10.10.10.0/24`). Cursor/cloud makina honek ez du sarbiderik lab sare horretara.

## FPCloud-en hasierako pausoak

1. Sartu [fpcloud.izarraitz.eus](https://fpcloud.izarraitz.eus) → Kali mahaigaina ireki (Arp Kali edo zuk sortutakoa).
2. Egiaztatu lab sarea: `ip -br a` → edozein interfazetan (`eth1`, `eth2`, …) `10.10.10.x/24` IP bat.
   - Adibide OK: `eth2` → `10.10.10.140/24` (interfazaren izenak ez du axola; tartea bai).
3. Kopiatu karpeta hau Kalian (git clone / USB / partekatutako karpeta).
4. Exekutatu prestaketa:

```bash
cd he-ezagutzea/metadatuak-lab
chmod +x scriptak/*.sh
sudo ./scriptak/01-dns-prestatu.sh
./scriptak/00-tresnak-egiaztatu.sh
```

## DNS

`01-dns-prestatu.sh` scriptak:

1. `/etc/resolv.conf` → lehen `nameserver 10.10.10.9`
2. `ping -c 2 ziberit.org` egiten du
3. Huts egiten badu, `/etc/hosts` gehitzen du: `10.10.10.12 ziberit.org`

Eskuz:

```bash
sudo nano /etc/resolv.conf
# nameserver 10.10.10.9  (lehenengo lerroa)

ping ziberit.org
# huts →:
echo '10.10.10.12 ziberit.org' | sudo tee -a /etc/hosts
```

## Lan-fluxua (labur)

| Pausua | Script / komandoa |
|--------|-------------------|
| 1. DNS | `sudo ./scriptak/01-dns-prestatu.sh` |
| 2. Direktorioak | `./scriptak/02-gobuster-bilatu.sh` |
| 3. Fitxategiak | `./scriptak/03-wget-jeitsi.sh` |
| 4. Metadatuak | `./scriptak/04-exiftool-analisi.sh` |

Hiztegia: `hiztegiak/ziberit-dir.txt` (jarduerarako prestatua).

## Entregagaiak

Scriptak `emaitzak/` karpetan uzten ditu:

- `jpg_geolokalizazioa.txt` — JPG GPS metadatuak
- `pdf_egileak.txt` — PDF Author ezberdinak (errepikatu gabe)
- `fitxategien_zerrenda.txt` — wget-ek jeitsitako fitxategiak

Hiru hauek igo zereginera.

## Oharrak

- Helburua lab sarea da soilik (`10.10.10.12` / `ziberit.org`).
- Gobuster emaitzetan `200`/`301`/`403` interesgarriak begiratu; gero `03-wget-jeitsi.sh`-n `DIRS` aldagaiari intereseko path-ak gehitu.
