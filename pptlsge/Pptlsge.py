'''
CLASE Pptlsge: Piedra-pape-tigera-lagarto-spock-garrafa-edans
'''

# Importamos librerias que nos ayudaran en la clase
import os
import random
import time


class Pptlsge():

    OPCIONES = {

        0: 'piedra',
        1: 'papel',
        2: 'tijera',
        3: 'lagarto',
        4: 'spock',
        5: 'garrafa',
        6: 'edans'

        }


    REGLAS = {

    'piedra': [OPCIONES[2], OPCIONES[3], OPCIONES[5]],
    'papel': [OPCIONES[6], OPCIONES[4], OPCIONES[0]],
    'tijera': [OPCIONES[1], OPCIONES[3], OPCIONES[6]],
    'lagarto': [OPCIONES[1], OPCIONES[4], OPCIONES[5]],
    'spock': [OPCIONES[0], OPCIONES[2], OPCIONES[5]],
    'garrafa': [OPCIONES[1], OPCIONES[2], OPCIONES[6]],
    'edans': [OPCIONES[0], OPCIONES[3], OPCIONES[4]],

    }
    
    def __init__(self):

        self.aleatorio = random.choice(self.OPCIONES)


    def piedra(self, opcionYmensaje):


        piedra = self.OPCIONES[0]

        if piedra == self.aleatorio:

            opcionYmensaje.append(self.aleatorio)
            opcionYmensaje.append(' Has empatado')

            return opcionYmensaje

        elif self.aleatorio == self.OPCIONES[2] or self.aleatorio == self.OPCIONES[3] or self.aleatorio == self.OPCIONES[5]:

            opcionYmensaje.append(self.aleatorio)
            opcionYmensaje.append(' Has ganado ')

            return opcionYmensaje

        elif self.aleatorio == self.OPCIONES[1] or self.aleatorio == self.OPCIONES[4] or self.aleatorio == self.OPCIONES[6]:

            opcionYmensaje.append(self.aleatorio)
            opcionYmensaje.append(' Has perdido ')

            return opcionYmensaje

# ************************************************************

    def papel(self, opcionYmensaje):


        papel = self.OPCIONES[1]

        if papel == self.aleatorio:

            opcionYmensaje.append(self.aleatorio)
            opcionYmensaje.append(' Has empatado')

            return opcionYmensaje

        elif self.aleatorio == self.OPCIONES[6] or self.aleatorio == self.OPCIONES[4] or self.aleatorio == self.OPCIONES[0]:

            opcionYmensaje.append(self.aleatorio)
            opcionYmensaje.append(' Has ganado ')

            return opcionYmensaje

        elif self.aleatorio == self.OPCIONES[2] or self.aleatorio == self.OPCIONES[3] or self.aleatorio == self.OPCIONES[5]:

            opcionYmensaje.append(self.aleatorio)
            opcionYmensaje.append(' Has perdido ')

            return opcionYmensaje

# ************************************************************

    def tijera(self, opcionYmensaje):


        tijera = self.OPCIONES[2]

        if tijera == self.aleatorio:

            opcionYmensaje.append(self.aleatorio)
            opcionYmensaje.append(' Has empatado')

            return opcionYmensaje

        elif self.aleatorio == self.OPCIONES[1] or self.aleatorio == self.OPCIONES[3] or self.aleatorio == self.OPCIONES[6]:

            opcionYmensaje.append(self.aleatorio)
            opcionYmensaje.append(' Has ganado ')

            return opcionYmensaje

        elif self.aleatorio == self.OPCIONES[0] or self.aleatorio == self.OPCIONES[4] or self.aleatorio == self.OPCIONES[5]:

            opcionYmensaje.append(self.aleatorio)
            opcionYmensaje.append(' Has perdido ')

            return opcionYmensaje


# ************************************************************

    def lagarto(self, opcionYmensaje):


        lagarto = self.OPCIONES[3]

        if lagarto == self.aleatorio:

            opcionYmensaje.append(self.aleatorio)
            opcionYmensaje.append(' Has empatado')

            return opcionYmensaje

        elif self.aleatorio == self.OPCIONES[1] or self.aleatorio == self.OPCIONES[4] or self.aleatorio == self.OPCIONES[5]:

            opcionYmensaje.append(self.aleatorio)
            opcionYmensaje.append(' Has ganado ')

            return opcionYmensaje

        elif self.aleatorio == self.OPCIONES[0] or self.aleatorio == self.OPCIONES[2] or self.aleatorio == self.OPCIONES[6]:

            opcionYmensaje.append(self.aleatorio)
            opcionYmensaje.append(' Has perdido ')

            return opcionYmensaje


# ************************************************************

    def spock(self, opcionYmensaje):


        spock = self.OPCIONES[4]

        if spock == self.aleatorio:

            opcionYmensaje.append(self.aleatorio)
            opcionYmensaje.append(' Has empatado')

            return opcionYmensaje

        elif self.aleatorio == self.OPCIONES[0] or self.aleatorio == self.OPCIONES[2] or self.aleatorio == self.OPCIONES[5]:

            opcionYmensaje.append(self.aleatorio)
            opcionYmensaje.append(' Has ganado ')

            return opcionYmensaje

        elif self.aleatorio == self.OPCIONES[1] or self.aleatorio == self.OPCIONES[3] or self.aleatorio == self.OPCIONES[6]:

            opcionYmensaje.append(self.aleatorio)
            opcionYmensaje.append(' Has perdido ')

            return opcionYmensaje


# ************************************************************

    def garrafa(self, opcionYmensaje):


        garrafa = self.OPCIONES[5]

        if garrafa == self.aleatorio:

            opcionYmensaje.append(self.aleatorio)
            opcionYmensaje.append(' Has empatado')

            return opcionYmensaje

        elif self.aleatorio == self.OPCIONES[1] or self.aleatorio == self.OPCIONES[2] or self.aleatorio == self.OPCIONES[6]:

            opcionYmensaje.append(self.aleatorio)
            opcionYmensaje.append(' Has ganado ')

            return opcionYmensaje

        elif self.aleatorio == self.OPCIONES[0] or self.aleatorio == self.OPCIONES[3] or self.aleatorio == self.OPCIONES[4]:

            opcionYmensaje.append(self.aleatorio)
            opcionYmensaje.append(' Has perdido ')

            return opcionYmensaje


# ************************************************************

    def edans(self, opcionYmensaje):


        edans = self.OPCIONES[6]

        if edans == self.aleatorio:

            opcionYmensaje.append(self.aleatorio)
            opcionYmensaje.append(' Has empatado')

            return opcionYmensaje

        elif self.aleatorio == self.OPCIONES[0] or self.aleatorio == self.OPCIONES[3] or self.aleatorio == self.OPCIONES[4]:

            opcionYmensaje.append(self.aleatorio)
            opcionYmensaje.append(' Has ganado ')

            return opcionYmensaje

        elif self.aleatorio == self.OPCIONES[1] or self.aleatorio == self.OPCIONES[2] or self.aleatorio == self.OPCIONES[5]:

            opcionYmensaje.append(self.aleatorio)
            opcionYmensaje.append(' Has perdido ')

            return opcionYmensaje

# *****************************************************************

    def resultado(self, inputOpcion, opcionYmensaje):

        resultado = {

            'piedra': self.piedra(opcionYmensaje),
            'papel': self.papel(opcionYmensaje),
            'tijera': self.tijera(opcionYmensaje),
            'lagarto': self.lagarto(opcionYmensaje),
            'spock': self.spock(opcionYmensaje),
            'garrafa': self.garrafa(opcionYmensaje),
            'edans': self.edans(opcionYmensaje),

        }

        for llave, valor in resultado.items():

            if inputOpcion == llave:

                return valor
