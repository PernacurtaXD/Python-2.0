import os 

os.system("cls || clear")
#SOLICITANDO DADOS 
morango = int(input("Quantos (kg) de morango você deseja:"))
maca = int(input("Quantos (kg) de maçã você deseja:"))

#CALCULANDO MORANGO
preco_morango1 = morango * 2.50
preco_morango2 = morango * 2.20

#CALCULANDO MAÇÃ
preco_maca1 = maca * 1.80
preco_maca2 = maca * 1.20

os.system("cls || clear")
#MORANGO 
if morango > 5: 
    preco_certo = preco_morango1
    print(f"Usuário comprou {morango}kg em morango, com preço equivalente R${preco_certo:.2f}")    
else:
    preco_certo = preco_morango2
    print(f"Usuário comprou {morango}kg em morango, com preço equivalente R${preco_certo:.2f}")    

#MAÇÃ
if maca > 5:
    preco_certo2 = preco_maca1
    print(f"Usuário comprou {maca}kg em maçã, com preço equivalente R${preco_certo2:.2f}")    
else: 
    preco_certo2 = preco_maca2
    print(f"Usuário comprou {maca}kg em maçã, com preço equivalente R${preco_certo2:.2f}")    

#FAZENDO TOTAL DOS PREÇOS E O TOTAL DOS KG
preco_total = preco_certo + preco_certo2
total_kg = morango + maca

if  preco_total > 25 or total_kg > 8:
    desconto = preco_total - (preco_total * 10 / 100) 
    print(f"\t||Nota fiscal||\nTotal do preço com 10% de desconto = R${desconto:.2f}")
else:
    print(f"\t||Nota fiscal||\nTotal a se pagar R${preco_total:.2f}")    
    