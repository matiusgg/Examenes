<?php

// Incluyo el archivo funcionesmercadona.php para que no halla necesidad de siempre ir poniendo un include dentro de las funciones cada vez que cree una nueva funcion
include_once('funcionesmercadona.php');

$productos = [
'tio pepe' => 1.30,
'cerveza botellin' => 1,20,
'huevos' => 4,50,
'croquetas' => 4,50,
'queso curado' => 6.80,
'jamon cocido' => 1.30,
'papel de cocina' => 3.80,
'zumo natural' => 4.10,
'pechugas de pollo' => 5.56,
'higado' => 0.80,
'manzanas' => 3.50

];


for($i=0; $i < 5; $i++){


    if(($_POST['descripcion0' . $i] != "" ) && ($_POST['unidad0' . $i]) != "") {
// Aqui le digo que me ponga los datos que revise dentro de los input
        precioproducto(
           (int) $_POST['descripcion0' . $i], 
           (int) $_POST['unidad0' . $i]);
        

      // Con (int), con convierte string en Enterio, esto nos beneficia porque nos permite mas comodamente en el caso de un numero, ponerlo en entero para que vaya mejor
     
      }
      // Aqui le digo que si al momento de poner la descripcion o unidades no ponen algun valor o dato dentro de algun input entonces que me ponga NULL
      

    }     




?>
