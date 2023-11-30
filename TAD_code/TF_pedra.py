from random import randint

## TAD pedra
def cria_pedra_branca():
    return ['pedra', '.O.', 'mais', (3.14, randint(0, 10**6))]

def cria_pedra_preta():
    return ['pedra', '.X.', 'mais', (3.14, randint(0, 10**6))]

def cria_pedra_neutra():
    return ['pedra', '...', 'mais', (3.14, randint(0, 10**6))]

def eh_pedra(arg):
    return isinstance(arg, list) and len(arg) == 4 and arg[0] == 'pedra' and arg[2] == 'mais' and \
        isinstance(arg[3], tuple) and arg[3][0] == 3.14 and isinstance(arg[3][1], int) and \
        (arg[1] == '.O.' or arg[1] == '.X.' or arg[1] == '...')
        
def eh_pedra_branca(arg):
    return eh_pedra(arg) and arg[1] == '.O.'

def eh_pedra_preta(arg):
    return eh_pedra(arg) and arg[1] == '.X.'

def pedras_iguais(p1, p2):
    return eh_pedra(p1) and eh_pedra(p2) and p1[1] == p2[1]

def pedra_para_str(p):
    return p[1][1]

## FAN pedra!?!? 
def eh_pedra_jogador(pedra):
    return eh_pedra_branca(pedra) or eh_pedra_preta(pedra)

