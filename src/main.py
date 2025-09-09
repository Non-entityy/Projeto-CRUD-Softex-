#from utils.additens import 
from utils.edit import editar_item
from utils.pesq import search_planet
from utils.remitens import remover_planeta_nome
#from utils.list import listar_planeta


def menu():
    itens = []
    while True:
        print("\n=== MENU DE PLANETAS ===")
        print("1 - Adicionar Planeta")
        print("2 - Pesquisar Planeta")
        print("3 - Editar Planeta")
        print("4 - Remover Planeta")
        print("5 - Listar todos os Planetas")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_item(itens)
        elif opcao == "2":
            search_planet(itens)
        elif opcao == "3":
            editar_item(itens)
        elif opcao == "4":
            remover_planeta_nome(itens)
        elif opcao == "5":
            listar_planeta(itens)
        elif opcao == "0":
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == '__main__':
    menu()
