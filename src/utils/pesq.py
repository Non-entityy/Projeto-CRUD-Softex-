#Danielly
def search_planet(planets):
    termo = str(input("Digite o nome do planeta para buscar: ").strip().lower())
    encontrados = [p for p in planets if termo in p['nome'].lower()]

    if not encontrados:
        print("🔎 Nenhum planeta encontrado com esse nome.\n")
        return

    print("\n--- Resultados da Pesquisa ---")
    for planet in encontrados:
        # print(f"ID: {planet['id']} | Nome: {planet['nome']} | Tamanho: {planet['tamanho']} km | Habitável: {planet['habitavel']}")
        return planet
    print()
