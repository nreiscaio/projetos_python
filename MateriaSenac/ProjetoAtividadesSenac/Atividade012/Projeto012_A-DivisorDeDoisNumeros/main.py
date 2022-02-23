#Curso Tecnico de Informatica
#Autor: Caio Nascimento
#Data inicio: 22/02/2022
#Data Termino: 22/02/2022


import os
from operacao import Operacao

os.system('cls')

#Entrada:
print('-'*40)
print('DIVISOR DE 2 NUMEROS QUE EXIBE EM ATÉ 4 CASAS DECIMAIS')
print('='*40)

#Entrada de Dados:
a = float(input('Insira o primeiro valor: '))
b = float(input('Insira o segundo valor: '))

#Criando Instancais:
valor = Operacao


resultado = valor.divisao(a, b)

#Saída:
print('-'*40)
print(f'Resultado da divisão: {resultado:.4f}')

#Texto de encerramento:
print('-'*40)
print('FIM DO PROGRAMA')
print('='*40)