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
        self.mensaje = []


    def operacion(self, inputOpcion):


        if inputOpcion == self.aleatorio:

            self.mensaje.append(inputOpcion)
            self.mensaje.append('EMPATE')
                    

            return self.mensaje

        else:

            for llave, valor in self.REGLAS.items():

                if inputOpcion == llave:

                    for ganas in valor:

                        if self.aleatorio == ganas:

                            self.mensaje.append(self.aleatorio)
                            self.mensaje.append('GANAS')

                            return self.mensaje
                
                        else:

                            self.mensaje.append(self.aleatorio)
                            self.mensaje.append('PIERDES')

                            return self.mensaje





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
