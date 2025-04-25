from functions.back_end.gerar_codigo import generate_chat_response

def identificar_entidade_model(mapping_code):
    prompt = f"""
    {mapping_code}
    1) Identifique a entidade e suas propriedades e retorne um JSON.
    {{
        "Entidade": "",
        "Propriedades": []
    }}
    """

    response = generate_chat_response(prompt)
    
    json = response.choices[0].message.content.strip()
    validar_json_estrutura(json)
    return json

def validar_json_estrutura(dado):
    if not isinstance(dado, dict):
        return False, "O dado não é um dicionário."

    if "Entidade" not in dado or "Propriedades" not in dado:
        return False, "Chaves obrigatórias ausentes ('Entidade' e 'Propriedades')."

    if not isinstance(dado["Entidade"], str) or not dado["Entidade"]:
        return False, "A chave 'Entidade' deve ser uma string não vazia."

    if not isinstance(dado["Propriedades"], list):
        return False, "A chave 'Propriedades' deve ser uma lista."

    for prop in dado["Propriedades"]:
        if not isinstance(prop, str) or not prop:
            return False, f"Todas as propriedades devem ser strings não vazias. Erro em: {prop}"

    return True, "Formato válido."

def identificar_entidade_funcoes_service(service_js):
    prompt = f"""
    {service_js}
    
    1) Identifique o nome da service e sas funções retorne um JSON.
    {{
        "Service": "",
        "Funcoes": []
    }}
    """

    response = generate_chat_response(prompt)    
    json = response.choices[0].message.content.strip()
    validar_json_estrutura(json)
    return json