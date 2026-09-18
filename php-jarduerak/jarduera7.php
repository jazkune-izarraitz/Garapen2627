<!DOCTYPE html>
<html lang="eu">
<head>
    <meta charset="UTF-8">
    <title>Jarduera 7: Funtzioa</title>
</head>
<body>
    <h1>Jarduera 7: Funtzio sinple bat</h1>
    <?php
    /**
     * Zenbaki bat bikoizten du.
     */
    function bikoiztu($x)
    {
        return $x * 2;
    }

    $zenbakia = 7;
    echo "bikoiztu($zenbakia) = " . bikoiztu($zenbakia);
    ?>
</body>
</html>
