from utils.load_save import load_data, save_data
# #Lorena
# # atributos = [] nome, data, local, descricao, tipo
def adicionar_evento(Class_obj, eventos):
    print("\nAdicionando um novo evento:")
    tipo = input("Tipo do Evento: ")
    nome = input("Nome do Evento: ")
    data = input("Data do Evento (DD-MM-AAAA): ")
    local = input("Local do Evento: ")
    ingressos = input("Quantidade de ingressos: ")
    idade = input("Idade mínima: ")
    descricao = input("Descrição do Evento: ")
   

    novo_evento = Class_obj(tipo, nome, data, local, ingressos, idade, descricao)
    evento_dict = novo_evento.to_dict()
    eventos.append(evento_dict)
    save_data("event", eventos)
    print("Evento adicionado com sucesso!")
    return novo_evento