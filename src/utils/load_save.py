import json
from models.event import Evento
#from models.event import Evento
#from utils.load_save import carregar_eventos, salvar_eventos

# Função para carregar eventos do arquivo JSON
def carregar_eventos():
    try:
        with open('events.json', 'r') as f:
            dados = json.load(f)
            return [Evento(**evento) for evento in dados]  # Converte dicionários em objetos Evento
    except FileNotFoundError:
        return []

# Função para salvar os eventos no arquivo JSON
def salvar_eventos(eventos):
    eventos_dict = [evento.to_dict() for evento in eventos]  # Converte objetos Evento em dicionários
    with open('events.json', 'w') as f:
        json.dump(eventos_dict, f, indent=4)