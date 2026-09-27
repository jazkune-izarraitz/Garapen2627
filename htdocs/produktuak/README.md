# Produktuak (PHP + MySQL)

Helbidea: `http://localhost/produktuak/`

## 1. Docker MySQL martxan
Ataka `3306`, pasahitza `2paag3`.

## 2. Datu-basea sortu (`setup.sql`)

**PowerShell** (Windows):
```powershell
Get-Content setup.sql | docker exec -i mysql-8-0-30 mysql -uroot -p2paag3
```

**CMD** edo bash:
```bat
docker exec -i mysql-8-0-30 mysql -uroot -p2paag3 < setup.sql
```

> PowerShell-ek ez du onartzen `<` birbideratzea; horregatik `Get-Content ... |`.

## 3. Fitxategiak htdocs-en
`produktuak` → `C:\xampp\htdocs\produktuak`

## 4. Ireki
`http://localhost/produktuak/`

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
| `index.php` | Zerrenda + gehitu + ezabatu + editatu |
| `xehetasunak.php` | Xehetasunak + itzuli |
| `editatu.php` | Editatu |
| `ezabatu.php` | Ezabatu |
