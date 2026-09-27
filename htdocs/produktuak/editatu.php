<?php
// Produktua editatu (gehigarria)
require 'konexioa.php';

$id = (int) ($_GET['id'] ?? $_POST['id'] ?? 0);

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $stmt = $pdo->prepare('UPDATE produktuak SET izena=?, deskribapena=?, prezioa=?, irudia=? WHERE id=?');
    $stmt->execute([
        $_POST['izena'],
        $_POST['deskribapena'],
        $_POST['prezioa'],
        $_POST['irudia'] ?: 'lehenetsia.png',
        $id,
    ]);
    header('Location: index.php');
    exit;
}

$stmt = $pdo->prepare('SELECT * FROM produktuak WHERE id = ?');
$stmt->execute([$id]);
$p = $stmt->fetch();
if (!$p) {
    die('Produktua ez da aurkitu.');
}
?>
<!DOCTYPE html>
<html lang="eu">
<head>
  <meta charset="UTF-8">
  <title>Editatu</title>
</head>
<body>
  <h1>Editatu produktua</h1>
  <form method="post">
    <input type="hidden" name="id" value="<?= $p['id'] ?>">
    Izena: <input name="izena" value="<?= htmlspecialchars($p['izena']) ?>" required><br><br>
    Deskribapena: <input name="deskribapena" value="<?= htmlspecialchars($p['deskribapena']) ?>"><br><br>
    Prezioa: <input name="prezioa" type="number" step="0.01" value="<?= $p['prezioa'] ?>" required><br><br>
    Irudia: <input name="irudia" value="<?= htmlspecialchars($p['irudia']) ?>"><br><br>
    <button type="submit">Gorde</button>
    <a href="index.php">Utzi</a>
  </form>
</body>
</html>
