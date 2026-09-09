# QUESTÃO 3 - SOMADOR DE NÚMEROS

soma = 0

numero = int(input("Digite um número inteiro (0 para encerrar): "))

while numero != 0:
    soma = soma + numero
    numero = int(input("Digite outro número inteiro (0 para encerrar): "))

print("A soma dos números digitados é:", soma)
