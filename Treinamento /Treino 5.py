import os 

os.system("cls || clear")

QUANT = 2
soma = 0


notas = []
for i in range (QUANT):
    nota = float(input(f"Digite sua {i+1}ª nota:"))
    notas.append(nota)
    soma+=nota

media = soma / QUANT

print(f"Média = {media}")
if media >= 6:
    print("Aprovado")
elif media >= 4: 
    print("Recuperação")
elif media < 4: 
    print("Reprovado")     
