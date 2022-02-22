class Pessoa:

    #O método construtor do python é o __init__
    #O parametro self é obrigatorio
    def __init__(self, nome, idade, nascimento):

        #Criando os atributos dentro do construtor:
        self.nome = nome
        self.idade = idade
        self.nascimento = nascimento

    def __str__(self): #Método interno para dar saída String
        return f'''
        Nome: {self.nome}
        Data de Nascimento: {self.nascimento}
        Idade: {self.idade} anos.'''