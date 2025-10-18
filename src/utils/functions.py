import inspect

def try_input_int(msg_input: str):
    """Faz um input verificando possíveis erros do úsuario como:
    - Escrever uma letra
    - Escrever um alfanúmerico
    - Digitar um número decimal
    Logo ele vai pedir novamente o input e encerrar se o úsuario digitar um numero inteiro corretamente

    Args:
        msg_input (str): A mensagem que vai ser exibida no input().

    Returns:
        int: Retorna o número recebido no input pelo úsuario
    """
    msg_input = msg_input.replace(":","").strip()
    try:
        var_int = int(input(f"{msg_input}: "))
    except ValueError:
        while True:
            try: var_int = int(input(f"{msg_input} apenas com números: "))
            except: pass
            else: break
    
    return var_int

def criar_instancia(classe):
    """Pega uma classe como parametro e cria uma instância a partir dessa classe

    Args:
        classe (class): Classe do objeto/instância que deseja criar

    Returns:
        classe: Retorna uma instância do tipo <classe>
    """
    # Obtém os parâmetros do construtor da classe (__init__)
    parametros = inspect.signature(classe.__init__).parameters
    
    # Ignora o primeiro parâmetro 'self'
    args_necessarios = [p for p in parametros if p != "self"]

    print(f"A classe recebida foi: {classe.__name__}")
    print("Atributos necessários:", args_necessarios)
    
    valores = {}
    for arg in args_necessarios:
        valor = input(f"Digite o valor para o atributo '{arg}': ")
        valores[arg] = valor
    
    # Cria uma instância da classe usando os valores coletados
    instancia = classe(**valores)
    return instancia