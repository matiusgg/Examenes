
<?php
namespace models;

class Agente{

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
    private $placaAuto;
    private $nacionalidad;


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


    public function verInfractor($nombretabla) {



$leer = $this->conexion->query("select * from $nombretabla;");



echo('<pre>');
print_r($leer);
echo('</pre>');


foreach($leer AS $valor) {



if($nombretabla == 'infractor') {

echo 'DNI: ' . $valor['dni'] . '<br>';
echo 'NOMBRE COMPLETO: ' . $valor['nombre'] . '<br>';
echo 'CORREO: ' . $valor['correo'] . '<br>';
echo 'TELEFONO: ' . $valor['telefono'] . '<br>';
echo 'POBLACION: ' . $valor['poblacion'] . '<br>';
echo 'CODIGOPOSTAL: ' . $valor['codigoPostal'] . '<br>';
echo 'FECHA DE NACIMIENTO: ' . $valor['fNacimiento'] . '<br>';
echo 'FECHA DE ACTIVACION: ' . $valor['fechaActivo'] . '<br>';
echo 'DIRECCION: ' . $valor['direccion'] . '<br>';
echo 'NACIONALIDAD: ' . $valor['nacionalidad'] . '<br>';
echo 'ACTIVO ACTUALMENTE?: ' . $valor['activo'] . '<br>';

$inputPlaca = $_POST['placacoche'];
if($inputPlaca == $valor['placaAuto']) {
echo 'PLACA AUTO: ' . $valor['placaAuto'] . '<br>';

} else {

echo('Placa de Auto Incorrecta' . '<br>');
}


echo 'CANTIDAD MULTAS: ' . $valor['cantidadMultas'] . '<br>';
echo 'ID DEL AGENTE QUE PUSO LA MULTA: ' . $valor['id_Agente'] . '<br>';
echo 'TIPO DE MULTA: ' . $valor['tipoMultas'] . '<br>';


}


}


}


}