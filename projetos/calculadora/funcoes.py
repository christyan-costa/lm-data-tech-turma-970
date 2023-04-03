# Funções

def soma(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a+b
    else:
        raise TypeError(f"Os inbuts 'a' e 'b' devem ser números. \n recebido a = {a}, tipo = {type(a)} \n recebido b = {b}, tipo = {type(b)}")
