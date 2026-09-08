codigo = int(input("Digite o código do produto (1 a 4): "))

match codigo:
    case 1:
        print("Cachorro-quente - R$ 10,00")
    case 2:
        print("Hambúrguer - R$ 15,00")
    case 3:
        print("Batata Frita - R$ 8,00")
    case 4:
        print("Refrigerante - R$ 5,00")
    case _:
        print("Código inválido")
