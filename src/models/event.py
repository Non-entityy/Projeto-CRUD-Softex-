class Evento:
    def __init__(self, nome, data, local, descricao, tipo):
        self.id = id((nome, data, local, descricao, tipo)) # O id pode ser uma tupla do proprio objeto
        self.nome = nome
        self.data = data
        self.local = local
        self.descricao = descricao
        self.tipo = tipo
        self.status = True # True para ativo | False para inativo

    def __repr__(self):
        return f"Evento({self.id}, {self.tipo}, {self.nome}, {self.data}, {self.local})"

    def to_dict(self):
        return {
            "id": self.id,
            "tipo": self.tipo,
            "nome": self.nome,
            "data": self.data,
            "local": self.local,
            "descricao": self.descricao,
            
        }