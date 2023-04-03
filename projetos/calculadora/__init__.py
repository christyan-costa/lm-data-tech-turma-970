from funcoes import soma

def calcule():
    a = input("Digite um valor numérico para 'a':")
    try:
        a = float(a)
    except:
        print(f"valor inválido")
    
    b = input("Digite um valor numérico para 'b':")
    try:
        b = float(b)
    except:
        print(f"valor inválido")

    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        print(soma(a,b))
    else:
        raise TypeError(f"Os inbuts 'a' e 'b' devem ser números. \n recebido a = {a}, tipo = {type(a)} \n recebido b = {b}, tipo = {type(b)}")
