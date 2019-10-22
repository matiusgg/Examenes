'''
CLASE RULETA
'''

# * Importamos JSON y el RANDOM y CSV
import json
import random
import csv


class Ruleta():

    # * Diccionario Opciones

    opcionesDicc = {
        'suma': {
            'dinero 1000€': 1000,
            'dinero 500€': 500,
            'dinero 200€': 200,
            'dinero 100€': 100,
            'dinero 5000€': 5000,
        },
        'x2': 2,

        'dinero Mitad': 2,
        'pierdes': 1,
        'carcel': 1000,
        'cosas': ['coche', 'ordenador', 'nevera', 'moto', 'bicicleta'],
        'saltar': 'saltar',
        'bote': ['bote', 'bote x2']
    }

    def __init__(self):

        # * Opciones Lista

        self.OPCIONES = ['dinero 1000€', "pierdes", 'dinero Mitad',
                         "x2", 'dinero 500€', 'dinero 200€', 'carcel', 'dinero 5000€', 'dinero 100€', 'coche', 'ordenador', 'nevera', 'moto', 'bicicleta', 'saltar', 'bote', 'bote x2']

        self.aleatorio = random.choice(self.OPCIONES)

        self.score = 1

        self.ListaScore = []

        # self.intentos = intentos

    #*metodo ruleta

    def ruleta(self, inputRuleta):

        if inputRuleta == 'activar':

            # self.intentos += 1

            # print(self.intentos)

            for llave, valor in self.opcionesDicc.items():

                if llave == 'suma':

                    for llaveSuma, valorSuma in valor.items():

                        if self.aleatorio == llaveSuma:

                            suma = self.score + valorSuma

                            separacion = llaveSuma.split(' ')

                            self.ListaScore.append(separacion[0])

                            self.ListaScore.append(separacion[1])
                            
                            self.ListaScore.append(suma)

                            self.guardarOpcion(llaveSuma, valorSuma)

                            return self.ListaScore

                            

                if self.aleatorio == llave and llave == 'carcel':

                    resta = self.score - valor

                    self.ListaScore.append(llave)
                    self.ListaScore.append(' ')
                    self.ListaScore.append(resta)

                    print(self.ListaScore)
                    self.guardarOpcion(llave, valor)

                    return self.ListaScore

                    

                if self.aleatorio == llave and llave == 'x2':

                    mult = self.score * valor

                    self.ListaScore.append(llave)
                    self.ListaScore.append(' ')
                    self.ListaScore.append(mult)

                    print(self.ListaScore)
                    self.guardarOpcion(llave, valor)

                    return self.ListaScore

                    

                if self.aleatorio == llave and llave == 'dinero Mitad':

                    mitdinero = self.score / valor

                    separacion = llave.split(' ')

                    self.ListaScore.append(separacion[0])
                    self.ListaScore.append(separacion[1])
                    self.ListaScore.append(valor)

                    print(self.ListaScore)
                    self.guardarOpcion(llave, mitdinero)

                    return self.ListaScore

                    

                if self.aleatorio == llave and llave == 'pierdes':

                    pierde = self.score

                    self.ListaScore.append(llave)
                    self.ListaScore.append(' ')
                    self.ListaScore.append(pierde)

                    print(self.ListaScore)
                    self.guardarOpcion(llave, pierde)

                    return self.ListaScore

                    

                if llave == 'cosas':

                    for cosa in valor:

                        if self.aleatorio == cosa:

                            self.ListaScore.append(cosa)
                            self.ListaScore.append(' ')
                            self.ListaScore.append(' ')

                            print(self.ListaScore)
                            self.guardarOpcion(llave, cosa)

                            return self.ListaScore

                            

                if self.aleatorio == llave and llave == 'saltar':

                    self.ListaScore.append(llave)
                    self.ListaScore.append(' ')
                    self.ListaScore.append(valor)

                    print(self.ListaScore)
                    self.guardarOpcion(llave, valor)

                    return self.ListaScore

                    

                if llave == 'bote':

                    for botes in valor:

                        if self.aleatorio == botes:

                            self.ListaScore.append(llave)
                            self.ListaScore.append(' ')
                            self.ListaScore.append(botes)

                            print(self.ListaScore)
                            self.guardarOpcion(llave, botes)

                            return self.ListaScore

                            

        # self.mostrarOpcion()

# ****************************************************************

        # * metodo guardarOpcion()
    def guardarOpcion(self, opcion, score):

        escribir = open('score.csv', 'a', newline='')

        salida = csv.writer(escribir)

        salida.writerow(['opcion', 'score'])

        salida.writerow([(opcion), (score)])

        # del salida
        escribir.close()

# *****************************************************************

    # * metodo mostrarScore()
    def mostrarScore(self, fecha, frase):

        base = 0

        with open('score.csv', 'r') as File:

            reader = csv.reader(File)

            for row in reader:

                print('**************************')

                print(row)

                if row[0] != 'opcion' and row[1] != 'score':

                    if row[0] != ' ' and row[1] != ' ':

                        if row[0] == 'dinero 1000€' or row[0] == 'dinero 100€' or row[0] == 'dinero 200€' or row[0] == 'dinero 500€' or row[0] == 'dinero 5000€':

                            base += row[1]

                            print(base)

                        else:

                            print('No hay dinero')


