from random import randint

## TAD goban
def cria_goban_vazio(n):
    if type(n) == int and n in (9, 13, 19):
        return [randint(0, 10**6), (n, {})]
    raise ValueError('cria_goban_vazio: argumento invalido')    

def cria_goban(n, ib, ip):
    if type(n) == int and n in (9, 13, 19):
        goban = cria_goban_vazio(n)
        if type(n) == int and n in (9, 13, 19) and \
            type(ib) == tuple and all(eh_intersecao(i) and eh_intersecao_valida(goban, i) for i in ib) and \
                type(ip) == tuple and all(eh_intersecao(i) and eh_intersecao_valida(goban, i) for i in ip):
                    for i in ib: 
                        if eh_pedra_jogador(obtem_pedra(goban, i)):
                            raise ValueError('cria_goban: argumentos invalidos')   
                        coloca_pedra(goban, i, cria_pedra_branca())
                    
                    for i in ip: 
                        if eh_pedra_jogador(obtem_pedra(goban, i)):
                            raise ValueError('cria_goban: argumentos invalidos')  
                        coloca_pedra(goban, i, cria_pedra_preta())
                    return goban
    
    raise ValueError('cria_goban: argumentos invalidos')   

def cria_copia_goban(tab):
    return [tab[0], (tab[1][0], tab[1][1].copy())]

# def obtem_tamanho(tab):
#     return tab[0]

def obtem_ultima_intersecao(tab):
    LETTERS = tuple('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return cria_intersecao(LETTERS[tab[1][0]-1], tab[1][0])

def obtem_pedra(tab, pos):
    if pos in tab[1][1]:
        return tab[1][1][pos]
    else:
        return cria_pedra_neutra()


def obtem_cadeia(board, pos):
    
    state = obtem_pedra(board, pos)
    last = obtem_ultima_intersecao(board)
    
    chain, to_check = [], [pos]
    
    while to_check:
        pos = to_check.pop()
        chain.append(pos)
        for new_pos in obtem_intersecoes_adjacentes(pos, last):
            if pedras_iguais(obtem_pedra(board, new_pos), state) and new_pos not in chain + to_check:
                to_check.append(new_pos)
                
    return ordena_intersecoes(tuple(chain))



def coloca_pedra(tab, pos, pedra):
    tab[1][1][pos] = pedra
    return tab

def remove_pedra(tab, pos):
    if pos in tab[1][1]:
        del tab[1][1][pos]
    return tab

def remove_cadeia(tab, tuplo):
    for pos in tuplo:
        remove_pedra(tab, pos)
    return tab


def eh_goban(arg):
    def intersecao_dentro_limites(i1, i2):
        return 'A' <= obtem_col(i1) <= obtem_col(i2) and 1 <= obtem_lin(i1) <= obtem_lin(i2)
    return isinstance(arg,list) and len(arg) == 2 and type(arg[0]) == int and \
        type(arg[1]) == tuple and len(arg[1]) == 2 and type(arg[1][0]) == int and arg[1][0] in (9, 13, 19) \
        and type(arg[1][1]) == dict and  all(eh_intersecao(k) for k in arg[1][1]) and \
            all(intersecao_dentro_limites(k, obtem_ultima_intersecao(arg)) for k in arg[1][1]) and \
                all(eh_pedra(arg[1][1][k]) for k in arg[1][1])
        # todaos os indexes são interseções, todas as intereseções são validas e todos os valores são pedras e todos 
        
def eh_intersecao_valida(tab, pos):
    def intersecao_dentro_limites(i1, i2):
        return 'A' <= obtem_col(i1) <= obtem_col(i2) and 1 <= obtem_lin(i1) <= obtem_lin(i2)
    return intersecao_dentro_limites(pos, obtem_ultima_intersecao(tab))

def gobans_iguais(g1, g2):
    if eh_goban(g1) and eh_goban(g2) and g1[1][0] == g2[1][0]: 
        if sorted(g1[1][1].keys()) == sorted(g2[1][1].keys()): # mesmas chaves
            return all(pedras_iguais(g1[1][1][k], g2[1][1][k]) for k in g1[1][1])
    return False

def goban_para_str(tab):    
    LETTERS = tuple('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    n_v, n_h = tab[1][0], tab[1][0]
    cad = '   ' + ''.join(f'{l} ' for l in LETTERS[:n_v]).rstrip() + '\n' 
    for i in range(n_h):
        cad += '{:>2} '.format(n_h-i)
        for j in LETTERS[:n_v]:
            cad += pedra_para_str(obtem_pedra(tab, cria_intersecao(j, n_h-i))) + ' '
        cad += '{:>2}'.format(n_h-i) + '\n'
        
    cad += '   ' + ''.join(f'{l} ' for l in LETTERS[:n_v]).rstrip()
    
    return cad
   


## FAN goban 

def obtem_adjacentes_diferentes(board, cadeia_pedras):
    
    if cadeia_pedras:
        state = obtem_pedra(board, cadeia_pedras[0])
        # eh_diferente = (lambda x:not pedras_iguais(x, neutral)) if pedras_iguais(state, neutral) else (lambda x: pedras_iguais(x, neutral))
        eh_diferente = (lambda x:not eh_pedra_jogador(x)) if eh_pedra_jogador(state) else eh_pedra_jogador
        
        liberdades = []
        
        for pos in cadeia_pedras:
            for new_pos in obtem_intersecoes_adjacentes(pos, obtem_ultima_intersecao(board)):
                if eh_diferente(obtem_pedra(board, new_pos)) and new_pos not in liberdades:
                    liberdades.append(new_pos)
                    
        return ordena_intersecoes(tuple(liberdades))
    return ()

def jogada(board, pos, pedra):
    coloca_pedra(board, pos, pedra)
    for new_pos in obtem_intersecoes_adjacentes(pos, obtem_ultima_intersecao(board)):
        outra_pedra = obtem_pedra(board, new_pos)
        if eh_pedra_jogador(outra_pedra) and not pedras_iguais(pedra, outra_pedra): #há uma pedra  adjacente de outro jogador
            cadeia = obtem_cadeia(board, new_pos)
            if len(obtem_adjacentes_diferentes(board, cadeia)) == 0:
                remove_cadeia(board, cadeia)
    return board
                    
def obtem_pedras_jogadores(board):
    LETTERS = tuple('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    num_b, num_p = 0, 0
    branca, preta = cria_pedra_branca(), cria_pedra_preta()
    
    # PERCORRER TODAS AS INTERSECOES
    last_pos = obtem_ultima_intersecao(board)
    last_h, last_v = LETTERS.index(obtem_col(last_pos)), obtem_lin(last_pos)
    
    for h in LETTERS[:last_h+1]:
        for v in range(1, last_v+1):
            pos = cria_intersecao(h, v)
            if pedras_iguais(branca, obtem_pedra(board, pos)):
                num_b+=1
            elif pedras_iguais(preta, obtem_pedra(board, pos)):
                num_p += 1
    return num_b, num_p



def obtem_territorios(board):
    LETTERS = tuple('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    all_cadeias, cadeias_seen = [], ()
    
    last_pos = obtem_ultima_intersecao(board)
    last_h, last_v = LETTERS.index(obtem_col(last_pos)), obtem_lin(last_pos)
    
    for h in LETTERS[:last_h+1]:
        for v in range(1, last_v+1):
            pos = cria_intersecao(h, v)
            if pedras_iguais(obtem_pedra(board, pos), cria_pedra_neutra()) and pos not in cadeias_seen:
                this_cadeia = obtem_cadeia(board, pos)
                all_cadeias.append(this_cadeia)
                cadeias_seen += this_cadeia
    
    # return all_cadeias            
    return tuple(sorted(all_cadeias, key=lambda x:(obtem_lin(x[0]), obtem_col(x[0]))))
