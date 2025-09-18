# #Lorena
# # atributos = [] nome, data, local, descricao, tipo
def adicionar_evento(evento):
    print("\nAdicionando um novo evento:")
    nome = input("Nome do Evento: ")
    data = input("Data do Evento (AAAA-MM-DD): ")
    local = input("Local do Evento: ")
    descricao = input("Descrição do Evento: ")
    tipo = input("Tipo do Evento: ")

    novo_evento = evento(nome, data, local, descricao, tipo)
    evento.append(novo_evento)
    salvar_evento = (evento)
    print("Evento adicionado com sucesso!")
