#Gleiciane Farias
from utils.load_save import salvar_eventos

# lista_planeta = [
#     {"id": 1, 
#     "nome": "Mercúrio", 
#     "tipo": "Rochoso",
#     "massa": "3,30 × 10²³",
#     "gravidade": 3.7,
#     "temperatura": ~167},

#     {"id": 2,
#     "nome": "Vênus",
#     "tipo": "Rochoso",
#     "massa": "4,87 x 10²⁴",
#     "gravidade": 8.87,
#     "temperatura": ~464},

#     {"id": 3, 
#     "nome": "Terra", 
#     "tipo": "Rochoso",
#     "massa": "5,97 x 10²⁴",
#     "gravidade": 9.8,
#     "temperatura": ~15},


#     {"id": 4, 
#      "nome": "Marte", 
#      "tipo": "Rochoso",
#      "massa": "6,42 x 10²³",
#      "gravidade": 3.71,
#      "temperatura": ~-63},
# ]

def reordenar_id(lista_evento): # Função que não vai ser utilizada pelo conceito de Design Patterns
     for id, evento in enumerate(lista_evento, start=1):
          evento["id"] = id
     return lista_evento

def remover_evento_nome(lista_evento, evento_remover):
     for evento in lista_evento:
          if evento_remover["nome"] == evento["nome"]:
               lista_evento.remove(evento)
               print(f"O evento {evento_remover} foi removido com  sucesso.") 
               # reordenar_id(lista_evento) 
               print(f"{lista_evento}")
               salvar_eventos(lista_evento)
               return lista_evento
     else:
          print(f"O Planeta digitado {evento_remover} não foi encontrado. Verifique se digitou corretamente.")    
      

# Testes

# remove = input("Digite o Planeta que você deseja remover: ")
# planeta_remover = remove
# remover_planeta_nome(lista_planeta, remove)      
