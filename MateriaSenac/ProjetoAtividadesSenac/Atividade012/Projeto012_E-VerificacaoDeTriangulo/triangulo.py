class Triangulo:

    def __init__(self, a, b, c):
        
        self.a = a
        self.b = b
        self.c = c

    def conta(a, b, c):

        if (a <= 0 or b <= 0 or c <= 0):
            print('Valor de segmento inválido')
        elif ((a < (b + c)) and (b < (a + c)) and 9< (a + c)):
            print(f'{a} + {b} + {c}, formam um triângulo!')
        else:
            print(f'{a} + {b} + {c}, não formam um triângulo!')