from funcoes import soma
from funcoes import subtracao
from funcoes import coletar_opcao

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
    
    
    operacoes = {'+': soma, '-': subtracao}
    
    print("Escolha uma das operações (digite o número correspondente à operação desejada):")
    for idx, operacao in enumerate(operacoes.keys()):
        print(f"{idx +1}: {operacao}")
        
    operacao_escolhida = coletar_opcao(operacoes.keys())
        
    
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        print(operacoes[operacao_escolhida](a,b))
    else:
        raise TypeError(f"Os inbuts 'a' e 'b' devem ser números. \n recebido a = {a}, tipo = {type(a)} \n recebido b = {b}, tipo = {type(b)}")
