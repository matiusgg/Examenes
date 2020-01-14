import random
import os
import csv

class Dados():

    def __init__(self, activar, tiposConCantidad, collectionTipos, usuario):

        #* usuario mediante session
        self.usuario = usuario

        #* BD de mongoDB
        self.collectionTipos = collectionTipos

        #* Input hidden Activar
        self.activar = activar

        #*Lista donde ira la puntuación del usuario
        self.listaPuntuacion = []

        #*Lista donde ira el números de caras según el tipo que escogio el usuario
        self.NumCaras = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'diez']

        #*Lista con los tipos de dados que si tiene una cantidad
        self.tiposConCantidad = tiposConCantidad


        #* Random no iniciado sobre la cual cara sacara
        self.randomCara = random.choice(self.NumCaras)

        #*Cantidad total de veces
        self.cantidadTotal = 0

        #* números de intentos
        self.intentos = 0

        #* Lista con tipos de dados
        self.tiposDados = ['cuatro', 'seis', 'ocho', 'diez']


    def activarJuego(self):

        cantidadCaras = 0

        if self.activar == 'activar':

            for tipo in self.tiposConCantidad:

                if tipo['tipoDado'] == 'cuatro':

                    randomCara = random.randint(1, 4)

                    if tipo['cantidad'] > 0:

                        restarCantidad = self.collectionTipos.update_one({'tipoDado': tipo['tipoDado'], 'usuario': self.usuario}, {"$set": {'cantidad': tipo['cantidad']-1}})

                        print('SE ha restado un intento por el tipo de cara: Cuatro')
                        
                        return tipo['tipoDado'], randomCara, tipo['cantidad']
                    
                    if tipo['cantidad'] == 0:

                        return tipo['tipoDado'], 0, tipo['cantidad']
