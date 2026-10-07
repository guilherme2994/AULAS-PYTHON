import json

# ETAPA 1 — Lendo o Arquivo TXT Legado

catalogo_livros = []

# O arquivo TXT deve estar na mesma pasta do script ou ter o caminho especificado
caminho_txt = "banco_livros.txt"

try:
    with open(caminho_txt, "r", encoding="utf-8") as arquivo_txt:
        for linha in arquivo_txt:
            # Limpa espaços em branco e quebras de linha nas pontas
            linha_limpa = linha.strip()

            # Pula linhas vazias caso existam
            if not linha_limpa:
                continue

            # Separa os atributos pelo caractere ';'
            dados = linha_limpa.split(";")

            # Cria o dicionário com os campos convertidos para os tipos apropriados
            livro = {
                "id": int(dados[0]),
                "nome": dados[1],
                "descricao": dados[2],
                "preco": float(dados[3]),
                "em_estoque": int(dados[4])
            }

            # Adiciona à lista principal
            catalogo_livros.append(livro)

    print(f"Etapa 1 Concluída: {len(catalogo_livros)} livros lidos do arquivo TXT.")

except FileNotFoundError:
    print(f"Erro: O arquivo '{caminho_txt}' não foi encontrado. Baixe o arquivo e coloque no mesmo diretório.")

# ETAPA 2 — Gerando o Arquivo JSON ('w' - write)

caminho_json = "catalogo.json"

with open(caminho_json, "w", encoding="utf-8") as arquivo_json:
    # Escreve a lista de dicionários no formato JSON com indentação de 4 espaços
    json.dump(catalogo_livros, arquivo_json, indent=4, ensure_ascii=False)

print("Etapa 2 Concluída: Arquivo 'catalogo.json' criado com sucesso.")

# ETAPA 3 — Instanciando Novos Livros e Atualizando o JSON

# Criação de 5 novos livros
novos_livros = [
    {
        "id": 31,
        "nome": "Entendendo Algoritmos",
        "descricao": "Um guia ilustrado para programadores e curiosos.",
        "preco": 69.90,
        "em_estoque": 12
    },
    {
        "id": 32,
        "nome": "O Codificador Limpo",
        "descricao": "Código de conduta para programadores profissionais.",
        "preco": 75.00,
        "em_estoque": 8
    },
    {
        "id": 33,
        "nome": "Estruturas de Dados e Algoritmos com Python",
        "descricao": "Guia prático sobre manipulação de dados em Python.",
        "preco": 89.90,
        "em_estoque": 20
    },
    {
        "id": 34,
        "nome": "Padrões de Projeto",
        "descricao": "Soluções reutilizáveis de software orientado a objetos.",
        "preco": 110.00,
        "em_estoque": 5
    },
    {
        "id": 35,
        "nome": "Refatoração",
        "descricao": "Aperfeiçoando o projeto de código existente.",
        "preco": 95.50,
        "em_estoque": 18
    }
]

# Adiciona os novos livros à lista existente (mantendo a lista com 35 itens)
catalogo_livros.extend(novos_livros)

# Sobrescreve/atualiza o arquivo 'catalogo.json' original
with open(caminho_json, "w", encoding="utf-8") as arquivo_json:
    json.dump(catalogo_livros, arquivo_json, indent=4, ensure_ascii=False)

print(f"Etapa 3 Concluída: 'catalogo.json' atualizado! Total de livros no catálogo: {len(catalogo_livros)}")

# ETAPA 4 — Lendo atributos dentro do arquivo final (json)

def analisar_estoque(caminho_arquivo):
    # Leitura do arquivo JSON permanente para garantir persistência dos dados
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        dados_carregados = json.load(arquivo)

    livros_baixo_estoque = []
    valor_total_estoque = 0.0

    # Iteração sobre cada livro carregado do JSON
    for livro in dados_carregados:
        # Verifica livros com menos de 15 unidades em estoque
        if livro["em_estoque"] < 15:
            livros_baixo_estoque.append(livro["nome"])

        # Calcula o valor total do estoque (preço * quantidade)
        valor_total_estoque += livro["preco"] * livro["em_estoque"]

    # Exibição dos resultados no terminal
    print("\n" + "=" * 50)
    print("      RELATÓRIO DE ESTOQUE DA LIVRARIA")
    print("=" * 50)

    print("\n📚 Livros com menos de 15 unidades em estoque:")
    for nome in livros_baixo_estoque:
        print(f"  - {nome}")

    print(f"\n💰 Valor Total do Estoque: R$ {valor_total_estoque:,.2f}")
    print("=" * 50)

# Executa o método de análise
analisar_estoque(caminho_json)