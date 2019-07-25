<?php
require '../vendor/autoload.php';
use models\{Cliente};

$registro = new Cliente('localhost', 'root', '', 'restaurante');



if( !empty($_REQUEST)){

    $inputNombre = $_POST['nombre'];
    $inputApellidos = $_POST['apellidos'];
    $inputLocalidad = $_POST['localidad'];
    $inputTelefono = $_POST['telefono'];
    $inputEmail = $_POST['email'];
    $inputDni = $_POST['dni'];



    $AtributosDatos = [

        'nombre' => $inputNombre,
        'apellidos' => $inputApellidos,
        'localidad' => $inputLocalidad,
        'telefono' => $inputTelefono,
        'gmail' => $inputEmail,
        'dni' => $inputDni
];

print_r($AtributosDatos);

$registro->RegistrarInputsUsuario('clientes', $AtributosDatos);

// echo('PERFECTO, HA SIDO REGISTRADO');

}


?>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Productos</title>
    <link rel="stylesheet" href="../css/reset.css">
    <link rel="stylesheet" href="../css/styles.css">
    
</head>
<body>
 <form action="registroUsuario.php" method="post">
        <!-- <input type="text" name="dniLogin" placeholder="introduce tu DNI"
        pattern="[0-9]{8}[a-zA-Z]{1}">
        <button type="submit">Enviar</button> -->

        
  

    <!-- HEADER -->

    <header>
    <nav>

    <a href="../index.php">VOLVER</a>

    </nav>
    </header>

<!-- SECTION -->
    <section>
    <article>


    <div class="formulario">



    <label for="nombre">
    NOMBRE
    </label>

    <input type="text" name="nombre">


<br>

    <label for="apellidos">
    Apellidos
    </label>

    <input type="text" name="apellidos">


<br>

    <label for="localidad">
    LOCALIDAD
    </label>

    <input type="text" name="localidad">


<br>

    <label for="telefono">
    TELEFONO
    </label>

    <input type="text" name="telefono">


<br>
    <label for="email">
    EMAIL
    </label>

    <input type="text" name="email">

<br>

<label for="dni">
DNI
</label>

<input type="text" name="dni">

    <button type="submit">REGISTRARSE</button>


    </div>
    </article>
    </section>

    <!-- FOOTER -->

    <footer>
    
    
    </footer>

    </form>
</body>
</html>