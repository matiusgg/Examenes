<?php
namespace models;

class Infractor{

    // PROPIEDADES
    
    
    private $conexion;
    private $Atributos;
    private $nombre;
    private $telefono;
    private $correo;
    private $poblacion;
    private $codigoPostal;
    private $fNacimiento;
    private $fechaActivo;
    private $dni;
    private $direccion;
    private $cantidadMultas;
    private $tipoMultas;
    private $placaAuto;
    private $nacionalidad;
    private $activo;
    private $id_Agente;


    // CONSTRUCTOR

    public function __construct($servidor, $usuario, $password, $basededatos){

       

$this->conexion = new \mysqli($servidor, $usuario, $password, $basededatos);



    }

    // METODOS

// METODO PARA INSERTAR TUPLA

    public function InsertarTupla($nombretabla, $AtributosyDatos){

      
                $atributos = implode(", " , array_keys($AtributosyDatos));
				 
				 
		
				  $i = 0;
				  foreach($AtributosyDatos as $key=>$valor) {

				 
				   $dato[$i] = "'" . $valor . "'";
                      $i++;
                      
				  }
				  
		
				  $datos = implode(", ", $dato);


				 
				//Insertamos los valores en cada campo
				$this->conexion->query(" insert into $nombretabla ($atributos) VALUES ($datos);");
      


     

    }


    public function verInfractor($nombretabla, $inputDNI, $inputPlaca) {



$infractor = $this->conexion->query("select * from $nombretabla;");



echo('<pre>');
print_r($infractor);
echo('</pre>');


foreach($infractor AS $valor) {



if($nombretabla == 'infractor') {

 $this->nombre = $valor['nombre'];
 $this->telefono = $valor['telefono'];
 $this->correo = $valor['correo'];
 $this->poblacion = $valor['poblacion'];
 $this->codigoPostal = $valor['codigoPostal'];
 $this->fNacimiento = $valor['fNacimiento'];
 $this->fechaActivo = $valor['fechaActivo'];
 $this->dni = $valor['dni'];
 $this->direccion = $valor['direccion'];
 $this->cantidadMultas = $valor['cantidadMultas'];
 $this->tipoMultas = $valor['tipoMultas'];
 $this->placaAuto = $valor['placaAuto'];
 $this->nacionalidad = $valor['nacionalidad'];
 $this->activo = $valor['activo'];
 $this->id_Agente = $valor['id_Agente'];

 if($inputDNI == $this->dni) {

echo 'DNI: ' . $this->dni . '<br>';
echo 'NOMBRE COMPLETO: ' . $this->nombre . '<br>';
echo 'CORREO: ' . $this->correo . '<br>';
echo 'TELEFONO: ' . $this->telefono . '<br>';
echo 'POBLACION: ' . $this->poblacion . '<br>';
echo 'CODIGOPOSTAL: ' . $this->codigoPostal . '<br>';
echo 'FECHA DE NACIMIENTO: ' . $this->fNacimiento . '<br>';
echo 'FECHA DE ACTIVACION: ' . $this->fechaActivo . '<br>';
echo 'DIRECCION: ' . $this->direccion . '<br>';
echo 'NACIONALIDAD: ' . $this->nacionalidad . '<br>';
echo 'ACTIVO ACTUALMENTE?: ' . $this->activo . '<br>';


if($inputPlaca == $this->placaAuto) {
echo 'PLACA AUTO: ' . $this->placaAuto . '<br>';

} else {

echo('Placa de Auto Incorrecta' . '<br>');
}


echo 'CANTIDAD MULTAS: ' . $this->cantidadMultas . '<br>';
echo 'ID DEL AGENTE QUE PUSO LA MULTA: ' . $this->id_Agente . '<br>';
echo 'TIPO DE MULTA: ' . $this->tipoMultas . '<br>';


echo('<a href="formularioMultar.php?placacoche=' . $inputPlaca . '&dniformulario=' . $inputDNI . '"> MULTAR AL INFRACTOR</a>');


}



}


}


}


public function registrarInfractor($request){



foreach($request AS $valorinput) {

  



  if(!empty($request)) {

  //     echo('<pre>');
  // print_r($request);
  // echo('</pre>');



  // echo('<pre>');
  // print_r($valorinput);
  // echo('</pre>');

  $AtributosyDatos = [

      'dni' => $request['dniformulario'],
      'nombre' => $request['nombreCompleto'],
      'correo' => $request['correo'],
      'telefono' => $request['telefono'],
      'poblacion' => $request['poblacion'],
      'codigoPostal' => $request['codigoPostal'],
      'fNacimiento' => $request['fNacimiento'],
      'nacionalidad' => $request['nacionalidad'],
      'placaAuto' => $request['placacoche'],

  
  
  ];


  echo('<pre>');
  print_r($AtributosyDatos);
  echo('</pre>');

  


  $atributos = implode(", " , array_keys($AtributosyDatos));
   
   
  // creamos un nuevo array, para despues convertirlo en string con implode 
    $i = 0;
    foreach($AtributosyDatos as $key=>$valor) {

     $dato[$i] = "'" . $valor . "'";
        $i++;
        
    }
    
   // convertir el array anterio en un string
    $datos = implode(", ", $dato);

  //Insertamos los valores en cada campo
  $this->conexion->query(" insert into infractor ($atributos) VALUES ($datos);");



  
  

}

}


}


public function InsertarMulta($nombretabla, $inputmulta, $inputDNI) {

     
       
  //Insertamos el tipo de multa al infractor
  $this->conexion->query(" update $nombretabla set tipoMultas = '$inputmulta' where dni = $inputDNI;");

 

}

public function InsertarAgenteID($nombretabla, $inputmulta, $inputDNI) {

$Agente = $this->conexion->query("select * from agente");

foreach($Agente AS $valor) {

    $Agente_id = $valor['id_Agente'];
    $inputAgente = $_POST['agenteID'];

    if($Agente_id == $inputAgente){

        // insertar el id_Agente que hizo la multa

        $this->conexion->query(" update $nombretabla set id_Agente = $inputAgente where dni = $inputDNI;");
        $this->conexion->query(" update $nombretabla set cantidadMultas = 1 where dni = $inputDNI;");
    }
}




}


}