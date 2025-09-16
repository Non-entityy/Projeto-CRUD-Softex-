
import json
import os

DB_FILE = 'planets.json'


# === Funções de carregamento e salvamento ===

def load_planets():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, 'r') as f:
        return json.load(f)

def save_planets(planets):
    with open(DB_FILE, 'w') as f:
        json.dump(planets, f, indent=4)


# === Criar planeta ===

def generate_id(planets):
    if not planets:
        return 1
    return max(p["id"] for p in planets) + 1

def create_planet(planets):
    print("\n--- Criar Novo Planeta ---")
    nome = input("Nome do planeta: ")
    tamanho = input("Tamanho (em km): ")
    habitavel = input("É habitável? (sim/não): ").strip().lower() == 'sim'

    novo_planeta = {
        "id": generate_id(planets),
        "nome": nome,
        "tamanho": tamanho,
        "habitavel": habitavel
    }

    planets.append(novo_planeta)
    save_planets(planets)
    print(" Planeta criado com sucesso!\n")


# === Listar planetas ===

def list_planets(planets):
    print("\n--- Lista de Planetas ---")
    if not planets:
        print("Nenhum planeta cadastrado.\n")
        return

    for p in planets:
        print(f"ID: {p['id']} | Nome: {p['nome']} | Tamanho: {p['tamanho']} km | Habitável: {p['habitavel']}")
    print()


# === Editar planeta ===

def update_planet(planets):
    print("\n--- Editar Planeta ---")
    try:
        id_alvo = int(input("ID do planeta a editar: "))
    except ValueError:
        print("ID inválido.\n")
        return

    for p in planets:
        if p["id"] == id_alvo:
            print(f"Editando planeta: {p['nome']}")
            novo_nome = input("Novo nome (ou Enter para manter): ")
            novo_tamanho = input("Novo tamanho (km): ")
            novo_habitavel = input("É habitável? (sim/não): ")

            if novo_nome:
                p["nome"] = novo_nome
            if novo_tamanho:
                p["tamanho"] = novo_tamanho
            if novo_habitavel.strip():
                p["habitavel"] = novo_habitavel.strip().lower() == 'sim'

            save_planets(planets)
            print(" Planeta atualizado!\n")
            return

    print(" Planeta não encontrado.\n")


# === Deletar planeta ===

def delete_planet(planets):
    print("\n--- Deletar Planeta ---")
    try:
        id_alvo = int(input("ID do planeta a deletar: "))
    except ValueError:
        print("ID inválido.\n")
        return

    for p in planets:
        if p["id"] == id_alvo:
            planets.remove(p)
            save_planets(planets)
            print(" Planeta deletado com sucesso!\n")
            return

    print(" Planeta não encontrado.\n")


# ===  Pesquisar planeta ===

def search_planet(planets):
    print("\n--- Pesquisar Planeta ---")
    termo = input("Digite o nome do planeta: ").strip().lower()
    encontrados = [p for p in planets if termo in p["nome"].lower()]

    if not encontrados:
        print(" Nenhum planeta encontrado.\n")
        return

    print("\n--- Resultados da Pesquisa ---")
    for p in encontrados:
        print(f"ID: {p['id']} | Nome: {p['nome']} | Tamanho: {p['tamanho']} km | Habitável: {p['habitavel']}")
    print()


# === Menu principal ===

def menu():
    planets = load_planets()
    while True:
        print("=== MENU PLANETAS ===")
        print("1. Listar planetas")
        print("2. Criar planeta")
        print("3. Editar planeta")
        print("4. Deletar planeta")
        print("5. Pesquisar planeta")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            list_planets(planets)
        elif opcao == '2':
            create_planet(planets)
        elif opcao == '3':
            update_planet(planets)
        elif opcao == '4':
            delete_planet(planets)
        elif opcao == '5':
            search_planet(planets)
        elif opcao == '6':
            print("Encerrando o programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

# Início da aplicação
if __name__ == '__main__':
    menu()
