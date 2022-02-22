class Bissexto:

    def __init__(self, a):

        self.a = a

    def conta(a):

        if (a <= 0):
            print('Ano inválido!')
        elif(a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
            print(f'O ano {a} é bissexto!')
        else:
            print(f'O ano {a} não é bissexto!')