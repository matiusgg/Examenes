from flask import Flask, request, make_response, redirect, render_template, session, url_for
from calculadora.Calcular import Calculadora

# *****************************************

app = Flask(__name__)

# *****************************************

app.config['SECRET_KEY'] = 'SUPER SECRETO'

# *****************************************


@app.route('/')
def redireccionar():

    return redirect('/home')

# *****************************************


@app.route('/home')
def home():

    return render_template('home.html')

# *****************************************


@app.route('/home', methods=['POST'])
def llegada():

    # * Variable global que nos permite usarla en otras rutas

    global result

    # * Datos de los input y el <select>

    valor1 = int(request.form['valor1'])

    valor2 = int(request.form['valor2'])

    operador = request.form['operador']

    # * Creacion objetos

    objetoCalc = Calculadora(valor1, valor2, operador)

    result = objetoCalc.resultado()

    return redirect(url_for('resultado'))

# *****************************************


@app.route('/resultado', methods=['GET'])
def resultado():

    return render_template('resultado.html', resultado=result)

# *****************************************


@app.errorhandler(404)
def page_no_found(error):
    return '<h1> Pagina no encontrada, siga buscando</h1>'

# *****************************************


if __name__ == "__main__":

    app.run('0.0.0.0', '5000', debug=True)
