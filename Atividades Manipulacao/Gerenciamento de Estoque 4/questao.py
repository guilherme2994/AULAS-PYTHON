import json

# PARTE 1: Criando e Salvando os Dados

# 1. Criação do dicionário 'loja'
loja = {
    "nome": "TechStore",
    "produtos": [
        {"nome": "Teclado Mecânico", "preco": 250.00, "quantidade": 15},
        {"nome": "Mouse Gamer", "preco": 120.00, "quantidade": 30},
        {"nome": "Monitor 24''", "preco": 850.00, "quantidade": 8}
    ]
}

# 2. Salvando o dicionário no arquivo 'estoque.json'
with open("estoque.json", "w", encoding="utf-8") as arquivo:
    json.dump(loja, arquivo, indent=4, ensure_ascii=False)

print("Dados iniciais salvos com sucesso no estoque.json!\n")

# PARTE 2: Lendo e Atualizando os Dados

# 1. Leitura do arquivo 'estoque.json'
with open("estoque.json", "r", encoding="utf-8") as arquivo:
    dados_lidos = json.load(arquivo)

# 2. Imprimindo nome e preço de cada produto
print(f"--- Produtos da loja {dados_lidos['nome']} ---")
for produto in dados_lidos["produtos"]:
    print(f"O produto {produto['nome']} custa R$ {produto['preco']:.2f}")

# 3. Adicionando um novo produto à lista
novo_produto = {
    "nome": "Fone Bluetooth",
    "preco": 200.00,
    "quantidade": 20
}
dados_lidos["produtos"].append(novo_produto)

# DESAFIO EXTRA (Opcional)

# Aplicando 10% de desconto no preço de um produto (exemplo: Mouse Gamer)
for produto in dados_lidos["produtos"]:
    if produto["nome"] == "Mouse Gamer":
        produto["preco"] = round(produto["preco"] * 0.90, 2)
        print(f"\n[DESCONTO APLICADO] Novo preço do {produto['nome']}: R$ {produto['preco']:.2f}")


# 4. Salvando o dicionário 'dados_lidos' atualizado no 'estoque.json'
with open("estoque.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados_lidos, arquivo, indent=4, ensure_ascii=False)

print("\nArquivo 'estoque.json' atualizado com sucesso!")