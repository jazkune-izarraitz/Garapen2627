<?php
declare(strict_types=1);

/**
 * Datu-base konexioaren konfigurazioa.
 * Fitxategi honek PDO instantzia partekatua itzultzen du, aplikazioa eskalagarri eta segurua izan dadin.
 */
$settings = [
    'host' => '127.0.0.1',
    'dbname' => 'ikasleak_db',
    'user' => 'root',
    'password' => '',
    'charset' => 'utf8mb4',
];

/**
 * Hemen DSNa eraikitzen dugu konfigurazioaren arabera.
 */
$dsn = sprintf('mysql:host=%s;dbname=%s;charset=%s', $settings['host'], $settings['dbname'], $settings['charset']);

/**
 * PDO aukerak definitzen dira, erroen kudeaketa eta segurtasuna bermatzeko.
 */
$options = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    PDO::ATTR_EMULATE_PREPARES => false,
];

/**
 * Saiatu konektatzen eta salbuespenen bidez hutsak harrapatu.
 */
try {
    $pdo = new PDO($dsn, $settings['user'], $settings['password'], $options);
} catch (PDOException $e) {
    error_log('Database connection failed: ' . $e->getMessage());
    die('Unable to connect to the database.');
}

return $pdo;
