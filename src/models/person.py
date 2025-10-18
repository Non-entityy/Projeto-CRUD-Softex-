from enum import Enum
import re

class Genero(Enum):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"
    NAO_BINARIO = "Não Binario"
    OUTRO = "Outro"

class CPFInvalido(Exception): ... # Classe CPF invalido
class CPF:
    def __init__(self, numero: str):
        self.numero = self._limpar(numero)
        if not self._validar():
            raise CPFInvalido("O CPF digitado não é valido por favor digite novamente")
    
    def _limpar(self, numero: str) -> str:
        """Remove pontos e traços do CPF."""
        return re.sub(r'[^0-9]', '', numero) # aceita apenas números

    def _validar(self) -> bool:
        """Valida o CPF (checando os dígitos verificadores)."""
        if len(self.numero) != 11 or len(set(self.numero)) == 1:
            return False

        # Cálculo dos dígitos verificadores
        for i in range(9, 11):
            soma = sum(int(self.numero[num]) * ((i + 1) - num) for num in range(i))
            digito = (soma * 10 % 11) % 10
            if digito != int(self.numero[i]):
                return False
        return True

    def formatado(self) -> str:
        """Retorna o CPF no formato 000.000.000-00."""
        return f"{self.numero[:3]}.{self.numero[3:6]}.{self.numero[6:9]}-{self.numero[9:]}"

    def __str__(self):
        return self.formatado()

class Pessoa:
    def __init__(
            self, cpf: CPF, nome: str, 
            idade: int, genero: Genero, 
            ingressos_ativos=[], ingressos_vencidos=[]):
        self.id = id((cpf, nome, idade, genero, ingressos_ativos, ingressos_vencidos))
        self.cpf = CPF(cpf)
        self.nome = nome
        self.idade = idade
        self.genero = genero
        self.ingressos_ativos = ingressos_ativos
        self.ingressos_vencidos = ingressos_vencidos

    def to_dict(self):
        return {
            "id": self.id,
            "cpf": self.cpf,
            "nome": self.nome,
            "idade": self.idade,
            "genero": self.genero,
            "ingressos ativos": self.ingressos_ativos,
            "ingressos inativos": self.ingressos_vencidos   
        }
