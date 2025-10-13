import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def get_file_path(categoria):
    nome_arquivo = categoria.lower() + 's.json'
    caminho = os.path.join(BASE_DIR, "data", nome_arquivo)
    return caminho

def load_data(categoria) -> list:
    """Carrega a lista de eventos do arquivo JSON principal

    Args:
        categoria (str): Categoria do arquivo ex: event → events.json

    Returns:
        list: Se encontrar o arquivo retornara a lista com os dados, se não retornara uma lista vazia
    """
    caminho = get_file_path(categoria)
    if not os.path.exists(caminho):
        return []
    with open(caminho, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_data(categoria, dados):
    """Salva a lista completa com dados no arquivo JSON

    Args:
        categoria (str): Categoria do arquivo ex: event → events.json
        dados (list): Lista com todos os eventos que vão ser salvos no JSON (Incluindo os já existentes)
    """
    caminho = get_file_path(categoria)
    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)

get_file_path("event")