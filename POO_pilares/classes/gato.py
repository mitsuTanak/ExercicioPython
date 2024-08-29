# Classe Gato herda de Animal tudo (Herança)
from classes.animal import Animal

class Gato(Animal):
    def __init__(self, nome, cor):
        #  Chama construtor da classe pai
        super().__init__(nome)
        self.cor = cor

# Importação do polimorfismo
    def fazer_som(self):
        return "Miau Miau"