COLUNAS = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S')
LINHAS = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19)

#TAD intersecao
def cria_intersecao(col,lin): # Tem de ser alterado
    if not (col in COLUNAS and lin in LINHAS):
        raise ValueError('cria_intersecao: argumentos invalidos')
    return (col,lin)


def obtem_col(i):
    return i[0]


def obtem_lin(i):
    return i[1]


def eh_intersecao(arg): # Alterar usando o construtor
    return type(arg) == tuple and obtem_col(arg) in COLUNAS and obtem_lin(arg) in LINHAS

def intersecoes_iguais(i1,i2):
    if eh_intersecao(i1) and eh_intersecao(i2):
        return obtem_col(i1) == obtem_col(i2) and obtem_lin(i1) == obtem_lin(i2)
    return False


def intersecao_para_str(i):
    return obtem_col(i)+str(obtem_lin(i))

def str_para_intersecao(str):
    return cria_intersecao(str[0],int(str[1:])) 

#Funções de Alto nível que estão associadas a este TAD (intersecao)
def obtem_intersecoes_adjacentes(i,l):
    #Ordem de leitura (left to right, bottom  to top)
    interadj = ()
    if COLUNAS[COLUNAS.index(obtem_col(i))-1] in COLUNAS[:COLUNAS.index(obtem_col(l))]:
        interadj += (cria_intersecao(COLUNAS[COLUNAS.index(obtem_col(i))-1],obtem_lin(i))),
    if 0 < obtem_lin(i)-1 <= obtem_lin(l):
        interadj += (cria_intersecao(obtem_col(i),obtem_lin(i)-1)),
    if COLUNAS[COLUNAS.index(obtem_col(i))+1] in COLUNAS[:COLUNAS.index(obtem_col(l))+1]:
        interadj += (cria_intersecao(COLUNAS[COLUNAS.index(obtem_col(i))+1],obtem_lin(i))),
    if obtem_lin(i)+1 <= obtem_lin(l):
        interadj += (cria_intersecao(obtem_col(i),obtem_lin(i)+1)),
    return interadj
    
def ordena_intersecoes(t):
    return tuple(sorted((sorted(t,key= lambda t: t[0])), key= lambda i: i[1]))


#TAD pedra
#Pedra [0,()] O tuplo vazio corresponde à interseção onde se localiza a pedra
#0 --> pedra neutro
#1 --> pedra branco
#2 --> pedra preto

def cria_pedra_branca():
    return 1
def cria_pedra_preta():
    return 2
def cria_pedra_neutra():
    return 0

def eh_pedra(arg):
    return type(arg) == int and arg in (0,1,2)
def eh_pedra_branca(p):
    return p == 1
def eh_pedra_preta(p):
    return p== 2

def pedras_iguais(p1,p2):
    if eh_pedra(p1) and eh_pedra(p2):
        return p1 == p2
    return False

def pedra_para_str(p):
    switch = {
        0:'.',
        1:'O',
        2:'X'
    }
    return switch[p]

#Funções de Alto nível que estão associadas a este TAD (pedra)
def eh_pedra_jogador(p):
    return eh_pedra_branca(p) or eh_pedra_preta(p)
   


#TAD goban
#O tabuleiro vai ser representado por uma tuplo de listas ([],[],[])
def cria_goban_vazio(n):
    if n not in (9,13,19):
        raise ValueError('cria_goban_vazio: argumentos invalido')
    return tuple([0 for i in range(n)] for i1 in range(n))

def cria_goban(n,ib,ip):
    if n not in (9,13,19):
        raise ValueError('cria_goban_vazio: argumentos invalido')
    g = cria_goban_vazio(n)
    for inter in ib:
        if not eh_intersecao(inter):
            raise ValueError('cria_goban: argumentos invalidos')
        g[COLUNAS.index(obtem_col(inter))][obtem_lin(inter)-1] = cria_pedra_branca()
    for inter in ip:
        if not eh_intersecao(inter):
            raise ValueError('cria_goban: argumentos invalidos')
        g[COLUNAS.index(obtem_col(inter))][obtem_lin(inter)-1] = cria_pedra_preta()
    return g

def cria_copia_goban(t):
    tcopy = []
    for l in t:
        tcopy += [l.copy()]
    return tuple(tcopy)

def obtem_ultima_intersecao(g):
    return (COLUNAS[len(g)-1],len(g[-1]))

def obtem_pedra(g,i):
    return (g[COLUNAS.index(obtem_col(i))][obtem_lin(i)-1])


def obtem_cadeia(g,i):
    tipo = g[COLUNAS.index(obtem_col(i))][obtem_lin(i)-1]
    igual, inter, cadeia= (i,), (), ()
    while len(igual) > 0: 
        testcoord = igual[-1] 
        cadeia += (testcoord,)
        interigualtemp = ()
        for el in obtem_intersecoes_adjacentes(testcoord,obtem_ultima_intersecao(g)):
            if el not in inter and g[COLUNAS.index(obtem_col(el))][obtem_lin(el)-1] == tipo:
                interigualtemp += (el,)
                inter += (el,)
        igual = igual[:-1] + interigualtemp 
    cadeiafinal = []
    for el in cadeia:
        if el not in cadeiafinal:
            cadeiafinal += [el]
    return tuple(ordena_intersecoes(cadeiafinal)) 

def coloca_pedra(g,i,p):
    g[COLUNAS.index(obtem_col(i))][obtem_lin(i)-1] = p
    return g

def remove_pedra(g,i,):
    g[COLUNAS.index(obtem_col(i))][obtem_lin(i)-1] = 0
    return g

def remove_cadeia(g,t):
    for inter in t:
        g[COLUNAS.index(obtem_col(inter))][obtem_lin(inter)-1] = 0
    return g

def eh_goban(arg):
    if type(arg) == tuple and type(arg[0]) == list:
        if len(arg) in LINHAS and len(arg[0]) in LINHAS:
            for col in range(len(arg)):
                if len(arg[col]) == len(arg[col-1]):
                    for el in arg[col]:
                        if el in (0,1,2):
                            return True
    return False

def eh_intersecao_valida(g,i):
    if eh_goban(g) and eh_intersecao(i):
        if COLUNAS.index(obtem_col(i)) in range(len(g)) and obtem_lin(i)-1 in range(len(g[COLUNAS.index(obtem_col(i))])):
            return True
    return False

def goban_iguais(g1,g2):
    if eh_goban(g1) and eh_goban(g2) and len(g1) == len(g2):
        for icol in range(len(g1)):
            for irow in range(len(g1[icol])):
                if g1[icol][irow] != g2[icol][irow]:
                    return False
    return True
   


def goban_para_str(g):
    gobanstr = '  '
    for icol in range(len(g)):
        gobanstr += ' ' + COLUNAS[icol]
    i = -1
    gobanstr += '\n'
    while i >= -len(g[0]):
        gobanstr += ' ' + str(i+len(g[0])+1) + ' '
        for col in g:
            if col[i] == 0:
                gobanstr += '.'+ ' '
            elif col[i] == 1:
                gobanstr += 'O' + ' '
            else:
                gobanstr += 'X' + ' '
        gobanstr += ' ' + str(i+len(g[0])+1)
        gobanstr += '\n'
        i -= 1
    gobanstr += '  '
    for icol in range(len(g)):
        gobanstr += ' ' + COLUNAS[icol]
    return gobanstr

#Funções de Alto nível que estão associadas a este TAD (goban)
def obtem_territorios(g):
    terr = ()
    inter = ()
    for icol in range(len(g)):
        for irow in range(len(g[icol])):
            if cria_intersecao(COLUNAS[icol],irow+1) not in inter:
                if g[icol][irow] == 0:
                    nterr = obtem_cadeia(g,cria_intersecao(COLUNAS[icol],irow+1))
                    if nterr not in terr:
                        terr += (nterr,)
                        inter += nterr
    
    return terr   #Tem de ser ordenado no interrior por ordem de leitura e no exterior por menor para maior

def obtem_adjacentes_diferentes(g,t):
    adj = ()
    for inter in t:
        if eh_pedra_jogador(obtem_pedra(g,inter)):
            for cord in obtem_intersecoes_adjacentes(inter, obtem_ultima_intersecao(g)):
                if obtem_pedra(g,cord) not in (cria_pedra_branca(), cria_pedra_preta()):
                    if cord not in adj:
                        adj+= (cord),
        if not eh_pedra_jogador(obtem_pedra(g,inter)):
            for cord in obtem_intersecoes_adjacentes(inter, obtem_ultima_intersecao(g)):
                 if obtem_pedra(g,cord) in (cria_pedra_branca(), cria_pedra_preta()):
                    if cord not in adj:
                        adj+= (cord),
    return ordena_intersecoes(adj)

def jogada(g,i,p):
     coloca_pedra(g,i,p)    
     for cord in obtem_intersecoes_adjacentes(i,obtem_ultima_intersecao(g)):
         if obtem_pedra(g,cord) not in (0,p):
             remove_cadeia(g,obtem_cadeia(g,cord))
     return g
         

def obtem_pedras_jogadores(g):
    cadia_branco = ()
    cadeia_preto =()
    for icol in range(len(g)):
        for irow in range(len(g[icol])):
            for cord in obtem_cadeia(g,cria_intersecao(COLUNAS[icol],irow+1)):
                if eh_pedra_branca(obtem_pedra(g,cord)):
                    if cord not in cadia_branco:
                        cadia_branco += (cord),
                elif eh_pedra_preta(obtem_pedra(g,cord)):
                    if cord not in cadeia_preto:
                        cadeia_preto += (cord),
    return (len(cadia_branco),len(cadeia_preto))


#Funções adicionais
def calcula_pontos(g):
    t = obtem_territorios(g)
    terreno_branco = ()   
    terreno_preto = ()
    pontos = obtem_pedras_jogadores(g)
    for terreno in t:
        tempcord =()
        for cord in obtem_adjacentes_diferentes(g,terreno):
            if cord not in tempcord:
                tempcord += (obtem_pedra(g,cord)),
        if not (cria_pedra_neutra() or cria_pedra_preta() in tempcord):
            terreno_branco += (terreno)
        if not (cria_pedra_neutra() or cria_pedra_branca() in tempcord):
            terreno_preto += (terreno)
    return (pontos[0]+len(terreno_branco), pontos[1]+len(terreno_preto))


def eh_jogada_legal(g,i,p,l):
    value = True
    if not eh_intersecao_valida(g,i):
        value = False
    if obtem_pedra(g,i) is not cria_pedra_neutra():
        value = False
    gtemp = cria_copia_goban(g)
    jogada(gtemp,i,p)
    for cord in obtem_cadeia(gtemp,i):
        for pedra in obtem_intersecoes_adjacentes(cord,obtem_ultima_intersecao(gtemp)):
            if obtem_pedra(gtemp,pedra) not in (cria_pedra_neutra(),p):   #FIXME
                value = False
    if goban_iguais(gtemp,l):
        value = False
    
    return value

def turno_jogador():
    pass

def go():
    pass

    
    

#Ser jogada legal estar fora do território ou posição ocupada, ver se é situiação de suicidio