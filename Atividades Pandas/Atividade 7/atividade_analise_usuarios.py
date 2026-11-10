import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Buscar os 100 usuários da API
url = "https://dummyjson.com/users?limit=100"
resposta = requests.get(url, timeout=30)
resposta.raise_for_status()
dados_json = resposta.json()

# 2. Criar o DataFrame com as 9 colunas da atividade
df_completo = pd.DataFrame(dados_json["users"])

colunas = [
    "firstName", "age", "bloodGroup",
    "height", "weight", "eyeColor", "role",
    "university", "birthDate"
]
df = df_completo[colunas].copy()

# Garantir que as colunas numéricas e as datas estejam nos formatos corretos
df["age"] = pd.to_numeric(df["age"], errors="coerce")
df["height"] = pd.to_numeric(df["height"], errors="coerce")
df["weight"] = pd.to_numeric(df["weight"], errors="coerce")
df["birthDate"] = pd.to_datetime(df["birthDate"], errors="coerce")

print("\nTOTAL DE USUÁRIOS:", len(df))
print("COLUNAS:", df.columns.to_list())


# ---------------------------------------------------------
# 1. DISTRIBUIÇÃO DE TIPOS SANGUÍNEOS
# ---------------------------------------------------------
tipos_sanguineos = df["bloodGroup"].value_counts().sort_index()
porcentagens_sangue = df["bloodGroup"].value_counts(normalize=True).sort_index() * 100

print("\n1. QUANTIDADE POR TIPO SANGUÍNEO")
print(tipos_sanguineos)
print("\nPORCENTAGEM POR TIPO SANGUÍNEO")
print(porcentagens_sangue.round(2).astype(str) + "%")

plt.figure(figsize=(8, 6))
plt.pie(
    tipos_sanguineos.values,
    labels=tipos_sanguineos.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Distribuição dos tipos sanguíneos")
plt.axis("equal")
plt.tight_layout()
plt.savefig("grafico_01_tipos_sanguineos.png", dpi=150)
plt.show()


# ---------------------------------------------------------
# 2. ANÁLISE E FILTROS DE IDADE
# ---------------------------------------------------------
jovens = (df["age"] < 30).sum()
trinta_ou_mais = (df["age"] >= 30).sum()

print("\n2. FAIXAS ETÁRIAS")
print(f"Jovens (abaixo de 30 anos): {jovens}")
print(f"30 anos ou mais: {trinta_ou_mais}")

plt.figure(figsize=(8, 5))
plt.hist(df["age"].dropna(), bins=10, edgecolor="black")
plt.title("Distribuição das idades dos usuários")
plt.xlabel("Idade")
plt.ylabel("Quantidade de pessoas")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig("grafico_02_idades.png", dpi=150)
plt.show()


# ---------------------------------------------------------
# 3. CARACTERÍSTICAS FÍSICAS: COR DOS OLHOS
# ---------------------------------------------------------
cores_olhos = df["eyeColor"].value_counts().sort_values(ascending=False)

print("\n3. QUANTIDADE POR COR DOS OLHOS")
print(cores_olhos)
print(f"Mais comum: {cores_olhos.idxmax()} ({cores_olhos.max()} pessoas)")
print(f"Menos comum: {cores_olhos.idxmin()} ({cores_olhos.min()} pessoas)")

plt.figure(figsize=(8, 5))
cores_olhos.plot(kind="bar", edgecolor="black")
plt.title("Ranking das cores dos olhos")
plt.xlabel("Cor dos olhos")
plt.ylabel("Quantidade de usuários")
plt.xticks(rotation=35, ha="right")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig("grafico_03_cores_olhos.png", dpi=150)
plt.show()


# ---------------------------------------------------------
# 4. RELAÇÃO DE MEDIDAS CORPORAIS: ALTURA X PESO
# ---------------------------------------------------------
correlacao = df["height"].corr(df["weight"])
print("\n4. RELAÇÃO ENTRE ALTURA E PESO")
print(f"Correlação entre altura e peso: {correlacao:.2f}")

if correlacao > 0.3:
    print("Existe uma tendência positiva: pessoas mais altas tendem a pesar mais.")
elif correlacao < -0.3:
    print("Existe uma tendência negativa: pessoas mais altas tendem a pesar menos.")
else:
    print("A relação linear entre altura e peso é fraca ou pouco evidente.")

plt.figure(figsize=(8, 5))
plt.scatter(df["height"], df["weight"], alpha=0.7)
plt.title("Relação entre altura e peso")
plt.xlabel("Altura (cm)")
plt.ylabel("Peso (kg)")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("grafico_04_altura_peso.png", dpi=150)
plt.show()


# ---------------------------------------------------------
# 5. DISTRIBUIÇÃO DE CARGOS (ROLES)
# ---------------------------------------------------------
cargos = df["role"].value_counts()

print("\n5. QUANTIDADE DE USUÁRIOS POR CARGO")
print(cargos)

plt.figure(figsize=(7, 6))
plt.pie(
    cargos.values,
    labels=cargos.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Distribuição dos cargos")
plt.axis("equal")
plt.tight_layout()
plt.savefig("grafico_05_cargos.png", dpi=150)
plt.show()


# ---------------------------------------------------------
# 6. MÉDIA DE ALTURA POR CARGO
# ---------------------------------------------------------
media_altura_cargo = df.groupby("role")["height"].mean().sort_values(ascending=False)

print("\n6. MÉDIA DE ALTURA POR CARGO (cm)")
print(media_altura_cargo.round(2))
print(
    f"Grupo com maior média de altura: {media_altura_cargo.idxmax()} "
    f"({media_altura_cargo.max():.2f} cm)"
)

plt.figure(figsize=(8, 5))
media_altura_cargo.plot(kind="bar", edgecolor="black")
plt.title("Média de altura por cargo")
plt.xlabel("Cargo")
plt.ylabel("Altura média (cm)")
plt.xticks(rotation=0)
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig("grafico_06_altura_por_cargo.png", dpi=150)
plt.show()


# ---------------------------------------------------------
# 7. TOP 5 UNIVERSIDADES
# ---------------------------------------------------------
top_universidades = df["university"].value_counts().head(5)

print("\n7. TOP 5 UNIVERSIDADES")
print(top_universidades)

plt.figure(figsize=(9, 5))
top_universidades.sort_values().plot(kind="barh", edgecolor="black")
plt.title("Top 5 universidades com mais usuários")
plt.xlabel("Quantidade de usuários")
plt.ylabel("Universidade")
plt.grid(axis="x", alpha=0.3)
plt.tight_layout()
plt.savefig("grafico_07_top_universidades.png", dpi=150)
plt.show()


# ---------------------------------------------------------
# 8. CONCENTRAÇÃO DE PESO
# ---------------------------------------------------------
faixa_peso = pd.cut(
    df["weight"],
    bins=[0, 50, 60, 70, 80, 90, 100, np.inf],
    right=False,
    labels=["Abaixo de 50", "50 a 59,9", "60 a 69,9",
            "70 a 79,9", "80 a 89,9", "90 a 99,9", "100 ou mais"]
)
contagem_faixa_peso = faixa_peso.value_counts().sort_index()

print("\n8. QUANTIDADE POR FAIXA DE PESO (kg)")
print(contagem_faixa_peso)
print(
    "Faixa com maior concentração:",
    contagem_faixa_peso.idxmax(),
    f"({contagem_faixa_peso.max()} pessoas)"
)
print("\nResumo estatístico do peso (kg):")
print(df["weight"].describe().round(2))

plt.figure(figsize=(8, 5))
plt.hist(df["weight"].dropna(), bins=10, edgecolor="black")
plt.title("Distribuição do peso dos usuários")
plt.xlabel("Peso (kg)")
plt.ylabel("Quantidade de pessoas")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig("grafico_08_pesos.png", dpi=150)
plt.show()


# ---------------------------------------------------------
# 9. PESO ACIMA DE 75 KG E TIPO SANGUÍNEO O+
# ---------------------------------------------------------
condicao = (df["weight"] > 75) & (df["bloodGroup"] == "O+")
quantidade_condicao = condicao.sum()
restante = len(df) - quantidade_condicao

print("\n9. PESO ACIMA DE 75 KG E TIPO SANGUÍNEO O+")
print(f"Atendem às duas condições: {quantidade_condicao}")
print(f"Restante dos usuários: {restante}")

plt.figure(figsize=(7, 5))
plt.bar(
    ["Mais de 75 kg e O+", "Restante"],
    [quantidade_condicao, restante],
    edgecolor="black"
)
plt.title("Usuários com peso acima de 75 kg e sangue O+")
plt.ylabel("Quantidade de pessoas")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig("grafico_09_peso_e_sangue.png", dpi=150)
plt.show()


# ---------------------------------------------------------
# 10. SAZONALIDADE DE NASCIMENTOS
# ---------------------------------------------------------
meses_nomes = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]
nascimentos_mes = (
    df["birthDate"].dt.month
    .value_counts()
    .reindex(range(1, 13), fill_value=0)
    .sort_index()
)
nascimentos_mes.index = meses_nomes

print("\n10. NASCIMENTOS POR MÊS")
print(nascimentos_mes)
mes_mais_aniversarios = nascimentos_mes.idxmax()
quantidade_aniversarios = nascimentos_mes.max()
print(
    f"Mês com mais aniversariantes: {mes_mais_aniversarios} "
    f"({quantidade_aniversarios} pessoas)"
)

plt.figure(figsize=(10, 5))
plt.plot(
    nascimentos_mes.index,
    nascimentos_mes.values,
    marker="o"
)
plt.title("Quantidade de nascimentos por mês")
plt.xlabel("Mês")
plt.ylabel("Quantidade de usuários")
plt.xticks(rotation=35, ha="right")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("grafico_10_nascimentos_por_mes.png", dpi=150)
plt.show()


print("\nATIVIDADE CONCLUÍDA!")
print("Foram salvos 10 gráficos PNG na mesma pasta deste programa.")
