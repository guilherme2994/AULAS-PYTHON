#Questão 3: A Catraca do Parque (Operadores de Comparação)

#Para entrar na montanha-russa, a criança precisa ter no mínimo 1.40m de altura.
#Crie um formulário que pergunte a altura da criança em metros (ex: 1.35).
#O programa deve verificar se a altura é maior ou igual a 1.40 e imprimir o resultado da comparação na tela
#(True se puder entrar, False se não puder).

altura = float(input("Digite a altura da criança em metros: "))

pode_entrar = altura >= 1.40

print(pode_entrar)