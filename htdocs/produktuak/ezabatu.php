<?php
// Produktua ezabatu
require 'konexioa.php';

$id = (int) ($_GET['id'] ?? 0);
$pdo->prepare('DELETE FROM produktuak WHERE id = ?')->execute([$id]);

header('Location: index.php');
exit;
