import os


os.system('cls')

with open('C:/ProjetosPythonGit/projetos_python/MateriaSenac/Aula_Senac/Aula019_07-03-2022/arquivo.csv', 'w+') as arquivo:

    #Inserindo um cabeçalho para os caompos da tabela csv:
    arquivo.write('Nome' + ';' + 'Endereço' + ';' + 'Telefone')

    #Salvar linha:
    arquivo.write('\n')

    while (True):

        #Inserindo informações no arquivo:
        nome = input('Insira seu nome: ')
        endereco = input('Insira seu endereço: ')
        celular = input('Insira seu telefone: ')

        #Armazenamento das informações no arquivo
        #com o método write
        arquivo.write(nome)
        arquivo.write(';')
        arquivo.write(endereco)
        arquivo.write(';')
        arquivo.write(celular)

        resposta = input('Deseja continuar (s/n): ').lower()

        if resposta == 's':

            #Seek()
            #0: define o ponto de referencia no inicio do arquivo.
            #1: define o ponto de referencia na posição aual do arquivo.
            #2: define o ponto de referenia no final do arquivo.
            arquivo.seek(0,0)

            #Saltar linha:
            arquivo.write('\n')
            continue

        else:
            lista = arquivo.readlines()
            break

    #Fazer uma pesquisa dentro do arquivo csv
    for linha in lista:
        if 'Jhon' in linha:

            print(linha)