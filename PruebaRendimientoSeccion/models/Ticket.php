<?php
namespace models;

class Ticket extends Conexion{

    // PROPIEDADES

     // CONSTRUCTOR

     public function __construct($servidor, $usuario, $password, $basededatos){

        $this->conexion = new \mysqli($servidor, $usuario, $password, $basededatos);
        
            }

    // METODOS


}

?>