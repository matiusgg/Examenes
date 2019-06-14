
<?php
if( !empty($_POST['multar'])) {


    header('Location: formularioMultar.php');
}

if( !empty($_POST['tramitepago'])) {


    header('Location: tipoPago.php');
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

<form action="opciones.php" method="post">

<!-- HEADER -->
    <header>
        <h1>
        ESCOGE ENTRE LAS OPCIONES
        </h1>
    </header>

<!-- SECTION -->
<section>
    <article>
    <!-- Input enviar multar -->

<input type="submit" name="multar" class="formulario__inbox_botonmultar" value="MULTAR">

<!-- Input enviar tramitarpago -->

<input type="submit" name="tramitepago" class="formulario__inbox_botontramitepago" value="TRAMITAR PAGO">


    </article>
</section>

<!-- FOOTER -->
<footer>
</footer>

</form>

</body>
</html>