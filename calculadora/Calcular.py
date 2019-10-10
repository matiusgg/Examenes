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

        datosSumar = Historial(
            self._valor1, self._operador, self._valor2, sumar)

        self._listaDatos.append(datosSumar.listaOperacion())

        self._guardar()

        return sumar
        

    # * RESTAR

    def _restar(self):

        restar = self._valor1 - self._valor2

        datosrestar = Historial(
            self._valor1, self._operador, self._valor2, restar)

        self._listaDatos.append(datosrestar.listaOperacion())

        

        return restar

    # * MULTIPLICAR

    def _multiplicar(self):

        multiplicar = self._valor1 * self._valor2

        datosmultiplicar = Historial(
            self._valor1, self._operador, self._valor2, multiplicar)

        self._listaDatos.append(datosmultiplicar.listaOperacion())

        

        return multiplicar

    # * DIVIDIR

    def _dividir(self):

        dividir = self._valor1 / self._valor2

        datosdividir = Historial(
            self._valor1, self._operador, self._valor2, dividir)

        self._listaDatos.append(datosdividir.listaOperacion())

        

        return dividir

    # * POTENCIA

    def _potencia(self):

        potencia = self._valor1 ** self._valor2

        datospotencia = Historial(
            self._valor1, self._operador, self._valor2, potencia)

        self._listaDatos.append(datospotencia.listaOperacion())

        

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
            '√': self._raizCuadrada()
        }

        for llave, valor in raiz.items():

            if self._operador == str(llave):

                print(llave)

                print(valor)

                return valor

    # * Agregar al historial

    def _guardar(self):

        escribir = open('historial.csv', 'a', newline='')

        salida = csv.writer(escribir)

        salida.writerow(['valor1', 'operador', 'valor2', 'resultado'])

        for i in self._listaDatos:

            salida.writerows(i)

        # del salida
        escribir.close()

    def verHistorial(self, listaHistorial):

        with open('historial.csv', 'r') as File:

            reader = csv.reader(File)

            for row in reader:

                print('**************************')

                print(row)

                if row[0] != 'valor1' and row[1] != 'operacion' and row[2] != 'valor2' and row[3] != 'resultado':

                    listaHistorial.append(row)

                    print(listaHistorial)
