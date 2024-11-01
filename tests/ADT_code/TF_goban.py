from random import randint

## ADT goban
def new_empty_goban(n):
    if type(n) == int and n in (9, 13, 19):
        return [randint(0, 10**6), (n, {})]
    raise ValueError('new_empty_goban: invalid arguments')

def new_goban(n, ib, ip):
    if type(n) == int and n in (9, 13, 19):
        goban = new_empty_goban(n)
        if type(n) == int and n in (9, 13, 19) and \
            type(ib) == tuple and all(is_intersection(i) and is_valid_intersection(goban, i) for i in ib) and \
                type(ip) == tuple and all(is_intersection(i) and is_valid_intersection(goban, i) for i in ip):
                    for i in ib:
                        if is_player_stone(get_stone(goban, i)):
                            raise ValueError('new_goban: invalid arguments')
                        set_stone(goban, i, new_white_stone())
                    
                    for i in ip:
                        if is_player_stone(get_stone(goban, i)):
                            raise ValueError('new_goban: invalid arguments')
                        set_stone(goban, i, new_black_stone())
                    return goban
    
    raise ValueError('new_goban: argumentos invalidos') 

def copy_goban(board):
    return [board[0], (board[1][0], board[1][1].copy())]

# def obtem_tamanho(tab):
#     return tab[0]

def get_last_intersection(board):
    LETTERS = tuple('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return new_intersection(LETTERS[board[1][0]-1], board[1][0])

def get_stone(board, pos):
    if pos in board[1][1]:
        return board[1][1][pos]
    else:
        return new_empty_stone()


def get_stone_chain(board, pos):
    
    state = get_stone(board, pos)
    last = get_last_intersection(board)
    
    chain, to_check = [], [pos]
    
    while to_check:
        pos = to_check.pop()
        chain.append(pos)
        for new_pos in get_adjacent_intersections(pos, last):
            if equals_stones(get_stone(board, new_pos), state) and new_pos not in chain + to_check:
                to_check.append(new_pos)
                
    return sort_intersections(tuple(chain))



def set_stone(board, pos, stone):
    board[1][1][pos] = stone
    return board

def remove_stone(tab, pos):
    if pos in tab[1][1]:
        del tab[1][1][pos]
    return tab

def remove_stone_chain(board, tuple):
    for pos in tuple:
        remove_stone(board, pos)
    return board


def is_goban(arg):
    def intersecao_dentro_limites(i1, i2):
        return 'A' <= get_col(i1) <= get_col(i2) and 1 <= get_row(i1) <= get_row(i2)
    return isinstance(arg,list) and len(arg) == 2 and type(arg[0]) == int and \
        type(arg[1]) == tuple and len(arg[1]) == 2 and type(arg[1][0]) == int and arg[1][0] in (9, 13, 19) \
        and type(arg[1][1]) == dict and  all(is_intersection(k) for k in arg[1][1]) and \
            all(intersecao_dentro_limites(k, get_last_intersection(arg)) for k in arg[1][1]) and \
                all(is_stone(arg[1][1][k]) for k in arg[1][1])
        # todaos os indexes são interseções, todas as intereseções são validas e todos os valores são pedras e todos 
        
def is_valid_intersection(board, pos):
    def intersecao_dentro_limites(i1, i2):
        return 'A' <= get_col(i1) <= get_col(i2) and 1 <= get_row(i1) <= get_row(i2)
    return intersecao_dentro_limites(pos, get_last_intersection(board))

def goban_equals(g1, g2):
    if is_goban(g1) and is_goban(g2) and g1[1][0] == g2[1][0]: 
        if sorted(g1[1][1].keys()) == sorted(g2[1][1].keys()): # mesmas chaves
            return all(equals_stones(g1[1][1][k], g2[1][1][k]) for k in g1[1][1])
    return False

def goban_to_str(board):  
    LETTERS = tuple('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    n_v, n_h = board[1][0], board[1][0]
    cad = '   ' + ''.join(f'{l} ' for l in LETTERS[:n_v]).rstrip() + '\n' 
    for i in range(n_h):
        cad += '{:>2} '.format(n_h-i)
        for j in LETTERS[:n_v]:
            cad += stone_to_str(get_stone(board, new_intersection(j, n_h-i))) + ' '
        cad += '{:>2}'.format(n_h-i) + '\n'
        
    cad += '   ' + ''.join(f'{l} ' for l in LETTERS[:n_v]).rstrip()
    
    return cad
   


## HLF goban 

def get_adjacents_different(board, stone_chain):
    
    if stone_chain:
        state = get_stone(board, stone_chain[0])
        # eh_diferente = (lambda x:not equals_stones(x, neutral)) if equals_stones(state, neutral) else (lambda x: equals_stones(x, neutral))
        eh_diferente = (lambda x:not is_player_stone(x)) if is_player_stone(state) else is_player_stone
        
        freedomns = []
        
        for pos in stone_chain:
            for new_pos in get_adjacent_intersections(pos, get_last_intersection(board)):
                if eh_diferente(get_stone(board, new_pos)) and new_pos not in freedomns:
                    freedomns.append(new_pos)
                    
        return sort_intersections(tuple(freedomns))
    return ()

def move(board, pos, stone):
    set_stone(board, pos, stone)
    for new_pos in get_adjacent_intersections(pos, get_last_intersection(board)):
        outra_pedra = get_stone(board, new_pos)
        if is_player_stone(outra_pedra) and not equals_stones(stone, outra_pedra): #há uma pedra  adjacente de outro jogador
            cadeia = get_stone_chain(board, new_pos)
            if len(get_adjacents_different(board, cadeia)) == 0:
                remove_stone_chain(board, cadeia)
    return board
                    
def get_player_stones(board):
    LETTERS = tuple('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    num_b, num_p = 0, 0
    branca, preta = new_white_stone(), new_black_stone()
    
    # PERCORRER TODAS AS INTERSECOES
    last_pos = get_last_intersection(board)
    last_h, last_v = LETTERS.index(get_col(last_pos)), get_row(last_pos)
    
    for h in LETTERS[:last_h+1]:
        for v in range(1, last_v+1):
            pos = new_intersection(h, v)
            if equals_stones(branca, get_stone(board, pos)):
                num_b+=1
            elif equals_stones(preta, get_stone(board, pos)):
                num_p += 1
    return num_b, num_p



def get_territories(board):
    LETTERS = tuple('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    all_stone_chains, seen_stone_chains = [], ()
    
    last_pos = get_last_intersection(board)
    last_h, last_v = LETTERS.index(get_col(last_pos)), get_row(last_pos)
    
    for h in LETTERS[:last_h+1]:
        for v in range(1, last_v+1):
            pos = new_intersection(h, v)
            if equals_stones(get_stone(board, pos), new_empty_stone()) and pos not in seen_stone_chains:
                this_cadeia = get_stone_chain(board, pos)
                all_stone_chains.append(this_cadeia)
                seen_stone_chains += this_cadeia
    
    # return all_cadeias            
    return tuple(sorted(all_stone_chains, key=lambda x:(get_row(x[0]), get_col(x[0]))))
