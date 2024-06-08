from modelos.livro import Livro
import os
os.system('cls')

'''
Biblioteca: Representa a coleção de livros, contendo métodos para adicionar, remover e procurar livros, bem como para emprestar e devolver livros.
Funcionalidades:

Adicionar livro à biblioteca.
Remover livro da biblioteca.
Procurar livro por título ou autor.
Emprestar livro a um usuário (se disponível).
Devolver livro.
'''

class Biblioteca(Livro):
    def __init__(self):
        self.livros = [{

}]
    
    def cadastro_livro(self):
        titulo = input("Digite o título do livro: ").title().strip()
        autor = Livro.verifica_autor(titulo)
        genero = input("Digite o gênero do livro: ").title().strip()
        status = input("Digite o status do livro: ").title().strip()
        novo_livro = Livro(titulo, autor, genero, status)
        
        self.adicionar_livro(novo_livro)
        print(f'Livro {titulo} cadastrado na biblioteca')

    def adicionar_livro(self):
        self.livros.append(self)


    def remover_livro(self):
        pass

    def procurar_livro(self):
        pass

    def emprestar_livro(self):
        pass
    
    def devolver_livro(self):
        pass

    def exibir(self):
        print(Livro.titulo_livro())

    def verifica_livro(valor):
        pass
    

    def verifica_livro(valor):
        pass