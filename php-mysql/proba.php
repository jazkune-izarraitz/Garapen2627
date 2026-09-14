<?php
/**
 * proba.php
 * Konexioa azkar egiaztatu: SELECT 1 + ikasleen kopurua.
 *
 * Exekutatu: php proba.php
 * edo nabigatzailean: http://localhost:8000/proba.php
 */

require __DIR__ . '/konexioa.php';

$cli = (PHP_SAPI === 'cli');

try {
    $pdo->query('SELECT 1');
    $kopurua = (int) $pdo->query('SELECT COUNT(*) FROM ikasleak')->fetchColumn();
    $lerroak = $pdo->query('SELECT id, izena, emaila FROM ikasleak ORDER BY id')->fetchAll();

    if ($cli) {
        echo "OK: konexioa ondo dago\n";
        echo "Ikasleak taulan: $kopurua\n\n";
        foreach ($lerroak as $i) {
            echo "  #{$i['id']}  {$i['izena']}  <{$i['emaila']}>\n";
        }
        exit(0);
    }

    header('Content-Type: text/html; charset=utf-8');
    echo '<!DOCTYPE html><html lang="eu"><head><meta charset="UTF-8"><title>Proba</title>';
    echo '<style>body{font-family:system-ui;max-width:40rem;margin:2rem auto;padding:0 1rem}';
    echo '.ok{color:#0a7a2f;font-weight:700}</style></head><body>';
    echo '<p class="ok">OK: konexioa ondo dago</p>';
    echo "<p>Ikasleak taulan: <strong>$kopurua</strong></p><ul>";
    foreach ($lerroak as $i) {
        echo '<li>#' . htmlspecialchars((string) $i['id']) . ' '
            . htmlspecialchars($i['izena']) . ' &lt;'
            . htmlspecialchars($i['emaila']) . '&gt;</li>';
    }
    echo '</ul><p><a href="zerrenda.php">Zerrenda</a> · <a href="gehitu.php">Gehitu</a></p>';
    echo '</body></html>';
} catch (PDOException $e) {
    if ($cli) {
        fwrite(STDERR, 'Errorea: ' . $e->getMessage() . "\n");
        exit(1);
    }
    http_response_code(500);
    echo 'Errorea: ' . htmlspecialchars($e->getMessage());
}
