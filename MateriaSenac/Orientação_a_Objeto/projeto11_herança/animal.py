class Animal():

    def __init__(self, nome, idade, peso):
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso

    def latir(self):
        print(f'O {self.__nome} está latindo...')

    def miar(self):
        print(f'O {self.__nome} está miando...')

    def falar(self):
        print(f'O {self.__nome} está falando...')