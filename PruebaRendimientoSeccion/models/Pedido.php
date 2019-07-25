<?php
namespace models;
class pedido extends Conexion{

    // PROPIEDADES

    private $dni;
    private $nombre;
    private $apellidos;
    private $localidad;
    private $email;
    private $telefono;


     // CONSTRUCTOR

     public function __construct($servidor, $usuario, $password, $basededatos){

        $this->conexion = new \mysqli($servidor, $usuario, $password, $basededatos);
        
            }

    // METODOS

    


}

?>