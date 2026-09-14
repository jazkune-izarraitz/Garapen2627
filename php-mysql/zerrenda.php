<?php
/**
 * zerrenda.php
 * Ikasleak irakurri (SELECT) eta taula batean erakutsi.
 */

require __DIR__ . '/konexioa.php';

$ikasleak = $pdo->query(
    'SELECT id, izena, emaila, sortua FROM ikasleak ORDER BY id'
)->fetchAll();
?>
<!DOCTYPE html>
<html lang="eu">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Ikasleen zerrenda</title>
  <style>
    :root { --bg: #f3f6f4; --ink: #1a2e24; --line: #c5d4cb; --accent: #1f6b4a; }
    body { font-family: "Segoe UI", system-ui, sans-serif; background: linear-gradient(160deg, #e8f0ea, #f7f3ea); color: var(--ink); margin: 0; padding: 2rem 1rem; }
    main { max-width: 42rem; margin: 0 auto; }
    h1 { font-size: 1.6rem; margin: 0 0 .35rem; }
    p.lead { margin: 0 0 1.25rem; opacity: .85; }
    table { width: 100%; border-collapse: collapse; background: #fff; }
    th, td { text-align: left; padding: .65rem .75rem; border-bottom: 1px solid var(--line); }
    th { background: #eef5f0; font-size: .85rem; text-transform: uppercase; letter-spacing: .04em; }
    a { color: var(--accent); }
    .actions { margin-top: 1.25rem; }
  </style>
</head>
<body>
<main>
  <h1>Ikasleen zerrenda</h1>
  <p class="lead"><code>SELECT</code> bidez datu-basetik irakurritako errenkadak.</p>

  <table>
    <thead>
      <tr><th>ID</th><th>Izena</th><th>Emaila</th><th>Sortua</th></tr>
    </thead>
    <tbody>
    <?php if (!$ikasleak): ?>
      <tr><td colspan="4">Ez dago ikaslerik. <a href="gehitu.php">Gehitu bat</a>.</td></tr>
    <?php else: ?>
      <?php foreach ($ikasleak as $i): ?>
        <tr>
          <td><?= (int) $i['id'] ?></td>
          <td><?= htmlspecialchars($i['izena']) ?></td>
          <td><?= htmlspecialchars($i['emaila']) ?></td>
          <td><?= htmlspecialchars($i['sortua']) ?></td>
        </tr>
      <?php endforeach; ?>
    <?php endif; ?>
    </tbody>
  </table>

  <p class="actions">
    <a href="gehitu.php">Ikaslea gehitu</a> ·
    <a href="proba.php">Konexioa probatu</a>
  </p>
</main>
</body>
</html>
