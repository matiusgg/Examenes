from flask import Flask, url_for, session, request, redirect, render_template
from dados.Dados import Dados
import random
import csv
# *Importar MONGO DB
from pymongo import MongoClient

# *DATOS BASE DE DATOS EN LA NUBE
'''
usuario: mongodb
contraseña:mongodb
'''

# * Inicializar nuestra clase de conexion a la BD


# * Intanciar Flask
app = Flask(__name__)

# * Crear un llave/clave secreta para SESSION
app.config['SECRET_KEY'] = 'SUPER SECRETO'

# **************************************
# * ULR Conexion
MONGO_URL_ATLAS = 'mongodb+srv://mongodb:mongodb@cluster0-l6v7e.mongodb.net/test?retryWrites=true&w=majority'

# * Establecer conexion
client = MongoClient(MONGO_URL_ATLAS, ssl_cert_reqs=False)

# * Creacion base de datos
db = client['examen_m4_c1']

# * Creacion coleccion
collectionUsuarios = db['usuarios']

# * Creacion coleccion
collectionPuntuacion = db['puntuacion']

#* coleccion de cantidad de dados y con su tipo de dados
collectionTipos = db['cantidad']


# ******************************************
@app.route('/')
def redireccionar():

    return redirect(url_for('home'))

# ******************************************
@app.route('/home', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':

        session.clear()

    if 'usuario' in session:

        return redirect(url_for('tipoDados'))

    return render_template('home.html')


@app.route('/usuario')
def usuario():

    return render_template('usuario.html')

# ******************************************
@app.route('/usuario', methods=['POST'])
def usuariodatos():

    # * Lista que almacena al usuario
    listaUsuarioCorrecto = []

    usuario = request.form['usuario']

    leer_usuario = collectionUsuarios.find({'usuario': f'{usuario}'})

    # print(list(leer_usuario))

    for i in leer_usuario:

        print(i['usuario'])
        listaUsuarioCorrecto.append(i['usuario'])

    # print(listaUsuarioCorrecto[0])

    if listaUsuarioCorrecto != []:

        if listaUsuarioCorrecto[0] == usuario:
            # * iniciar sesion
            # * Limpiamos la session cada vez que haga una nueva session.
            session.clear()
            session['usuario'] = usuario
            print('session creada')

            return redirect(url_for('tipoDados'))

        else:

            return render_template('usuario.html', no_usuario=True)
    else:

        return render_template('usuario.html', no_usuario=True)

    return render_template('usuario.html')


# ******************************************
@app.route('/registro')
def registro():

    return render_template('registro.html')


# ******************************************
@app.route('/registro', methods=['GET', 'POST'])
def registroDatos():

    if request.method == 'POST':

        usuario = request.form['usuario']

        leer_usuario = collectionUsuarios.find({'usuario': f'{usuario}'})

        # print(list(leer_usuario))

        # * Si en la BD no esta vacio, entonces el email que se ingreso en el input existe en la BD
        if list(leer_usuario) != []:

            return render_template('registro.html', usuario_existe=True)

        collectionUsuarios.insert_one({"usuario": usuario})

        return redirect(url_for('usuario'))

    return render_template('registro.html')


# ******************************************
listaTipos = ['cuatro', 'seis', 'ocho', 'diez']
# ******************************************
@app.route('/tipoDados')
def tipoDados():

    return render_template('tipoDados.html', listaTipos=listaTipos)


# ******************************************
@app.route('/juegoDados')
def juegoDados():

    return render_template('juegoDados.html')


# ******************************************


@app.route('/juegoDados', methods=['POST'])
def juegoDadosDatos():

    activar = request.form['activar']

    tiposConCantidad = collectionTipos.find({'usuario': session['usuario']})

    # * Objeto juego Dados
    objDados = Dados(activar, list(tiposConCantidad), collectionTipos, session['usuario'])

    #* metodo con los resultados
    (tipoDado, numCara, intentos) = objDados.activarJuego()

    return render_template('juegoDados.html', tipoDado=tipoDado, numCara=str(numCara), intentos=intentos)


# ******************************************

@app.route('/agregar')
def agregar():

    return render_template('agregar.html')
# ******************************************

@app.route('/agregar', methods=['POST'])
def agregarDatos():

    # listaCantidad = []

    cantidad = request.form['cantidad']
    tipoDado = request.form['tipoDado']

    datosCantidad = {
    "tipoDado": tipoDado,
     "cantidad": cantidad,
     "usuario": session['usuario']
    }

    buscadorCantidad = {
        "tipoDado": tipoDado
        # f"{tipoDado}.cantidad": cantidad 
        }

    # agregarDatos = collectionTipos.insert_one(datosCantidad)

    # #*lista con ID
    listaID = []

    verCantidad = collectionTipos.find(buscadorCantidad)

    if list(verCantidad) == []:

        agregarDatos = collectionTipos.insert_one(datosCantidad)
        print('Se ha añadido un nuevo tipo')

        buscarUnTipo = collectionTipos.find(buscadorCantidad)

        for i in list(buscarUnTipo):

            listaID.append(str(i['_id']))

        actualizarCantidad = collectionTipos.update_one(buscadorCantidad, {"$set": {'id_cantidad': listaID[0]}})

    else:

        print('''Hay más de un documento''')

        listaID.clear()

        buscar = collectionTipos.find(buscadorCantidad)

        for i in list(buscar):

            print(f'diccionario: {i}')

            print('\n')

            listaID.append(int(i['cantidad']))

        print(f'cantidad{listaID}')

        agregarSuma = collectionTipos.update_one(buscadorCantidad, {"$set": {'cantidad': listaID[0]+int(cantidad)}})

    # buscarDeNuevo = collectionTipos.find({'id_cantidad': })



    return redirect(url_for('tipoDados'))

# ******************************************

@app.errorhandler(404)
def page_no_found(error):
    return '<h1> Pagina no encontrada, siga buscando</h1>'


# ******************************************
if __name__ == "__main__":

    app.run('0.0.0.0', '5000', debug=True)
