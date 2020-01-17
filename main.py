# * IMPORTACIONES del FLASK y del PAQUETE donde se alberga la CLASE Horoscopo()
from flask import Flask, request, make_response, redirect, render_template, session, url_for

from ruleta.Ruleta import Ruleta

import random
import csv
# *Importar MONGO DB
from pymongo import MongoClient

# *****************************************
# * variable APP
app = Flask(__name__)

# *****************************************

app.config['SECRET_KEY'] = 'SUPER SECRETO'

# *****************************************

# **************************************
# * ULR Conexion
MONGO_URL_ATLAS = 'mongodb+srv://mongodb:mongodb@cluster0-l6v7e.mongodb.net/test?retryWrites=true&w=majority'

# * Establecer conexion
client = MongoClient(MONGO_URL_ATLAS, ssl_cert_reqs=False)

# * Creacion base de datos
db = client['examen_m3_final']

# * Creacion coleccion
collectionUsuarios = db['usuarios']

#*****************************************

# Objeto
# ruletaObj = Ruleta()

#*******************************************

# *Ruta que direcciona a '/home'
@app.route('/')
def redireccionar():

    return redirect('/home')
    

# *****************************************

# *Ruta HOME
@app.route('/home')
def home():

    return render_template('home.html')

# ******************************************
@app.route('/home', methods=['GET', 'POST'])
def homeDatos():

    if request.method == 'POST':

        session.clear()

    if 'usuario' in session:

        return redirect(url_for('tipoDados'))

    return render_template('home.html')


#********************************************


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

            return redirect(url_for('reglas'))

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

# *****************************************

# *Ruta REGLAS
@app.route('/reglas')
def reglas():

    opcionesFijas = ['dinero', 'pierdes', 'carcel']

    return render_template('reglas.html', opcionesFijas=opcionesFijas)

# *****************************************

# *Ruta OPCIONES
@app.route('/opciones')
def opciones():

    opcionesUsuario = ['dinero', 'saltar', 'coche', 'ordenador', 'nevera', 'moto', 'bote', 'bicicleta']

    return render_template('opciones.html', opcionesUsuario=opcionesUsuario)

# *****************************************

# *Ruta opciones
@app.route('/opciones', methods=['POST'])
def opcionesDatos():

    opcion = request.form['opcion']

    usuario = session['usuario']

    queryOpciones = collectionUsuarios.find({'usuario': usuario, f'opcionesUsuarios.{opcion}': opcion})
        

    if list(queryOpciones) == []:

       agregarOpcion = collectionUsuarios.update_one({'usuario': usuario}, {"$set": {f'opcionesUsuarios.{opcion}': opcion}})

       print('Se ha agregado la nueva opción')

    else:
        print('''Ya se encuentra esta opcion agregada''')

    return redirect(url_for('opciones'))

# *****************************************

# *Ruta INTENTOS
@app.route('/intentos')
def intentos():

    return render_template('intentos.html')
    

# *****************************************

# # *Ruta LLEGADA POST INTENTOS
@app.route('/intentos', methods=['POST'])
def llegadaIntentos():

    # * Variables globales
    global activar

    #* input hidden activar
    activar = request.form['activar']
    
    # * Modo intento escogido
    intento = request.form['intento']

    # Objeto
    ruletaObj = Ruleta(collectionUsuarios, session['usuario'], intento)

    #* metodo intentos
    registrarIntentos = ruletaObj.intentos(intento)

    # * Redireccion a la ruta 'RULETA'
    return redirect(url_for('ruleta'))

# *****************************************

# *Ruta RULETA
@app.route('/ruleta', methods=['GET'])
def ruleta():

    #* Nuevo objeto para activar el juego
    ruletaObj = Ruleta(collectionUsuarios, session['usuario'])

    #* metodo Juego
    activarJuego = ruletaObj.Juego(activar)
    
    return render_template('ruleta.html')

# *****************************************

# *Ruta LLEGADA POST RULETA
@app.route('/ruleta', methods=['POST'])
def ruletaDatos():



    return render_template('ruleta.html')

# *****************************************

# * RUTA PAGINA ERROR
@app.errorhandler(404)
def page_no_found(error):
    return '<h1> Pagina no encontrada, siga buscando</h1>'

# *****************************************


# * MAIN
if __name__ == "__main__":

    app.run('0.0.0.0', '5000', debug=True)