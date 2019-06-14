

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



<form action="resumenMulta.php" method="post">

<!-- HEADER -->
    <header>
        <h1>
        AGREGAR MULTA
        </h1>
    </header>

<!-- SECTION -->
<section>
    <article>

    <!-- Nombre Completo Infractor -->
    
    <label for="nombreCompleto">
    Nombre Completo
    </label>

    <input type="text" name="nombrecompleto" placeholder="Nombre Completo">

    <br>

      <!-- DNI -->
    
      <label for="dniformulario">
    DNI infractor
    </label>

    <input type="text" name="dniformulario" placeholder="Introduzca el dni">

    <br>

      <!-- Tipo de Multa -->

      <label for="tipomultas">
      Tipo de Multas
      </label>
    
       <select name="tipoMultas" > 

 <option value=""> 

 </option> 
 <option value="mal_estacionado"> 
 mal estacionado
             </option> 
             <option value="choque_leve_a_otro_individuo"> 
             choque leve a otro individuo
             </option> 

             <option value="maxima_velocidad_superada"> 
             maxima velocidad superada
             </option> 

             <option value="agresion_a_personal_del_transito"> 
             agresion a personal del transito
             </option> 

             <option value="Incumplimiento_señales_transito"> 
             Incumplimiento señales transito
             </option> 
            
            
             </select> 

             <br>

      <!-- PLACA COCHE -->
    
      <label for="placacoche">
    Placa del Coche
    </label>

    <input type="text" name="placacoche" placeholder="Introduzca la placa del coche ">

    <br>

     <!-- Id Agente quien hizo la multa -->
    
     <label for="agenteID">
    Id del AGENTE
    </label>

    <input type="text" name="agenteID" placeholder="Introduzca ID">

    <button type="submit">
    MULTAR
    </button>


    
    </article>
</section>

<!-- FOOTER -->
<footer>
</footer>


</form>
</body>
</html>