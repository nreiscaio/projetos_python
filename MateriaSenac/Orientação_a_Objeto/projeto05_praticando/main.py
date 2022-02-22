import os
from equacao import Equacao

os.system('cls')

#Instanciando o objeto:
equacao1 = Equacao

#Invocando o metodo para o calculo
x1, x2 = equacao1.equacao(1, 5, -6)


#Saída:
print('-'*50)
print(f'Valor de x1: {x1}')
print(f'Valor de x2: {x2}')
print('-'*50)

print()