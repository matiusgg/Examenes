'''
Clase Horoscopo
QUE CADA DIA TENGA UN UNICO MENSAJE, QUE SI REINICIAS EL MISMO DIA NO TE CAMBIE LA FRASE SI NO QUE SE MANTENGA
'''
# * Importamos JSON y el RANDOM y CSV
import json
import random
import csv


class Horoscopo():

    def __init__(self, fecha):

        # *atributo que recibira el input
        self.fecha = fecha
        # *diccionario donde estara las fecha
        self.diccFecha = {}
        # *diccionario donde estaran el signo y frase
        self.resultado = {}
        # * FRASE
        self.frase = ''

    # *****************************************************

    # * METODOS

    # * Metodo signo
    def signo(self):

        splitFecha = self.fecha.split('-')

        self.diccFecha['anyo'] = splitFecha[0]
        self.diccFecha['mes'] = splitFecha[1]
        self.diccFecha['dia'] = splitFecha[2]

        mesInput = int(self.diccFecha['mes'])
        diaInput = int(self.diccFecha['dia'])

        # * Abrimos el archivo signo.json donde tenemos el diccionario de signos para poder retornarnos el signo

        with open('static/json/signos.json') as contenido:

            diccionarioSignos = json.load(contenido)

            for i in diccionarioSignos:

                if ((i.get('mes')[0] == mesInput) and (diaInput >= i.get('dias')[0])) or ((i.get('mes')[1] == mesInput) and (diaInput <= i.get('dias')[1])):

                    self.resultado['signo'] = i.get('signo')

                    self.frase = random.choice(i.get('frases'))

                    self.guardarFrase(self.fecha, self.frase)
                    self.mostrarFrase(self.fecha, self.frase)

                    print(self.resultado)

                    return self.resultado

    # * REgistro de la fecha introducida

    # * metodo guardarFrase()
    def guardarFrase(self, fecha, frase):

        escribir = open('frases.csv', 'a', newline='')

        salida = csv.writer(escribir)

        salida.writerow(['fecha', 'frase'])

        salida.writerow([(fecha), (frase)])

        # del salida
        escribir.close()

    # * metodo mostrarFrase()
    def mostrarFrase(self, fecha, frase):

        with open('frases.csv', 'r') as File:

            reader = csv.reader(File)

            for row in reader:

                print('**************************')

                print(row)

                if row[0] != 'fecha' and row[1] != 'frase':

                    if fecha == row[0]:

                        # Agregamos al diccionario la frase agregada al archivo csv que salio del RANDOM

                        self.resultado['frase'] = row[1]

                    else:

                        print('La frase esta repetida para la misma fecha')
