from utils.load_save import load_data
from time import sleep

def list_events(exibir_id: bool= True, time: float= 0):
    events = load_data("event")
    for indice, evento in enumerate(events, start=1):
        print(f"Evento ID {indice}:") if not exibir_id else None
        for dados, informacao in evento.items():
            if exibir_id:
                pass
            else:
                if dados == "id":
                    continue
            
            if exibir_id: print(f"{dados}: {informacao}")

            if not exibir_id: print(f"    {dados}: {informacao}")
        sleep(time)
        print()
        