import os 

os.system("cls || clear")

#SOLICITANDO DADOS 
morango = int(input("Quantos (kg) de morango você deseja:"))
maca = int(input("Quantos (kg) de maçã você deseja:"))


os.system("cls || clear")


#MORANGO 
if morango <= 5: 
    preco_morango = morango * 2.50
    
else:
    preco_morango = morango * 2.20
     
#MAÇÃ
if maca <= 5:
    preco_maca = maca * 1.80
    
else: 
    preco_maca = maca * 1.20


#FAZENDO TOTAL DOS PREÇOS E O TOTAL DOS KG
total = preco_morango + preco_maca
total_kg = morango + maca


if  total > 25 or total_kg > 8:
    desconto = total - (total * 10 / 100) 

    print(f"\t||Nota fiscal||\nPreço de morango R${preco_morango:.2f}\nPreço da maçã R${preco_maca:.2f}")
    print(f"Total do preço com 10% de desconto = R${desconto:.2f}")

else:
    print(f"\t||Nota fiscal||\nPreço de morango R${preco_morango:.2f}\nPreço da maçã R${preco_maca:.2f}\nTotal a se pagar R${preco_total:.2f}")    
    