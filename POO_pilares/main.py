from classes.cachorro import Cachorro
from classes.gato import Gato

# Função para demonstrar Polimorfismo
def emitir_som(animal):
    print(f"{animal.get_nome()} faz: {animal.fazer_som()}")
    print("")

def main(): 
    # Criando Instancias (Objetos) das Classes
    rex = Cachorro("Rex", "Labrador")
    mimi = Gato("Mimi", "Branco")

    # Demonstrando o funcionamento 
    print(" ")
    print(f"Nome do cachorro: {rex.get_nome()}")
    print(f"Raça do Cachorro: {rex.raca}")
    print(" ")
    print(f"Nome do gato: {mimi.get_nome()}")
    print(f"Cor do gato: {mimi.cor}")
    print(" ")

    # Demonstrando polimorfismo
    emitir_som(rex)
    emitir_som(mimi)


# Demonstrando polimorfismo
if __name__ == "__main__":
    main()