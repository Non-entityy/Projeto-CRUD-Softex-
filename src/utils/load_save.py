import json

PATH_EVENTOS = "src/data/events.json" # Executar no diretorio principal
PATH_INGRESSOS = "src/data/ingress.json"
PATH_EMPRESA = "src/data/enterprises.json"
PATH_PESSOA = "src/data/persons.json"

def carregar_eventos():
    """Carrega a lista de eventos do arquivo JSON principal

    Returns:
        list: Se encontrar o arquivo retornara a lista com os eventos, se não retornara uma lista vazia
    """
    try:
        with open(PATH_EVENTOS, 'r', encoding="utf-8") as f:
            dados = json.load(f)
            return dados
            # return [Evento(**evento) for evento in eventos_json if not evento["id"]]  # Converte dicionários em objetos Evento
    except FileNotFoundError:
        return []
    except TypeError:
        return []

def salvar_eventos(eventos):
    """Salva a lista completa com eventos no arquivo JSON

    Args:
        eventos (list): Lista com todos os eventos que vão ser salvos no JSON (Incluindo os já existentes)
    """
    eventos_dict = [evento for evento in eventos]  # Converte objetos Evento em dicionários
    with open(PATH_EVENTOS, 'w', encoding="utf-8") as f:
        json.dump(eventos_dict, f, indent=4, ensure_ascii=False)
        
def carregar_ingressos():
    """Carrega a lista de ingressos do arquivo JSON principal

    Returns:
        list: Se encontrar o arquivo retornara a lista com os ingressos, se não retornara uma lista vazia
    """
    try:
        with open(PATH_INGRESSOS, 'r', encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except TypeError:
        return []

def salvar_ingressos(ingressos):
    """Salva a lista completa com ingressos no arquivo JSON

    Args:
        ingressos (list): Lista com todos os ingressos que vão ser salvos no JSON (Incluindo os já existentes)
    """
    ingressos_dict = [ingresso for ingresso in ingressos]
    with open(PATH_INGRESSOS, 'w', encoding="utf-8") as f:
        json.dump(ingressos_dict, f, indent=4, ensure_ascii=False)
        
def carregar_ingressos():
    """Carrega a lista de ingressos do arquivo JSON principal

    Returns:
        list: Se encontrar o arquivo retornara a lista com os ingressos, se não retornara uma lista vazia
    """
    try:
        with open(PATH_INGRESSOS, 'r', encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except TypeError:
        return []

def salvar_ingressos(ingressos):
    """Salva a lista completa com ingressos no arquivo JSON

    Args:
        ingressos (list): Lista com todos os ingressos que vão ser salvos no JSON (Incluindo os já existentes)
    """
    ingressos_dict = [ingresso for ingresso in ingressos]
    with open(PATH_INGRESSOS, 'w', encoding="utf-8") as f:
        json.dump(ingressos_dict, f, indent=4, ensure_ascii=False)