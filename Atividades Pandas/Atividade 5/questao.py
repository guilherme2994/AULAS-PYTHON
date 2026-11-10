
import pandas as pd
import numpy as np

# ==========================================
# 1. CARREGAR OS DADOS
# ==========================================

df = pd.read_csv("vendas_mercados.csv", encoding="utf-8-sig")

print("========== BASE DE VENDAS ==========")
print(df.head())

# Garantir que as colunas numéricas sejam números
colunas_numericas = [
    "Quantidade",
    "Preco_Unitario",
    "Custo_Unitario"
]

for coluna in colunas_numericas:
    df[coluna] = pd.to_numeric(
        df[coluna],
        errors="coerce"
    )

# ==========================================
# QUESTÃO 1 - MAIOR LUCRO POR MERCADO
# ==========================================

# Lucro = (Preço - Custo) * Quantidade
df["Lucro"] = (
    (df["Preco_Unitario"] - df["Custo_Unitario"])
    * df["Quantidade"]
)

lucro_mercado = df.groupby("Mercado")["Lucro"].sum()

print("\n========== QUESTÃO 1 ==========")
print("LUCRO TOTAL POR MERCADO:")
print(lucro_mercado.sort_values(ascending=False))

maior_lucro = lucro_mercado.idxmax()

print("\nMercado com maior lucro:")
print(maior_lucro)

print(
    "Lucro total: R$",
    round(lucro_mercado.max(), 2)
)

# ==========================================
# QUESTÃO 2 - FORMA DE PAGAMENTO POR REGIÃO
# ==========================================

pagamentos = pd.crosstab(
    df["Regiao"],
    df["Forma_Pagamento"]
)

print("\n========== QUESTÃO 2 ==========")
print("QUANTIDADE DE PAGAMENTOS POR REGIÃO:")
print(pagamentos)

pagamento_mais_usado = pagamentos.idxmax(axis=1)

print("\nFORMA DE PAGAMENTO MAIS UTILIZADA:")
print(pagamento_mais_usado)

# ==========================================
# QUESTÃO 3 - PRODUTO MAIS E MENOS VENDIDO
# ==========================================

vendas_produtos = df.groupby("Produto")[
    "Quantidade"
].sum().sort_values(ascending=False)

print("\n========== QUESTÃO 3 ==========")
print("TOTAL DE ITENS VENDIDOS POR PRODUTO:")
print(vendas_produtos)

produto_mais_vendido = vendas_produtos.idxmax()
produto_menos_vendido = vendas_produtos.idxmin()

print("\nProduto mais vendido:")
print(produto_mais_vendido)
print("Quantidade:", vendas_produtos.max())

print("\nProduto menos vendido:")
print(produto_menos_vendido)
print("Quantidade:", vendas_produtos.min())

# ==========================================
# QUESTÃO 4 - MÉDIA DE PREÇOS POR MERCADO
# ==========================================

media_precos = df.groupby("Mercado")[
    "Preco_Unitario"
].mean().sort_values(ascending=False)

print("\n========== QUESTÃO 4 ==========")
print("MÉDIA DE PREÇOS POR MERCADO:")
print(media_precos.round(2))

print("\nCLASSIFICAÇÃO DOS MERCADOS:")

for posicao, (mercado, media) in enumerate(
    media_precos.items(), start=1
):
    print(
        f"{posicao}º lugar - {mercado}: "
        f"R$ {media:.2f}"
    )

print("\nMercado com produtos mais caros:")
print(media_precos.idxmax())

print("\nMercado com produtos mais baratos:")
print(media_precos.idxmin())

# ==========================================
# QUESTÃO 5 - FATURAMENTO TOTAL
# ==========================================

# Faturamento = Preço Unitário * Quantidade
df["Faturamento"] = (
    df["Preco_Unitario"] * df["Quantidade"]
)

faturamento_total = df["Faturamento"].sum()

faturamento_mercado = df.groupby("Mercado")[
    "Faturamento"
].sum().sort_values(ascending=False)

print("\n========== QUESTÃO 5 ==========")
print("FATURAMENTO TOTAL DA REDE:")
print(f"R$ {faturamento_total:.2f}")

print("\nFATURAMENTO POR MERCADO:")
print(faturamento_mercado.round(2))

print("\nMercado com maior faturamento:")
print(faturamento_mercado.idxmax())

print(
    "Valor: R$",
    round(faturamento_mercado.max(), 2)
)

# ==========================================
# QUESTÃO 6 - SIMULAÇÃO DE PROMOÇÃO
# ==========================================

# Desconto de 10% para compras com quantidade >= 10
df["Preco_Promocional"] = np.where(
    df["Quantidade"] >= 10,
    df["Preco_Unitario"] * 0.90,
    df["Preco_Unitario"]
)

# Calcular faturamento com desconto
df["Faturamento_Promocional"] = (
    df["Preco_Promocional"] * df["Quantidade"]
)

novo_faturamento = df[
    "Faturamento_Promocional"
].sum()

print("\n========== QUESTÃO 6 ==========")

print("FATURAMENTO ORIGINAL:")
print(f"R$ {faturamento_total:.2f}")

print("\nNOVO FATURAMENTO COM PROMOÇÃO:")
print(f"R$ {novo_faturamento:.2f}")

print("\nDESCONTO TOTAL CONCEDIDO:")
print(f"R$ {faturamento_total - novo_faturamento:.2f}")

# ==========================================
# SALVAR RESULTADOS
# ==========================================

df.to_csv(
    "vendas_mercados_analisado.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\n========== FINALIZAÇÃO ==========")
print("Análise concluída com sucesso!")
print("Arquivo vendas_mercados_analisado.csv salvo.")
