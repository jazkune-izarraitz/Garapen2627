# Produktuak (PHP + MySQL) — bertsio sinplea

## Beharrezkoa
- XAMPP: **Apache Start**, MySQL **Stop**
- Docker: `mysql-8-0-30` martxan (3306, pasahitza `2paag3`)

## setup.sql
```powershell
cd C:\xampp\htdocs\produktuak
Get-Content setup.sql | docker exec -i mysql-8-0-30 mysql -uroot -p2paag3
```

## Ireki
- http://localhost/produktuak/
- http://localhost/produktuak/proba.php

## Kodea
`mysqli` + `while` (foreach gabe). HTML oso sinplea.
