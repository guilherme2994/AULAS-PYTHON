import json
import requests


def consultar_viacep_por_cep(cep):
    """Consulta o ViaCEP a partir de um CEP formatado ou numérico."""
    # Remove caracteres não numéricos
    cep_limpo = "".join(filter(str.isdigit, str(cep)))
    if len(cep_limpo) != 8:
        return None

    url = f"https://viacep.com.br/ws/{cep_limpo}/json/"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            dados = response.json()
            if "erro" not in dados:
                return dados
    except requests.RequestException:
        pass
    return None


def consultar_viacep_por_endereco(uf, cidade, logradouro):
    """Consulta o ViaCEP a partir de UF, Cidade e Logradouro."""
    if not (uf and cidade and logradouro):
        return None

    # O ViaCEP exige logradouro com no mínimo 3 caracteres
    if len(logradouro.strip()) < 3:
        return None

    url = f"https://viacep.com.br/ws/{uf}/{cidade}/{logradouro}/json/"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            dados = response.json()
            if isinstance(dados, list) and len(dados) > 0:
                # Retorna o primeiro resultado correspondente
                return dados[0]
    except requests.RequestException:
        pass
    return None


def processar_e_atualizar_funcionarios(url_fonte, arquivo_saida):
    # 1. Obter os dados da API/Endpoint
    try:
        response = requests.get(url_fonte, timeout=10)
        response.raise_for_status()
        funcionarios = response.json()
    except requests.RequestException as e:
        print(f"Erro ao obter dados do servidor: {e}")
        return

    funcionarios_atualizados = []

    for func in funcionarios:
        # Cria uma cópia do registro para manter a integridade dos dados originais
        f = func.copy()

        # Extrai os campos com fallback para string vazia
        cep = str(f.get("cep", "") or "").strip()
        logradouro = str(f.get("logradouro", "") or "").strip()
        bairro = str(f.get("bairro", "") or "").strip()
        cidade = str(f.get("cidade", "") or "").strip()
        estado = str(f.get("uf", f.get("estado", "")) or "").strip()

        dados_cep = None

        # --- Regra 1: Tenta enriquecer a partir de um CEP existente ---
        if cep:
            dados_cep = consultar_viacep_por_cep(cep)
            # Se o CEP for inválido, limpa o campo CEP para tentar recuperar via endereço
            if not dados_cep:
                f["cep"] = ""
                cep = ""

        # --- Regra 2: Se não tem CEP válido, tenta buscar por Logradouro/Cidade/UF ---
        if not dados_cep and logradouro and cidade and estado:
            dados_cep = consultar_viacep_por_endereco(estado, cidade, logradouro)
            if dados_cep and not f.get("cep"):
                f["cep"] = dados_cep.get("cep", "")

        # --- Regra 3: Preenche apenas os campos VAZIOS mantendo os pré-existentes ---
        if dados_cep:
            if not f.get("logradouro") and dados_cep.get("logradouro"):
                f["logradouro"] = dados_cep["logradouro"]

            if not f.get("bairro") and dados_cep.get("bairro"):
                f["bairro"] = dados_cep["bairro"]

            if not f.get("cidade") and dados_cep.get("localidade"):
                f["cidade"] = dados_cep["localidade"]

            # Trata chave de estado (suporta 'uf' ou 'estado' conforme estrutura da base)
            if "uf" in f and not f["uf"] and dados_cep.get("uf"):
                f["uf"] = dados_cep["uf"]
            elif "estado" in f and not f["estado"] and dados_cep.get("uf"):
                f["estado"] = dados_cep["uf"]
            elif "uf" not in f and "estado" not in f:
                f["uf"] = dados_cep.get("uf", "")

        funcionarios_atualizados.append(f)

    # 4. Salvar o resultado no novo arquivo JSON
    with open(arquivo_saida, "w", encoding="utf-8") as file:
        json.dump(funcionarios_atualizados, file, ensure_ascii=False, indent=4)

    print(f"Processamento concluído! Dados salvos em '{arquivo_saida}'.")


# Execução do script
link_funcionarios = "http://192.168.205.100:8080/funcionarios"
arquivo_destino = "dados_funcionarios_atualizados.json"

processar_e_atualizar_funcionarios(link_funcionarios, arquivo_destino)