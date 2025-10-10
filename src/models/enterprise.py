class Empresa:
    def __init__(self, nome: str, evenetos_ativos=[], eventos_desativos=[]):
        self.nome = nome
        self.eventos_ativos = evenetos_ativos
        self.eventos_desativos = eventos_desativos
