import os

import gato, cachorro, papagaio


os.system('cls')

gato = gato.Gato('CN', 20 , 10)
cachorro = cachorro.Cachorro('Dn', 27, 89)
papagaio = papagaio.Papagaio('Jv', 50, 5)

gato.miar()
cachorro.latir()
papagaio.falar()