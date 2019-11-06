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

    return render_template('opciones.html')


# *****************************************


@app.errorhandler(404)
def page_no_found(error):
    return '<h1> Pagina no encontrada, siga buscando</h1>'

# *****************************************


if __name__ == "__main__":

    app.run('0.0.0.0', '5000', debug=True)