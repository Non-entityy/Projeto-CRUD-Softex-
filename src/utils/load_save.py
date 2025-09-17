import json
# from models.event import Evento
#from models.event import Evento
#from utils.load_save import carregar_eventos, salvar_eventos

PATH = "src/data/events.json" # Executar no diretorio principal

# Função para carregar eventos do arquivo JSON
def carregar_eventos():
    try:
        with open(PATH, 'r') as f:
            dados = list(json.load(f))
            return dados
            # return [Evento(**evento) for evento in dados]  # Converte dicionários em objetos Evento
    except FileNotFoundError:
        return []
    except TypeError:
        return []

# Função para salvar os eventos no arquivo JSON
def salvar_eventos(eventos):
    eventos_dict = [evento.to_dict() for evento in eventos]  # Converte objetos Evento em dicionários
    with open(PATH, 'w') as f:
        json.dump(eventos_dict, f, indent=4)