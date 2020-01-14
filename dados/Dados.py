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
        self.tiposDados = {
            'cuatro': 4, 
            'seis': 6, 
            'ocho': 8, 
            'diez': 10
            }


    def activarJuego(self):

        cantidadCaras = 0

        if self.activar == 'activar':

            if self.tiposConCantidad != []:

                for tipo in self.tiposConCantidad:

                    for nombreTipo, valorTipo in self.tiposDados.items():

                        if tipo['tipoDado'] == nombreTipo:

                            randomCara = random.randint(1, valorTipo)

                            if int(tipo['cantidad']) > 0:

                                restarCantidad = self.collectionTipos.update_one({'tipoDado': tipo['tipoDado'], 'usuario': self.usuario}, {"$set": {'cantidad': int(tipo['cantidad'])-1}})

                                print('SE ha restado un intento por el tipo de cara: Cuatro')
                        
                                return tipo['tipoDado'], randomCara, tipo['cantidad']
                    
                            if int(tipo['cantidad']) == 0:

                                eliminarTipo = self.collectionTipos.delete_one({'tipoDado': tipo['tipoDado'], 'usuario': self.usuario})

                                return tipo['tipoDado'], 0, tipo['cantidad']

            else:

                return 'game over', 0, '1'


            

