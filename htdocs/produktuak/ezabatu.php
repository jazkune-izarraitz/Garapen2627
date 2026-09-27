<?php
// Produktua ezabatu
require "konexioa.php";

$id = $_GET["id"];
mysqli_query($konexioa, "DELETE FROM produktuak WHERE id = $id");

header("Location: index.php");
exit;
?>
