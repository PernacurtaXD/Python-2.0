import os


os.system("cls || clear")
nome = input("Digite o nome do produto:")
quantidade_adquirida = int(input("Digite a quantidade adquirida:"))
preco_unitario = float(input("Qual é o preço do produto?"))

os.system("cls || clear")

#Desconto de 2%
if quantidade_adquirida <= 5:
 total = quantidade_adquirida * preco_unitario
 desconto = total - (total * 2/100)

 
 print(f"Usuário comprou um {nome} de R${preco_unitario:.2f}\nQuantidade = {quantidade_adquirida}")
 print(f"Total pagar com 2% de desconto R${desconto:.2f}")

#Desconto 3%
if quantidade_adquirida <= 10:
 total = quantidade_adquirida * preco_unitario
 desconto = total - (total * 3/100)


 print(f"Usuário comprou um {nome} de R${preco_unitario:.2f}\nQuantidade = {quantidade_adquirida}")
 print(f"Total pagar com 3% de desconto R${desconto:.2f}")

 #Desconto 5%
if quantidade_adquirida > 10:
   total = quantidade_adquirida * preco_unitario
   desconto = total - (total * 5/100)
   

   print(f"Usuário comprou um {nome} de R${preco_unitario:.2f}\nQuantidade = {quantidade_adquirida}")
   print(f"Total pagar com 5% de desconto R${desconto:.2f}")