<?php
/**
 * gehitu.php
 * Formularioa + INSERT (prepared statement-ekin).
 */

require __DIR__ . '/konexioa.php';

$mezua = '';
$errorea = '';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $izena  = trim($_POST['izena'] ?? '');
    $emaila = trim($_POST['emaila'] ?? '');

    if ($izena === '' || $emaila === '') {
        $errorea = 'Izena eta emaila beharrezkoak dira.';
    } elseif (!filter_var($emaila, FILTER_VALIDATE_EMAIL)) {
        $errorea = 'Email formatua ez da zuzena.';
    } else {
        // Prepared statement: ? markak = erabiltzailearen datuak, ez SQL kodea
        $stmt = $pdo->prepare(
            'INSERT INTO ikasleak (izena, emaila) VALUES (?, ?)'
        );
        $stmt->execute([$izena, $emaila]);
        $mezua = 'Gordeta! ID berria: ' . $pdo->lastInsertId();
    }
}
?>
<!DOCTYPE html>
<html lang="eu">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Ikaslea gehitu</title>
  <style>
    :root { --accent: #1f6b4a; --err: #a11; --ok: #0a7a2f; }
    body { font-family: "Segoe UI", system-ui, sans-serif; background: linear-gradient(160deg, #e8f0ea, #f7f3ea); margin: 0; padding: 2rem 1rem; color: #1a2e24; }
    main { max-width: 28rem; margin: 0 auto; }
    h1 { font-size: 1.6rem; margin: 0 0 .35rem; }
    p.lead { margin: 0 0 1.25rem; opacity: .85; }
    label { display: block; font-weight: 600; margin: .75rem 0 .25rem; }
    input { width: 100%; box-sizing: border-box; padding: .55rem .65rem; border: 1px solid #c5d4cb; border-radius: 4px; font-size: 1rem; }
    button { margin-top: 1rem; background: var(--accent); color: #fff; border: 0; padding: .6rem 1.1rem; font-size: 1rem; cursor: pointer; border-radius: 4px; }
    .ok { color: var(--ok); font-weight: 600; }
    .err { color: var(--err); font-weight: 600; }
    a { color: var(--accent); }
  </style>
</head>
<body>
<main>
  <h1>Ikaslea gehitu</h1>
  <p class="lead"><code>INSERT</code> prepared statement bidez (SQL injection saihesteko).</p>

  <?php if ($mezua): ?><p class="ok"><?= htmlspecialchars($mezua) ?></p><?php endif; ?>
  <?php if ($errorea): ?><p class="err"><?= htmlspecialchars($errorea) ?></p><?php endif; ?>

  <form method="post" action="">
    <label for="izena">Izena</label>
    <input id="izena" name="izena" required maxlength="100"
           value="<?= htmlspecialchars($_POST['izena'] ?? '') ?>">

    <label for="emaila">Emaila</label>
    <input id="emaila" name="emaila" type="email" required maxlength="150"
           value="<?= htmlspecialchars($_POST['emaila'] ?? '') ?>">

    <button type="submit">Gorde</button>
  </form>

  <p style="margin-top:1.25rem">
    <a href="zerrenda.php">Zerrenda ikusi</a> ·
    <a href="proba.php">Konexioa probatu</a>
  </p>
</main>
</body>
</html>
