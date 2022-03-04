import os
from curso import Curso

os.system('cls')

#Instanciando objetos:
curso1 = Curso()

print(curso1.__nome) #Não encontra o atributo nome
print(curso1.versao)
print(curso1.ano)


print(f'{curso1.nome_curso()}: {curso1.ano_curso()}')

print()