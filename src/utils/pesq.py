#Danielly
def search_eventos (Evento):
    termo = input("Digite o nome do evento para buscar: ").strip().lower()
    encontrados = [p for p in Evento if termo in p['nome'].lower()]

    if not encontrados:
        print("Nenhum evento encontrado com esse nome.\n")
        return

    print("\n--- Resultados da Pesquisa ---")
    for Evento in encontrados:
        print(f"ID: {Evento['id']} | Nome: {Evento['nome']} | Local: {Evento['local']} | Descrição: {Evento['descrição']} | Tipo: {Evento['tipo']}")
    print()
