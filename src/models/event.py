class Evento:
    def __init__(
            self, nome: str, data: str, 
            local: str, descricao: str, tipo: str, 
            qtd_ingressos_disponiveis: int, idade_minima: int):
        self.id = id((nome, data, local, descricao, tipo, qtd_ingressos_disponiveis, idade_minima)) # O id pode ser uma tupla do proprio objeto
        self.tipo = tipo
        self.nome = nome
        self.data = data
        self.local = local
        self.qtd_ingressos_disponiveis = qtd_ingressos_disponiveis
        self.idade_minima = idade_minima
        self.status = True # True para ativo | False para inativo
        self.descricao = descricao

    def __repr__(self):
        return f"Evento({self.id},'{self.tipo}', '{self.nome}', {self.data}, '{self.local}', {self.qtd_ingressos_disponiveis}, {self.idade_minima}, {self.status},'{self.descricao}')"

    def to_dict(self):
        return {
            "id": self.id,
            "tipo": self.tipo,
            "nome": self.nome,
            "data": self.data,
            "local": self.local,
            "quantidade ingressos disponiveis": self.qtd_ingressos_disponiveis,
            "idade minima": self.idade_minima,
            "status": self.status,
            "descricao": self.descricao
        }