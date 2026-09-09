# QUESTÃO 4 - MENU INTERATIVO

opcao = 0

while opcao != 2:
    print("\n===== MENU =====")
    print("1 - Mostrar saudação")
    print("2 - Sair do programa")

    opcao = int(input("Digite uma opção: "))

    if opcao == 1:
        print("Olá, seja muito bem-vindo(a)!")
    elif opcao != 2:
        print("Opção inválida!")

print("Programa encerrado.")
