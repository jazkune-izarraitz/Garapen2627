<?php
// Produktuaren xehetasunak
require "konexioa.php";

$id = $_GET["id"];
$emaitza = mysqli_query($konexioa, "SELECT * FROM produktuak WHERE id = $id");
$p = mysqli_fetch_assoc($emaitza);
?>
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Xehetasunak</title>
</head>
<body>

<h1><?php echo $p["izena"]; ?></h1>
<p>Prezioa: <?php echo $p["prezioa"]; ?> €</p>
<p>Deskribapena: <?php echo $p["deskribapena"]; ?></p>
<p><img src="irudiak/<?php echo $p["irudia"]; ?>" width="200"></p>

<p><a href="index.php">Zerrendara itzuli</a></p>

</body>
</html>
