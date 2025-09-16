#Lorena
# planetas = [] 
def adicionar_eventos():
    nome = input("digite o nome do planeta:" )
    tamanho = float(input("digite o tamanho do planeta (em km):"))
    distancia = float(input("digite a distancia do sol (em milhões de km):"))

    planeta = {
        "nome": nome,
        "tamanho": tamanho,
        "distancia": distancia 
        }  
    eventos.append(planeta)
    print(f"\n evento '{ }) registrado com sucesso!")
    print(adicionar_eventos)

adicionar_eventos()