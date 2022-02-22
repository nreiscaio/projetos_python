import os
os.system('cls')

from retangulo import Retangulo


#Instanciando os objetos
retangulo1 = Retangulo
retangulo2 = Retangulo
retangulo3 = Retangulo
retangulo4 = Retangulo

#Cabeçalho:
print('Calculos para area e perimetro de um retangulo')
print('-'*50)

#Argumentos para encontrar a area:
resultado1 = retangulo1.area(10, 5)
resultado2 = retangulo2.area(100, 5)

print('ÁREA------------------------------------------------------------------')
print(f'A area do retangulo é: {resultado1}')
print(f'A area do retangulo é: {resultado2}')
print('-'*50)

#Argumentos para encontrar o perimetro:
resultado3 = retangulo3.perimetro(10, 5)
resultado4 = retangulo4.perimetro(100, 5)

print('PERIMETRO-------------------------------------------------------------')
print(f'A area do retangulo é: {resultado3}')
print(f'A area do retabgulo é: {resultado4}')
print('='*50)

print()