# Crie uma lista que ela armazene um numero x de funcionarios. Usando o "while", adicione quantos funcionarios quiser.
# Com o "for", voce ira imprimir duas listas:
# Uma lista com todos os funcionários que receberão um aumento;
# Outra lista, com todos os funcionarios que serao demitidos.
# Voce irá decidir qual funcionário será demitido ou recebera aumento pelo "index" do funcionário lista [].

funcionarios = []

while True:
    nome = input("Digite o funcionário: ")

    if nome == "sair":
        break

    funcionarios.append(nome)


aumento = [0, 2]
demissao = [1, 3]

lista_aumento = []
lista_demissao = []


for index in range(len(funcionarios)):

    print("Índice:", index, "Funcionário:", funcionarios[index])

    if index in aumento:
        lista_aumento.append(funcionarios[index])

    elif index in demissao:
        lista_demissao.append(funcionarios[index])


print("Aumento:", lista_aumento)
print("Demissão:", lista_demissao)
