from flask import Flask, request, make_response, redirect, render_template, session, url_for
from pptlsge.Pptlsge import Pptlsge

# *****************************************

app = Flask(__name__)

# *****************************************

app.config['SECRET_KEY'] = 'SUPER SECRETO'

# *****************************************


@app.route('/')
def redireccionar():

    global OPCIONES

    OPCIONES = [

        'piedra',
        'papel',
        'tijera',
        'lagarto',
        'spock',
        'garrafa',
        'edans'

    ]

    return redirect('/home')

# *****************************************


@app.route('/home')
def home():

    return render_template('home.html', opciones=OPCIONES)

# *****************************************

@app.route('/home', methods=['POST'])
def llegadaDatos():

    global resultPiedra
    global opcionAleatoria
    global mensaje
    global opcionYmensaje

    opcionYmensaje = []

    # valorInputs = {
    #     'piedra': request.form['piedra'],
    #     'papel': request.form['papel'],
    #     'tijera': request.form['tijera'],
    #     'lagarto': request.form['lagarto'],
    #     'spock': request.form['spock'],
    #     'garrafa': request.form['garrafa'],
    #     'edans': request.form['edans']
    # }
    juegoObj = Pptlsge()

    opcionYmensaje = juegoObj.piedra(opcionYmensaje)

    opcionAleatoria = opcionYmensaje[0]

    mensaje = opcionYmensaje[1]

    return redirect(url_for('resultado'))

# *****************************************

@app.route('/resultado', methods=['GET'])
def resultado():

    return render_template('resultado.html', resultado=opcionYmensaje, opcionAleatoria=opcionAleatoria, mensaje =mensaje)


# *****************************************


@app.errorhandler(404)
def page_no_found(error):
    return '<h1> Pagina no encontrada, siga buscando</h1>'

# *****************************************


if __name__ == "__main__":

    app.run('0.0.0.0', '5000', debug=True)
