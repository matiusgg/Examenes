#*libreria Flask
from flask import Flask, request, make_response, redirect, render_template, session, url_for
#*JSON
import json
#* Importacion de la Clase
from cajero.Cajero import Cajero

# *****************************************

app = Flask(__name__)

# *****************************************

app.config['SECRET_KEY'] = 'SUPER SECRETO'

# *****************************************
#* Objeto
cajeroObj = Cajero()

#* Ruta REDIRECCIONAR
@app.route('/')
def redireccionar():

    return redirect('/home')

# *****************************************
#* #* Ruta HOME
@app.route('/home')
def home():

    return render_template('home.html')

# *****************************************
#* #* Ruta HOMEUSUARIO
@app.route('/home', methods=['POST'])
def homeUsuario():

    #* Variable codigo que alberga la informacion del input CODIGO
    codigo = request.form['codigo']

    #* en el archivo CUENTAS.json estan los datos de las cuentas de los usuarios: nombre, codigo y numero de targeta.
    #* El codigo sera con el cual podra acceder al cajero Automatico.
    with open('static/json/cuentas.json') as contenido:

            cuentas = json.load(contenido)

            for i in cuentas:

                #* si CODIGO es igual al codigo que hay en JSON del usuario.
                if codigo == i.get('codigo'):

                    #* Redireccioname a la ruta OPCIONES
                    return redirect(url_for('opciones'))

                else:

                    #* Si no, mandame un mensaje de que el codigo esta incorrecto.
                    mensajeError = 'El codigo es incorrecto'


    return render_template('home.html', mensaje=mensajeError)

# *****************************************
#* Ruta OPCIONES
@app.route('/opciones')
def opciones():

    global opciones

    #* Lista de opciones para hacer el bucle en jinja de los botones de las opciones del cajero automatico.
    opciones = ['ingresar', 'consultar', 'retirar', 'movimientos']

    return render_template('opciones.html', opciones=opciones)

# *****************************************
#* Ruta OPCIONESESCOGIDA
@app.route('/opciones', methods=['POST'])
def opcionesEscogida():

    #* OPCION en global para poder usarlo en las demas rutas con el fin de ponerlo en el metodo de la clase Cajero.
    global opcion

    #* variable OPCION del input hidden.
    opcion = request.form['opcion']

    for i in opciones:

        #* Si OPCION es igual ha algun elemento de la lista, redireccioname a la ruta de la opcion escogida en el input hidden OPCION
        if i == opcion:

            return redirect(url_for(f'{opcion}'))

            

    return render_template('opciones.html')


# *****************************************
#* Ruta INGRESAR
@app.route('/ingresar')
def ingresar():

    return render_template('ingresar.html')

# *****************************************
#* Ruta INGRESARPOST
@app.route('/ingresar', methods=['POST'])
def ingresarPost():

    #* INGRESARINPUT es la cantidad que el usuario ingreso en el input para INGRESAR.
    ingresarInput = request.form['ingresar']

    #* la variable global OPCION la colocamos en el metodo OPERACIONESOPCION(). hacemos esto con las demas opciones.
    ingresar = cajeroObj.OperacionesOpcion(opcion, int(ingresarInput))


    #* Llevamos a INGRESAR a la plantilla ingresar.html
    return render_template('ingresar.html', ingresar=ingresar)

# *****************************************
#* Ruta CONSULTAR
@app.route('/consultar')
def consultar():

    #* Como en consultar no hay un input ya que simplemente el usuario quiere consultar su sueldo, colocamos 'ninguna'
    saldo = cajeroObj.OperacionesOpcion(opcion, 'ninguna')
    print(saldo)

    return render_template('consultar.html', saldo=saldo)


# *****************************************
#* Ruta RETIRAR
@app.route('/retirar')
def retirar():

    return render_template('retirar.html')

# *****************************************
#* Ruta RETIRARPOST
@app.route('/retirar', methods=['POST'])
def retiraPost():

    #* RETIRARINPUT es la cantidad que el usuario ingreso en el input para retirar dinero.
    retirarInput = request.form['retirar']

    retirar = cajeroObj.OperacionesOpcion(opcion, int(retirarInput))





    return render_template('retirar.html', retirar=retirar)

# *****************************************
#* Ruta MOVIMIENTOS
@app.route('/movimientos')
def movimientos():

    movimientos = cajeroObj.OperacionesOpcion(opcion, 'ninguna')
    print('x'*30)
    print(movimientos)
    print('x'*30)




    return render_template('movimientos.html', movimientos=movimientos)


# *****************************************

#* Ruta PAGE_NO_FOUND
@app.errorhandler(404)
def page_no_found(error):
    return '<h1> Pagina no encontrada, siga buscando</h1>'

# *****************************************

#*MAIN
if __name__ == "__main__":

    app.run('0.0.0.0', '5000', debug=True)