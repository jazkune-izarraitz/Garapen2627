<?php
// Produktua editatu
require "konexioa.php";

// Gorde aldaketak
if (isset($_POST["gorde"])) {
    $id = $_POST["id"];
    $izena = $_POST["izena"];
    $deskribapena = $_POST["deskribapena"];
    $prezioa = $_POST["prezioa"];
    $irudia = $_POST["irudia"];

    $sql = "UPDATE produktuak SET
            izena = '$izena',
            deskribapena = '$deskribapena',
            prezioa = '$prezioa',
            irudia = '$irudia'
            WHERE id = $id";
    mysqli_query($konexioa, $sql);

    header("Location: index.php");
    exit;
}

// Formularioa bete
$id = $_GET["id"];
$emaitza = mysqli_query($konexioa, "SELECT * FROM produktuak WHERE id = $id");
$p = mysqli_fetch_assoc($emaitza);
?>
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Editatu</title>
</head>
<body>

<h1>Editatu produktua</h1>

<form method="post">
  <input type="hidden" name="id" value="<?php echo $p["id"]; ?>">
  Izena: <input type="text" name="izena" value="<?php echo $p["izena"]; ?>"><br><br>
  Deskribapena: <input type="text" name="deskribapena" value="<?php echo $p["deskribapena"]; ?>"><br><br>
  Prezioa: <input type="text" name="prezioa" value="<?php echo $p["prezioa"]; ?>"><br><br>
  Irudia: <input type="text" name="irudia" value="<?php echo $p["irudia"]; ?>"><br><br>
  <input type="submit" name="gorde" value="Gorde">
  <a href="index.php">Utzi</a>
</form>

</body>
</html>
