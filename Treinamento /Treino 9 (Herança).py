import os 

class Livro:
    def __init__(self, titulo: str, autor: str, numero_paginas: int, preco: float) -> None:
        self.titulo = titulo
        self.autor = autor
        self.numero_paginas = numero_paginas
        self.preco = preco


    def exibir_dados_livro(self) -> str:
        return f"\nTítulo do Livro: {self.titulo}\nAutor: {self.autor}\nNúmero de Páginas: {self.numero_paginas}\nPreço do Livro: R${self.preco}"    
    

livro = Livro("KING KONG", "ALbert", 190, 52.90)

print(livro.exibir_dados_livro())


