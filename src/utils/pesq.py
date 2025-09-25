#Danyelle
# input 




# def search_eventos (Evento):
#     termo = input("Digite o nome do evento para buscar: ").strip().lower()
#     encontrados = [p for p in Evento if termo in p['nome'].lower()]

#     if not encontrados:
#         print("Nenhum evento encontrado com esse nome.\n")
#         return

#     print("\n--- Resultados da Pesquisa ---")
#     for Evento in encontrados:
#         print(f"ID: {Evento['id']} | Nome: {Evento['nome']} | Local: {Evento['local']} | Descrição: {Evento['descrição']} | Tipo: {Evento['tipo']}")
#     print()

from utils.load_save import carregar_eventos

def search_event(events=None):
    """Pesquisa eventos pelo nome (case insensitive)."""
    if events is None:
        events = carregar_eventos()

    termo = input("Digite o nome (ou parte) do evento: ").strip().lower()
    encontrados = [evento for evento in events if termo in evento["nome"].lower()]

    if not encontrados:
        print("\nNenhum evento encontrado.\n")
        return []

    print("\n--- Resultados da Pesquisa ---")
    for idx, evento in enumerate(encontrados, start=1):
        print(f"\nResultado {idx}:")
        for chave, valor in evento.items():
            print(f"  {chave}: {valor}")
    print()

    return encontrados