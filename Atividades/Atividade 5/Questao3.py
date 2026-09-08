turno = input("Digite o turno em que você estuda (M, V ou N): ")

match turno:
    case "M" | "m":
        print("Bom Dia!")
    case "V" | "v":
        print("Boa Tarde!")
    case "N" | "n":
        print("Boa Noite!")
    case _:
        print("Turno inválido!")
