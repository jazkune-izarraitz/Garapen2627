# Produktuak (PHP + MySQL)

## Garrantzitsua
- **Ez** ireki `http://localhost:3306` nabigatzailean (MySQL ez da web orria).
- Web orria: `http://localhost/produktuak/`
- Datu-basea ikusi: `http://localhost/produktuak/proba.php`
- edo phpMyAdmin: `http://localhost/phpmyadmin` (erabiltzailea `root`, pasahitza `2paag3`)

## 1. Docker MySQL martxan
Edukiontzia: `mysql-8-0-30`, ataka `3306`, pasahitza `2paag3`.

## 2. Datu-basea sortu (`setup.sql`)

**PowerShell:**
```powershell
cd C:\xampp\htdocs\produktuak
Get-Content setup.sql | docker exec -i mysql-8-0-30 mysql -uroot -p2paag3
```

## 3. Fitxategiak
`produktuak` → `C:\xampp\htdocs\produktuak`

## 4. Ireki nabigatzailean
1. `http://localhost/produktuak/proba.php` → konexioa + taula ikusi
2. `http://localhost/produktuak/` → aplikazioa

## Kredentzialak (`konexioa.php`)
- host: `127.0.0.1`
- user: `root`
- pass: `2paag3`
- db: `denda`

## Fitxategiak
| Fitxategia | Helburua |
|---|---|
| `setup.sql` | DB + taula sortu |
| `konexioa.php` | PDO konexioa |
| `proba.php` | DB ikusi / froga |
| `index.php` | Zerrenda + gehitu + ezabatu + editatu |
| `xehetasunak.php` | Xehetasunak + itzuli |
| `editatu.php` | Editatu |
| `ezabatu.php` | Ezabatu |
