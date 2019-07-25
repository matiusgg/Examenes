<?php
$codigo = $_POST['codigo'];

$login = [

    'Xisco78' => 35456,
'Catalina94'  => 45466,
'Pedro99' => 12342,
'Manuel01' => 87900,
'Lisa96' => 57678

];



if( isset($codigo)) {

    foreach($login AS $valor) {

        if($valor == $codigo) {

      
            echo "Bienvenido " . $codigo;

        } 
    }
    if($valor != $codigo) {

        echo('Cogido incorrecto'. ' ' . '<a href="index.php"> Volver a Login </a>');
    }
}





?>



<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <form action="php/ticket.php" method="post">

    <section>
    <div class="contenedorgeneral">

    <!-- Logo Mercadona -->
    
    <img src="img/mercadonalogo.png">

    <!-- Unidades -->
    
    <label for="text">
    UNIDADES
    </label>

    <!-- inputs unidades -->

<input type="number" name="unidad00" id="unidad00">

<input type="number" name="unidad01" id="unidad01">

<input type="number" name="unidad02" id="unidad02">

<input type="number" name="unidad03" id="unidad03">

<input type="number" name="unidad04" id="unidad04">

<input type="number" name="unidad05" id="unidad05">

<input type="number" name="unidad06" id="unidad06">

<input type="number" name="unidad07" id="unidad07">

<input type="number" name="unidad08" id="unidad08">

<input type="number" name="unidad09" id="unidad09">

<input type="number" name="unidad010" id="unidad010">

<input type="number" name="unidad011" id="unidad011">



<!-- Descripcion -->
    
<label for="text">
   DESCRIPCION
    </label>

    <!-- selects descripcion -->

    <select name="descripcion00[]">
       
			<option value="tio pepe">tio pepe
			</option>
			<option value="cerveza botellin">cerveza botellin
			</option>
			<option value="huevos">huevos
			</option>
			<option value="croquetas">croquetas
            </option>
            <option value="queso curado">queso curado
			</option>
			<option value="jamon cocido">jamon cocido
			</option>
			<option value="papel de cocina">papel de cocina
			</option>
			<option value="zumo natural">zumo natural
            </option>
            <option value="pechugas de pollo">pechugas de pollo
			</option>
			<option value="higado">higado
			</option>
			<option value="manzanas">manzanas
			</option>
		</select>

        <select name="descripcion01[]">
        
			<option value="tio pepe">tio pepe
			</option>
			<option value="cerveza botellin">cerveza botellin
			</option>
			<option value="huevos">huevos
			</option>
			<option value="croquetas">croquetas
            </option>
            <option value="queso curado">queso curado
			</option>
			<option value="jamon cocido">jamon cocido
			</option>
			<option value="papel de cocina">papel de cocina
			</option>
			<option value="zumo natural">zumo natural
            </option>
            <option value="pechugas de pollo">pechugas de pollo
			</option>
			<option value="higado">higado
			</option>
			<option value="manzanas">manzanas
			</option>
		</select>

        <select name="descripcion02[]">
        
			<option value="tio pepe">tio pepe
			</option>
			<option value="cerveza botellin">cerveza botellin
			</option>
			<option value="huevos">huevos
			</option>
			<option value="croquetas">croquetas
            </option>
            <option value="queso curado">queso curado
			</option>
			<option value="jamon cocido">jamon cocido
			</option>
			<option value="papel de cocina">papel de cocina
			</option>
			<option value="zumo natural">zumo natural
            </option>
            <option value="pechugas de pollo">pechugas de pollo
			</option>
			<option value="higado">higado
			</option>
			<option value="manzanas">manzanas
			</option>
		</select>

   

        <select name="descripcion03[]">
        
			<option value="tio pepe">tio pepe
			</option>
			<option value="cerveza botellin">cerveza botellin
			</option>
			<option value="huevos">huevos
			</option>
			<option value="croquetas">croquetas
            </option>
            <option value="queso curado">queso curado
			</option>
			<option value="jamon cocido">jamon cocido
			</option>
			<option value="papel de cocina">papel de cocina
			</option>
			<option value="zumo natural">zumo natural
            </option>
            <option value="pechugas de pollo">pechugas de pollo
			</option>
			<option value="higado">higado
			</option>
			<option value="manzanas">manzanas
			</option>
		</select>


        <select name="descripcion04[]">
        
			<option value="tio pepe">tio pepe
			</option>
			<option value="cerveza botellin">cerveza botellin
			</option>
			<option value="huevos">huevos
			</option>
			<option value="croquetas">croquetas
            </option>
            <option value="queso curado">queso curado
			</option>
			<option value="jamon cocido">jamon cocido
			</option>
			<option value="papel de cocina">papel de cocina
			</option>
			<option value="zumo natural">zumo natural
            </option>
            <option value="pechugas de pollo">pechugas de pollo
			</option>
			<option value="higado">higado
			</option>
			<option value="manzanas">manzanas
			</option>
		</select>


        <select name="descripcion05[]">
        
			<option value="tio pepe">tio pepe
			</option>
			<option value="cerveza botellin">cerveza botellin
			</option>
			<option value="huevos">huevos
			</option>
			<option value="croquetas">croquetas
            </option>
            <option value="queso curado">queso curado
			</option>
			<option value="jamon cocido">jamon cocido
			</option>
			<option value="papel de cocina">papel de cocina
			</option>
			<option value="zumo natural">zumo natural
            </option>
            <option value="pechugas de pollo">pechugas de pollo
			</option>
			<option value="higado">higado
			</option>
			<option value="manzanas">manzanas
			</option>
		</select>

    
        <select multiple name="descripcion06[]">
      
			<option value="tio pepe">tio pepe
			</option>
			<option value="cerveza botellin">cerveza botellin
			</option>
			<option value="huevos">huevos
			</option>
			<option value="croquetas">croquetas
            </option>
            <option value="queso curado">queso curado
			</option>
			<option value="jamon cocido">jamon cocido
			</option>
			<option value="papel de cocina">papel de cocina
			</option>
			<option value="zumo natural">zumo natural
            </option>
            <option value="pechugas de pollo">pechugas de pollo
			</option>
			<option value="higado">higado
			</option>
			<option value="manzanas">manzanas
			</option>
		</select>

    
        <select multiple name="descripcion07[]">
        
			<option value="tio pepe">tio pepe
			</option>
			<option value="cerveza botellin">cerveza botellin
			</option>
			<option value="huevos">huevos
			</option>
			<option value="croquetas">croquetas
            </option>
            <option value="queso curado">queso curado
			</option>
			<option value="jamon cocido">jamon cocido
			</option>
			<option value="papel de cocina">papel de cocina
			</option>
			<option value="zumo natural">zumo natural
            </option>
            <option value="pechugas de pollo">pechugas de pollo
			</option>
			<option value="higado">higado
			</option>
			<option value="manzanas">manzanas
			</option>
		</select>


        <select multiple name="descripcion08[]">
      
			<option value="tio pepe">tio pepe
			</option>
			<option value="cerveza botellin">cerveza botellin
			</option>
			<option value="huevos">huevos
			</option>
			<option value="croquetas">croquetas
            </option>
            <option value="queso curado">queso curado
			</option>
			<option value="jamon cocido">jamon cocido
			</option>
			<option value="papel de cocina">papel de cocina
			</option>
			<option value="zumo natural">zumo natural
            </option>
            <option value="pechugas de pollo">pechugas de pollo
			</option>
			<option value="higado">higado
			</option>
			<option value="manzanas">manzanas
			</option>
		</select>

        <select multiple name="descripcion09[]">
       
			<option value="tio pepe">tio pepe
			</option>
			<option value="cerveza botellin">cerveza botellin
			</option>
			<option value="huevos">huevos
			</option>
			<option value="croquetas">croquetas
            </option>
            <option value="queso curado">queso curado
			</option>
			<option value="jamon cocido">jamon cocido
			</option>
			<option value="papel de cocina">papel de cocina
			</option>
			<option value="zumo natural">zumo natural
            </option>
            <option value="pechugas de pollo">pechugas de pollo
			</option>
			<option value="higado">higado
			</option>
			<option value="manzanas">manzanas
			</option>
		</select>

        <select  multiple name="descripcion010[]">
       
			<option value="tio pepe">tio pepe
			</option>
			<option value="cerveza botellin">cerveza botellin
			</option>
			<option value="huevos">huevos
			</option>
			<option value="croquetas">croquetas
            </option>
            <option value="queso curado">queso curado
			</option>
			<option value="jamon cocido">jamon cocido
			</option>
			<option value="papel de cocina">papel de cocina
			</option>
			<option value="zumo natural">zumo natural
            </option>
            <option value="pechugas de pollo">pechugas de pollo
			</option>
			<option value="higado">higado
			</option>
			<option value="manzanas">manzanas
			</option>
		</select>

 
        <select name="descripcion011[]">
        
			<option value="tio pepe">tio pepe
			</option>
			<option value="cerveza botellin">cerveza botellin
			</option>
			<option value="huevos">huevos
			</option>
			<option value="croquetas">croquetas
            </option>
            <option value="queso curado">queso curado
			</option>
			<option value="jamon cocido">jamon cocido
			</option>
			<option value="papel de cocina">papel de cocina
			</option>
			<option value="zumo natural">zumo natural
            </option>
            <option value="pechugas de pollo">pechugas de pollo
			</option>
			<option value="higado">higado
			</option>
			<option value="manzanas">manzanas
			</option>
		</select>

        <input type="submit" value="Enviar">
        <input type="reset" value="Borrar">



    </div>
    
    
    </section>

    </form>
</body>
</html>