<?php
/**
 * ezabatu.php — Produktua ezabatu
 */
require __DIR__ . '/konexioa.php';

$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if (!$id) {
    http_response_code(400);
    exit('Produktuaren IDa beharrezkoa da.');
}

$stmt = $pdo->prepare('DELETE FROM produktuak WHERE id = ?');
$stmt->execute([$id]);

header('Location: index.php?ezabatuta=1');
exit;
