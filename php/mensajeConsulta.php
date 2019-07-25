<?php

require_once '../vendor/autoload.php';
use models\{Conexion};

// echo('<pre>');
// print_r($_REQUEST);
// echo('</pre>');

$tipoMulta = new Conexion('localhost', 'root', '', 'multasagentes');


$inputNombre = $_GET['nombrecompleto'];
$inputDNI = $_GET['dniformulario'];
    $inputMulta = $_GET['tipoMultas'];
    $inputPlaca = $_GET['placacoche'];

    echo '<h3>DNI DEL INFRACTOR = </h3>' . $inputDNI;
    echo '<br>';
    echo '<h3>NOMBRE DEL INFRACTOR DEL INFRACTOR = </h3>' . $inputNombre;
    echo '<br>';
    echo '<h3>TIPO DE MULTA DEL INFRACTOR = </h3>' . $inputMulta;
    echo '<br>';
    echo '<h3>PLACA DEL INFRACTOR = </h3>' . $inputPlaca;
    echo '<br>';


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

<form action="../mailfactura.php">

<!-- HEADER -->
    <header>
        TRAMITE DE CONSULTA
    </header>

    <br>

<!-- SECTION -->
<section>
    <article>
    <h1>
    ENVIA UNA CONSULTA AL INFRACTOR SOBRE SU INFRACCION Y SU MULTA
    </h1>

<!-- De Parte de: -->

    <label for="de">
    De Parte de:
    </label>

    <input type="emailde" name="mailde" >

    <br>

    <!-- Para: -->

    <label for="de">
    Para: 
    </label>

    <input type="emailpara" name="mailde" >

    <br>

    <!-- Asunto: -->

    <h3>
    Asunto: 
    </h3>

    <textarea name="asunto" rows="10"></textarea>

    
    </article>

    <article>

    <br>
    <h2>
    Fecha de pago de la Multa(MAximo en 30 dias):
    </h2>

    <input type="date" name="fechapago">

    <br>

    <?php
$tipoMulta->MostrarPrecioMulta('infractor');
    ?>

<br>

<button type="submit">ENVIAR CONSULTA</button>
    </article>

    <br>

    <a href="../index.php">VOLVER AL INICIO</a>
</section>

<!-- FOOTER -->
<footer>
</footer>
</form>
</body>
</html>