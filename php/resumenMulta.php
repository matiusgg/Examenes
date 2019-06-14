<?php
require_once '../vendor/autoload.php';
use models\{Conexion};

// echo('<pre>');
// print_r($_REQUEST);
// echo('</pre>');

$infractor = new Conexion('localhost', 'root', '', 'multasagentes');

if(!empty($_REQUEST)) {

    $inputDNI = $_POST['dniformulario'];
    $inputMulta = $_POST['tipoMultas'];

    $infractor->InsertarMulta('infractor', $inputMulta, $inputDNI);

    $infractor->InsertarAgenteID('infractor', $inputMulta, $inputDNI);
}

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

$infractor-> verTuplas('infractor');

?>

<a href="opciones.php">VOLVER</a>

<br>

<?php

echo('<a href="mensajeConsulta.php?tipoMultas=' . $_POST['tipoMultas'] . '&nombreCompleto=' . $_POST['nombreCompleto'] . '&"> TRAMITAR CONSULTA AL INFRACTOR</a>');

?>
    </article>
</section>

<!-- FOOTER -->
<footer>
</footer>

</body>
</html>