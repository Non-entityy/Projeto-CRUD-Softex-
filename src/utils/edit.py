#Rodrigo
from utils.load_save import carregar_eventos, salvar_eventos
from utils.list import list_events
from utils.functions import try_input_int
from time import sleep

events_json = carregar_eventos()

def editar_item():
    """Função para editar um item
    # Funcionalidades:
    - Lista todos os itens
    - Seleciona a informação a ser alterada intuitivamente
    - Altera a lista
    - E ao final salva no arquivo
    """
    events = events_json # Definindo a lista pelo arquivo JSON

    print("Carregando todos os eventos..."), sleep(1.5) # EXIBIÇÃO
    list_events(False), sleep(1) # EXIBIÇÃO

    indice_item = try_input_int("Digite o ID do item: ") # Não altera durante a execução é o ID do item dentro da lista
    
    print(f"Carregando evento de ID {indice_item}..."), sleep(1.5) # EXIBIÇÃO
    evento_selecionado = dict(events[indice_item - 1]) # EXIBIÇÃO
    events.pop(indice_item - 1) # Removendo da lista o evento sem alteração

    # print("Evento:")
    # print(evento_selecionado.items())

    # ------------------------------------[ Selecionando uma informação para editar ]------------------------------------

    # Percorrendo o evento selecionado guardando os indices e os dados para selecionar uma informação para alterar
    for indice, tupla in enumerate(evento_selecionado.items(), start=1):
        if tupla[0] == "id": # Ignorando o ID
            continue

        print(f"[{indice}] -> ", end="")
        print(f"{tupla[0]}: {tupla[1]}")
    
    indice_informacao = try_input_int("Digite o ID da informação que deseja alterar: ") # Pedindo o ID da informação

    # ------------------------------------[ Editando a informação selecionada ]------------------------------------

    # Percorrendo novamente o evento buscando o dado selecionado pelo ID para alterar a informação
    for indice, tupla in enumerate(evento_selecionado.items(), start=1):
        if tupla[0] == "id": # Ignorando o ID
            continue

        if indice == indice_informacao: # Atualizando a informação selecionada pelo ID
            evento_selecionado[tupla[0]] = input(f"Digite o que deseja atualizar em [{tupla[0]}]: ")

    events.insert(indice_item - 1, evento_selecionado) # Salvando evento atualizado removendo a informação antiga e adicionando a nova

    salvar_eventos(events) # Salvando a lista de eventos diretamente no arquivo JSON
