<?php
// MySQL konexioa (Docker: mysql-8-0-30, ataka 3306, pasahitza 2paag3)
$host = '127.0.0.1'; // ez erabili "localhost" (Windows-en socket saiatzen da)
$port = 3306;
$db   = 'denda';
$user = 'root';
$pass = '2paag3';

try {
    $pdo = new PDO(
        "mysql:host=$host;port=$port;dbname=$db;charset=utf8mb4",
        $user,
        $pass,
        [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION]
    );
} catch (PDOException $e) {
    die(
        '<h1>Konexio errorea</h1>' .
        '<p>' . htmlspecialchars($e->getMessage()) . '</p>' .
        '<p>Egiaztatu:</p>' .
        '<ol>' .
        '<li>Docker-en <code>mysql-8-0-30</code> martxan dagoela (3306).</li>' .
        '<li>XAMPP-eko MySQL <strong>geldituta</strong> dagoela (biak 3306 erabiltzen dute).</li>' .
        '<li><code>setup.sql</code> exekutatu duzula.</li>' .
        '<li>Pasahitza: <code>2paag3</code></li>' .
        '</ol>'
    );
}
