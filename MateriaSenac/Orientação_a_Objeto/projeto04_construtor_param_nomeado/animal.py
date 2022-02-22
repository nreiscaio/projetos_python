class Animal:

    #Utilizando parâmetros nomeados:
    def __init__(self, nome='Sem nome', raca='Labrador', nascimento=1970):

        self.nome = nome
        self.raca = raca
        self.nascimento = nascimento

    #Método interno (__str__) para darsáida String
    def __str__(self):
        return f'''
        Nome: {self.nome}
        Data Nascimento: {self.raca}
        Idade: {self.nascimento} anos.'''