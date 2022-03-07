import math

class Formas():

    def __init__(self, base = None, altura = None, raio = None):
        self.base = base
        self.altura = altura
        self.raio = raio

    def areaRetangulo(self, altura, base):
        resultado = base * altura
        print(f'A área do retangulo é: {resultado}')

    def areaTriangulo(self, altura, base):
        resultado = (base * altura) / 2
        print(f'A área do triângulo é: {resultado}')

    def areaCirculo(self, raio):
        resultado = 3.14 * (raio ** 2)
        print(f'A área do circulo é: {resultado}')

