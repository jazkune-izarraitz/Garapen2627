# FPCloud Arp Kali — kontrol-zerrenda

Erabili hau mahaigaina prestatzen duzun bitartean.

## Sarrera

- [ ] https://fpcloud.izarraitz.eus ireki
- [ ] Kali mahaigaina abiarazi (Arp Kali edo ITErekin sortutakoa)
- [ ] Terminala ireki

## Sarea

```bash
ip -br a
```

- [ ] Edozein interfazetan (`eth1` / `eth2` / …) `10.10.10.x/24` IP bat dago
  - Adibide: `eth2  UP  10.10.10.140/24` → **ondo** (jarduerako “eth1” aipamena orientagarria da)

## DNS

```bash
sudo nano /etc/resolv.conf
```

Lehenengo lerroa:

```
nameserver 10.10.10.9
```

```bash
ping -c 3 ziberit.org
```

- [ ] ping erantzuten du  
  **Ez badu:**

```bash
echo '10.10.10.12 ziberit.org' | sudo tee -a /etc/hosts
ping -c 3 ziberit.org
```

- [ ] Orain erantzuten du

## Tresnak

```bash
command -v gobuster wget exiftool
# falta →:
sudo apt update
sudo apt install -y gobuster wget libimage-exiftool-perl
```

- [ ] Hiru tresnak instalatuta

## Lab kit-a

```bash
# Adibidea: repoa klonatu edo karpeta kopiatu
cd he-ezagutzea/metadatuak-lab
chmod +x scriptak/*.sh
./scriptak/00-tresnak-egiaztatu.sh
sudo ./scriptak/01-dns-prestatu.sh
```

- [ ] Egiaztapen scriptak OK

## Bilaketa eta analisi

```bash
./scriptak/02-gobuster-bilatu.sh
./scriptak/03-wget-jeitsi.sh
./scriptak/04-exiftool-analisi.sh
# edo dena:
./scriptak/run-all.sh
```

- [ ] gobuster emaitzak
- [ ] fitxategiak `emaitzak/fitxategiak/`-en (flat)
- [ ] `jpg_geolokalizazioa.txt`
- [ ] `pdf_egileak.txt` (Author bakarrak)
- [ ] `fitxategien_zerrenda.txt`

## Entrega

Hiru fitxategi igo zereginera:

1. `emaitzak/jpg_geolokalizazioa.txt`
2. `emaitzak/pdf_egileak.txt`
3. `emaitzak/fitxategien_zerrenda.txt`
