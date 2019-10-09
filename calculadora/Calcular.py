import math


class Calculadora():

    # ************************************

    # * CONTRUCTOR

    def __init__(self, valor1, valor2, operador):

        self._valor1 = valor1
        self._valor2 = valor2
        self._operador = operador

    # **********************************

    # * METODOS:

    # * SUMAR

    def _sumar(self):

        sumar = self._valor1 + self._valor2

        return sumar

    # * RESTAR

    def _restar(self):

        restar = self._valor1 - self._valor2

        return restar

    # * MULTIPLICAR

    def _multiplicar(self):

        multiplicar = self._valor1 * self._valor2

        return multiplicar

    # * DIVIDIR

    def _dividir(self):

        dividir = self._valor1 / self._valor2

        return dividir

    # * POTENCIA

    def _potencia(self):

        potencia = self._valor1 ** self._valor2

        return potencia

    # * RAIZ CUADRADA

    def _raizCuadrada(self):

        raizCuadrada = math.sqrt(self._valor1)

        return raizCuadrada

    # *Resultado

    def resultado(self):

        operador = {
            '+': self._sumar(),
            '-': self._restar(),
            '*': self._multiplicar(),
            '/': self._dividir(),
            '**': self._potencia(),
            '√': self._raizCuadrada()

        }

        for llave, valor in operador.items():

            if self._operador == str(llave):

                print(llave)

                print(valor)

                return valor

                break
