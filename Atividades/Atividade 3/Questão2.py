#Questão 2: A Fábrica de Caixas (Operador de Módulo)

#Uma fábrica empacota maçãs em caixas que cabem exatamente 12 unidades.
#Crie um programa que pergunte ao usuário a quantidade total de maçãs colhidas no dia.
#Utilizando o operador de módulo (%), calcule e exiba na tela quantas maçãs sobrarão fora das caixas
#(ou seja, o resto da divisão por 12).

macas = int(input("Digite a quantidade total de maçãs colhidas: "))

sobras = macas % 12

print("Quantidade de maçãs que sobrarão fora das caixas: ", sobras)