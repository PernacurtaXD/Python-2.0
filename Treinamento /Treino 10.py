def contar_acertos(tipo_cha, respostas):
    return respostas.count(tipo_cha)


tipo_cha = int(input())
respostas = list(map(int, input().split()))


print(contar_acertos(tipo_cha, respostas))

