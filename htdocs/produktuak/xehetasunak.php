<?php
/**
 * xehetasunak.php — Produktuaren xehetasunak
 * Izena, deskribapena, irudia, prezioa + zerrendara itzuli.
 */
require __DIR__ . '/konexioa.php';

$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if (!$id) {
    http_response_code(400);
    exit('Produktuaren IDa beharrezkoa da.');
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

$irudiIzena = $produktua['irudia'] ?: 'lehenetsia.png';
$irudiBidea = __DIR__ . '/irudiak/' . basename($irudiIzena);
$irudiUrl = is_file($irudiBidea)
    ? 'irudiak/' . rawurlencode(basename($irudiIzena))
    : 'irudiak/lehenetsia.png';
?>
<!DOCTYPE html>
<html lang="eu">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title><?= htmlspecialchars($produktua['izena']) ?> — Denda</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,550;9..144,650&family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css">
</head>
<body>
<div class="wrap">
  <header class="brand">
    <strong>Denda</strong>
    <span>Produktuaren xehetasunak</span>
  </header>

  <section class="panel detail">
    <div class="detail-media">
      <img src="<?= htmlspecialchars($irudiUrl) ?>"
           alt="<?= htmlspecialchars($produktua['izena']) ?>">
    </div>
    <div>
      <h1><?= htmlspecialchars($produktua['izena']) ?></h1>
      <p class="price-tag"><?= number_format((float) $produktua['prezioa'], 2, ',', '.') ?> €</p>
      <p class="lead" style="margin-bottom:1.5rem">
        <?= nl2br(htmlspecialchars($produktua['deskribapena'] ?? 'Deskribapenik ez.')) ?>
      </p>
      <div class="actions">
        <a class="btn secondary" href="index.php">← Zerrendara itzuli</a>
        <a class="btn" href="editatu.php?id=<?= (int) $produktua['id'] ?>">Editatu</a>
        <a class="btn danger" href="ezabatu.php?id=<?= (int) $produktua['id'] ?>"
           onclick="return confirm('Ziur produktua ezabatu nahi duzula?');">Ezabatu</a>
      </div>
    </div>
  </section>
</div>
</body>
</html>
