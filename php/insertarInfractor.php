<?php
require_once '../vendor/autoload.php';


use models\{Conexion, Infractor};

$infractor = new Infractor('localhost', 'root', '', 'multasagentes');


if(!empty($_REQUEST)){

    $infractor-> registrarInfractor($_REQUEST);

    $inputPlaca = $_POST['placacoche'];

    $inputDNI = $_POST['dniformulario'];

    $inputNombre = $_POST['nombreCompleto'];


    header('Location: resumenInfractor.php?placacoche='. $inputPlaca . '&dniformulario=' . $inputDNI . '&nombreCompleto=' . $inputNombre);
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



<form action="insertarInfractor.php" method="post">

<!-- HEADER -->
    <header>
        <h1>
        AGREGAR INFRACTOR
        </h1>
    </header>

<!-- SECTION -->
<section>
    <article>

    <!-- Nombre Completo Infractor -->
    
    <label for="nombreCompleto">
    Nombre Completo
    </label>

    <input type="text" name="nombreCompleto" placeholder="Nombre Completo">

    <br>

      <!-- DNI -->
    
      <label for="dniformulario">
    DNI infractor
    </label>

    <input type="text" name="dniformulario" placeholder="Introduzca el dni">
    
    
    
     <br>

      <!-- PLACA COCHE -->
    
      <label for="placacoche">
    Placa del Coche
    </label>

    <input type="text" name="placacoche" placeholder="Introduzca la placa del coche ">

    <br>

     <!-- TELEFONO -->
    
     <label for="telefono">
    Telefono
    </label>

    <input type="text" name="telefono" placeholder="Introduzca su Telefono">



    <br>
         <!-- CORREO -->
    
         <label for="correo">
    Correo
    </label>

    <input type="text" name="correo" placeholder="Introduzca su correo">

    <br>

         <!-- POBLACION -->
    
         <label for="poblacion">
    Poblacion
    </label>

    <input type="text" name="poblacion" placeholder="Introduzca su poblacion">

    <br>

         <!-- codigo postal -->
    
         <label for="codigoPostal">
    Codigo Postal
    </label>

    <input type="text" name="codigoPostal" placeholder="Introduzca su codigoPostal">

    <br>

         <!-- fecha de nacimiento -->
    
         <label for="fNacimiento">
    fecha de Nacimiento
    </label>

    <input type="text" name="fNacimiento" placeholder="Introduzca su fNacimiento">

    <br>

         <!-- Id Agente quien hizo la multa -->
    
         <label for="nacionalidad">
    acionalidad
    </label>

    <input type="text" name="nacionalidad" placeholder="Introduzca su nacionalidad">

    <br>

    <button type="submit">
    REGISTRAR
    </button>


    
    </article>
</section>

<!-- FOOTER -->
<footer>
</footer>


</form>
</body>
</html>