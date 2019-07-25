<?php
namespace models;

class Conexion{

    // PROPIEDADES
    
    
    private $conexion;
    private $Atributos;


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



    public function verTuplas($nombretabla) {



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

  

    public function CrearTabla($nombretabla, $Atributos) {

   

        $codigotabla = $this->conexion->query("create table if not exists $nombretabla (id_$nombretabla INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT, $Atributos");

    }

    public function BorrarTabla($nombretabla) {

        $codigotabla = $this->conexion->query("drop table $nombretabla;");
    }

    public function dniAcceso($nombretabla) {

        $dniTabla = $this->conexion->query("select dni from $nombretabla");

        foreach($dniTabla AS $valor) {

            $dni = $valor['dni'];

            if($dni == $_POST['dni']){

                header('Location: php/opciones.php');
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

public function MostrarPrecioMulta($nombretabla) {

    $leer = $this->conexion->query("select * from $nombretabla;");



echo('<pre>');
print_r($leer);
echo('</pre>');


foreach($leer AS $valor) {



if($nombretabla == 'infractor') {

    if($valor['tipoMultas'] == 'mal_estacionado') {

// if()
        echo 'PRECIO DE LA MULTA DE ESTE TIPO: 50 EUROS';
    }

    if($valor['tipoMultas'] == 'choque_leve_a_otro_individuo') {

        echo 'PRECIO DE LA MULTA DE ESTE TIPO: 150 EUROS';
    }

    if($valor['tipoMultas'] == 'maxima_velocidad_superada') {

        echo 'PRECIO DE LA MULTA DE ESTE TIPO: 80 EUROS';
    }

    if($valor['tipoMultas'] == 'agresion_a_personal_del_transito') {

        echo 'PRECIO DE LA MULTA DE ESTE TIPO: 350 EUROS';
    }

    if($valor['tipoMultas'] == 'Desorden_publico') {

        echo 'PRECIO DE LA MULTA DE ESTE TIPO: 60 EUROS';
    }

    if($valor['tipoMultas'] == 'Incumplimiento_señales_transito') {

        echo 'PRECIO DE LA MULTA DE ESTE TIPO: 100 EUROS';
    }



}
}

}




}


?>