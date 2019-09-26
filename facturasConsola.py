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

        escribir = open('nuevaFactura.csv', 'w', newline='')

        salida = csv.writer(escribir)

        salida.writerow(['fecha', 'gasto', 'hora', 'lugar'])

        for i in self._Registro:

            salida.writerows(i)

        # del salida
        escribir.close()

    def Buscar(self, fecha):

        with open('nuevaFactura.csv', 'r') as File:

            reader = csv.reader(File)

            for row in reader:

                if fecha == row[0]:

                    print(row[0], row[1], row[2], row[3])

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

    def VerFacturas(self):

        print('***************************')

        with open('nuevaFactura.csv', 'r') as File:

            reader = csv.reader(File)

            for row in reader:

                print('**************************')

                print(row)

        print('***************************')




def run():

    # Creacion del objeto

    facturas = Facturas()

    with open('nuevaFactura.csv', 'r') as File:

        reader = csv.reader(File)

        for row in reader:

            if row[0] != 'fecha' and row[1] != 'gasto' and row[2] != 'hora' and row[3] != 'lugar':

                facturas.Reinicio(row[0], row[1], row[2], row[3])

    print('BIENVENIDO, ESCOGE ENTRE LAS OPCIONES: ')
    print('1. Agregar factura')
    print('2. Buscar factura')
    print('3. Eliminar factura')
    print('4. Ver todas las facturas')

    opcion = int(input('Escoge entre las opciones: '))

    if opcion == 1:

        fecha = input('Escribe la fecha de la factura(anyo/mes/dia): ')
        gasto = int(input('Escribe el gasto el gasto del ticket: '))
        hora = input('Escribe la hora del ticket: ')
        lugar = input(
            'Escribe el lugar donde se realizo el ticket(ciudad/pueblo): ')

        facturas.Agregar(fecha, gasto, hora, lugar)

    elif opcion == 2:

        buscar = input(
            'Ingresa la fecha que quieras para saber las facturas que tuvistes en esa fecha(anyo/mes/dia): ')

        facturas.Buscar(buscar)

    elif opcion == 3:

        eliminar = input(
            'Ingresa la fecha de la factura que quieres eliminar(anyo/mes/dia): ')
        lugarEliminar = input(
            'Ingresa el lugar de la factura que quieres eliminar: ')

        facturas.Eliminar(eliminar, lugarEliminar)

    elif opcion == 4:

        facturas.VerFacturas()

    else:

        print('No escogiste ninguna opcion')


if __name__ == "__main__":
    run()
