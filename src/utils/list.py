from load_save import carregar_eventos

def list_events(exibir_id: bool):
    events = carregar_eventos()
    for indice, evento in enumerate(events):
        print(f"Evento ID {indice}:")
        for dados, informacao in evento.items():
            if exibir_id:
                pass
            else:
                if dados == "id":
                    continue
            print(f"    {dados}: {informacao}")
