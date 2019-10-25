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

    def __init__(self):

        # * Opciones Lista

        self.OPCIONES = ['dinero 1000', "pierdes", 'dinero Mitad',
                         "x2", 'dinero 500', 'dinero 200', 'carcel', 'dinero 5000', 'dinero 100', 'coche', 'ordenador', 'nevera', 'moto', 'bicicleta', 'saltar', 'bote', 'bote x2']

        self.aleatorio = random.choice(self.OPCIONES)

        self.score = 1

        self.ListaScore = []

        # self.intentos = intentos

        #* Calculos
        self.calculos = []

        #*ListaDinero
        self.listaDinero = ['dinero 1000',
            'dinero 500',
            'dinero 200',
            'dinero 100',
            'dinero 5000']

        #*REsultado
        self.resultado = []


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
    def mostrarScore(self):

        base = []
        afectanBase = []
        contador = 0
        

        with open('score.csv', 'r') as File:

            reader = csv.reader(File)

            for row in reader:

                print('**************************')

                print(row)

                if row[0] != 'opcion' and row[1] != 'score':


                    self.calculos.extend([[row[0], row[1]]])


        print('*?*?'*50)

        print(self.calculos)

        print('*?*?'*50)

        for minilista in self.calculos:

            if ('dinero 100' in minilista) or ('dinero 200' in minilista) or ('dinero 500' in minilista) or ('dinero 1000' in minilista) or ('dinero 5000' in minilista):

                if minilista[0] == 'dinero 100':

                    base.append(minilista[1])

                if minilista[0] == 'dinero 200':

                    base.append(minilista[1])
                
                if minilista[0] == 'dinero 500':

                    base.append(minilista[1])
                
                if minilista[0] == 'dinero 1000':

                    base.append(minilista[1])
                
                if minilista[0] == 'dinero 5000':

                    base.append(minilista[1])


            else:

                print('no se encuentra ninguna opcion de dinero')

            if minilista[0] == 'x2':

                print(minilista)

                afectanBase.append(f'x{minilista[1]}')

            if minilista[0] == 'pierdes':

                print(minilista)

                afectanBase.append(minilista[1])

            if minilista[0] == 'dinero Mitad':

                print(minilista)

                afectanBase.append(f'/{minilista[1]}')

            if minilista[0] == 'carcel':

                print(minilista)

                afectanBase.append(f'-{minilista[1]}')

        print('/opem/'*50)

        for i in base:

            print(i)

            contador += int(i)
        
        print(f'base total sin operaciones: {contador}')

        print('/opem2/'*50)

        print(afectanBase)

        #********************************************************************

        listmult = []

        for operacionmult in afectanBase:

            if operacionmult == 'x2':

                listmult.append(operacionmult)

        print(listmult)

        for m in listmult:

            splitMult = m.split('x')

            contador *= int(splitMult[1])

        self.resultado.append(contador)

        print(f'base total multiplicada : {contador}')

        #********************************************************

        listdiv = []

        for operaciondiv in afectanBase:

            if operaciondiv == '/2':

                listdiv.append(operaciondiv)

        print(listdiv)

        for d in listdiv:

            splitdiv = d.split('/')

            contador /= int(splitdiv[1])

        self.resultado.append(contador)

        print(f'base total dividir : {contador}')

        #********************************************************

        listCarcel = []

        for operacionCarcel in afectanBase:

            if operacionCarcel == '-1000':

                listCarcel.append(operacionCarcel)


        print(listCarcel)

        for d in listCarcel:

            splitCarcel = d.split('-')

            contador -= int(splitCarcel[1])

        self.resultado.append(contador)

        print(f'base total carcel : {contador}')

        #********************************************************

        if '1' in afectanBase:

            contador = 1

        self.resultado.append(contador)

        print(f'base total pierdes : {contador}')

        print(self.resultado)



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
                            
                            self.ListaScore.append(valorSuma)

                            self.guardarOpcion(llaveSuma, valorSuma)
                            self.mostrarScore()
                            print(self.resultado)

                            return self.ListaScore

                            

                if self.aleatorio == llave and llave == 'carcel':

                    resta = self.score - valor

                    self.ListaScore.append(llave)
                    self.ListaScore.append(' ')
                    self.ListaScore.append(self.resultado[2])

                    print(self.ListaScore)
                    self.guardarOpcion(llave, valor)
                    self.mostrarScore()
                    print(self.resultado)

                    return self.ListaScore

                    

                if self.aleatorio == llave and llave == 'x2':

                    mult = self.score * valor

                    self.ListaScore.append(llave)
                    self.ListaScore.append(' ')
                    self.ListaScore.append(self.resultado[0])

                    print(self.ListaScore)
                    self.guardarOpcion(llave, valor)
                    self.mostrarScore()
                    print(self.resultado)

                    return self.ListaScore

                    

                if self.aleatorio == llave and llave == 'dinero Mitad':

                    mitdinero = self.score / valor

                    separacion = llave.split(' ')

                    self.ListaScore.append(separacion[0])
                    self.ListaScore.append(separacion[1])
                    self.ListaScore.append(self.resultado[1])

                    print(self.ListaScore)
                    self.guardarOpcion(llave, valor)
                    self.mostrarScore()
                    print(self.resultado)

                    return self.ListaScore

                    

                if self.aleatorio == llave and llave == 'pierdes':

                    pierde = self.score

                    self.ListaScore.append(llave)
                    self.ListaScore.append(' ')
                    self.ListaScore.append(pierde)

                    print(self.ListaScore)
                    self.guardarOpcion(llave, pierde)
                    self.mostrarScore()
                    print(self.resultado)

                    return self.ListaScore

                    

                if llave == 'cosas':

                    for cosa in valor:

                        if self.aleatorio == cosa:

                            self.ListaScore.append(cosa)
                            self.ListaScore.append(' ')
                            self.ListaScore.append(' ')

                            print(self.ListaScore)
                            self.guardarOpcion(llave, cosa)
                            self.mostrarScore()
                            print(self.resultado)

                            return self.ListaScore

                            

                if self.aleatorio == llave and llave == 'saltar':

                    self.ListaScore.append(llave)
                    self.ListaScore.append(' ')
                    self.ListaScore.append(valor)

                    print(self.ListaScore)
                    self.guardarOpcion(llave, valor)
                    self.mostrarScore()
                    print(self.resultado)

                    return self.ListaScore

                    

                if llave == 'bote':

                    for botes in valor:

                        if self.aleatorio == botes:

                            self.ListaScore.append(llave)
                            self.ListaScore.append(' ')
                            self.ListaScore.append(botes)

                            print(self.ListaScore)
                            self.guardarOpcion(llave, botes)
                            self.mostrarScore()
                            print(self.resultado)

                            return self.ListaScore

                            

                