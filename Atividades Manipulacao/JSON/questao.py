```python
import json

# ==========================================
# PARTE 1 - Criando e salvando os dados
# ==========================================

# Criando o dicionário da loja
loja = {
    "nome": "TechStore",
    "produtos": [
        {
            "nome": "Teclado Mecânico",
            "preco": 250.00,
            "quantidade": 10
        },
        {
            "nome": "Mouse Gamer",
            "preco": 150.00,
            "quantidade": 15
        },
        {
            "nome": "Monitor LED",
            "preco": 899.90,
            "quantidade": 5
        }
    ]
}

# Salvando os dados no arquivo estoque.json
with open("estoque.json", "w", encoding="utf-8") as arquivo:
    json.dump(loja, arquivo, indent=4, ensure_ascii=False)

print("Estoque inicial salvo com sucesso!")


# ==========================================
# PARTE 2 - Lendo e atualizando os dados
# ==========================================

# Lendo o arquivo estoque.json
with open("estoque.json", "r", encoding="utf-8") as arquivo:
    dados_lidos = json.load(arquivo)

# Percorrendo os produtos e exibindo nome e preço
print("\nProdutos cadastrados:")

for produto in dados_lidos["produtos"]:
    print(f"O produto {produto['nome']} custa R$ {produto['preco']:.2f}")


# Adicionando um novo produto
novo_produto = {
    "nome": "Fone de Ouvido Bluetooth",
    "preco": 199.90,
    "quantidade": 20
}

dados_lidos["produtos"].append(novo_produto)


# ==========================================
# DESAFIO EXTRA - Desconto de 10%
# ==========================================

# Aplicando 10% de desconto no Monitor LED
for produto in dados_lidos["produtos"]:
    if produto["nome"] == "Monitor LED":
        produto["preco"] *= 0.90


# Salvando os dados atualizados no arquivo
with open("estoque.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados_lidos, arquivo, indent=4, ensure_ascii=False)

print("\nEstoque atualizado com sucesso!")

# Exibindo os produtos após a atualização
print("\nEstoque atualizado:")

for produto in dados_lidos["produtos"]:
    print(
        f"Produto: {produto['nome']} | "
        f"Preço: R$ {produto['preco']:.2f} | "
        f"Quantidade: {produto['quantidade']}"
    )

{
    "nome": "TechStore",
    "produtos": [
        {
            "nome": "Teclado Mecânico",
            "preco": 250.0,
            "quantidade": 10
        },
        {
            "nome": "Mouse Gamer",
            "preco": 150.0,
            "quantidade": 15
        },
        {
            "nome": "Monitor LED",
            "preco": 809.91,
            "quantidade": 5
        },
        {
            "nome": "Fone de Ouvido Bluetooth",
            "preco": 199.9,
            "quantidade": 20
        }
    ]
}