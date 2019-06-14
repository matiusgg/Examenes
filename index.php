<?php
require_once 'vendor/autoload.php';
use models\{Conexion};

$BDmultas = new Conexion('localhost', 'root', '', 'multasagentes');



if(!empty($_POST['dni'])) {

   $BDmultas-> dniAcceso('agente');

}


?>
<!-- HTML5 --> 
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

<form action="index.php" method="post">

<!-- HEADER -->
<header>
        <h1>
        BIENVENIDO A AGENTESCOMPANY!!
        </h1>
    </header>

<!-- SECTION -->
<section>
    <article>
    <h2>
    INGRESA TU DNI
    </h2>

    <input type="text" name="dni" placeholder='Introduce DNI' pattern = "[0-9]{8}[A-Z][z-a]{1}">

    <button type="submit">
    INGRESAR
    </button>
    </article>
</section>

<!-- FOOTER -->
<footer>
</footer>

</form>

</body>
</html>


