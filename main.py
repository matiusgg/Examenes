from flask import Flask, request, make_response, redirect, render_template, session, url_for
import csv


class Registro():

    def __init__(self, fecha, gasto, hora, lugar):

        self.fecha = fecha
        self.gasto = gasto
        self.hora = hora
        self.lugar = lugar

    def listaRegistro(self):

        lista = [(self.fecha, self.gasto, self.hora, self.lugar)]

        return lista


class Facturas():

    def __init__(self):

        self._Registro = []

    # Agregar

    def Agregar(self, fecha, gasto, hora, lugar):

        NuevoRegistro = Registro(fecha, gasto, hora, lugar)

        self._Registro.append(NuevoRegistro.listaRegistro())

        self._Guardar()

    def _Guardar(self):

        escribir = open('facturasR.csv', 'w', newline='')

        salida = csv.writer(escribir)

        salida.writerow(['fecha', 'gasto', 'hora', 'lugar'])

        for i in self._Registro:

            salida.writerows(i)

        del salida
        escribir.close()

    def Buscar(self, fecha, busqueda):

        with open('facturasR.csv', 'r') as File:

            reader = csv.reader(File)

            for row in reader:

                if fecha == row[0]:

                    busqueda['buscar'] = [row[0], row[1], row[2], row[3]]

                    return busqueda['buscar']

    def Reinicio(self, fecha, gasto, hora, lugar):

        ReinicioRegistro = Registro(fecha, gasto, hora, lugar)

        self._Registro.append(ReinicioRegistro.listaRegistro())

        print(self._Registro)

    def Eliminar(self, fecha, lugar):

        for facturas in self._Registro:

            for index, registro in enumerate(facturas):

                if fecha == registro[0] and lugar == registro[3]:

                    del facturas[index]

                    print(self._Registro)

                    self._Guardar()

    def VerFacturas(self, Diccionario):

        print('***************************')

        with open('facturasR.csv', 'r') as File:

            reader = csv.reader(File)

            for row in reader:

                print('**************************')

                print(row)

                for i in row:

                    print(i)

                    Diccionario.append(i)

                    print(Diccionario)


                # return Diccionario


# *************************************************************
# *************************************************************
app = Flask(__name__)

# Creacion del objeto

facturas = Facturas()


@app.route('/')
def redireccionar():

    respuesta = make_response(redirect('/menu'))

    return respuesta


@app.route('/menu')
def menu():

    with open('facturasR.csv', 'r') as File:

        reader = csv.reader(File)

        for row in reader:

            if row[0] != 'fecha' and row[1] != 'gasto' and row[2] != 'hora' and row[3] != 'lugar':

                facturas.Reinicio(row[0], row[1], row[2], row[3])

    return render_template('menu.html')


# *************************************************

@app.route('/buscar', methods=['GET', 'POST'])
def buscar():

    if request.method == 'POST':

        fecha = request.form['fechaBuscar']

        busqueda = {}

        facturas.Buscar(fecha, busqueda)

        return busqueda

    else:

        return render_template('buscar.html')

# *************************************************
@app.route('/mostrar', methods=['GET', 'POST'])
def mostrar():

    if request.method == 'POST':

        mostrarTodo = []

        facturas.VerFacturas(mostrarTodo)

        return f'Estas son todas tus facturas: {mostrarTodo}'
    else:

        return render_template('mostrar.html')

# *************************************************
@app.route('/eliminar', methods=['GET', 'POST'])
def eliminar():

    if request.method == 'POST':

        fecha = request.form['eliminar']
        lugar = request.form['eliminar2']

        registro = {}

        facturas.Eliminar(fecha, lugar)

        return f'Has eliminado la siguiente factura: {registro}'
    else:
        return render_template('eliminar.html')


# ********************************************

@app.route('/home', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':

        fecha = request.form['fecha']
        gasto = request.form['gasto']
        hora = request.form['hora']
        lugar = request.form['lugar']

        facturas.Agregar(fecha, gasto, hora, lugar)

        registro = {

            'fecha': fecha,
            'gasto': gasto,
            'hora': hora,
            'lugar': lugar
        }

        # return redirect(url_for('menu'))
        return registro
    else:
        return render_template('home.html')


@app.errorhandler(404)
def page_no_found(error):

    return '<h1> Pagina no encontrada, siga buscando</h1>'


# **********************************************************************


if __name__ == "__main__":

    app.run('0.0.0.0', '4000', debug=True)
