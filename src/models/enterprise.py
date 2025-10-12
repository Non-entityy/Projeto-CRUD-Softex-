class Empresa:
    def __init__(self, nome: str, evenetos_ativos=[], eventos_inativos=[]):
        self.id = id((nome, evenetos_ativos, eventos_inativos))
        self.nome = nome
        self.eventos_ativos = evenetos_ativos
        self.eventos_inativos = eventos_inativos
    
    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "eventos ativos": self.eventos_ativos,
            "eventos inativos": self.eventos_inativos   
        }