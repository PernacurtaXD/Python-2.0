import os 

os.system("cls || clear")

nome = str(input("Digite seu nome:"))
idade = int(input("Digite sua idade:"))
nota1 = float(input("Digite sua primeira nota:"))
nota2 = float(input("Digite sua segunda nota:"))
nota3 = float(input("Digite sua terceira nota:"))
nota4 = float(input("Digite sua quarta nota:"))

total = nota1 + nota2 + nota3 + nota4
media = total / 4

os.system("cls || clear")

print(f"Aluno: {nome}")
print(f"Idade: {idade}")
print(f"1ª nota: {nota1}")
print(f"2ª nota: {nota2}")
print(f"3ª nota: {nota3}")
print(f"4ª nota: {nota4}")
print(f"Média = {media}")

print("\n")
if media >= 7:
    print(f"APROVADO!!")
else:
    print(f"REPROVADO")