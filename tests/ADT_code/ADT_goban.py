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
    
    raise ValueError('new_goban: invalid arguments')

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

def remove_stone(board, pos):
    if pos in board[1][1]:
        del board[1][1][pos]
    return board

def remove_stone_chain(board, tuple):
    for pos in tuple:
        remove_stone(board, pos)
    return board


def is_goban(arg):
    def intersection_inside_limits(i1, i2):
        return 'A' <= get_col(i1) <= get_col(i2) and 1 <= get_row(i1) <= get_row(i2)
    return isinstance(arg,list) and len(arg) == 2 and type(arg[0]) == int and \
        type(arg[1]) == tuple and len(arg[1]) == 2 and type(arg[1][0]) == int and arg[1][0] in (9, 13, 19) \
        and type(arg[1][1]) == dict and  all(is_intersection(k) for k in arg[1][1]) and \
            all(intersection_inside_limits(k, get_last_intersection(arg)) for k in arg[1][1]) and \
                all(is_stone(arg[1][1][k]) for k in arg[1][1])
        # todaos os indexes são interseções, todas as intereseções são validas e todos os valores são pedras e todos 
        
def is_valid_intersection(board, pos):
    def intersection_inside_limits(i1, i2):
        return 'A' <= get_col(i1) <= get_col(i2) and 1 <= get_row(i1) <= get_row(i2)
    return intersection_inside_limits(pos, get_last_intersection(board))

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
   
