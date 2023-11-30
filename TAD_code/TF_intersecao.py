LETTERS = tuple('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

## TAD intersecao
def cria_intersecao(col, lin):
    if type(col) == str and len(col) == 1 and 'A' <= col <= 'S' \
        and type(lin) == int and  1 <= lin <= 19:
            return 'blabla', ('nothing',lin), (col,)
        
    raise ValueError("cria_intersecao: argumentos invalidos") 

def obtem_col(pos):
    return pos[2][0]

def obtem_lin(pos):
    return pos[1][1]

def eh_intersecao(arg):
    return type(arg) == tuple and len(arg) == 3 and arg[0] == 'blabla' \
        and type(arg[1]) == tuple and len(arg[1]) == 2 and arg[1][0] == 'nothing' \
            and type(arg[1][1]) == int and  1 <= arg[1][1] <= 19 \
                and type(arg[2]) == tuple and len(arg[2]) == 1 and type(arg[2][0]) == str and len(arg[2][0]) == 1 and  'A' <= arg[2][0] <= 'S'
                
def intersecoes_iguais(pos1, pos2):
    return eh_intersecao(pos1) and eh_intersecao(pos2) and obtem_col(pos1) == obtem_col(pos2) and obtem_lin(pos1) == obtem_lin(pos2)

def intersecao_para_str(pos):
    return f'{obtem_col(pos)}{obtem_lin(pos)}'

def str_para_intersecao(s):
    return cria_intersecao(s[0], int(s[1:]))

## FAN - TAD intersecao
def obtem_intersecoes_adjacentes(pos, last_pos):
    move = {
        'U': lambda x: 0 if obtem_lin(x) == obtem_lin(last_pos) else cria_intersecao(obtem_col(x), obtem_lin(x)+1),
        'D': lambda x: 0 if obtem_lin(x) == 1 else cria_intersecao(obtem_col(x), obtem_lin(x)-1),
        'L': lambda x: '' if obtem_col(x) == 'A' else cria_intersecao(LETTERS[LETTERS.index(obtem_col(x))-1], obtem_lin(x)),
        'R': lambda x: '' if obtem_col(x) == obtem_col(last_pos) else cria_intersecao(LETTERS[LETTERS.index(obtem_col(x))+1], obtem_lin(x))
    }
    return tuple(move[d](pos) for d in ('D', 'L', 'R', 'U') if move[d](pos))
    
def ordena_intersecoes(tup):
    return tuple(sorted(tup, key=lambda x:(obtem_lin(x), obtem_col(x))))
