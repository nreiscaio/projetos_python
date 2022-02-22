class Aluno:

    lista = []
    dicionario = {}

    #Construtor nomeado:
    def __init__(self, matricula=None, nome=None, turma=None, turno=None):
        self.matricula = matricula
        self.nome = nome
        self.turma = turma
        self.turno = turno