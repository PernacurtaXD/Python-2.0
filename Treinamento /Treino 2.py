import os 

os.system("cls || clear")
salario = 1412.00


salario_Atual = float(input("Quanto de salário você ganha? R$: "))

salario_cal = salario_Atual / salario

print(f"Quantidade do salário minímo que você possui R$: {salario_cal:.4f}")