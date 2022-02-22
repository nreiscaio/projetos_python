#Importando as bibliotecas:
from conta import Conta
from carros import Carros
from pessoa import Pessoa
import os
os.system('cls')


#------------------------------------------------------------------------------
print('Programa Principal----------------------------------------------------')
print()

print('Objetos do tipo Pessoa------------------------------------------------')

#Criando objetos pessoa
gerente = Pessoa('Jhon Doe', 50)
officeboy = Pessoa('Smith', 20)

print(f'\tNome: {gerente.nome}')
print(f'\tIdade: {gerente.idade}')
print()

#------------------------------------------------------------------------------
print('Objetos do tipo Carro-------------------------------------------------')

#Criando objetos Carros
gol = Carros('Volkswagen', 'Branco', 'BRA3049', 1985)
ferrari = Carros('F250', 'Vermelha', 'BRA6060', 2020)
prius = Carros('Toyota', 'Marrom', 'BRA5070', 2022)
print(f'\tFabricante: {gol.fabricante}')
print(f'\tCor: {gol.cor}')
print(f'\tPlaca: {gol.placa}')
print(f'\tAno: {gol.ano}')

print()

#------------------------------------------------------------------------------
print('Objetos do tipo Conta-------------------------------------------------')

#Criando objetos Conta:
jhon = Conta('Jhon Doe', 123456, 1550, 13)
jane = Conta('Jane Doe', 654321, 2525, 15)

print(f'\tNome do Cliente: {jhon.cliente}')
print(f'\tAgencia: {jhon.agencia}')
print(f'\tNúmero da Conta: {jhon.conta}')
print(f'\tDigito: {jhon.digito}')

#------------------------------------------------------------------------------
print('='*50)