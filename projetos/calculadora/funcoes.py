# Funções

def soma(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a+b
    else:
        raise TypeError(f"Os inbuts 'a' e 'b' devem ser números. \n recebido a = {a}, tipo = {type(a)} \n recebido b = {b}, tipo = {type(b)}")

def subtracao(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a - b
    else:
        raise TypeError(f"Os inbuts 'a' e 'b' devem ser números. \n recebido a = {a}, tipo = {type(a)} \n recebido b = {b}, tipo = {type(b)}")

# Funções auxiliares

def checar_validade(opcao, opcoes):
    if opcao not in opcoes:
        raise Exception()
    
def coletar_opcao(opcoes):
    while True:
        try: 
            opcao = input('> ')   
            checar_validade(opcao, opcoes)

        except:
            print('Erro! Digite uma das opções presentes no menu.') 

        else:
            return opcao
        
