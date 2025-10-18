from models.event import Evento
from utils.additens import adicionar_evento
from utils.load_save import carregar_eventos
from utils.edit import editar_item
from utils.pesq import search_event
from utils.remitens import remover_evento_nome
from utils.menu import menu
from utils.list import list_events
#from eventos import adicionar_evento, listar_eventos, editar_evento, remover_evento, pesquisar_evento

def main():
    while True:
        events = carregar_eventos()
        opcao = menu()

        match opcao:
            case "1":
                adicionar_evento(Evento, events)
            case "2":
                search_event(events)
            case "3":
                editar_item(events)
            case "4":
                list_events(False)
                remover_evento_nome(events, search_event(events))
            case "5":
                list_events(time=0.5)
            case "0":
                print("Saindo... Até logo!")
                break
            case _:
                print("Opção inválida, tente novamente.")

if __name__ == '__main__':
    main()
