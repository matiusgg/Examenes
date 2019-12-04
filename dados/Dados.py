import random
import os
import csv

class Dados():

    def __init__(self):

        #*Lista donde ira la puntuación del usuario
        self.listaPuntuacion = []

        #*Lista donde ira el números de caras según el tipo que escogio el usuario
        self.NumCaras = []

        #*Lista con los tipos de dados que si tiene una cantidad
        self.tiposConCantidad = []


        #* Random no iniciado sobre la cual cara sacara
        self.randomCara = 0

        #*Cantidad total de veces
        self.cantidadTotal = 0

        #* números de intentos
        self.intentos = 0

    def activarJuego(self, listaPuntuacion, listaTipos, activar):

        cantidadCaras = 0

        if activar == 'activar':

            print(listaPuntuacion)

            for i in listaPuntuacion:

                if i[1] == '0':

                    print(f'No se coloco una cantidad en este tipo: {i[0]}')
            
                else:

                    self.tiposConCantidad.append(i)

            for i in self.tiposConCantidad:

                print('****???*****')
                print(i)

                self.cantidadTotal += int(i[1])

            for i in self.tiposConCantidad:

                if i[0] == 'cuatro':

                    cantidadCaras = 4
                    self.randomCara = random.randint(0, cantidadCaras)

                    print(self.randomCara)

                    self.intentos += 1

                    return i[0], self.intentos, self.randomCara, self.cantidadTotal

            
                if i[0] == 'seis':

                    cantidadCaras = 6
                    self.randomCara = random.randint(0, cantidadCaras)

                    print(self.randomCara)

                    self.intentos += 1

                    return i[0], self.intentos, self.randomCara, self.cantidadTotal

                if i[0] == 'ocho':

                    cantidadCaras = 8
                    self.randomCara = random.randint(0, cantidadCaras)

                    print(self.randomCara)

                    self.intentos += 1

                    return i[0], self.intentos, self.randomCara, self.cantidadTotal

                if i[0] == 'diez':

                    cantidadCaras = 10
                    self.randomCara = random.randint(0, cantidadCaras)

                    print(self.randomCara)

                    self.intentos += 1

                    return i[0], self.intentos, self.randomCara, self.cantidadTotal



