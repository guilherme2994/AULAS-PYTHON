
import pandas as pd
import numpy as np

# ==========================================
# 1. CARREGAMENTO DOS DADOS
# ==========================================

df = pd.read_csv("estoque_supermercado.csv")

print("BASE ORIGINAL:")
print(df.head())


# ==========================================
# 2. LIMPEZA DA COLUNA PRECO
# ==========================================

# Remover R$ e espaços em branco
df["preco"] = (
    df["preco"]
    .astype("string")
    .str.replace("R$", "", regex=False)
    .str.strip()
    .str.replace(r"\s+", "", regex=True)
)

# Converter preços para números
def converter_preco(valor):
    if pd.isna(valor):
        return np.nan

    valor = str(valor)

    # Formato brasileiro: 1.234,56
    if "," in valor:
        valor = valor.replace(".", "")
        valor = valor.replace(",", ".")

    return pd.to_numeric(valor, errors="coerce")


df["preco"] = df["preco"].apply(converter_preco)

# Preencher preços inválidos com a média
media_precos = df["preco"].mean()

df["preco"] = df["preco"].fillna(media_precos)

df["preco"] = df["preco"].astype(float)


# ==========================================
# 3. LIMPEZA DA COLUNA QUANTIDADE
# ==========================================

# Remover palavras e textos
df["quantidade"] = (
    df["quantidade"]
    .astype("string")
    .str.strip()
    .str.replace(r"[^\d,.-]", "", regex=True)
    .str.replace(",", ".", regex=False)
)

# Converter para números
df["quantidade"] = pd.to_numeric(
    df["quantidade"],
    errors="coerce"
)

# Preencher valores vazios com zero
df["quantidade"] = df["quantidade"].fillna(0)

# Converter para inteiro
df["quantidade"] = df["quantidade"].astype(int)


# ==========================================
# 4. PADRONIZAÇÃO DA COLUNA SETOR
# ==========================================

df["setor"] = (
    df["setor"]
    .fillna("sem setor")
    .astype(str)
    .str.strip()
    .str.lower()
)

# Tratar strings vazias
df["setor"] = df["setor"].replace("", "sem setor")


# ==========================================
# 5. TRATAMENTO DAS DATAS
# ==========================================

df["data_compra"] = pd.to_datetime(
    df["data_compra"],
    format="%d/%m/%Y",
    errors="coerce"
)

df["data_vencimento"] = pd.to_datetime(
    df["data_vencimento"],
    format="%d/%m/%Y",
    errors="coerce"
)


# ==========================================
# 6. EXIBIÇÃO DA BASE LIMPA
# ==========================================

print("\n--- BASE DE DADOS LIMPA ---")

print(df.head())

print("\nTIPOS DE DADOS:")
print(df.dtypes)


# ==========================================
# 7. ALERTA DE VENCIMENTO
# ==========================================

data_inicio = pd.Timestamp("2026-10-27")
data_fim = pd.Timestamp("2026-11-03")

produtos_vencendo = df[
    (df["data_vencimento"] >= data_inicio) &
    (df["data_vencimento"] <= data_fim)
]

print("\n--- PRODUTOS VENCENDO ESTA SEMANA ---")

if not produtos_vencendo.empty:
    print(
        produtos_vencendo[
            ["nome", "quantidade", "preco",
             "setor", "data_vencimento"]
        ]
    )
else:
    print("Nenhum produto vencendo nesta semana.")


# ==========================================
# 8. MAIOR QUANTIDADE A VENCER
# ==========================================

print("\n--- MAIOR QUANTIDADE A VENCER ---")

if not produtos_vencendo.empty:

    maior_quantidade = produtos_vencendo[
        "quantidade"
    ].max()

    produtos_maior_quantidade = produtos_vencendo[
        produtos_vencendo["quantidade"] == maior_quantidade
    ]

    print(produtos_maior_quantidade[
        ["nome", "quantidade", "data_vencimento"]
    ])

else:
    print("Não existem produtos vencendo nesta semana.")


# ==========================================
# 9. COMPRAS RECENTES
# ==========================================

data_compra_inicio = pd.Timestamp("2026-10-24")
data_compra_fim = pd.Timestamp("2026-10-27")

compras_recentes = df[
    (df["data_compra"] >= data_compra_inicio) &
    (df["data_compra"] <= data_compra_fim)
]

print("\n--- COMPRAS REALIZADAS NOS ÚLTIMOS 3 DIAS ---")

if not compras_recentes.empty:
    print(compras_recentes[
        ["nome", "quantidade", "data_compra"]
    ])
else:
    print("Nenhuma compra recente encontrada.")


# ==========================================
# 10. PRODUTOS SEM VENCIMENTO
# ==========================================

produtos_sem_vencimento = df[
    df["data_vencimento"].isna()
]

print("\n--- PRODUTOS SEM DATA DE VENCIMENTO ---")

if not produtos_sem_vencimento.empty:
    print(produtos_sem_vencimento[
        ["nome", "setor", "quantidade", "data_vencimento"]
    ])
else:
    print("Todos os produtos possuem data de vencimento.")


# ==========================================
# 11. VALOR PATRIMONIAL DO ESTOQUE
# ==========================================

df["valor_total_estoque"] = (
    df["preco"] * df["quantidade"]
)

valor_por_setor = (
    df.groupby("setor")["valor_total_estoque"]
    .sum()
    .sort_values(ascending=False)
)

print("\n--- VALOR PATRIMONIAL POR SETOR ---")

print(valor_por_setor)

print("\n--- SETOR COM MAIOR VALOR FINANCEIRO ---")

if not valor_por_setor.empty:

    maior_valor = valor_por_setor.max()

    setores_maior_valor = valor_por_setor[
        valor_por_setor == maior_valor
    ]

    print(setores_maior_valor)


# ==========================================
# 12. SALVAR A BASE LIMPA
# ==========================================

df.to_csv(
    "estoque_supermercado_limpo.csv",
    index=False,
    date_format="%d/%m/%Y"
)

print("\n--- PROCESSAMENTO CONCLUÍDO ---")
print("Arquivo limpo salvo com sucesso!")
