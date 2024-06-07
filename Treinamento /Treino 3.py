import os 

os.system("cls || clear")

preco = float(input("Digite o preço do produto:"))

preco_reajustado = preco - (preco * 5/100)


print(f"Preço do produto {preco}, com 10% de desconto ficaria de {preco_reajustado}")