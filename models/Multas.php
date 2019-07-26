<?php
namespace models;

class Multas{

    // PROPIEDADES
    
    
    private $conexion;
    private $Atributos;
    private $dni;
    private $placaAuto;
    private $tipoMulta;
    private $idAgente;
    private $precio;
    private $comentario;
    private $nombre;
    private $direccionInfraccion;
    private $fechaMulta;


    // CONSTRUCTOR

    public function __construct($servidor, $usuario, $password, $basededatos){

       

$this->conexion = new \mysqli($servidor, $usuario, $password, $basededatos);



    }

    // METODOS



        public function InsertarMulta($tabla1, $request){

        $multar = $this->conexion -> query('select * from ' . $tabla1);

    
    // CREAMO SUN FOREACH PARA QUE $resultados, para uqe nos muestre los datos de la base de datos, en este caso dentro de [nosmbre de atributo].
    
    echo('<pre>');
    print_r($multar);
    echo('</pre>');
    
    foreach($multar AS $valor) {

  $this->dni = $valor['dni'];
  $this->nombre = $valor['nombre'];
  $this->placaAuto = $valor['placaAuto'];

  $tipomultas = $this->conexion -> query('select * from tipomultas');

  foreach($tipomultas AS $valortipo) {

    $this->tipoMulta = $valortipo['tipoMulta'];

  foreach($request AS $valorinput) {

      
    // $inputPlaca = $valorinput['placacoche'];

    // $inputDNI = $valorinput['dniformulario'];
  
    // $inputAgente = $valorinput['agenteID'];

    // $inputTipo = $valorinput['tipoMultas'];


    //   if(!empty($request)) {

    //       echo('<pre>');
    //   print_r($request);
    //   echo('</pre>');



    //   echo('<pre>');
    //   print_r($valorinput);
    //   echo('</pre>');

          if($this->dni == $valorinput && $this->nombre == $_POST['nombrecompleto'] && $this->placaAuto == $_POST['placacoche']){

            if($this->tipoMulta == $_POST['tipoMultas']) {

echo($this->tipoMulta);
echo($valortipo['id_Multa']);
            
            $AtributosyDatos = [

          'dni' => $request['dniformulario'],
        //   'nombre' => $request['nombreCompleto'],
          'placaAuto' => $request['placacoche'],
          'id_Agente' => $request['agenteID'],
          'id_Multas' => $valortipo['id_Multa'],
          'tipoMultas' => $request['tipoMultas'],
          'direccionInfraccion' => $request['direccionInfraccion'],
          'comentario' => $request['comentario'],
          'fechaMulta' => $request['fechaMulta'],
          'nombre' => $request['nombrecompleto']
      
      
      ];


      echo('<pre>');
      print_r($AtributosyDatos);
      echo('</pre>');

      


      $atributos = implode(", " , array_keys($AtributosyDatos));

      echo($atributos);
       
       
      // creamos un nuevo array, para despues convertirlo en string con implode 
        $i = 0;
        foreach($AtributosyDatos as $key=>$valor) {

         $dato[$i] = "'" . $valor . "'";
            $i++;
            
        }
        
       // convertir el array anterio en un string
        $datos = implode(", ", $dato);

        echo($datos);

      //Insertamos los valores en cada campo
      $this->conexion->query(" insert into puentemultas_infractor ($atributos) VALUES ($datos);");



      
      }

            }

//   }

  }

}



}

}


public function MostrarAgenteID($nombretabla, $inputAgente) {

    $Agente = $this->conexion->query("select * from $nombretabla");
    
    foreach($Agente AS $valor) {
    
        $this->idAgente = $valor['id_Agente'];
    
        if($this->idAgente == $inputAgente){
    
            // insertar el id_Agente que hizo la multa
    
            echo('<li>');


        
            echo('id Agente: ' . '<span>' . $this->idAgente . '</span>');
    
    
    
    
            echo('</li>');

            break;
        }
        else{

            echo('No hay ningun agente con ese ID');
        }
    }

}



public function mostrarMulta($tabla1, $tabla2, $tabla3, $tabla4) {

    
$resultados = $this->conexion -> query('select p.dni, i.placaAuto, m.tipoMulta, a.id_Agente, m.precio, m.comentario, i.nombre, p.direccionInfraccion, p.fechaMulta
    FROM ' . $tabla1 . ' as p
    JOIN ' . $tabla2 . ' as i
    ON p.dni = i.dni
    JOIN ' . $tabla3 . ' as a
    ON p.id_Agente = a.id_Agente
    JOIN ' . $tabla4 . ' as m
    ON p.id_Multas = m.id_Multa');


    // 'select p.dni, i.placaAuto, m.tipoMulta, a.id_Agente, m.precio, m.comentario, i.nombre, p.direccionInfraccion, p.fechaMulta
    // FROM puentemultas_infractor as p
    // JOIN infractor as i
    // ON p.dni = i.dni
    // JOIN agente as a
    // ON p.id_Agente = a.id_Agente
    // JOIN as m
    // ON p.id_Multas = m.id_Multa'

// CREAMO SUN FOREACH PARA QUE $resultados, para uqe nos muestre los datos de la base de datos, en este caso dentro de [nosmbre de atributo].

echo('<pre>');
print_r($resultados);
echo('</pre>');

foreach($resultados AS $valor) {



  

    if($tabla1 == 'puentemultas_infractor' and $tabla2 == 'infractor' and $tabla3 == 'agente' and $tabla4 == 'tipomultas') {



$this->dni = $valor['dni'];
$this->nombre = $valor['nombre'];
$this->placaAuto = $valor['placaAuto'];
$this->precio = $valor['precio'];
$this->tipoMulta = $valor['tipoMulta'];
$this->idAgente = $valor['id_Agente'];
$this->direccionInfraccion = $valor['direccionInfraccion'];
$this->fechaMulta = $valor['fechaMulta'];
$this->comentario = $valor['comentario'];




        echo('<div class="mostrar_Multas">');


        echo('<ul>');




        echo('<li>');

        
        
        
        echo('DNI: ' . '<span>' . $this->dni . '</span>');

        
        
        echo('</li>');

        
        echo('<li>');

        
        
        echo('nombre: ' . '<span>' . $this->nombre . '</span>');

        
        
        echo('</li>');

echo('<li>');


        
        echo('placaAuto: ' . '<span>' . $this->placaAuto . '</span>');

        echo('</li>');
        


        echo('<li>');


        
        echo('tipoMulta: ' . '<span>' . $this->tipoMulta . '</span>');




        echo('</li>');
        

        // if($this->idAgente)


        // echo('<li>');


        
        // echo('id Agente: ' . '<span>' . $this->idAgente . '</span>');




        // echo('</li>');

        // $this->MostrarAgenteID($tabla3, $inputAgente)

        echo('<li>');


        
        echo('precio: ' . '<span>' . $this->precio . '</span>');




        echo('</li>');

        echo('<li>');


        
        echo('direccionInfraccion: ' . '<span>' . $this->direccionInfraccion . '</span>');




        echo('</li>');

        echo('<li>');


        
        echo('fechaMulta: ' . '<span>' . $this->fechaMulta . '</span>');




        echo('</li>');

        echo('<li>');


        
        echo('comentario: ' . '<span>' . $this->comentario . '</span>');




        echo('</li>');



        
        echo('</ul>');


        
        echo('<div>');


echo('<br>');


// $total += $precioCantidad;

// echo('TOTAL: ' . $total);

    

}



}


}

}

?>