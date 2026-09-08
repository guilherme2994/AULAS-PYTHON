letra = input("Digite uma letra: ")

match letra:
    case "a" | "e" | "i" | "o" | "u":
        print("Você digitou uma vogal.")
    case _:
        print("Não é uma vogal.")
