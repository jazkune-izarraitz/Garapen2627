# Produktuak (PHP + MySQL) — ariketa sinplea

Helbidea: `http://localhost/produktuak/`

## 1. Docker MySQL (3306)

```bash
docker start mysql-30-0-8
# edo sortu:
# docker run -d --name mysql-30-0-8 -p 3306:3306 -e MYSQL_ROOT_PASSWORD=2paag3 mysql:8.0.30
```

## 2. Datu-basea

```bash
docker exec -i mysql-30-0-8 mysql -uroot -p2paag3 < setup.sql
```

## 3. Fitxategiak htdocs-en

Kopiatu `produktuak` karpeta → `C:\xampp\htdocs\produktuak` (edo `/opt/lampp/htdocs/produktuak`)

## Kredentzialak (`konexioa.php`)

- host: `127.0.0.1`
- user: `root`
- pass: `2paag3`
- db: `denda`

## Orrialdeak

| Fitxategia | Helburua |
|---|---|
| `index.php` | Zerrenda + gehitu + ezabatu + editatu |
| `xehetasunak.php` | Xehetasunak + itzuli |
| `editatu.php` | Editatu (gehigarria) |
| `ezabatu.php` | Ezabatu |
| `konexioa.php` | PDO konexioa |
| `setup.sql` | DB + taula |
