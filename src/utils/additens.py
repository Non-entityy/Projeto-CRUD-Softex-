from utils.load_save import carregar_eventos, salvar_eventos
# #Lorena
# # atributos = [] nome, data, local, descricao, tipo
def adicionar_evento(Class_obj, eventos):
    print("\nAdicionando um novo evento:")
    nome = input("Nome do Evento: ")
    data = input("Data do Evento (DD-MM-AAAA): ")
    local = input("Local do Evento: ")
    descricao = input("Descrição do Evento: ")
    tipo = input("Tipo do Evento: ")

    novo_evento = Class_obj(nome, data, local, descricao, tipo)
    evento_dict = novo_evento.to_dict()
    eventos.append(evento_dict)
    salvar_eventos(eventos)
    print("Evento adicionado com sucesso!")
    return novo_evento