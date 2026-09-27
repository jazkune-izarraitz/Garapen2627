<?php
// Datu-basea ikusi
require "konexioa.php";

$emaitza = mysqli_query($konexioa, "SELECT * FROM produktuak");
?>
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>DB froga</title>
</head>
<body>

<h1>Datu-basea OK</h1>
<p>Konektatuta: denda</p>

<table border="1">
  <tr>
    <th>id</th>
    <th>izena</th>
    <th>deskribapena</th>
    <th>prezioa</th>
    <th>irudia</th>
  </tr>

<?php
while ($p = mysqli_fetch_assoc($emaitza)) {
    echo "<tr>";
    echo "<td>" . $p["id"] . "</td>";
    echo "<td>" . $p["izena"] . "</td>";
    echo "<td>" . $p["deskribapena"] . "</td>";
    echo "<td>" . $p["prezioa"] . "</td>";
    echo "<td>" . $p["irudia"] . "</td>";
    echo "</tr>";
}
?>

</table>

<p><a href="index.php">Zerrendara itzuli</a></p>

</body>
</html>
