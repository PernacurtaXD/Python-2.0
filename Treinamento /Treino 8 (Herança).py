import os

os.system("cls || clear")

class Aluno:
    def __init__(self, nome: str, idade: str) -> None:
        self.nome = nome
        self.idade = idade


    def exibir_dados(self) -> str:
        return f"Nome: {self.nome} \nIdade: {self.idade}"
    

aluno = Aluno("Luis", "18")

print(aluno.exibir_dados())