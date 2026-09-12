# Crie uma única função que receba como parâmetro o nome de um aluno, sua nota do primeiro, segundo, terceiro e quarto bimestre.
# Sua função deve calcular a média final desse aluno, e imprimir na tela todos os valores, e informar se o aluno foi reprovado ou aprovado pela média final.

def aluno(nome, nota1, nota2, nota3, nota4):
    media = (nota1 + nota2 + nota3 + nota4) / 4

    print(f"Aluno: {nome}")
    print(f"Nota do 1º bimestre: {nota1}")
    print(f"Nota do 2º bimestre: {nota2}")
    print(f"Nota do 3º bimestre: {nota3}")
    print(f"Nota do 4º bimestre: {nota4}")
    print(f"Média final: {media:.2f}")

    if media >= 7:
        print("Situação: APROVADO, NÃO FEZ MAIS QUE A SUA OBRIGAÇÃO!")
    else:
        print("Situação: REPROVADO")


aluno("João", 8, 7, 9, 6)
