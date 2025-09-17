#Lorena
# atributos = [] nome, data, local, descricao, tipo
def create_eventos():
   evento = float(input("nome do evento:"))
    data = float(input("data do evento:"))
    local = float(input("local do evento:"))
    descricao = float(input("Descrição do evento"))
    tipo = float(input("tipo de evento:"))

    evento = {
        "evento": evento,
        "data": data,
        "local": local,
        "descricao": descricao,
        "tipo": tipo,
        }  
    eventos.append(evento)
    print(f"\n evento '{ }) registrado com sucesso!")
    print(create_eventos)

create_eventos()

