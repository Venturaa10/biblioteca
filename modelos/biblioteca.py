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
        self.livros = []
    
    def cadastro_livro(self):
        novo_titulo = input('Digite o título do livro: ').title().strip()
        novo_autor = input('Digite o nome do Autor: ').title().strip()
        novo_genero = input('Digite o gênero do livro: ').title().strip()
        status = input('Digite o status do livro: ').title().strip()
        novo_livro = Livro(novo_titulo, novo_autor, novo_genero, status)
        self.livros.append(novo_livro)
        self.adicionar_livro(novo_livro)
        print(self.livros)
        print(f'Livro {novo_titulo} cadastrado na biblioteca')

    def adicionar_livro(self, novo_livro):
        Livro.titulo_livro(novo_livro)
        Livro.autor_livro(novo_livro)
        Livro.genero_livro(novo_livro)
        Livro.status_livro(novo_livro)
        Biblioteca()    
            
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

    def exibir_biblioteca(self):
        print(f'Informações do livro cadastrado!\nTitulo do Livro: {self.titulo}\nAutor: {self.autor}\nGenero: {self.genero}\nStatus: {self.status}')

    def __str__(self):
        return self.livros