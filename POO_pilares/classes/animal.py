# Importando ABC (Abstractb Base Classes) para criar classe
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome):
        # Atributo privado (Encapsulado)
        self._nome = nome

# Metodo getter para o atributo o atributo privado (Encapsulamento)
    def get_nome(self):
        return self._nome

# Metodo abstrato(Abstraçã)
    @abstractmethod
    def fazer_som(self):
        pass