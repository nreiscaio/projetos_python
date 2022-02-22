#Curso Tecnico de Informatica
#Autor: Caio Nascimento
#Data inicio: 21/02/2022
#Data Termino: 21/02/2022

import os
from equacao import Equacaco

os.system('cls')


print('-'*50)
print('PROGRAMA PARA CALCULAR A EQUAÇÃO DO SEGUNDO GRAU')
print('='*50)

#Entrada:
a = int(input('Informe o valor de "a": '))
b = int(input('Informe o valor de "b": '))
c = int(input('Informe o valor de "c": '))

conta = Equacaco

resultado1, resultado2 = conta.conta(a, b, c)

#Saida:
print('-'*50)
print('CALCULO DE RAIZ QUADRADA')
print('='*50)
print(f" x': {resultado1},  x'': {resultado2}")
print('-'*50)
print('FIM DO PROGRAMA')
print('-'*50)