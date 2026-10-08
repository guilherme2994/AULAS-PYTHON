import json

# ==========================================
# Parte 1: Leitura das Bases de Dados
# ==========================================

# Leitura do primeiro arquivo
with open("base1.json", "r", encoding="utf-8") as f1:
    dados1 = json.load(f1)

# Leitura do segundo arquivo
with open("base2.json", "r", encoding="utf-8") as f2:
    dados2 = json.load(f2)

# Leitura do terceiro arquivo
with open("base3.json", "r", encoding="utf-8") as f3:
    dados3 = json.load(f3)

# ==========================================
# Parte 2: Processamento e Filtragem
# ==========================================

lista_aniversariantes = []

# Consolidação das 3 bases em uma lista para facilitar a iteração
todas_as_bases = [dados1, dados2, dados3]

# Percorre cada base de dados e cada funcionário dentro delas
for base in todas_as_bases:
    for funcionario in base:
        # Extrai apenas 'nome' e 'aniversario' criando um novo dicionário
        novo_registro = {
            "nome": funcionario["nome"],
            "aniversario": funcionario["aniversario"],
        }
        # Adiciona o dicionário filtrado à lista final
        lista_aniversariantes.append(novo_registro)

# ==========================================
# Desafio Extra (Opcional)
# ==========================================

# Ordena a lista em ordem alfabética pelo nome
lista_aniversariantes.sort(key=lambda item: item["nome"])

# Exibe o total de registros processados
total_registros = len(lista_aniversariantes)
print(
    f"Processamento concluído! Total de registros processados: {total_registros}"
)

# ==========================================
# Parte 3: Salvando o Arquivo Consolidado
# ==========================================

with open("aniversariantes.json", "w", encoding="utf-8") as f_out:
    json.dump(
        lista_aniversariantes, f_out, indent=4, ensure_ascii=False
    )