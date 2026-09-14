# Irakaslearentzako gidoia (5–10 min)

## 1. Zergatik bi gauza?

- **HTML/CSS/JS**: nabigatzailean ikusten dena.
- **PHP**: zerbitzarian exekutatzen den logika.
- **MySQL**: datuak gordetzen dituen tokia (taulak, errenkadak).

PHP da “zubia”: formularioa jasotzen du → SQL bidaltzen du → emaitza erakusten du.

## 2. Demo ordena (klasean)

1. `sudo mysql` ireki → `SHOW DATABASES;` → `USE ikasleak;` → `SELECT * FROM ikasleak;`
2. `php proba.php` → “OK: konexioa ondo dago”
3. `php -S localhost:8000` → nabigatzailean `zerrenda.php`
4. `gehitu.php`-n ikasle berria → freskatu zerrenda
5. Berriro MySQL-n `SELECT *` → PHP-k idatzitako errenkada ikusi

## 3. Galdera erabilgarriak

- Zer gertatzen da pasahitza okerra bada? (`konexioa.php` catch)
- Zergatik `?` markak `INSERT`-ean? (SQL injection)
- Non dago “egiazko” datua: PHP fitxategian ala datu-basean?

## 4. Ohiko erroreak

| Mezua / sintoma | Kausa ohikoa |
|---|---|
| Connection refused | MariaDB ez dago abiarazita |
| Access denied | erabiltzailea/pasahitza okerra |
| Unknown database | `setup.sql` ez da exekutatu |
| Table doesn't exist | taula sortu gabe |

## 5. Hurrengo urratsak (aukerakoa)

- Eguneratu (`UPDATE`) eta ezabatu (`DELETE`)
- Pasahitzak `.env`-era atera
- Login sinple bat (saioak / `$_SESSION`)
