from utils.additens import adicionar_item
from utils.load_save import carregar_eventos, salvar_eventos
from utils.edit import editar_item
from utils.pesq import search_planet
from utils.remitens import remover_planeta_nome
from utils.menu import menu
from utils.list import list_planets
#from eventos import adicionar_evento, listar_eventos, editar_evento, remover_evento, pesquisar_evento

def main():
    events = carregar_eventos()
    while True:
        opcao = menu()

        match opcao:
            case "1":
                adicionar_item(events)
            case "2":
                search_planet(events)
            case "3":
                editar_item(events)
            case "4":
                remover_planeta_nome(events)
            case "5":
                list_planets(events)
            case "0":
                print("Saindo... Até logo!")
                break
            case _:
                print("Opção inválida, tente novamente.")

if __name__ == '__main__':
    main()
