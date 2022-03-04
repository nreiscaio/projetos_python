import animal

class Gato(animal.Animal):

    def __init__(self, nome, idade, peso):
        super().__init__(nome, idade, peso)
        