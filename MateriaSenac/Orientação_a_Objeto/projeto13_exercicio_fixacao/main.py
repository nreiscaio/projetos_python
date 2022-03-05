import os
import retangulo, triangulo, circulo
os.system('cls')


digito = int(input('Qual a operação desejada: '))




if digito == 1:
    altura = float(input('Altura: '))
    base = float(input('Base: '))
    retangulo = retangulo.Retangulo(altura, base)
    retangulo.areaRetangulo(altura, base)
    
elif digito == 2:
    altura = float(input('Altura: '))
    base = float(input('Base: '))
    triangulo = triangulo.Triangulo(altura, base)
    triangulo.areaTriangulo(altura, base)

elif digito == 3:
    raio = float(input('Raio: '))
    pi = float(input('Pi: '))
    triangulo = triangulo.Triangulo(raio, pi)
    triangulo.areaTriangulo(raio, pi)



