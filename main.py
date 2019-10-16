# * IMPORTACIONES del FLASK y del PAQUETE donde se alberga la CLASE Horoscopo()
from flask import Flask, request, make_response, redirect, render_template, session, url_for
from horoscopo.Horoscopo import Horoscopo

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


@app.route('/home', methods=['POST'])
def llegada():

    # * Variable global SIGNO para llevarla a la ruta 'SIGNO'
    global signo
    global fecha

    # *Recoger el dato del input
    fecha = request.form['fecha']

    # * Creacion Objeto
    objHoroscopo = Horoscopo(str(fecha))

    # *Definimos la variable global con el metodo de la clase
    signo = objHoroscopo.signo()

    # * Redireccion a la ruta 'SIGNO'
    return redirect(url_for('signo'))

# *****************************************

# * Ruta SIGNO
@app.route('/signo', methods=['GET'])
def signo():

    return render_template('signo.html', **signo, fecha=fecha)

# *****************************************

# * RUTA PAGINA ERROR
@app.errorhandler(404)
def page_no_found(error):
    return '<h1> Pagina no encontrada, siga buscando</h1>'

# *****************************************


# * MAIN
if __name__ == "__main__":

    app.run('0.0.0.0', '5000', debug=True)
