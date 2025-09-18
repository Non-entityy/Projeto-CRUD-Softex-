# #Lorena
# # atributos = [] nome, data, local, descricao, tipo
def adicionar_evento(eventos):
    print("\nAdicionando um novo evento:")
    nome = input("Nome do Evento: ")
    data = input("Data do Evento (AAAA-MM-DD): ")
    local = input("Local do Evento: ")
    descricao = input("Descrição do Evento: ")
    tipo = input("Tipo do Evento: ")

    novo_evento = Evento(nome, data, local, descricao, tipo)
    
    eventos.append(novo_evento)
    salvar_eventos(evento)
    print("Evento adicionado com sucesso!")
