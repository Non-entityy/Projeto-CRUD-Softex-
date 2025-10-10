from datetime import datetime as Date

class Ingresso:
    def __init__(self, valor: float, tipo_ingresso: str, lote: int, validade_lote: Date):
        self.valor = valor
        self.tipo_ingresso = tipo_ingresso
        self.lote = lote
        self.validade_lote = validade_lote
