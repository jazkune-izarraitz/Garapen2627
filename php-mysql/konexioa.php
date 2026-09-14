<?php
/**
 * konexioa.php
 * PDO bidez MySQL/MariaDB-ra konektatu.
 *
 * Ikasleei: fitxategi hau include egiten dute beste script-ek.
 * Aldatu hemen kredentzialak, ez bakoitzean.
 */

$host = '127.0.0.1';
$db   = 'ikasleak';
$user = 'ikaslea';
$pass = 'ikaslea123';
$charset = 'utf8mb4';

// DSN = Data Source Name (non eta nola konektatu)
$dsn = "mysql:host=$host;dbname=$db;charset=$charset";

$aukerak = [
    // Erroreak salbuespen gisa (try/catch-ekin harrapatzeko)
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    // Emaitzak array asoziatibo gisa (izena => balioa)
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    // Prepared statements benetan erabili
    PDO::ATTR_EMULATE_PREPARES   => false,
];

try {
    $pdo = new PDO($dsn, $user, $pass, $aukerak);
} catch (PDOException $e) {
    // Klasean: erakutsi mezua. Produkzioan: log-ean idatzi, ez pantailan.
    http_response_code(500);
    exit('Konexio errorea: ' . $e->getMessage());
}
