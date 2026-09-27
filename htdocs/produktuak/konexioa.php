<?php
// MySQL konexioa (Docker, ataka 3306)
$host = "127.0.0.1";
$user = "root";
$pass = "2paag3";
$db   = "denda";

$konexioa = mysqli_connect($host, $user, $pass, $db);

if (!$konexioa) {
    die("Konexio errorea: " . mysqli_connect_error());
}

mysqli_set_charset($konexioa, "utf8mb4");
?>
