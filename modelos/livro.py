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

    @property
    def titulo(self):
        return self.titulo
    
    @titulo.setter
    def valida_titulo(self):
        pass

    @property
    def autor(self):
        return self.autor
    
    @autor.setter
    def valida_autor(self,novo_titulo, novo_autor):
        if len(novo_autor) <= 5:
            print(f'O Livro "{novo_titulo}" deve conter o nome do autor!')
        elif len(novo_autor) > 50:
            print(f'O nome "{novo_autor}" ultrapassou o limite de 50 letras!')
            return 
        else:
            print('Validado!')
            return novo_autor
        
        
    @property
    def genero(self):
        return self.genero

    @genero.setter
    def valida_genero(self):
        pass

    @property
    def status(self):
        return self.status

    @status.setter
    def valida_status(self):
        pass


        

            

        
        
    