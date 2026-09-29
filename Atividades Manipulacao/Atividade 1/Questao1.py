# Sistema de Carrinho de Compras e Pagamento

# 1. Solicitando nome do usuário
usuario = input("Digite seu nome para iniciar a compra: ")

# Lista que armazenará os produtos e preços
produtos = []
total = 0.0

# 2. Loop de inserção de produtos no carrinho
while True:
    produto = input("Digite o nome do produto (ou 'fim' para finalizar): ")

    # Condição de parada
    if produto.lower() == "fim":
        break

    preco = float(input(f"Digite o preço de {produto}: R$ "))

    # Guarda o produto e o preço na lista
    produtos.append([produto, preco])

    # Soma o preço ao total
    total += preco

# 3. Geração do arquivo pagamento.txt
print("\n--- FINALIZANDO COMPRA ---")

with open("pagamento.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("===== RECIBO DE COMPRA =====\n")
    arquivo.write(f"Cliente: {usuario}\n\n")

    arquivo.write("Produtos:\n")

    for produto, preco in produtos:
        arquivo.write(f"- {produto}: R$ {preco:.2f}\n")

    arquivo.write(f"\nTOTAL: R$ {total:.2f}\n")

print("Recibo salvo com sucesso em pagamento.txt")

# 4. Leitura e exibição final de pagamento
print("\n--- PROCESSANDO PAGAMENTO ---")

with open("pagamento.txt", "r", encoding="utf-8") as arquivo:
    texto = arquivo.read()

# Localiza a informação do TOTAL no texto
posicao_total = texto.find("TOTAL:")

if posicao_total != -1:
    # Pega o texto que vem depois de "TOTAL:"
    valor_total = texto[posicao_total + len("TOTAL:"):].strip()

    # Pega somente a primeira linha
    valor_total = valor_total.split("\n")[0]

    print(f"Compra processada com sucesso! Valor cobrado: {valor_total}")
else:
    print("Não foi possível encontrar o valor total da compra.")
