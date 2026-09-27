# Produktuak (PHP + MySQL)

Helbidea: `http://localhost/produktuak/`

## Beharrezkoa
1. Docker MySQL martxan (`mysql-30-0-8`, ataka **3306**, pasahitza `2paag3`)
2. Karpeta `htdocs/produktuak`-en
3. Nabigatzailea: `http://localhost/produktuak/`

Datu-basea (`denda`) eta taula (`produktuak`) **PHP-k berak sortzen ditu** lehenengo aldiz kargatzean (`konexioa.php`). Ez da `setup.sql` behar.

## Kredentzialak (`konexioa.php`)
- host: `127.0.0.1`
- user: `root`
- pass: `2paag3`
- db: `denda`

## Fitxategiak
| Fitxategia | Helburua |
|---|---|
| `index.php` | Zerrenda + gehitu + ezabatu + editatu |
| `xehetasunak.php` | Xehetasunak + itzuli |
| `editatu.php` | Editatu |
| `ezabatu.php` | Ezabatu |
| `konexioa.php` | Konexioa + taula sortu |
