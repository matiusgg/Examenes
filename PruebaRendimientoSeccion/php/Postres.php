<?php
require '../vendor/autoload.php';
use models\{Producto};

$comidaRapida = new Producto('localhost', 'root', '', 'restaurante');

// echo('<pre>');
// print_r($_REQUEST);
// echo('</pre>');

session_start();

$datos = $_SESSION['requestHamb'];

$_SESSION['requestBebidas'] = $_REQUEST;

echo('<pre>');
print_r($datos);
echo('</pre>');


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
 <form action="Ticket.php" method="post">
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

<h2>ESCOGE ENTRE LAS OPCIONE SQUE QUIERES PEDIR</h2>

<br>

<?php


// if(!empty($_REQUEST)) {

// $i = 0;

// foreach($_REQUEST AS $key => $valor) {

//     if($valor == "") {

//     echo('<input type="hidden" name="' . $key . '" value="' . $valor .'">');

//     }

//     else{

//         echo('<input type="hidden" name="' . $key . '" value="' . $valor .'">');
//     }

//     $i++;

// }

// }

$comidaRapida-> MostrarProductosPostres('productos');

?>

<br>

<button type="submit">Almacenar</button>

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