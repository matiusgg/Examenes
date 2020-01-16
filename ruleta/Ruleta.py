'''
CLASE RULETA
'''

# * Importamos JSON y el RANDOM y CSV
import json
import random
import csv


class Ruleta():

    def __init__(self):

        # * Diccionario Opciones

        opcionesDicc = {
            'suma': {
                'dinero 1000': 1000,
                'dinero 500': 500,
                'dinero 200': 200,
                'dinero 100': 100,
                'dinero 5000': 5000,
            },
            'x2': 2,

            'dinero Mitad': 2,
            'pierdes': 1,
            'carcel': 1000,
            'cosas': ['coche', 'ordenador', 'nevera', 'moto', 'bicicleta'],
            'saltar': 'saltar',
            'bote': ['bote', 'bote x2']
        }

        # self.inputRuleta = inputRuleta

        self.OPCIONES = ['dinero 1000', "pierdes", 'dinero Mitad',
                         "x2", 'dinero 500', 'dinero 200', 'carcel', 'dinero 5000', 'dinero 100', 'coche', 'ordenador', 'nevera', 'moto', 'bicicleta', 'saltar', 'bote', 'bote x2']

    #*************************************

    def Programa(self):

        if self.inputRuleta == 'activar':

            randomOpcion = random.choice(self.OPCIONES)

            for llaveDinero, valorDinero in self.opcionesDicc.items():

                if randomOpcion == llaveDinero:

                    escribir = open('dinero.csv', 'a', newline='')

                    salida = csv.writer(escribir)

                    salida.writerow(['opcion', 'score'])

                    salida.writerow([(opcion), (score)])

                    # del salida
                    escribir.close()