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
    private $nss;
    private $zonaAsignada;
    private $nacionalidad;
    private $tipoMultas;


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

    


}