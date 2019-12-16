#* Librerias utiles para la clase
import random
import os

class InmobiliariaCalc():

    def __init__(self, valor1, operador, valor2):

        self.valor1 = valor1
        self.operador = operador
        self.valor2 = valor2

    def resultado(self):

        if self.operador == '+': 
            suma =  self.valor1 +  self.valor2
            print(f'El resultado de la suma es: {suma}')
            return suma
        if self.operador == '-':
            resta =  self.valor1 -  self.valor2
            print(f'El resultado de la resta es: {resta}')
            return resta
        if self.operador == '*':
            multiplicacion =  self.valor1 *  self.valor2
            print(f'El resultado de la multiplicacion es: {multiplicacion}')
            return multiplicacion
        if self.operador == '/':
            division =  self.valor1 /  self.valor2
            print(f'El resultado de la division es: {division}')
            return division