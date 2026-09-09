numero_secreto = 14
tentativas = 0

palpite = int(input("Digite seu palpite: "))
tentativas += 1

while palpite != numero_secreto:
    print("Você errou! Tente novamente.")
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1

print("Parabéns! Você acertou o número secreto em", tentativas, "tentativas!")
