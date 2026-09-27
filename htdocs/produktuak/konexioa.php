<?php
/**
 * konexioa.php
 * PDO bidez MySQL-ra konektatu (Docker: mysql-30-0-8, 3306 ataka).
 */

$host = '127.0.0.1';
$port = 3306;
$db   = 'denda';
$user = 'root';
$pass = '2paag3';
$charset = 'utf8mb4';

$dsn = "mysql:host=$host;port=$port;dbname=$db;charset=$charset";

$aukerak = [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    PDO::ATTR_EMULATE_PREPARES   => false,
];

try {
    $pdo = new PDO($dsn, $user, $pass, $aukerak);
} catch (PDOException $e) {
    http_response_code(500);
    exit('Konexio errorea: ' . htmlspecialchars($e->getMessage()));
}
