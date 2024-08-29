# Classe Cachorro herda de Animal tudo (Herança)
from classes.animal import Animal

class Cachorro(Animal):
    def __init__(self, nome, raca):
        #  Chama construtor da classe pai
        super().__init__(nome)
        self.raca = raca

    # Importação do polimorfismo
    def fazer_som(self):
        return "Au Au"