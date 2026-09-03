#Questão 1: A Divisão da Conta (Calculadora)

#Crie um programa para um restaurante que funciona como uma calculadora de divisão de conta.
#O sistema deve solicitar ao usuário o valor total da conta (ex: 150.00) e a quantidade de pessoas na mesa.
#O programa deve calcular o valor que cada um deve pagar e exibir a mensagem:
#"O valor total foi de R$ [Total], e cada pessoa deve pagar R$ [Valor Dividido]".

total = int(input("Digite o valor total da conta: R$ "))
pessoas = int(input("Digite a quantidade de pessoas: "))

valor_por_pessoa = total / pessoas

print("O valor total foi de: R$" , total, "cada pessoa deve pagar R$" ,valor_por_pessoa)
