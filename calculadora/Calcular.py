import math
import csv


class Historial():

    def __init__(self, valor1, operador, valor2, resultado):

        self.valor1 = valor1
        self.operador = operador
        self.valor2 = valor2
        self.resultado = resultado

    def listaOperacion(self):

        lista = [(self.valor1, self.operador, self.valor2, self.resultado)]

        return lista


class Calculadora():

    # ************************************

    # * CONTRUCTOR

    def __init__(self, valor1, valor2, operador):

        self._valor1 = valor1
        self._valor2 = valor2
        self._operador = operador
        self._listaDatos = []

    # **********************************

    # * METODOS:

    # * SUMAR

    def _sumar(self):

        sumar = self._valor1 + self._valor2

        # datosSumar = Historial(
        #     self._valor1, self._operador, self._valor2, sumar)

        # self._listaDatos.append(datosSumar.listaOperacion())

        return sumar

    # * RESTAR

    def _restar(self):

        restar = self._valor1 - self._valor2

        # datosrestar = Historial(
        #     self._valor1, self._operador, self._valor2, restar)

        # self._listaDatos.append(datosrestar.listaOperacion())

        return restar

    # * MULTIPLICAR

    def _multiplicar(self):

        multiplicar = self._valor1 * self._valor2

        # datosmultiplicar = Historial(
        #     self._valor1, self._operador, self._valor2, multiplicar)

        # self._listaDatos.append(datosmultiplicar.listaOperacion())

        return multiplicar

    # * DIVIDIR

    def _dividir(self):

        dividir = self._valor1 / self._valor2

        # datosdividir = Historial(
        #     self._valor1, self._operador, self._valor2, dividir)

        # self._listaDatos.append(datosdividir.listaOperacion())

        return dividir

    # * POTENCIA

    def _potencia(self):

        potencia = self._valor1 ** self._valor2

        # datospotencia = Historial(
        #     self._valor1, self._operador, self._valor2, potencia)

        # self._listaDatos.append(datospotencia.listaOperacion())

        return potencia

    # * RAIZ CUADRADA

    def _raizCuadrada(self):

        raizCuadrada = math.sqrt(self._valor1)

        # datosraizCuadrada = Historial(
        #     self._valor1, self._operador, self._valor2, raizCuadrada)

        # self._listaDatos.append(datosraizCuadrada.listaOperacion())

        return raizCuadrada

    # *Resultado

    def resultado(self):

        operador = {
            '+': self._sumar(),
            '-': self._restar(),
            '*': self._multiplicar(),
            '/': self._dividir(),
            '**': self._potencia()

        }

        for llave, valor in operador.items():

            if self._operador == str(llave):

                print(llave)

                print(valor)

                return valor

                break

    def resultadoRaiz(self):

        raiz = {
            'raizCuadrada': self._raizCuadrada()
        }

        for llave, valor in raiz.items():

            if self._operador == str(llave):

                print(llave)

                print(valor)

                return valor

    # * Agregar al historial

    def insertar(self, numero1, operacion, numero2, resultado):
        with open('historial.csv', 'a') as f:
            f.write(f'{numero1} {operacion} {numero2} = {resultado}\n')

    def mostrar(self, historial):
        with open('historial.csv', 'rt') as f:
            for linea in f:
                historial.append(linea)
        return historial

        # del salida
        escribir.close()
