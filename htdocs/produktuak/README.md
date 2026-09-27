# Produktuen web aplikazioa (PHP + MySQL CRUD)

Ariketaren helburua: **denda** datu-basean produktuak kudeatzea PHP bidez, bi orrialde nagusirekin.

## Helbidea

```
http://IP_helbidea/produktuak
```

Adibidez: `http://127.0.0.1/produktuak/` edo `http://localhost/produktuak/`

Fitxategi hauek **htdocs/produktuak** karpetan egon behar dute (XAMPP: `C:\xampp\htdocs\produktuak` edo Linux: `/opt/lampp/htdocs/produktuak`).

## Docker MySQL (`mysql-30-0-8`)

Aplikazioak **3306** atakan dagoen MySQL edukiontzia erabiltzen du (pasahitza: `2paag3`):

```bash
docker run -d --name mysql-30-0-8 -p 3306:3306 \
  -e MYSQL_ROOT_PASSWORD=2paag3 \
  mysql:8.0.30
```

Datu-basea sortu:

```bash
docker exec -i mysql-30-0-8 mysql -uroot -p2paag3 < setup.sql
```

### Kredentzialak (`konexioa.php`)

| Eremua | Balioa |
|---|---|
| Ostalaria | `127.0.0.1` |
| Ataka | `3306` |
| Datu-basea | `denda` |
| Erabiltzailea | `root` |
| Pasahitza | `2paag3` |

## Orrialdeak

| Fitxategia | Funtzioa |
|---|---|
| `index.php` | Zerrenda (izena + prezioa), gehitu, ezabatu, editatu |
| `xehetasunak.php` | Xehetasunak (izena, deskribapena, irudia, prezioa) |
| `editatu.php` | Eguneratu (gehigarria) |
| `ezabatu.php` | Ezabatu |
| `konexioa.php` | PDO konexioa |
| `setup.sql` | DB + taula + adibide datuak |
| `irudiak/` | Produktuen irudiak |

## Taula: `produktuak`

- `id` INT AUTO_INCREMENT PRIMARY KEY
- `izena` VARCHAR
- `deskribapena` TEXT
- `prezioa` DECIMAL(6,2)
- `irudia` VARCHAR
