#Curso Tecnico de Informatica
#Autor: Caio Nascimento
#Data inicio: 07/03/2022
#Data Termino: 07/03/2022

import os
import retangulo, triangulo, circulo
import time, sys



while (True):
    

    try:

        

        os.system('cls')

        print('Programa para calcular áreas.')
        print('-'*50)
        print()
        print('Para calcular a área de um retangulo digite: 1; ')
        print('Para calcular a área de um triângulo digite: 2; ')
        print('Para calcular a área de um circulo digite: 3; ')
        print('='*50)
        print()

        digito = int(input('Qual a operação desejada: '))

        if digito == 1:

            altura = float(input('Altura: '))
            base = float(input('Base: '))
            retangulo = retangulo.Retangulo(altura, base)
            retangulo.areaRetangulo(altura, base)
            print('-'*50)
            print()
            break
    
        elif digito == 2:

            altura = float(input('Altura: '))
            base = float(input('Base: '))
            triangulo = triangulo.Triangulo(altura, base)
            triangulo.areaTriangulo(altura, base)
            print('-'*50)
            print()
            break

        elif digito == 3:

            raio = float(input('Raio: '))
            circulo = circulo.Circulo(raio)
            circulo.areaCirculo(raio)
            print('-'*50)
            print()
            break

        else:

            os.system('cls')
            print()
            print('-'*50)
            print('Operação não encontrada, digite novamente.')
            print('-'*50)
            print()

            for i in range(0, 3):
                sys.stdout.write('\r{}'.format(i))
                sys.stdout.flush()
                time.sleep(1)

    except ValueError:

        os.system('cls')
        print('-'*50)
        print('ValueError: Valor não inserido!')
        print('-'*50)
        print()

        for i in range(0, 3):
            sys.stdout.write('\r{}'.format(i))
            sys.stdout.flush()
            time.sleep(1)