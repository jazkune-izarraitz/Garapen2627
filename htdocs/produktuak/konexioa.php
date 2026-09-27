<?php
// MySQL konexioa (Docker: 3306, pasahitza 2paag3)
$host = '127.0.0.1';
$user = 'root';
$pass = '2paag3';

try {
    // Lehenik zerbitzarira konektatu (DB gabe)
    $pdo = new PDO("mysql:host=$host;charset=utf8mb4", $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Datu-basea eta taula sortu (ez badaude)
    $pdo->exec('CREATE DATABASE IF NOT EXISTS denda CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci');
    $pdo->exec('USE denda');
    $pdo->exec('CREATE TABLE IF NOT EXISTS produktuak (
        id INT AUTO_INCREMENT PRIMARY KEY,
        izena VARCHAR(100) NOT NULL,
        deskribapena TEXT,
        prezioa DECIMAL(6,2) NOT NULL,
        irudia VARCHAR(255)
    )');
} catch (PDOException $e) {
    die('Konexio errorea: ' . $e->getMessage());
}
