<?php
/**
 * editatu.php — Produktua eguneratu (gehigarria)
 */
require __DIR__ . '/konexioa.php';

$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT)
    ?: filter_input(INPUT_POST, 'id', FILTER_VALIDATE_INT);

if (!$id) {
    http_response_code(400);
    exit('Produktuaren IDa beharrezkoa da.');
}

$errorea = '';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
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
            'UPDATE produktuak
             SET izena = ?, deskribapena = ?, prezioa = ?, irudia = ?
             WHERE id = ?'
        );
        $stmt->execute([
            $izena,
            $deskribapena !== '' ? $deskribapena : null,
            number_format((float) $prezioa, 2, '.', ''),
            $irudia !== '' ? $irudia : 'lehenetsia.png',
            $id,
        ]);
        header('Location: index.php?eguneratuta=1');
        exit;
    }
}

$stmt = $pdo->prepare(
    'SELECT id, izena, deskribapena, prezioa, irudia FROM produktuak WHERE id = ?'
);
$stmt->execute([$id]);
$produktua = $stmt->fetch();

if (!$produktua) {
    http_response_code(404);
    exit('Produktua ez da aurkitu.');
}

$izena = $_POST['izena'] ?? $produktua['izena'];
$deskribapena = $_POST['deskribapena'] ?? ($produktua['deskribapena'] ?? '');
$prezioa = $_POST['prezioa'] ?? $produktua['prezioa'];
$irudia = $_POST['irudia'] ?? ($produktua['irudia'] ?? '');
?>
<!DOCTYPE html>
<html lang="eu">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Editatu — <?= htmlspecialchars($produktua['izena']) ?></title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,550;9..144,650&family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css">
</head>
<body>
<div class="wrap">
  <header class="brand">
    <strong>Denda</strong>
    <span>Produktua editatu</span>
  </header>

  <section class="panel">
    <h1>Editatu: <?= htmlspecialchars($produktua['izena']) ?></h1>
    <p class="lead">Aldatu eremuak eta gorde. (#<?= (int) $produktua['id'] ?>)</p>

    <?php if ($errorea): ?><div class="flash err"><?= htmlspecialchars($errorea) ?></div><?php endif; ?>

    <form method="post" action="" class="form-grid">
      <input type="hidden" name="id" value="<?= (int) $id ?>">

      <label for="izena">Izena</label>
      <input id="izena" name="izena" required maxlength="100"
             value="<?= htmlspecialchars((string) $izena) ?>">

      <label for="deskribapena">Deskribapena</label>
      <textarea id="deskribapena" name="deskribapena" maxlength="2000"><?= htmlspecialchars((string) $deskribapena) ?></textarea>

      <label for="prezioa">Prezioa (€)</label>
      <input id="prezioa" name="prezioa" type="number" step="0.01" min="0" required
             value="<?= htmlspecialchars((string) $prezioa) ?>">

      <label for="irudia">Irudi fitxategia</label>
      <input id="irudia" name="irudia" maxlength="255"
             value="<?= htmlspecialchars((string) $irudia) ?>">

      <p style="margin-top:1rem" class="actions">
        <button class="btn" type="submit">Gorde aldaketak</button>
        <a class="btn secondary" href="xehetasunak.php?id=<?= (int) $id ?>">Utzi</a>
        <a class="btn secondary" href="index.php">Zerrenda</a>
      </p>
    </form>
  </section>
</div>
</body>
</html>
