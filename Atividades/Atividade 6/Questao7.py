orcamento = 500

while orcamento > 0:
    gasto = float(input("Digite o valor do gasto: "))

    orcamento -= gasto

    print("Saldo restante: R$", orcamento)

print("Atenção: Você ficou sem saldo ou estourou seu orçamento!")
