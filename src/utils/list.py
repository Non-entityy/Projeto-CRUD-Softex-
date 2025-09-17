from load_save import carregar_eventos

def list_events():
    events = carregar_eventos()
    for indice, evento in enumerate(events):
        print(f"Evento ID {indice}:")
        for dados, informacao in evento.items():
            print(f"    {dados}: {informacao}")
