<?php
// Produktuaren xehetasunak: izena, deskribapena, irudia, prezioa
require 'konexioa.php';

$id = (int) ($_GET['id'] ?? 0);
$stmt = $pdo->prepare('SELECT * FROM produktuak WHERE id = ?');
$stmt->execute([$id]);
$p = $stmt->fetch();

if (!$p) {
    die('Produktua ez da aurkitu.');
}

$irudia = 'irudiak/' . ($p['irudia'] ?: 'lehenetsia.png');
?>
<!DOCTYPE html>
<html lang="eu">
<head>
  <meta charset="UTF-8">
  <title><?= htmlspecialchars($p['izena']) ?></title>
</head>
<body>
  <h1><?= htmlspecialchars($p['izena']) ?></h1>
  <p><strong>Prezioa:</strong> <?= number_format($p['prezioa'], 2) ?> €</p>
  <p><strong>Deskribapena:</strong> <?= htmlspecialchars($p['deskribapena']) ?></p>
  <p><img src="<?= htmlspecialchars($irudia) ?>" alt="" width="200"></p>
  <p><a href="index.php">← Zerrendara itzuli</a></p>
</body>
</html>
