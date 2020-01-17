'''
CLASE RULETA
'''

# * Importamos JSON y el RANDOM y CSV
import json
import random
import csv


class Ruleta():

    def __init__(self, collection, usuario):

        # * Diccionario Opciones

        self.opcionesDicc = {
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

        #* collection mongodb
        self.collection = collection

        #* usuario
        self.usuario = usuario

        #* random resultado
        self.randomOpcion = random.choice(self.OPCIONES)

    #*************************************

    def definirIntentos(self, intento):

        if intentos == 7:


            registrarIntentos = self.collection.update_one({'usuario': self.usuario}, {"$set": {'intentos': intentos}})

        if intentos == 'infinito':

            registrarIntentos = self.collection.update_one({'usuario': self.usuario}, {"$set": {'intentos': intentos}})

    def Juego(self, activar):

        if activar == 'activar':

            for llave, valor in self.opcionesDicc:

                if llave == self.randomOpcion:

                    return resultado, premio, puntuacionTotal, intentos
            



