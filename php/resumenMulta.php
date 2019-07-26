<?php
require_once '../vendor/autoload.php';
use models\{Conexion, Multas};

// echo('<pre>');
// print_r($_REQUEST);
// echo('</pre>');

$infractor = new Multas('localhost', 'root', '', 'multasagentes');



    $inputDNI = $_GET['dniformulario'];
    $inputPlaca = $_GET['placacoche'];
    $inputAgente = $_GET['agenteID'];

    echo($inputDNI . '<br>');
    echo($inputPlaca . '<br>');
    echo($inputAgente . '<br>');




    $infractor->MostrarAgenteID('agente', $inputAgente);








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

$infractor->mostrarMulta('puentemultas_infractor', 'infractor', 'agente', 'tipomultas');

?>

<a href="opciones.php">VOLVER</a>

<br>

<?php


// $inputNombre = $_POST['nombrecompleto'];

// echo('<a href="mensajeConsulta.php?tipoMultas=' . $inputMulta . '&nombrecompleto=' . $inputNombre . '&placacoche=' . $_POST['placacoche'] . '&dniformulario=' . $inputDNI . '"> TRAMITAR CONSULTA AL INFRACTOR</a>');

?>
    </article>
</section>

<!-- FOOTER -->
<footer>
</footer>

</body>
</html>