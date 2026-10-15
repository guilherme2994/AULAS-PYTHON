
import requests
import json
import os

ARQUIVO = "historico_pesquisa.json"

# Solicita o CEP ao usuário
cep = input("Digite o CEP que deseja consultar: ").strip()
cep = cep.replace("-", "").replace(".", "")

# Verifica se o CEP possui 8 dígitos numéricos
if len(cep) != 8 or not cep.isdigit():
    print("Erro: digite um CEP válido com 8 números.")
else:
    try:
        # Consulta a API ViaCEP
        url = f"https://viacep.com.br/ws/{cep}/json/"
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()

        dados = resposta.json()

        # Verifica se o CEP existe
        if dados.get("erro"):
            print("Erro: CEP não encontrado.")
        else:
            # Exibe os dados do endereço
            print("\n--- Endereço encontrado ---")
            print(f"CEP: {dados.get('cep', '')}")
            print(f"Logradouro: {dados.get('logradouro', '')}")
            print(f"Bairro: {dados.get('bairro', '')}")
            print(f"Cidade: {dados.get('localidade', '')}")
            print(f"Estado: {dados.get('uf', '')}")

            # Lê o histórico existente
            if os.path.exists(ARQUIVO):
                with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
                    try:
                        historico = json.load(arquivo)
                    except json.JSONDecodeError:
                        historico = []
            else:
                historico = []

            # Adiciona a nova pesquisa como um dicionário
            historico.append({
                "cep": dados.get("cep", ""),
                "logradouro": dados.get("logradouro", ""),
                "bairro": dados.get("bairro", ""),
                "cidade": dados.get("localidade", ""),
                "estado": dados.get("uf", "")
            })

            # Salva o histórico sem apagar as pesquisas anteriores
            with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
                json.dump(
                    historico,
                    arquivo,
                    indent=4,
                    ensure_ascii=False
                )

            print("\nPesquisa salva no histórico com sucesso!")

    except requests.exceptions.Timeout:
        print("Erro: a consulta demorou muito para responder.")
    except requests.exceptions.ConnectionError:
        print("Erro: não foi possível conectar à API ViaCEP.")
    except requests.exceptions.HTTPError:
        print("Erro: ocorreu um problema na resposta HTTP.")
    except requests.exceptions.RequestException as erro:
        print(f"Erro na requisição: {erro}")
    except (OSError, json.JSONDecodeError) as erro:
        print(f"Erro ao acessar o arquivo JSON: {erro}")
