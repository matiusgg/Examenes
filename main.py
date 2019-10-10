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
    global mostrarHistorial

    # * lista que alberga el historial

    historial = []

    # * Datos de los input y el <select>

    valor1 = int(request.form['valor1'])

    valor2 = int(request.form['valor2'])

    operador = request.form['operador']

    # * Creacion objetos

    objetoCalc = Calculadora(valor1, valor2, operador)

    # * metodo para sacar el resultado

    result = objetoCalc.resultado()

    # * Historial metodo

    insertarHistoria = objetoCalc.insertar(valor1, operador, valor2, result)

    # *

    mostrarHistorial = objetoCalc.mostrar(historial)

    return redirect(url_for('resultado'))

# ****************************************


@app.route('/raiz')
def raiz():

    return render_template('raiz.html')


# ****************************************

@app.route('/raiz', methods=['POST'])
def llegadaRaiz():

    # * Variable global que nos permite usarla en otras rutas

    global resultRaiz
    global mostrarHistorial

    # * lista que alberga el historial

    historial = []

    # * Datos de los input y el <select>

    valor1 = int(request.form['valor1'])

    raiz = request.form['raiz']

    # * Creacion objetos

    objetoRaiz = Calculadora(valor1, '', raiz)

    # * Metodo resultado Raiz

    resultRaiz = objetoRaiz.resultadoRaiz()

    # * Historial metodo

    insertarHistoria = objetoRaiz.insertar(valor1, raiz, '-->', resultRaiz)

    # *

    mostrarHistorial = objetoRaiz.mostrar(historial)

    # RETURN

    return render_template('raiz.html', resultadoRaiz=resultRaiz, historial=mostrarHistorial)

# *****************************************


@app.route('/resultado', methods=['GET'])
def resultado():

    return render_template('resultado.html', resultado=result, historial=mostrarHistorial)

# *****************************************


@app.errorhandler(404)
def page_no_found(error):
    return '<h1> Pagina no encontrada, siga buscando</h1>'

# *****************************************


if __name__ == "__main__":

    app.run('0.0.0.0', '5000', debug=True)
