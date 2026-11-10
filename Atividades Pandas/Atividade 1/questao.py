import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv('funcionarios.csv', sep=";")

# 1. Todos os salários menores do que 3000, maiores do que 5000 e iguais a 3100
# Nota: Supondo que a coluna se chame 'salario' e que o critério aceite qualquer uma dessas condições (OU / |)
filtro_salarios = df[(df['salario'] < 3000) | (df['salario'] > 5000) | (df['salario'] == 3100)]

# 2. Todos os cargos de Analista de Dados, Analista de Sistemas, Desenvolvedor Java e Cientista de dados
cargos_desejados = ['Analista de Dados', 'Analista de Sistemas', 'Desenvolvedor Java', 'Cientista de dados']
filtro_cargos = df[df['cargo'].isin(cargos_desejados)]

# 3. Listar os nomes e cargos de quem tem um salário maior do que 6000
nomes_cargos_salario_6000 = df[df['salario'] > 6000][['nome', 'cargo']]

# 4. Listar todos os funcionários com ID par
filtro_id_par = df[df['id'] % 2 == 0]


# --- Imprimir todos os dados na tela em uma única execução ---

print("="*60)
print("1. SALÁRIOS (< 3000, > 5000 OU == 3100):")
print("="*60)
print(filtro_salarios)

print("\n" + "="*60)
print("2. CARGOS ESPECÍFICOS:")
print("="*60)
print(filtro_cargos)

print("\n" + "="*60)
print("3. NOMES E CARGOS COM SALÁRIO > 6000:")
print("="*60)
print(nomes_cargos_salario_6000)

print("\n" + "="*60)
print("4. FUNCIONÁRIOS COM ID PAR:")
print("="*60)
print(filtro_id_par)
