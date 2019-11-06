import os
import csv

class Cajero():

    def __init__(self):

        self.opciones = {}

    def OperacionesOpcion(self, inputOpcion, operacion):

        if inputOpcion == 'consultar':
            print(inputOpcion)

            self.mostrarSaldo(inputOpcion)

            return self.opciones['consultar']

        if inputOpcion == 'retirar':

            self.mostrarSaldo('consultar')

            saldo = self.opciones['consultar']

            print(type(saldo))
            print(type(operacion))

            if saldo < operacion:

                # self.opciones['mensajeRetirar'] = 'No tienes suficiente dinero para retirar'

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
            #* Sino para agregar a los movimientos.csv

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

            #* Sino agrega al diccionario todos los movimientos

            with open('movimientos.csv', 'r') as File:

                reader = csv.reader(File)

                for row in reader:

                    print('**************************')

                    print(row)

                    if row[0] != 'opcion' and row[1] != 'saldo':

                        self.opciones[f'{row[0]}'] = row[1]


                    

# *****************************************************************

