<?php
declare(strict_types=1);

// Saioa martxan jarri erabiltzailearen egoera mantentzeko
session_start();

// BASE_URL kalkulatzen da edozein kokapenetik aplikazioa eskalagarria izan dadin
$scriptName = str_replace('\\', '/', $_SERVER['SCRIPT_NAME']);
$basePath = rtrim(str_replace('\\', '/', dirname($scriptName)), '/');
if ($basePath === '/' || $basePath === '\\') {
    $basePath = '';
}
define('BASE_URL', $basePath);

// Konfigurazio eta kontrol geruzak kargatu
$pdo = require __DIR__ . '/../config/db.php';
$translations = require __DIR__ . '/../config/lang.php';
require __DIR__ . '/../controllers/IkasleController.php';

$controller = new IkasleController($pdo, $translations);
$action = $_GET['action'] ?? 'index';

// Ekintzen router sinplea, eskalagarritasuna kontuan hartuta eraikia
switch ($action) {
    case 'create':
        $controller->create();
        break;
    case 'store':
        $controller->store();
        break;
    case 'edit':
        $controller->edit();
        break;
    case 'update':
        $controller->update();
        break;
    case 'delete':
        $controller->delete();
        break;
    case 'show':
        $controller->show();
        break;
    case 'logs':
        $controller->logs();
        break;
    default:
        $controller->index();
        break;
}
