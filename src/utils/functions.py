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