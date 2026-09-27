<?php
// Produktuen zerrenda
require "konexioa.php";

// Produktu berria gorde
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $izena = $_POST["izena"];
    $deskribapena = $_POST["deskribapena"];
    $prezioa = $_POST["prezioa"];
    $irudia = $_POST["irudia"];

    $sql = "INSERT INTO produktuak (izena, deskribapena, prezioa, irudia)
            VALUES ('$izena', '$deskribapena', '$prezioa', '$irudia')";
    mysqli_query($konexioa, $sql);

    header("Location: index.php");
    exit;
}

$emaitza = mysqli_query($konexioa, "SELECT id, izena, prezioa FROM produktuak");
?>
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Produktuak</title>
</head>
<body>

<h1>Produktuen zerrenda</h1>

<table border="1">
  <tr>
    <th>Izena</th>
    <th>Prezioa</th>
    <th>Ekintzak</th>
  </tr>

<?php
while ($p = mysqli_fetch_assoc($emaitza)) {
    echo "<tr>";
    echo "<td>" . $p["izena"] . "</td>";
    echo "<td>" . $p["prezioa"] . " €</td>";
    echo "<td>";
    echo "<a href='xehetasunak.php?id=" . $p["id"] . "'>Ikusi</a> | ";
    echo "<a href='editatu.php?id=" . $p["id"] . "'>Editatu</a> | ";
    echo "<a href='ezabatu.php?id=" . $p["id"] . "'>Ezabatu</a>";
    echo "</td>";
    echo "</tr>";
}
?>

</table>

<h2>Produktu berria</h2>
<form method="post">
  Izena: <input name="izena"><br><br>
  Deskribapena: <input name="deskribapena"><br><br>
  Prezioa: <input name="prezioa"><br><br>
  Irudia: <input name="irudia"><br><br>
  <button type="submit">Gorde</button>
</form>

</body>
</html>
