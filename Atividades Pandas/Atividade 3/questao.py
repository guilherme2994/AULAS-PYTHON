
import pandas as pd

# 1. Ler o arquivo CSV original
df = pd.read_csv("funcionarios.csv")

print("DADOS ORIGINAIS:")
print(df)

# 2. Criar arquivo somente com funcionários que ganham acima de 6000
cargos_altos = df[df["salario"] > 6000]
cargos_altos.to_csv("cargos_altos.csv", index=False)

print("\nFUNCIONÁRIOS COM SALÁRIO ACIMA DE 6000:")
print(cargos_altos)

# 3. Cadastrar novos funcionários com cargos diferentes
novos_funcionarios = pd.DataFrame([
    {"id": 10, "nome": "Carlos", "salario": 7500, "cargo": "Analista"},
    {"id": 11, "nome": "Mariana", "salario": 8200, "cargo": "Coordenadora"},
    {"id": 12, "nome": "Roberto", "salario": 6800, "cargo": "Designer"}
])

df = pd.concat([df, novos_funcionarios], ignore_index=True)

# 4. Remover os dois primeiros funcionários (índices 0 e 1)
df = df.drop(index=[0, 1]).reset_index(drop=True)

# 5. Criar a coluna tempo_empresa com valores inteiros
df["tempo_empresa"] = [12, 24, 36, 18, 30, 10, 8, 6, 14, 20, 16]

# 6. Adicionar um funcionário Estagiário
estagiario = pd.DataFrame([{
    "id": 13,
    "nome": "Pedro",
    "salario": 1800,
    "cargo": "Estagiário",
    "tempo_empresa": 3
}])

df = pd.concat([df, estagiario], ignore_index=True)

# Garantir que tempo_empresa seja do tipo inteiro
df["tempo_empresa"] = df["tempo_empresa"].astype(int)

# 7. Salvar o arquivo atualizado
df.to_csv("funcionarios.csv", index=False)

# 8. Conferir os dados finais
print("\nDADOS ATUALIZADOS:")
print(df)

print("\nTIPO DA COLUNA tempo_empresa:")
print(df["tempo_empresa"].dtype)

print("\nARQUIVOS SALVOS COM SUCESSO!")
