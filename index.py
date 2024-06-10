from modelos.biblioteca import Biblioteca
from modelos.livro import Livro
import os
os.system('cls')

biblioteca = Biblioteca()
biblioteca.cadastro_livro()
Biblioteca()

def main():
    Biblioteca.exibir_biblioteca()


if __name__ == '__main__': 
    main()

