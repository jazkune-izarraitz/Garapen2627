<?php
// Datu-basea froga: konexioa + taulako datuak ikusi
require 'konexioa.php';

$taulak = $pdo->query('SHOW TABLES')->fetchAll(PDO::FETCH_COLUMN);
$produktuak = $pdo->query('SELECT * FROM produktuak')->fetchAll(PDO::FETCH_ASSOC);
?>
<!DOCTYPE html>
<html lang="eu">
<head>
  <meta charset="UTF-8">
  <title>DB froga</title>
</head>
<body>
  <h1>Datu-basea OK</h1>
  <p>Konektatuta: <strong>denda</strong> (127.0.0.1:3306)</p>

  <h2>Taulak</h2>
  <ul>
    <?php foreach ($taulak as $t): ?>
      <li><?= htmlspecialchars($t) ?></li>
    <?php endforeach; ?>
  </ul>

  <h2>produktuak taula</h2>
  <?php if (!$produktuak): ?>
    <p>Taula hutsik dago. <a href="index.php">Gehitu produktu bat</a>.</p>
  <?php else: ?>
    <table border="1" cellpadding="6">
      <tr>
        <?php foreach (array_keys($produktuak[0]) as $zutabea): ?>
          <th><?= htmlspecialchars($zutabea) ?></th>
        <?php endforeach; ?>
      </tr>
      <?php foreach ($produktuak as $errenkada): ?>
        <tr>
          <?php foreach ($errenkada as $balioa): ?>
            <td><?= htmlspecialchars((string) $balioa) ?></td>
          <?php endforeach; ?>
        </tr>
      <?php endforeach; ?>
    </table>
  <?php endif; ?>

  <p><a href="index.php">← Produktuen zerrenda</a></p>
</body>
</html>
