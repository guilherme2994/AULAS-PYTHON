nome = input("Nome do aluno: ")
turma = input("Turma: ")

try:
    nota1 = float(input("Nota do 1º bimestre: "))
    nota2 = float(input("Nota do 2º bimestre: "))
    nota3 = float(input("Nota do 3º bimestre: "))
    nota4 = float(input("Nota do 4º bimestre: "))

    media = (nota1 + nota2 + nota3 + nota4) / 4

    if media >= 7.0:
        status = "Aprovado"
    else:
        status = "Reprovado"

    with open("alunos.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(
            f"{nome};{turma};{nota1};{nota2};{nota3};{nota4};{status}\n"
        )

    print(f"\nAluno {nome} adicionado com sucesso!")
    print(f"Média: {media:.2f}")
    print(f"Status: {status}")

except ValueError:
    print("\nErro: digite apenas números válidos para as notas.")
