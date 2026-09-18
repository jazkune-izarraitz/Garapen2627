<!DOCTYPE html>
<html lang="eu">
<head>
    <meta charset="UTF-8">
    <title>Jarduera 5: Formularioa</title>
</head>
<body>
    <h1>Jarduera 5: Formularioaren datuak jasotzea</h1>

    <form method="post" action="">
        <label for="izena">Izena:</label>
        <input type="text" id="izena" name="izena" required>
        <button type="submit">Bidali</button>
    </form>

    <?php
    // Formularioa bidali ondoren izena erakutsi
    if ($_SERVER["REQUEST_METHOD"] === "POST" && isset($_POST["izena"])) {
        $izena = htmlspecialchars($_POST["izena"], ENT_QUOTES, "UTF-8");
        echo "<p>Kaixo, <strong>$izena</strong>!</p>";
    }
    ?>
</body>
</html>
