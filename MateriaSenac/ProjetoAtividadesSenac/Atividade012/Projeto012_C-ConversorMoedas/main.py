#Curso Tecnico de Informatica
#Autor: Caio Nascimento
#Data inicio: 22/02/2022
#Data Termino: 22/02/2022


from ast import Break, While
import os
from conversor import Conversor

os.system('cls')

#Entrada:
print('-'*50)
print('CONVERSOR DE REAIS EM DOLAR, EURO, LIBRA')
print('-'*50)
print('Tecle "1" para converter R$ para U$ (Dolar);')
print('      "2" para converter R$ para € (Euro);')
print('      "3" para converter R$ para £ (Libra).')
print('='*50)

#Entrada de dados:
dolar = 1
euro = 2
libra = 3


digito = int(input('Insira qual conversao você deseja fazer: '))
a = float(input('Por favor, insira um valor em reais: '))

valor = Conversor

resultado = valor.conversorDolar(a)
resulatdo2 = valor.conversorEuro(a)
resultado3 = valor.conversorLibra(a)


while True:

    if digito == 1:
        print(f'R${a} vale U${resultado:.4f}')

        break

    elif digito == 2:
        print(f'R${a} vale €{resulatdo2:.4f}')

        break

    elif digito == 3:
        print(f'R${a} vale £{resultado3:.4f}')

        break

    else:
        print('Nâo encontrado')
        break