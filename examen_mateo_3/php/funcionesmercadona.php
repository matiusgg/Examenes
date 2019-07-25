<?php

// Aqui estaran las funciones para poder realizar las respectivas operaciones.

// Precio Producto * Unidad =

function precioproducto($unidad, $precio) {

    
    $solucion = $unidad * $precio;
    return $solucion;
}



// Subtotal
function subtotal($precio) {


    // Hacer un bucle con forache porque es un array, lo que queremos es que cada vez que nos haga una 'vuelta' en el array, nos sume uno, para que estemos en el siguiente llave=>valor
    $suma = 0;
foreach ($precio AS $valor){

    $suma += $valor;

};

return $suma;
}

// Calcular el IVA
 //Multiplicar el subtotal * 1.33 y sumar al sodium_crypto_box_keypair_from_secretkey_and_publickey
 function iva($subtotal, $iva = 1.33){ // cuando le ponemos el valor a un parametro nos permite que cada vez que haga la operacion, lo haga con el valor que le pusimos al parametro obviamente, esto  es mejor que asignarle un valor desde dentro y no estableciendo el valor fijo
    $porcentaje = $subtotal * $iva;
   
    // pusimos en comentarios esto porque no necesitamos que nos haga una operacion final, solo que nos muestre el dato final
      
    return $porcentaje;
    }




function total($precio) {

    $subtotal = subtotal($precio);

    $iva = iva($subtotal);

    $solucion = $subtotal + $iva;

    return $solucion;



}
