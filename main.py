from flask import Flask, url_for, session, request, redirect, render_template
from dados.Dados import Dados
import random
import csv
#*Importar MONGO DB
from pymongo import MongoClient


#* Inicializar nuestra clase de conexion a la BD


#* Intanciar Flask
app = Flask(__name__)

#* Crear un llave/clave secreta para SESSION
app.config['SECRET_KEY'] = 'SUPER SECRETO'

#**************************************
#* ULR Conexion
MONGO_URL_ATLAS = 'mongodb+srv://mongodb:mongodb@cluster0-l6v7e.mongodb.net/test?retryWrites=true&w=majority'

#* Establecer conexion
client = MongoClient(MONGO_URL_ATLAS, ssl_cert_reqs=False)

#* Creacion base de datos
db = client['ahorcadito']

#* Creacion coleccion
collectionUsuarios = db['usuarios']


#******************************************
@app.route('/')
def redireccionar():

    return redirect(url_for('home'))

#******************************************
@app.route('/home', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':

        session.clear()
    

    if 'usuario' in session:

        return redirect(url_for('juegoDados'))

    return render_template('home.html')

@app.route('/usuario')
def usuario():

    return render_template('usuario.html')

#******************************************
@app.route('/usuario', methods=['POST'])
def usuariodatos():

    #* Lista que almacena al usuario
    listaUsuarioCorrecto = []

    usuario = request.form['usuario']

    leer_usuario = collectionUsuarios.find( {'usuario':f'{usuario}'} )

    # print(list(leer_usuario))

    for i in leer_usuario:

        print(i['usuario'])
        listaUsuarioCorrecto.append(i['usuario'])

    # print(listaUsuarioCorrecto[0])

    if listaUsuarioCorrecto != []:


        if listaUsuarioCorrecto[0] == usuario:
            #* iniciar sesion 
            #* Limpiamos la session cada vez que haga una nueva session.
            session.clear()
            session['usuario'] = usuario
            print('session creada')

            # return redirect(url_for('intentos'))

        else:

            return render_template('usuario.html', no_usuario=True)
    else:

        return render_template('usuario.html', no_usuario=True)

    return render_template('usuario.html')



#******************************************
@app.route('/registro')
def registro():

    return render_template('registro.html')


#******************************************
@app.route('/registro', methods=['GET', 'POST'])
def registroDatos():

    if request.method == 'POST':

        usuario = request.form['usuario']

        leer_usuario = collectionUsuarios.find( {'usuario':f'{usuario}'} )

        # print(list(leer_usuario))

        #* Si en la BD no esta vacio, entonces el email que se ingreso en el input existe en la BD
        if list(leer_usuario) != []:

            return render_template('registro.html', usuario_existe=True)

        collectionUsuarios.insert_one({"usuario": usuario})


        return redirect(url_for('usuario'))

        

    return render_template('registro.html')

# #******************************************

#******************************************
@app.errorhandler(404)
def page_no_found(error):
    return '<h1> Pagina no encontrada, siga buscando</h1>'

#******************************************
if __name__ == "__main__":

    app.run('0.0.0.0', '5000', debug=True)
