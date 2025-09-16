class Evento:
    def __init__(self, id, nome, data, local, descricao, tipo):
        self.id = id
        self.nome = nome
        self.data = data
        self.local = local
        self.descricao = descricao
        self.tipo = tipo

    def __repr__(self):
        return f"Evento({self.id}, {self.nome}, {self.data}, {self.local}, {self.tipo})"

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "data": self.data,
            "local": self.local,
            "descricao": self.descricao,
            "tipo": self.tipo
        }