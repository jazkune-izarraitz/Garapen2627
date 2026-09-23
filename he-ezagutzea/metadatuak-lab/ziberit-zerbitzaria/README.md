# ZiberIT Ubuntu zerbitzaria (irakaslea)

Ikasleek aztertuko duten webgunea: `http://ziberit.org` → **`10.10.10.12`**.

## Edukia (`www/`)

| Path | Fitxategiak | Metadatuak |
|------|-------------|------------|
| `/images/` | donostia.jpg, bilbao.jpg | GPS |
| `/uploads/` | oficina.jpg, akta.pdf | GPS + Author |
| `/docs/` | memoria.pdf, aurrekontua.pdf | Author |
| `/files/` | txostena.pdf, gidaliburua.pdf | Author |

Author bakarrak: Ane Etxeberria, Mikel Arrieta, Leire Mendizabal, Jon Agirre  
(Ane bi PDF-tan agertzen da — ikasleek `sort -u` egin behar dute.)

## Ubuntu VM-an (FPCloud)

1. ITE sarean konektatu (ikasleen Kali-aren sare bera).
2. Karpeta hau kopiatu VMra (git clone, scp, partekatua…).
3. Exekutatu:

```bash
cd he-ezagutzea/metadatuak-lab/ziberit-zerbitzaria
sudo bash scriptak/01-ubuntu-prestatu.sh
```

Scriptak: IP `10.10.10.12`, nginx, `www/` → `/var/www/ziberit`.

Interfazea desberdina bada:

```bash
sudo ZIBERIT_IFACE=ens3 bash scriptak/01-ubuntu-prestatu.sh
```

## DNS (`10.10.10.9`)

DNS makinan (edo zure DNS zerbitzuan):

```
ziberit.org.  IN A  10.10.10.12
```

DNS gabe, ikasleen `/etc/hosts`:

```
10.10.10.12 ziberit.org
```

## Proba (zure Kali-tik)

```bash
ping -c 3 10.10.10.12
curl -I http://10.10.10.12/
curl -I http://ziberit.org/
```
