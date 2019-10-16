'''
Clase Horoscopo
QUE CADA DIA TENGA UN UNICO MENSAJE, QUE SI REINICIAS EL MISMO DIA NO TE CAMBIE LA FRASE SI NO QUE SE MANTENGA
'''


class Horoscopo():

    # SIGNOS = ['aries', 'tauro', 'geminis', 'cancer', 'leo', 'virgo',
    #           'libra', 'escorpio', 'sagitario', 'capricornio', 'acuario', 'piscis']

    # * diccionario Signo que nos ayudara en los metodos

    signos = {
        'acuario': {
            'mes': [1, 2],
            'dias': [20, 18]
        },
        'piscis': {
            'mes': [2, 3],
            'dias': [19, 20]
        },
        'aries': {
            'mes': [3, 4],
            'dias': [21, 20]
        },
        'tauro': {
            'mes': [4, 5],
            'dias': [21, 20]
        },
        'geminis': {
            'mes': [5, 6],
            'dias': [21, 20]
        },
        'cancer': {
            'mes': [6, 7],
            'dias': [21, 20]
        },
        'leo': {
            'mes': [7, 8],
            'dias': [21, 21]
        },
        'virgo': {
            'mes': [8, 9],
            'dias': [22, 22]
        },
        'libra': {
            'mes': [9, 10],
            'dias': [23, 22]
        },
        'escorpio': {
            'mes': [10, 11],
            'dias': [23, 22]
        },
        'sagitario': {
            'mes': [11, 12],
            'dias': [23, 20]
        },
        'capricornio': {
            'mes': [12, 1],
            'dias': [21, 19]
        }
    }

    def __init__(self, fecha):

        # *atributo que recibira el input
        self.fecha = fecha
        # *diccionario donde estara las fecha
        self.diccFecha = {}
        # *diccionario donde estaran el signo y frase
        self.resultado = {}

    # *****************************************************

    # * METODOS

    # * Metodo signo
    def signo(self):

        splitFecha = self.fecha.split('-')

        self.diccFecha['anyo'] = splitFecha[0]
        self.diccFecha['mes'] = splitFecha[1]
        self.diccFecha['dia'] = splitFecha[2]

        for signoLlave, valorFecha in self.signos.items():

            for llave, valor in valorFecha.items():

                for i in valor:

                    mesInput = int(self.diccFecha['mes'])
                    diaInput = int(self.diccFecha['dia'])

                    if llave == 'mes':

                        if ((valorFecha['mes'][0] == mesInput) and (diaInput >= valorFecha['dias'][0])) or ((valorFecha['mes'][1] == mesInput) and (diaInput <= valorFecha['dias'][1])):

                            return signoLlave


# objHoroscopo = Horoscopo('2019-5-21')

# print(objHoroscopo.signo())
