import os 

os.system("cls || clear")

while True:
 os.system("cls || clear")
 print("1- Verde\n2- Azul\n3- Amarelo\n4- Vermelho")
 opcao = int(input("Escolha uma cor:"))
 
 match (opcao):
    case 1:
        print("Verde R$10,00")
        break
    case 2:    
        print("Azul R$20,00")
        break
    case 3:
        print("Amarelo R$30,00") 
        break
    case 4:
        print("Vermelho R$40,00") 
        break
    case _:
        input("Opção escolhida, inválida.")         