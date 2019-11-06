#* Importar CSV
import csv

#* Clase Cajero
class Cajero():

    #*contructor
    def __init__(self):

        #* Diccionario que nos ayudara para realizar el contenido de los metodos
        self.opciones = {}

        #*Registro de movimientos
        self.movimientos = []
    
    #* Metodo OperacionesOpcion()
    def OperacionesOpcion(self, inputOpcion, operacion):

        #* Si INPUTOPCION es igual 'consultar'
        if inputOpcion == 'consultar':
            print(inputOpcion)

            #* llamada a self.mostrarSaldo() para que nos agregue el saldo de saldo.csv al diccionario self.opciones
            self.mostrarSaldo(inputOpcion)

            return self.opciones['consultar']

        if inputOpcion == 'retirar':

            #* Llamada a self.mostrarSaldo() para tener el saldo actual en el diccionario.
            self.mostrarSaldo('consultar')

            saldo = self.opciones['consultar']

            print(type(saldo))
            print(type(operacion))

            #* Si saldo es menor que la cantidad del input ingresada por el usuario.
            if saldo < operacion:

                return 'No tienes suficiente dinero para retirar'
            
            else:

                saldo -= operacion

                #* Guardamos los cambios del saldo en self.guardarSaldo()
                self.guardarSaldo('consultar', saldo)
                #* Tambien agregamos el movimiento de RETIRAR a movimientos.csv
                self.guardarSaldo(inputOpcion, saldo)

                #* Se ha actualizado el saldo
                self.mostrarSaldo('consultar')
                #* Agregamos al diccionario opciones el nuevo movimiento, en este caso RETIRAR dinero
                self.mostrarSaldo(inputOpcion)
                nuevoSaldo = self.opciones['retirar']

                return f'Acabas de retirar: {operacion} y tu saldo actual es: {nuevoSaldo}'

        if inputOpcion == 'ingresar':

            #* Llamada a self.mostrarSaldo() para tener el saldo actual en el diccionario.
            self.mostrarSaldo('consultar')

            saldo = self.opciones['consultar']

            print(type(saldo))
            print(type(operacion))

            #* Si operacion es igual 0, es decir no agrego ninguna cantidad para ingresar.
            if operacion == 0:

                # self.opciones['mensajeRetirar'] = 'No tienes suficiente dinero para retirar'

                return 'No ingresaste ninguna cantidad'
            
            else:

                saldo += operacion

                #* Guardamos los cambios del saldo en self.guardarSaldo()
                self.guardarSaldo('consultar', saldo)
                #* Tambien agregamos el movimiento de INGRESAR a movimientos.csv
                self.guardarSaldo(inputOpcion, saldo)

                #* Se ha actualizado el saldo
                self.mostrarSaldo('consultar')
                #* Agregamos al diccionario opciones el nuevo movimiento, en este caso INGRESAR dinero
                self.mostrarSaldo(inputOpcion)
                nuevoSaldo = self.opciones['ingresar']

                return f'Acabas de ingresar: {operacion} y tu saldo actual es: {nuevoSaldo}'

        if inputOpcion == 'movimientos':

            #* Llamada a self.mostrarSaldo() para tener todos los movimientos del archivo movimientos.csv en self.movimientos
            self.mostrarSaldo(inputOpcion)
            print(self.opciones)

            #* Aplicar REVERSE() para tener los ultimos movimientos que se han realizado.
            self.movimientos.reverse()

            print('?'*30)
            print(self.movimientos)

            #* Lista que albergara los ultimos 10 movimientos.
            ultimosMovimientos = []

            #* Si son mas de 10 movimientos, solo agrega 10 a la lista ultimosMovimientos.
            if len(self.movimientos) >= 10:

                ultimosMovimientos.extend([self.movimientos[0], self.movimientos[1], self.movimientos[2], self.movimientos[3], self.movimientos[4], self.movimientos[5], self.movimientos[6], self.movimientos[7], self.movimientos[8], self.movimientos[9]])

                return ultimosMovimientos
            
            else:
                #* Sino retorname los que se encuentren.
                return self.movimientos


# ****************************************************************

        # * metodo guardarSaldo()
    def guardarSaldo(self, opcion, saldo):


        #* Condicional para actualizar el saldo.csv

        if opcion == 'consultar':

            escribir = open('saldo.csv', 'w', newline='')

            salida = csv.writer(escribir)

            salida.writerow(['opcion', 'saldo'])

            salida.writerow([(opcion), (saldo)])

            # del salida
            escribir.close()
        
        else:
            #* Sino para agregar los demas movimientos al archivo movimientos.csv

            escribir = open('movimientos.csv', 'a', newline='')

            salida = csv.writer(escribir)

            salida.writerow(['opcion', 'saldo'])

            salida.writerow([(opcion), (saldo)])

            # del salida
            escribir.close()


# *****************************************************************

# * metodo mostrarSaldo()
    def mostrarSaldo(self, opcion):

        #* Condicional para actualizar el saldo.csv

        if opcion == 'consultar':

            with open('saldo.csv', 'r') as File:

                reader = csv.reader(File)

                for row in reader:

                    print('**************************')

                    print(row)

                    if row[0] != 'opcion' and row[1] != 'saldo':

                        self.opciones['consultar'] = int(row[1])

        else:

            #* Sino agrega al diccionario todos los movimientos de movimientos.csv

            with open('movimientos.csv', 'r') as File:

                reader = csv.reader(File)

                for row in reader:

                    print('**************************')

                    print(row)

                    if row[0] != 'opcion' and row[1] != 'saldo':

                        self.opciones[f'{row[0]}'] = row[1]

                        #* Ademas para la opcion MOVIMIENTOS, agregar a la lista tambien todos los movimientos.
                        self.movimientos.extend([[row[0], row[1]]])




                    

# *****************************************************************

