#Tarefas:
from datetime import datetime

class Agenda:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.data = datetime.now() #Data atual

    def concluir(self):
        self.feito = True

    def __str__(self):
        return self.descricao + (f'\t\t(Ok!)' if self.feito else '')