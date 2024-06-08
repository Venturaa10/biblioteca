import os

os.system('cls')
# Livro: Representa um livro na biblioteca, contendo atributos como título, autor, gênero, e status de empréstimo.


class Livro:
    def __init__(self, titulo, autor, genero, status):
        '''Metodo construtor'''
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.status = True

    def titulo_livro(self):
        return self.titulo
    
    def autor_livro(self):
        return self.autor
    
    def verifica_autor(titulo):
        autor = input("Digite o autor do livro: ").title().strip()

        if len(autor) <= 5:
            print(f'O Livro "{titulo}" deve conter o nome do autor!')
        elif len(autor) > 50:
            print(f'O nome "{autor}" ultrapassou o limite de 50 letras!')
            return 
        else:
            print('Validado!')
            return autor
            

    def genero_livro(self):
        return self.genero

    def status_livro(self):
        return self.status


            

        
        
    