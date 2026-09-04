idade = int(input("Digite sua idade: "))
vip = int(input("Possui convite VIP? Digite 1 para Sim ou 0 para Não: "))
organizador = int(input("É organizador? Digite 1 para Sim ou 0 para Não: "))

if idade >= 18 and vip == 1 or organizador == 1:
    print("Entrada PERMITIDA! Seja bem-vindo(a)")
else:
    print("Entrada NEGADA! Você não atende aos requisitos")
