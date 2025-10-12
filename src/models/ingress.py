from datetime import datetime as Date

class Ingresso:
    def __init__(self, valor: float, tipo_ingresso: str, lote: int, validade_lote: Date):
        self.id = id((valor, tipo_ingresso, lote, validade_lote))
        self.valor = valor
        self.tipo_ingresso = tipo_ingresso
        self.lote = lote
        self.validade_lote = validade_lote

    def to_dict(self):
        return {
            "id": self.id,
            "valor": self.valor,
            "tipo ingresso": self.tipo_ingresso,
            "lote": self.lote,
            "validade lote": self.validade_lote   
        }
