import pandas as pd

# 1. Ler o arquivo original
df = pd.read_csv('funcionarios.csv')

# 2. Filtrar funcionários com salário > 6000 e salvar em 'cargos_altos.csv'
df_cargos_altos = df[df['salario'] > 6000]
df_cargos_altos.to_csv('cargos_altos.csv', index=False)

# 3. Cadastrar novos funcionários com cargos inéditos
novos_funcionarios = pd.DataFrame([
    {'id': 101, 'nome': 'Carlos Silva', 'salario': 7500.0, 'cargo': 'Arquiteto de Software'},
    {'id': 102, 'nome': 'Mariana Souza', 'salario': 5200.0, 'cargo': 'Engenheira de Dados'}
])
df = pd.concat([df, novos_funcionarios], ignore_index=True)

# 4. Remover os dois primeiros funcionários (índices 0 e 1)
df = df.drop(index=[0, 1]).reset_index(drop=True)

# 5. Criar a coluna 'tempo_empresa' em meses (int)
# Atribui valores inteiros para as linhas existentes na DataFrame
df['tempo_empresa'] = [12, 24, 36, 18, 6][:len(df)]  # Ajuste os valores conforme o total de registros
df['tempo_empresa'] = df['tempo_empresa'].astype(int)

# 6. Adicionar um novo funcionário com o cargo de 'Estagiário' e tempo de empresa como int
estagiario = pd.DataFrame([{
    'id': 103,
    'nome': 'Lucas Pereira',
    'salario': 2000.0,
    'cargo': 'Estagiário',
    'tempo_empresa': int(3)
}])
df = pd.concat([df, estagiario], ignore_index=True)

# 7. Salvar as alterações no arquivo 'funcionarios.csv'
df.to_csv('funcionarios.csv', index=False)

# 8. Conferir os resultados
print("--- Conteúdo final de 'funcionarios.csv' ---")
print(df)

print("\n--- Conteúdo de 'cargos_altos.csv' ---")
print(pd.read_csv('cargos_altos.csv'))
