# Funções

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a-b

def multiplicacao(a, b):
    return a*b

def divisao(a,b):
    if b != 0:
        return a/b
    else:
        raise ZeroDivisionError(f"O divisor ('b') deve ser diferente de zero. \n recebido b = {b}")
    
        
# Funções auxiliares

def checar_validade(opcao, opcoes):
    if opcao not in opcoes:
        raise Exception()
    
def coletar_opcao(opcoes):
    while True:
        try: 
            opcao = input('>> ')   
            checar_validade(opcao, opcoes)

        except:
            print('Erro! Digite uma das opções presentes no menu.') 

        else:
            return opcao
        
