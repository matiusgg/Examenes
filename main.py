from flask import Flask, request, make_response, redirect, render_template, session, url_for
import json
from cajero.Cajero import Cajero

# *****************************************

app = Flask(__name__)

# *****************************************

app.config['SECRET_KEY'] = 'SUPER SECRETO'

# *****************************************
#* Objeto
cajeroObj = Cajero()


@app.route('/')
def redireccionar():

    return redirect('/home')

# *****************************************

@app.route('/home')
def home():

    return render_template('home.html')

# *****************************************

@app.route('/home', methods=['POST'])
def homeUsuario():

    global confirmarCodigo

    codigo = request.form['codigo']

    with open('static/json/cuentas.json') as contenido:

            cuentas = json.load(contenido)

            for i in cuentas:

                if codigo == i.get('codigo'):

                    return redirect(url_for('opciones'))

                else:

                    mensajeError = 'El codigo es incorrecto'


    return render_template('home.html', mensaje=mensajeError)

# *****************************************

@app.route('/opciones')
def opciones():

    global opciones

    opciones = ['ingresar', 'consultar', 'retirar', 'movimientos']

    return render_template('opciones.html', opciones=opciones)

# *****************************************

@app.route('/opciones', methods=['POST'])
def opcionesEscogida():

    global opcion


    opcion = request.form['opcion']

    for i in opciones:

        if i == opcion:

            return redirect(url_for(f'{opcion}'))

            

    return render_template('opciones.html')


# *****************************************

@app.route('/ingresar')
def ingresar():



    return render_template('ingresar.html')

# *****************************************

@app.route('/ingresar', methods=['POST'])
def ingresarPost():

    ingresarInput = request.form['ingresar']

    ingresar = cajeroObj.OperacionesOpcion(opcion, int(ingresarInput))



    return render_template('ingresar.html', ingresar=ingresar)

# *****************************************

@app.route('/consultar')
def consultar():

    saldo = cajeroObj.OperacionesOpcion(opcion, 'ninguna')
    print(saldo)

    return render_template('consultar.html', saldo=saldo)


# *****************************************

@app.route('/retirar')
def retirar():

    return render_template('retirar.html')

# *****************************************

@app.route('/retirar', methods=['POST'])
def retiraPost():

    retirarInput = request.form['retirar']

    retirar = cajeroObj.OperacionesOpcion(opcion, int(retirarInput))





    return render_template('retirar.html', retirar=retirar)

# *****************************************

@app.route('/movimientos')
def movimientos():

    registro = {}

    movimientos = cajeroObj.OperacionesOpcion(opcion, 'ninguna')


    return render_template('movimientos.html', movimientos=movimientos)


# *****************************************


@app.errorhandler(404)
def page_no_found(error):
    return '<h1> Pagina no encontrada, siga buscando</h1>'

# *****************************************


if __name__ == "__main__":

    app.run('0.0.0.0', '5000', debug=True)