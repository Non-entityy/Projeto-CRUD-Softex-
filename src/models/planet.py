
class Planeta:
    def __init__(self, id, nome, tipo, massa, gravidade, temperatura):
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.massa = massa
        self.gravidade = gravidade
        self.temperatura = temperatura

    def __repr__(self):
        return f"Planeta({self.id}, {self.nome}, {self.tipo}, {self.massa}, {self.gravidade}g, {self.temperatura}°C)"

    
    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "tipo": self.tipo,
            "massa": self.massa,
            "gravidade": self.gravidade,
            "temperatura": self.temperatura
        }
