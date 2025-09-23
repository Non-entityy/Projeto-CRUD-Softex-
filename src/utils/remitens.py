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

def reordenar_id(lista_planeta):
     for id, planeta in enumerate(lista_planeta, start=1):
          planeta["id"] = id   
     return lista_planeta   

def remover_planeta_nome(lista_planeta, planeta_remover):
     for planeta in lista_planeta:
          if planeta_remover["nome"] == planeta["nome"]:
               lista_planeta.remove(planeta)
               print(f"O planeta {planeta_remover} foi removido com  sucesso.") 
               # reordenar_id(lista_planeta) 
               print(f"{lista_planeta}")
               salvar_eventos(lista_planeta)
               return lista_planeta
     else:
          print(f"O Planeta digitado {planeta_remover} não foi encontrado. Verifique se digitou corretamente.")    
      

# Testes

# remove = input("Digite o Planeta que você deseja remover: ")
# planeta_remover = remove
# remover_planeta_nome(lista_planeta, remove)      
