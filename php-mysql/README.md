# PHP + MySQL konexioa (ikasleei)

Helburua: PHP script batek **MySQL/MariaDB** datu-baseari nola konektatzen dion ulertzea, datuak irakurri/idatzi, eta gero probatzea.

## Ideia nagusia (1 minutuan)

```
[ Nabigatzailea / terminala ]
        │
        ▼
   [ PHP scripta ]  ──PDO──▶  [ MySQL datu-basea ]
```

1. PHP-k **PDO** erabiltzen du MySQL-ra konektatzeko.
2. Konexioak 4 gauza behar ditu: ostalaria, datu-basea, erabiltzailea, pasahitza.
3. SQL kontsultak exekutatzen dira (`SELECT`, `INSERT`…).
4. Emaitzak HTML edo terminalean erakusten dira.

## Fitxategiak

| Fitxategia | Zertarako |
|---|---|
| `setup.sql` | Datu-basea, erabiltzailea eta taula sortu |
| `konexioa.php` | PDO konexioa (beste fitxategiek erabiltzen dute) |
| `zerrenda.php` | Ikasleak **irakurri** (`SELECT`) |
| `gehitu.php` | Ikasle berria **gehitu** (`INSERT`) |
| `proba.php` | Konexioa azkar **probatu** |

## Nola instalatu eta probatu

### 1. MariaDB / MySQL abiarazi

```bash
sudo service mariadb start
# edo: sudo systemctl start mariadb
```

### 2. Datu-basea sortu

```bash
sudo mysql < setup.sql
```

### 3. Konexioa probatu (CLI)

```bash
cd php-mysql
php proba.php
```

Arrakasta: `OK: konexioa ondo dago` eta ikasleen zerrenda.

### 4. Web zerbitzariarekin (aukerakoa)

```bash
cd php-mysql
php -S localhost:8000
```

Nabigatzailean:
- http://localhost:8000/proba.php
- http://localhost:8000/zerrenda.php
- http://localhost:8000/gehitu.php

## Ikasleei azaldu beharreko puntuak

1. **`konexioa.php`**: DSN + erabiltzailea + pasahitza. Huts egiten badu → `try/catch`.
2. **`PDO::ATTR_ERRMODE`**: erroreak salbuespen gisa (debugging errazagoa).
3. **Prepared statements** (`prepare` + `execute`): SQL injection saihesteko.
4. **Ez gorde pasahitzak Git-en** produkzioan: `.env` edo konfigurazio lokal bat erabili.

## Kredentzialak (klaseko froga)

- Datu-basea: `ikasleak`
- Erabiltzailea: `ikaslea`
- Pasahitza: `ikaslea123`
- Ostalaria: `127.0.0.1`

> Oharrak: hauek **ikasgelako adibideak** dira. Interneten ez jarri pasahitz hau irekita.
