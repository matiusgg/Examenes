<?php

include_once('datosmercadona.php');
include_once('funcionesmercadona.php');


$subtotalsuma = subtotal($productos);

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="../css/reset.css">
    <link rel="stylesheet" href="../css/ticket.css">
    <title>Document</title>
</head>
<body background="../img/fondopapelarrugado.jpg">
    <header>
    <h1>
    TICKET
    </h1>

    <h2>
    C HISTORIADOR AGUSTIN MU=0Z
    </h2>

    <h2>
    BRRDA. LA VID
    </h2>

    <h2>
    JEREZ DE LA FRONTERA
    </h2>
<h2>
<?php
// Aqui ira el codigo del empleado cajero
?>
</h2>

    <h2>

TICKET: COMP
    </h2>

    <h2>
        MESA 22
    </h2>
    </header>

    <br>

    <section class="contenidoproducto">
<article>

<span>Unidades</span>
<span>Descripcion</span>
<span>Precio/Unidad</span>



<?php
$contador = 0;

foreach ($productos AS $valor) {


    if($valor != NULL) {

        echo('<!-- Linea/fila -->');

    echo('<span>');

    
    echo($_POST['descripcion0' . $contador]);
    

echo('</span>');

echo('<span>');


    echo($_POST['unidad0' . $contador]);
    

echo('</span>');

echo('<span>');


    echo('producto = ' . $valor );
    

echo('</span>');

    }

$contador++;

}

echo('<h2> BASE </h2>');

// subtotal

echo('<br>' . $subtotalsuma);


// IVA

echo('<h2> IVA </h2>');

echo('<br>' . iva($subtotalsuma));

// TotalFactura. Aqui ponemos el array de datos $precios porque $precios contiene todas las operaciones anteriores  ademas de sus funciones, porque ahora mismo $precios es global porque lo que hicimos en datos y con los includes fue hacer que este array recopilara todo.


echo('<br>' . total($productos));



?>



</article>

    </section>

    <footer>

<h2>

IVA INCLUDO
</h2>
<br>

<h2>

GRACIAS POR SU VISITA
</h2>
    </footer>
</body>
</html>