# Web Garapena – Kontrol Puntua (Adei Belar)

Ikaslearen proiektua: **Ikasle Kudeaketa** (PHP + MySQL + MVC sinplea).
Hemen: nola dabilen ulertzeko eta klasean azaltzeko / probatzeko.

## Arkitektura (ikasleei marraztu)

```
Nabigatzailea
    │  ?action=index|create|store|edit|update|delete|show|logs
    ▼
public/index.php          ← router (switch)
    │
    ├── config/db.php     ← PDO konexioa → MySQL (ikasleak_db)
    ├── config/lang.php   ← EU/EN itzulpenak
    ├── controllers/IkasleController.php  ← negozio logika
    ├── models/Ikasle.php                 ← SQL (prepared statements)
    └── views/*.php                       ← HTML (Bootstrap)
```

## PHP ↔ MySQL nola dabilen (3 urrats)

1. **`config/db.php`**: `new PDO(...)` → `$pdo` objektua.
2. **`models/Ikasle.php`**: `$pdo->prepare(...)` + `execute(...)` → `SELECT` / `INSERT` / `UPDATE` / `DELETE`.
3. **`IkasleController`**: formularioa / URL jasotzen du → modeloa deitzen du → `views/` erakusten du.

Datuak **ez** daude PHP fitxategian: MySQL-ko `ikasleak` taulan daude.

## Nola instalatu eta probatu

Beharrezko PHP luzapenak: `pdo_mysql`, `mbstring`, `fileinfo`.

```bash
# 1) Datu-basea
sudo mysql < Web_Garapena_KP/kontrol_puntua/ikasleak_db.sql

# 2) Kredentzialak (XAMPP estiloa, config/db.php)
#    host=127.0.0.1  db=ikasleak_db  user=root  password=(hutsa)
#    Oharra: hodeiko/Linux inguruneetan localhost ordez 127.0.0.1 erabili
#    (TCP), XAMPPen localhost ondo dabil socket-ekin.

# 3) Zerbitzaria (public/ karpetatik!)
cd Web_Garapena_KP/kontrol_puntua/public
php -S localhost:8080
```

Nabigatzailea: http://localhost:8080/

| URL | Zertarako |
|---|---|
| `/?action=index` | Zerrenda + bilaketa + orrikatzea |
| `/?action=create` | Ikasle berria (argazkiarekin) |
| `/?action=show&id=1` | Xehetasuna |
| `/?action=edit&id=1` | Editatu |
| `/?action=logs` | `logs/app.log` ikusi |


## Proba azkarra (agentearen emaitza)

- Zerrenda: Ane, Mikel, Leire (+ Proba INSERT bidez)
- `?action=show&id=1`: Ane Lopez xehetasuna
- `?action=logs`: LOGIN/INSERT logak
- Sortzean **argazkia derrigorrezkoa** da (`required` + balidazioa)

## Klasean azaltzeko puntuak

1. **MVC**: Model (SQL) / Controller (logika) / View (HTML) bereizita.
2. **Router**: `?action=` parametroak erabakitzen du zer metodo deitu.
3. **PDO + prepared statements**: SQL injection saihesteko (`:izena` bezalako markak).
4. **CSRF token**: POST bakoitzean saioan gordetako tokena egiaztatzen da.
5. **Upload segurua**: MIME egiaztatu, 2MB muga, izen bakarra `time()_izena.ext`.
6. **Hizkuntza**: EU/EN saioan gordeta (`config/lang.php`).

## Ohiko erroreak

| Sintoma | Konponbidea |
|---|---|
| Unable to connect to the database | MySQL abiarazi; `db.php` kredentzialak |
| 404 / orri zuria | Zerbitzaria `public/`-etik abiarazi |
| Argazkia ez da igotzen | `public/uploads` idazgarria izan behar du |
| CSRF errorea | Formularioa berriz kargatu (saioa / token berria) |

## Jatorria

Adei Belar-en kontrol puntua (`Web_Garapena_KP.zip`).
SQL scripta: `script_sql.sql` / `kontrol_puntua/ikasleak_db.sql`.
