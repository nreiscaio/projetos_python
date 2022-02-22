import os
from aluno import Aluno

os.system('cls')

print('-----CADASTRO DE ALUNO------------------------------------------------')

#Instanciando o objeto aluno:
aluno = Aluno()

while True:
    aluno.dicionario['matricula'] = int(input('Digite a matricula: '))
    aluno.dicionario['nome'] = str(input('Entre com o nome do alno: '))
    aluno.dicionario['turma'] = str(input('Nome da turma: ')).capitalize()
    aluno.dicionario['turno'] = str(input('Informe o turno: ')).capitalize()

    sair = str(input('Seseja continuar (s/n): ')).lower()
    aluno.lista.append(aluno.dicionario.copy())
    print()

    if sair == 's':
        aluno.dicionario.clear()
    else:
        break


#Saída:
os.system('cls')
print('Matricula\tNome do Aluno\tTurma    \tTurno')
for registro in aluno.lista:
    print('', end=' ' + '\n')
    for chave, valor in registro.items():
        print(f'{valor}', end='\t\t')
print()
print()