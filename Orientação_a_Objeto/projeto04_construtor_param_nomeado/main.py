import os
from animal import Animal

#Criando as instâncias dos objetos
animal1 = Animal()
animal2 = Animal()
animal3 = Animal()
animal4 = Animal()

#Com parâmetros nomeados os argumentos são opicionais:
tobias = Animal(nome='Tobias')
felipe = Animal(nome='Felipe')
bob = Animal(nome='Bob')


#Saída:
print('-'*50)
print(animal1)
print('-'*50)
print(animal2)
print('-'*50)
print(animal3)
print('-'*50)
print()

print('-'*50)
print(tobias)
print('-'*50)
print(felipe)
print('-'*50)
print(bob)
print('='*50)
print()