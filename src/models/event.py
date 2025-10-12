class Evento:
    def __init__(
            self, nome: str, data: str, 
            local: str, descricao: str, tipo: str, 
            qtd_ingressos_disponiveis: int, idade_minima: int):
        self.id = id((nome, data, local, descricao, tipo)) # O id pode ser uma tupla do proprio objeto
        self.nome = nome
        self.data = data
        self.local = local
        self.descricao = descricao
        self.tipo = tipo
        self.qtd_ingressos_disponiveis = qtd_ingressos_disponiveis
        self.idade_minima = idade_minima
        self.status = True # True para ativo | False para inativo

    def __repr__(self):
        return f"Evento({self.id}, {self.tipo}, {self.nome}, {self.data}, {self.local})"

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "data": self.data,
            "local": self.local,
            "descricao": self.descricao,
            "tipo": self.tipo,
            "quantidade ingressos disponiveis": self.qtd_ingressos_disponiveis,
            "idade minima": self.idade_minima,
            "status": self.status
        }