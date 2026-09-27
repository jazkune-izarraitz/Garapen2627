<?php
// MySQL konexioa (Docker: 3306, pasahitza 2paag3)
$host = '127.0.0.1';
$db   = 'denda';
$user = 'root';
$pass = '2paag3';

try {
    $pdo = new PDO("mysql:host=$host;dbname=$db;charset=utf8mb4", $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die('Konexio errorea: ' . $e->getMessage());
}
