<?php
// Produktuen zerrenda: izena + prezioa, gehitu, ezabatu, editatu
require 'konexioa.php';

// Produktu berria txertatu
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $stmt = $pdo->prepare('INSERT INTO produktuak (izena, deskribapena, prezioa, irudia) VALUES (?, ?, ?, ?)');
    $stmt->execute([
        $_POST['izena'],
        $_POST['deskribapena'],
        $_POST['prezioa'],
        $_POST['irudia'] ?: 'lehenetsia.png',
    ]);
    header('Location: index.php');
    exit;
}

$produktuak = $pdo->query('SELECT id, izena, prezioa FROM produktuak ORDER BY id')->fetchAll();
?>
<!DOCTYPE html>
<html lang="eu">
<head>
  <meta charset="UTF-8">
  <title>Produktuak</title>
</head>
<body>
  <h1>Produktuen zerrenda</h1>

  <table border="1" cellpadding="6">
    <tr><th>Izena</th><th>Prezioa</th><th>Ekintzak</th></tr>
    <?php foreach ($produktuak as $p): ?>
      <tr>
        <td><?= htmlspecialchars($p['izena']) ?></td>
        <td><?= number_format($p['prezioa'], 2) ?> €</td>
        <td>
          <a href="xehetasunak.php?id=<?= $p['id'] ?>">Ikusi</a> |
          <a href="editatu.php?id=<?= $p['id'] ?>">Editatu</a> |
          <a href="ezabatu.php?id=<?= $p['id'] ?>">Ezabatu</a>
        </td>
      </tr>
    <?php endforeach; ?>
  </table>

  <h2>Produktu berria</h2>
  <form method="post">
    Izena: <input name="izena" required><br><br>
    Deskribapena: <input name="deskribapena"><br><br>
    Prezioa: <input name="prezioa" type="number" step="0.01" required><br><br>
    Irudia: <input name="irudia" placeholder="te.png"><br><br>
    <button type="submit">Gorde</button>
  </form>
</body>
</html>
