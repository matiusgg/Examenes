<?php
namespace models;
class Producto extends Conexion{

    // PROPIEDADES

    private $nombreProducto;
    private $ingredientes;
    private $precio;
    private $estado;
    private $categoria;
    private $imagen;
    private $cantidad;


     // CONSTRUCTOR

     public function __construct($servidor, $usuario, $password, $basededatos){

        $this->conexion = new \mysqli($servidor, $usuario, $password, $basededatos);
        
            }

    // METODOS

    public function MostrarProductosComida($nombretabla) {

        $producto = $this->conexion->query("select * from $nombretabla");

        // CREAMO SUN FOREACH PARA QUE $resultados, para uqe nos muestre los datos de la base de datos, en este caso dentro de [nosmbre de atributo].
        
        echo('<pre>');
        print_r($producto);
        echo('</pre>');

        foreach($producto AS $valor) {

            $this->categoria = $valor['categoria'];

            if($nombretabla == 'productos') {

            if($this->categoria == 'Comida Rapida') {

            

            $this->imagen = $valor['imagen'];
            $this->nombreProducto = $valor['nombreProducto'];
            $this->ingredientes = $valor['ingredientes'];
            $this->precio = $valor['precio'];

        

                echo('<div class="productos">');
       

                echo('<ul>');



                echo('<div class="imagenProducto">');
    
        
                echo ('<img src="../_assets/img/productos/' . $this->imagen . '"');
                
                
                echo('</div>');



                echo('<li>');
        
                
                
                
                echo('Producto: ' . '<span>' . $this->nombreProducto . '</span>');
        
                
                
                echo('</li>');
        
                
                echo('<li>');
        
                
                
                echo('Ingredientes: ' . '<span>' . $this->ingredientes . '</span>');
        
                
                
                echo('</li>');
        
        echo('<li>');
        
        
                
                echo('Precio: ' . '<span>' . $this->precio . '</span>');
        
                
                
                echo('</li>');


                echo('<li class ="boton" style="background-color: green"> 
                
                <input type="checkbox" name="' . $this->nombreProducto . '" value="' . $this->nombreProducto . '"> Almacenar en la compra
                
                </li>');

                  echo('<li>');

  
echo('Cantidad: ');
               
                    echo('<input type="number" name="unidad_' . $this->nombreProducto . '" >');

         

                echo('</li>');



                
                
                echo('</ul>');


                
                echo('<div>');
               
            
        
        }
    }
}



    }

        public function MostrarProductosLiquidos($nombretabla) {

            $producto = $this->conexion->query("select * from $nombretabla");
    
            // CREAMO SUN FOREACH PARA QUE $resultados, para uqe nos muestre los datos de la base de datos, en este caso dentro de [nosmbre de atributo].
            
            echo('<pre>');
            print_r($producto);
            echo('</pre>');
    
            foreach($producto AS $valor) {
    
                $this->categoria = $valor['categoria'];
    
                if($nombretabla == 'productos') {


        // condicional si la categoria es Liquidos

        if($this->categoria == 'Liquidos') {

            

            $this->imagen = $valor['imagen'];
            $this->nombreProducto = $valor['nombreProducto'];
            $this->ingredientes = $valor['ingredientes'];
            $this->precio = $valor['precio'];

        

                echo('<div class="productos_liquidos">');
       

                echo('<ul>');



                echo('<div class="imagenProducto">');
    
        
                echo ('<img src="../_assets/img/productos/' . $this->imagen . '"');
                
                
                echo('</div>');



                echo('<li>');
        
                
                
                
                echo('Producto: ' . '<span>' . $this->nombreProducto . '</span>');
        
                
                
                echo('</li>');
        
                
                echo('<li>');
        
                
                
                echo('Ingredientes: ' . '<span>' . $this->ingredientes . '</span>');
        
                
                
                echo('</li>');
        
        echo('<li>');
        
        
                
                echo('Precio: ' . '<span>' . $this->precio . '</span>');
        
                
                
                echo('</li>');


                echo('<li class ="boton" style="background-color: green"> 
                
                <input type="checkbox" name="' . $this->nombreProducto . '" value="' . $this->nombreProducto . '"> Almacenar en la compra
                
                </li>');

                echo('<li>');

  
                echo('Cantidad: ');
                               
                                    echo('<input type="number" name="unidad_' . $this->nombreProducto . '" >');
                
                         
                
                                echo('</li>');
                
                echo('</ul>');


                
                echo('<div>');
                

        }

    }

}

        }


        public function MostrarProductosPostres($nombretabla) {

            $producto = $this->conexion->query("select * from $nombretabla");
    
            // CREAMO SUN FOREACH PARA QUE $resultados, para uqe nos muestre los datos de la base de datos, en este caso dentro de [nosmbre de atributo].
            
            echo('<pre>');
            print_r($producto);
            echo('</pre>');
    
            foreach($producto AS $valor) {
    
                $this->categoria = $valor['categoria'];
    
                if($nombretabla == 'productos') {

        // condicional si la categoria es Liquidos

         if($this->categoria == 'Postres') {

            

            $this->imagen = $valor['imagen'];
            $this->nombreProducto = $valor['nombreProducto'];
            $this->ingredientes = $valor['ingredientes'];
            $this->precio = $valor['precio'];

        

                echo('<div class="productos_postres">');
       

                echo('<ul>');



                echo('<div class="imagenProducto">');
    
        
                echo ('<img src="../_assets/img/productos/' . $this->imagen . '"');
                
                
                echo('</div>');



                echo('<li>');
        
                
                
                
                echo('Producto: ' . '<span>' . $this->nombreProducto . '</span>');
        
                
                
                echo('</li>');
        
                
                echo('<li>');
        
                
                
                echo('Ingredientes: ' . '<span>' . $this->ingredientes . '</span>');
        
                
                
                echo('</li>');
        
        echo('<li>');
        
        
                
                echo('Precio: ' . '<span>' . $this->precio . '</span>');
        
                
                
                echo('</li>');


                echo('<li class ="boton" style="background-color: green"> 
                
                <input type="checkbox" name="' . $this->nombreProducto . '" value="' . $this->nombreProducto . '"> Almacenar en la compra
                
                </li>');


                echo('<li>');

  
echo('Cantidad: ');
               
                    echo('<input type="number" name="unidad_' . $this->nombreProducto . '" >');

         

                echo('</li>');
                
                echo('</ul>');


                
                echo('<div>');
                

        }


    }

    for($i = 0; $i < count($_REQUEST), $i++) {

        if($_REQUEST['unidad_' . $this->nombreProducto]) {

        echo('<li>');



                session_start();
                
                $_SESSION['requestCantidad' . $i] = $_REQUEST['unidad_' . $this->nombreProducto];
                
                


            echo('</li>');

        }
    }

}

        }


public function mostrarEnvio($nombretabla, $request) {

    
    $producto = $this->conexion->query("select * from $nombretabla");
    
    // CREAMO SUN FOREACH PARA QUE $resultados, para uqe nos muestre los datos de la base de datos, en este caso dentro de [nosmbre de atributo].
    
    echo('<pre>');
    print_r($producto);
    echo('</pre>');

    foreach($producto AS $valor) {

        $this->categoria = $valor['categoria'];

      

        if($nombretabla == 'productos') {



    $this->nombreProducto = $valor['nombreProducto'];
    $this->imagen = $valor['imagen'];
    $this->ingredientes = $valor['ingredientes'];
    $this->precio = $valor['precio'];


$i= 0;

    foreach($request AS $key => $valorinput) {

        if(!empty($valorinput)) {

        if($this->nombreProducto == $valorinput) {



            echo('<div class="productos_enviados">');


            echo('<ul>');
    
            echo('<div class="imagenProducto">');
    
    
            echo ('<img src="../_assets/img/productos/' . $this->imagen . '"');
            
            
            echo('</div>');
    
    
    
            echo('<li>');
    
            
            
            
            echo('Producto: ' . '<span>' . $this->nombreProducto . '</span>');
    
            
            
            echo('</li>');
    
            
            echo('<li>');
    
            
            
            echo('Ingredientes: ' . '<span>' . $this->ingredientes . '</span>');
    
            
            
            echo('</li>');
    
    echo('<li>');
    
    
            
            echo('Precio: ' . '<span>' . $this->precio . '</span>');

            echo('</li>');
            
    
            
            
            echo('</ul>');
    
    
            
            echo('<div>');


            
        }


    }

        
$i++;

        

        
    }

    


        

}



}


    }

    public function calcularPrecio($nombretabla, $request) {

    
        $producto = $this->conexion->query("select * from $nombretabla");
    
        // CREAMO SUN FOREACH PARA QUE $resultados, para uqe nos muestre los datos de la base de datos, en este caso dentro de [nosmbre de atributo].
        
        echo('<pre>');
        print_r($producto);
        echo('</pre>');
    
        foreach($producto AS $valor) {
    
            $this->categoria = $valor['categoria'];
    
          
    
            if($nombretabla == 'productos') {
    
    
    
        $this->nombreProducto = $valor['nombreProducto'];
        $this->imagen = $valor['imagen'];
        $this->ingredientes = $valor['ingredientes'];
        $this->precio = $valor['precio'];
    
    
    $i= 0;
    
        foreach($request AS $key => $valorinput) {
    
            if(!empty($valorinput)) {
    
            if($this->nombreProducto == $valorinput) {

                echo('<ul>');

                echo('<li>');
    
    
            
                echo('Precio: ' . '<span>' . $valor['unidad_'.$this->nombreProducto] . '</span>');
        
                
                
                echo('</li>');
        
                echo('</ul>');
                
                
            }

        }

    }

}

        }

    }

// public function precio($nombretabla, $request,  $descuento = 0 ){

//     $producto = $this->conexion->query("select * from $nombretabla");
    
//     // CREAMO SUN FOREACH PARA QUE $resultados, para uqe nos muestre los datos de la base de datos, en este caso dentro de [nosmbre de atributo].
    
//     echo('<pre>');
//     print_r($producto);
//     echo('</pre>');

//     foreach($producto AS $valor) {

//         $this->categoria = $valor['categoria'];

      

//         if($nombretabla == 'productos') {



//     $this->nombreProducto = $valor['nombreProducto'];

//     $this->precio = $valor['precio'];




//     foreach($request AS $key => $valorinput) {

//         if($this->nombreProducto == $valorinput) {


// if($valorinput['unidad_'.$this->nombreProducto]){

// echo($valorinput);

//     $cantidad = $valorinput['unidad_' . $this->nombreProducto];


//     $multiplicar = $this->precio * $cantidad;
    

    
//     $porcentaje = $multiplicar * $descuento;
    
//     $solucion = $multiplicar - $porcentaje;
//     return $solucion;

// }
    
//     }

// }

//         }

// }



// }


// public function pedido($request, $nombretabla) {

//     $resultados = $this -> conexion -> query('SELECT e.id_pedidos, e.cantidad, d.active, d.id_denuncia, d.id_multa, m.id_multa, d.created_at, d.matricula
//     FROM ' . $tabla1 . ' as e
//     JOIN ' . $tabla2 . ' as p
//     ON d.id_productos = m.id_productos');
    
//     // CREAMO SUN FOREACH PARA QUE $resultados, para uqe nos muestre los datos de la base de datos, en este caso dentro de [nosmbre de atributo].
    
//     echo('<pre>');
//     print_r($producto);
//     echo('</pre>');

//     foreach($producto AS $valor) {

//         $this->categoria = $valor['categoria'];

      

//         if($nombretabla == 'productos') {



//     $this->nombreProducto = $valor['nombreProducto'];
//     $this->imagen = $valor['imagen'];
//     $this->ingredientes = $valor['ingredientes'];
//     $this->precio = $valor['precio'];




//     foreach($request AS $key => $valorinput) {

//         if($this->nombreProducto == $valorinput) {

// }

// } 


//         }

}
?>