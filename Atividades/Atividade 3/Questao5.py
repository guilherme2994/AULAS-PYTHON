#Questão 5: O Sistema de Desconto (Lógica OR)

# Uma loja está em promoção:
# o cliente ganha frete grátis se o valor da compra for maior que R$ 200.00 OU se ele possuir o cartão VIP da loja.
# Peça ao usuário o valor da compra e pergunte se ele é VIP (peça para digitar 1 para "Sim, sou VIP" ou 0 para "Não sou VIP").
# Crie a lógica usando o operador or e imprima True se ele tem direito ao frete grátis ou False caso não tenha.

# Entrada de dados
valor_compra = float(input("Digite o valor da compra (R$): "))
opcao_vip = int(input("Você possui o cartão VIP? (1 para Sim / 0 para Não): "))

# Conversão da opção digitada para um valor booleano (True/False)
sou_vip = opcao_vip == 1

# Lógica com o operador OR
frete_gratis = (valor_compra > 200.0) or sou_vip

# Exibição do resultado
print(frete_gratis)