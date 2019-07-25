<?php
require_once '../vendor/autoload.php';
use models\{Conexion, Infractor};

// echo('<pre>');
// print_r($_REQUEST);
// echo('</pre>');



$infractor = new Infractor('localhost', 'root', '', 'multasagentes');


?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Inicio</title>
    <!-- links externos -->
    <link rel="stylesheet" href="css/reset.css">
    <link rel="stylesheet" href="css/style.css">
    <!-- Fontawesome -->
</head>

<body>

<!-- HEADER -->
    <header>
        
    </header>

<!-- SECTION -->
<section>
    <article>
    <?php


$inputDNI = $_GET['dniformulario'];

echo($inputDNI);


$inputPlaca = $_GET['placacoche'];

echo($inputPlaca);

$inputNombre = $_GET['nombreCompleto'];

$infractor-> verInfractor('infractor', $inputDNI, $inputPlaca);

?>

<br>

<a href="opciones.php">VOLVER</a>

<br>
    </article>
</section>

<!-- FOOTER -->
<footer>
</footer>

</body>
</html>