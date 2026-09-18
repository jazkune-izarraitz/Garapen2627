<!DOCTYPE html>
<html lang="eu">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Oinarrizko PHP jarduerak</title>
    <style>
        body {
            font-family: system-ui, sans-serif;
            max-width: 720px;
            margin: 2rem auto;
            padding: 0 1rem;
            line-height: 1.5;
        }
        h1 { margin-bottom: 0.25rem; }
        h2 {
            margin-top: 2rem;
            border-bottom: 1px solid #ccc;
            padding-bottom: 0.25rem;
        }
        .emaitza {
            background: #f4f4f4;
            padding: 0.75rem 1rem;
            border-radius: 4px;
        }
        form {
            margin-top: 0.75rem;
        }
        label { display: block; margin-bottom: 0.35rem; }
        input[type="text"] {
            padding: 0.35rem 0.5rem;
            width: min(100%, 280px);
        }
        button {
            margin-top: 0.5rem;
            padding: 0.4rem 0.9rem;
            cursor: pointer;
        }
        ul { margin: 0.5rem 0; }
    </style>
</head>
<body>
    <h1>Oinarrizko PHP jarduerak</h1>
    <p>Orrialde bakarrean: jarduera 1etik 7ra.</p>

    <?php
    // ============================================================
    // Jarduera 1: Hello World
    // ============================================================
    ?>
    <h2>Jarduera 1: Hello World</h2>
    <div class="emaitza">
        <?php
        echo "Hello World";
        ?>
    </div>

    <?php
    // ============================================================
    // Jarduera 2: Aldagaiak eta operazioak
    // ============================================================
    $zenbaki1 = 10;
    $zenbaki2 = 5;
    ?>
    <h2>Jarduera 2: Aldagaiak eta operazioak</h2>
    <div class="emaitza">
        <?php
        echo "zenbaki1 = $zenbaki1, zenbaki2 = $zenbaki2<br>";
        echo "Batuketa: " . ($zenbaki1 + $zenbaki2) . "<br>";
        echo "Kenketa: " . ($zenbaki1 - $zenbaki2) . "<br>";
        echo "Biderketa: " . ($zenbaki1 * $zenbaki2) . "<br>";
        echo "Zatiketa: " . ($zenbaki1 / $zenbaki2);
        ?>
    </div>

    <?php
    // ============================================================
    // Jarduera 3: Baldintzak
    // ============================================================
    $adina = 16;
    ?>
    <h2>Jarduera 3: Baldintzak</h2>
    <div class="emaitza">
        <?php
        echo "Adina: $adina<br>";
        if ($adina < 18) {
            echo "Adingabea zara";
        } else {
            echo "Heldua zara";
        }
        ?>
    </div>

    <?php
    // ============================================================
    // Jarduera 4: Bukleak
    // ============================================================
    ?>
    <h2>Jarduera 4: Bukleak</h2>
    <div class="emaitza">
        <?php
        for ($i = 1; $i <= 10; $i++) {
            echo $i;
            if ($i < 10) {
                echo " ";
            }
        }
        ?>
    </div>

    <?php
    // ============================================================
    // Jarduera 5: Formularioaren datuak jasotzea
    // ============================================================
    ?>
    <h2>Jarduera 5: Formularioaren datuak jasotzea</h2>
    <div class="emaitza">
        <form method="post" action="">
            <label for="izena">Izena:</label>
            <input type="text" id="izena" name="izena" required>
            <br>
            <button type="submit" name="bidali">Bidali</button>
        </form>
        <?php
        if ($_SERVER["REQUEST_METHOD"] === "POST" && isset($_POST["izena"])) {
            $izena = htmlspecialchars($_POST["izena"], ENT_QUOTES, "UTF-8");
            echo "<p>Kaixo, <strong>$izena</strong>!</p>";
        }
        ?>
    </div>

    <?php
    // ============================================================
    // Jarduera 6: Array-ak eta bukleak
    // ============================================================
    $frutak = ["sagarra", "banana", "kiwi"];
    ?>
    <h2>Jarduera 6: Array-ak eta bukleak</h2>
    <div class="emaitza">
        <ul>
            <?php
            foreach ($frutak as $fruta) {
                echo "<li>" . htmlspecialchars($fruta, ENT_QUOTES, "UTF-8") . "</li>";
            }
            ?>
        </ul>
    </div>

    <?php
    // ============================================================
    // Jarduera 7: Funtzio sinple bat
    // ============================================================

    /**
     * Zenbaki bat bikoizten du.
     */
    function bikoiztu($x)
    {
        return $x * 2;
    }

    $zenbakia = 7;
    $emaitza = bikoiztu($zenbakia);
    ?>
    <h2>Jarduera 7: Funtzio sinple bat</h2>
    <div class="emaitza">
        <?php
        echo "bikoiztu($zenbakia) = $emaitza";
        ?>
    </div>

</body>
</html>
