import os 

os.system("cls || clear")

preco = float(input("Digite o preço do produto: R$"))

preco_reajustado = preco - (preco * 5/100)


print(f"Preço do produto R${preco:.2f}, com 10% de desconto ficaria de R${preco_reajustado:.2f}")