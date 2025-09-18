#Rodrigo
from utils.load_save import carregar_eventos, salvar_eventos
from utils.list import list_events
from time import sleep

events_json = carregar_eventos()

def try_input_int(msg_input: str):
    
    msg_input = msg_input.replace(":","").strip()
    try:
        var_int = int(input(f"{msg_input}: "))
    except ValueError:
        while True:
            try: var_int = int(input(f"{msg_input} apenas com números: "))
            except: pass
            else: break
    
    return var_int
    

def editar_item(events= events_json):
    print("Carregando todos os eventos..."), sleep(1.5)
    list_events(False), sleep(1)

    indice_item = try_input_int("Digite o ID do item: ")
    
    print(f"Carregando evento de ID {indice_item}..."), sleep(1.5)
    evento_selecionado = dict(events[indice_item - 1])
    events.pop(indice_item - 1) # Removendo da lista

    # print("Evento:")
    # print(evento_selecionado.items())
    for indice, tupla in enumerate(evento_selecionado.items(), start=1):
        print(f"[{indice}] -> ", end="")
        print(f"{tupla[0]}: {tupla[1]}")
    
    indice_informacao = try_input_int("Digite o ID da informação que deseja alterar: ")
    # indice_informacao = int(input("Digite o ID da informação que deseja alterar: "))

    # ------------------------------------[ Percorrendo  ]------------------------------------

    for indice, tupla in enumerate(evento_selecionado.items(), start=1):
        if tupla[0] == "id":
            continue

        if indice == indice_informacao:
            evento_selecionado[tupla[0]] = input(f"Digite o que deseja atualizar em [{tupla[0]}]: ")

    events.insert(indice_item - 1, evento_selecionado) # Salvando evento atualizado

    salvar_eventos(events)
