saldo = float(input("Digite seu saldo: "))
saque = float(input("Digite o valor que deseja sacar: "))

if saque <= saldo:
    saldo = saldo - saque
    print("Saque realizado com sucesso! Saldo atual: R$", saldo)
else:
    print("Saldo insuficiente para realizar esta operação")
