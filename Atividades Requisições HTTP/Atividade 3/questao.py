import json
import requests

# 1. Leitura do arquivo JSON local
file_path = "dados_funcionarios_atualizados.json"

with open(file_path, "r", encoding="utf-8") as file:
    funcionarios = json.load(file)

base_url = "http://192.168.205.100:8080/funcionarios"

# 2 e 3. Percorre a lista de funcionários e envia as atualizações via PUT
print("--- Iniciando atualização dos funcionários ---")
for funcionario in funcionarios:
    funcionario_id = funcionario.get("id")
    url_put = f"{base_url}/{funcionario_id}"

    # Método HTTP PUT enviado via biblioteca requests
    response = requests.put(url_put, json=funcionario)

    # Validando o código de status 200
    if response.status_code == 200:
        print(f"[SUCESSO] Funcionário ID {funcionario_id} atualizado com êxito.")
    else:
        print(f"[ERRO] Falha ao atualizar ID {funcionario_id}. Status Code: {response.status_code}")

# 4. Verificação final com requisição GET
print("\n--- Verificação Final (GET) ---")
response_get = requests.get(base_url)

if response_get.status_code == 200:
    funcionarios_cadastrados = response_get.json()
    print("Lista atual de funcionários no sistema:")
    print(json.dumps(funcionarios_cadastrados, indent=4, ensure_ascii=False))
else:
    print(f"Erro ao buscar a lista de funcionários. Status Code: {response_get.status_code}")