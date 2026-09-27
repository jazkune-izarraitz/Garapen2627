<?php
/**
 * index.php — Produktuen zerrenda
 * Izena + prezioa, gehitu, ezabatu eta editatu.
 */
require __DIR__ . '/konexioa.php';

$mezua = '';
$errorea = '';

if ($_SERVER['REQUEST_METHOD'] === 'POST' && ($_POST['ekintza'] ?? '') === 'gehitu') {
    $izena = trim($_POST['izena'] ?? '');
    $deskribapena = trim($_POST['deskribapena'] ?? '');
    $prezioa = trim($_POST['prezioa'] ?? '');
    $irudia = trim($_POST['irudia'] ?? '');

    if ($izena === '' || $prezioa === '') {
        $errorea = 'Izena eta prezioa beharrezkoak dira.';
    } elseif (!is_numeric($prezioa) || (float) $prezioa < 0) {
        $errorea = 'Prezioak zenbaki positiboa izan behar du.';
    } else {
        $stmt = $pdo->prepare(
            'INSERT INTO produktuak (izena, deskribapena, prezioa, irudia) VALUES (?, ?, ?, ?)'
        );
        $stmt->execute([
            $izena,
            $deskribapena !== '' ? $deskribapena : null,
            number_format((float) $prezioa, 2, '.', ''),
            $irudia !== '' ? $irudia : 'lehenetsia.png',
        ]);
        header('Location: index.php?ok=1');
        exit;
    }
}

if (isset($_GET['ok'])) {
    $mezua = 'Produktua ondo gorde da.';
}
if (isset($_GET['ezabatuta'])) {
    $mezua = 'Produktua ezabatu da.';
}
if (isset($_GET['eguneratuta'])) {
    $mezua = 'Produktua eguneratu da.';
}

$produktuak = $pdo->query(
    'SELECT id, izena, prezioa FROM produktuak ORDER BY id'
)->fetchAll();
?>
<!DOCTYPE html>
<html lang="eu">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Denda — Produktuak</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,550;9..144,650&family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css">
</head>
<body>
<div class="wrap">
  <header class="brand">
    <strong>Denda</strong>
    <span>Produktuen katalogoa</span>
  </header>

  <section class="panel">
    <h1>Produktuen zerrenda</h1>
    <p class="lead">Izena eta prezioa. Hautatu bat xehetasunak ikusteko, edo kudeatu katalogoa.</p>

    <?php if ($mezua): ?><div class="flash"><?= htmlspecialchars($mezua) ?></div><?php endif; ?>
    <?php if ($errorea): ?><div class="flash err"><?= htmlspecialchars($errorea) ?></div><?php endif; ?>

    <?php if (!$produktuak): ?>
      <p class="empty">Ez dago produkturik oraindik. Gehitu lehenengoa behean.</p>
    <?php else: ?>
      <table>
        <thead>
          <tr>
            <th>Izena</th>
            <th class="prezioa">Prezioa</th>
            <th>Ekintzak</th>
          </tr>
        </thead>
        <tbody>
        <?php foreach ($produktuak as $p): ?>
          <tr>
            <td>
              <a href="xehetasunak.php?id=<?= (int) $p['id'] ?>">
                <?= htmlspecialchars($p['izena']) ?>
              </a>
            </td>
            <td class="prezioa"><?= number_format((float) $p['prezioa'], 2, ',', '.') ?> €</td>
            <td>
              <div class="actions">
                <a class="btn linkish" href="xehetasunak.php?id=<?= (int) $p['id'] ?>">Ikusi</a>
                <a class="btn linkish" href="editatu.php?id=<?= (int) $p['id'] ?>">Editatu</a>
                <a class="btn linkish" href="ezabatu.php?id=<?= (int) $p['id'] ?>"
                   onclick="return confirm('Ziur produktua ezabatu nahi duzula?');">Ezabatu</a>
              </div>
            </td>
          </tr>
        <?php endforeach; ?>
        </tbody>
      </table>
    <?php endif; ?>
  </section>

  <section class="panel">
    <h2>Produktu berria</h2>
    <p class="lead">Txertatu produktu bat datu-basean.</p>
    <form method="post" action="" class="form-grid">
      <input type="hidden" name="ekintza" value="gehitu">

      <label for="izena">Izena</label>
      <input id="izena" name="izena" required maxlength="100"
             value="<?= htmlspecialchars($_POST['izena'] ?? '') ?>">

      <label for="deskribapena">Deskribapena</label>
      <textarea id="deskribapena" name="deskribapena" maxlength="2000"><?= htmlspecialchars($_POST['deskribapena'] ?? '') ?></textarea>

      <label for="prezioa">Prezioa (€)</label>
      <input id="prezioa" name="prezioa" type="number" step="0.01" min="0" required
             value="<?= htmlspecialchars($_POST['prezioa'] ?? '') ?>">

      <label for="irudia">Irudi fitxategia (irudiak/ karpetan)</label>
      <input id="irudia" name="irudia" maxlength="255" placeholder="adib. te.png"
             value="<?= htmlspecialchars($_POST['irudia'] ?? '') ?>">

      <p style="margin-top:1rem">
        <button class="btn" type="submit">Gorde produktua</button>
      </p>
    </form>
  </section>
</div>
</body>
</html>
