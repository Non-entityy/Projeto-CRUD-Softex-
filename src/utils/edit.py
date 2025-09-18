#Rodrigo
from load_save import carregar_eventos, salvar_eventos
from list import list_events
from time import sleep

events_json = carregar_eventos()

def editar_item(events= events_json):
    print("Carregando todos os eventos..."), sleep(1.5)
    list_events(False), sleep(1)

    try:
        indice_item = int(input("Digite o ID do item: "))
    except ValueError:
        while True:
            try: indice_item = int(input("Digite o ID do item apenas com números: "))
            except: pass
            else: break
    
    print(f"Carregando evento de ID {indice_item}..."), sleep(1.5)
    evento_selecionado = dict(events[indice_item]) 
    
    print(evento_selecionado)
    print("Evento:")
    print(evento_selecionado.items())
    for indice, tupla in enumerate(evento_selecionado.items()):
        print(f"[{indice}] -> ", end="")
        print(f"{tupla[0]}: {tupla[1]}")
    try:
        indice_informacao = int(input("Digite o ID da informação que deseja alterar: "))
        for indice, tupla in enumerate(evento_selecionado):
            if tupla[0] == "id":
                continue

            if indice == indice_informacao:
                evento_selecionado[tupla[0]] = input(f"Digite o que deseja atualizar em [{tupla[0]}]: ")
    except ValueError:
        while True:
            try: indice_informacao = int(input("Digite o ID da informação apenas com números: "))
            except: pass
            else: break

editar_item()