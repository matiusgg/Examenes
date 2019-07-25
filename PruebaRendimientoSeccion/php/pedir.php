<?php
require '../vendor/autoload.php';
use models\{Producto};

$productos = new Producto('localhost', 'root', '', 'restaurante');

// $comidaRapida-> EnviarComida();

?>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Productos</title>
    <link rel="stylesheet" href="css/reset.css">
    <link rel="stylesheet" href="css/styles.css">
    
</head>
<body>
 <form action="Liquidos.php" method="post">
        <!-- <input type="text" name="dniLogin" placeholder="introduce tu DNI"
        pattern="[0-9]{8}[a-zA-Z]{1}">
        <button type="submit">Enviar</button> -->

        
  

    <!-- HEADER -->

    <header>
   <h1>
   BIENVENIDO A BURGUERS INC!!
   </h1>
   <br>
   <h2>
ESCOGE TU COMIDA FAVORITA!!!

</h2>
    </header>

<!-- SECTION -->
    <section>
    <article>
    <div>

<h2>ESCOGE ENTRE LAS OPCIONES QUE QUIERES PEDIR</h2>

<br>

<?php

$productos-> MostrarProductosComida('productos');

echo "<h1>";
"ESCOGE LAS BEBIDAS QUE QUIERAS";
echo "</h1>";




?>

<br>

<input type="submit" name="almacenar" class="almacenar">


<br>




    </div>
    </article>
    </section>

    <!-- FOOTER -->

    <footer>
    
    
    </footer>

    </form>
</body>
</html>