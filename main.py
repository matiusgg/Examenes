# * IMPORTACIONES del FLASK y del PAQUETE donde se alberga la CLASE Horoscopo()
from flask import Flask, request, make_response, redirect, render_template, session, url_for
from ruleta.Ruleta import Ruleta

# *****************************************
# * variable APP
app = Flask(__name__)

# *****************************************

app.config['SECRET_KEY'] = 'SUPER SECRETO'

# *****************************************

# *Ruta que direcciona a '/home'
@app.route('/')
def redireccionar():

    return redirect('/home')
    

# *****************************************

# *Ruta HOME
@app.route('/home')
def home():

    return render_template('home.html')

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

# *Ruta INTENTOS
@app.route('/intentos')
def intentos():

    return render_template('intentos.html')

# *****************************************

# # *Ruta LLEGADA POST INTENTOS
# @app.route('/intentos', methods=['POST'])
# def llegadaIntentos():

#     # * Variables globales
#     global intento
    
#     # * Modo intento escogido
#     intento = request.form['intento']

#     # * Redireccion a la ruta 'RULETA'
#     return redirect(url_for('ruleta'))

# *****************************************

# # *Ruta RULETA
# @app.route('/ruleta', methods=['GET'])
# def ruleta():

#     return render_template('ruleta.html')

# *****************************************

# *Ruta LLEGADA POST RULETA
@app.route('/ruleta', methods=['POST'])
def ruleta():

    #*Valor input para activar ruleta
    inputRuleta = request.form['ruleta']

    # # * Modo intento escogido
    # intento = request.form['intento']

    #* Objeto
    ruletaObj = Ruleta()

    #* metodo Ruleta()
    listaRandom = ruletaObj.ruleta(inputRuleta)

    # #*resultadoTotal
    # listaResultado = ruletaObj.resultado()


    return render_template('ruleta.html', opcion=listaRandom[0], splitOpcion=listaRandom[1], resultado=listaRandom[2])

# *****************************************

# * RUTA PAGINA ERROR
@app.errorhandler(404)
def page_no_found(error):
    return '<h1> Pagina no encontrada, siga buscando</h1>'

# *****************************************


# * MAIN
if __name__ == "__main__":

    app.run('0.0.0.0', '5000', debug=True)