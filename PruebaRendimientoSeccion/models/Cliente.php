<?php
namespace models;
class Cliente extends Conexion{

    // PROPIEDADES

    private $dni;
    private $nombre;
    private $apellidos;
    private $localidad;
    private $email;
    private $telefono;
    private $conexion;


    // CONSTRUCTOR

    public function __construct($servidor, $usuario, $password, $basededatos){

$this->conexion = new \mysqli($servidor, $usuario, $password, $basededatos);

    }

    // METODOS

    public function RegistrarInputsUsuario($nombretabla, $AtributosyDatos) {

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
        $this->conexion->query(" insert into $nombretabla ($atributos) VALUES ($datos);");
    }

    


}

?>