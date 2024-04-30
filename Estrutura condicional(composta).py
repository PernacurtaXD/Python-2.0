import os 

os.system("cls || clear")

peso = float (input("Digite seu peso:"))


if peso < 40:
    print(f"Magro")
elif peso < 80:
    print(f"Normal")
else:
    print(f"ACIMA DO PESO")