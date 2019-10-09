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
    global diccHistoria

    #* lista Historial que va a ir al metodo verHistorial

    listaHistoria = []

    #* Diccionario que nos permitira ver el historial

    diccHistoria = {}

    # * Datos de los input y el <select>

    valor1 = int(request.form['valor1'])

    valor2 = int(request.form['valor2'])

    operador = request.form['operador']

    # * Creacion objetos

    objetoCalc = Calculadora(valor1, valor2, operador)

    # * metodo para sacar el resultado

    result = objetoCalc.resultado()

    # * metodo donde tenemos el historial de operaciones

    historial = objetoCalc.verHistorial(listaHistoria)

    #* Bucle

    contador = 0

    for i in listaHistoria:

        diccHistoria[f'operacion{contador}'] = f'{i[0]} {i[1]} {i[2]} = {i[3]}'

        contador += 1

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

    # * Datos de los input y el <select>

    valor1 = int(request.form['valor1'])

    raiz = request.form['raiz']

    # * Creacion objetos

    objetoRaiz = Calculadora(valor1, '', raiz)

    # * Metodo resultado Raiz

    resultRaiz = objetoRaiz.resultadoRaiz()

    return render_template('raiz.html', resultadoRaiz=resultRaiz)

# *****************************************


@app.route('/resultado', methods=['GET'])
def resultado():

    return render_template('resultado.html', resultado=result, **diccHistoria)

# *****************************************


@app.errorhandler(404)
def page_no_found(error):
    return '<h1> Pagina no encontrada, siga buscando</h1>'

# *****************************************


if __name__ == "__main__":

    app.run('0.0.0.0', '5000', debug=True)
