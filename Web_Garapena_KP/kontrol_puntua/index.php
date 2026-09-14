<?php
declare(strict_types=1);

// Erro fitxategia: erabiltzailea automatikoki /public atarira eramaten du.
header('Location: ' . rtrim(dirname($_SERVER['SCRIPT_NAME']), '/\\') . '/public/');
exit;
