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
        raise ValueError('cria_goban_vazio: argumento invalido')
    return tuple([0 for i in range(n)] for i1 in range(n))

def cria_goban(n,ib,ip):
    if n not in (9,13,19):
        raise ValueError('cria_goban_vazio: argumento invalido')
    g = cria_goban_vazio(n)
    for inter in ib:
        if not (eh_intersecao(inter) and obtem_lin(inter) <= n):
            raise ValueError('cria_goban: argumentos invalidos')
        g[COLUNAS.index(obtem_col(inter))][obtem_lin(inter)-1] = cria_pedra_branca()
    for inter in ip:
        if not (eh_intersecao(inter) and obtem_lin(inter) <= n):
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

def gobans_iguais(g1,g2):
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
        if (i+len(g[0])+1) > 9:
            gobanstr += str(i+len(g[0])+1)+' '
            for col in g:
                if col[i] == 0:
                    gobanstr += '.'+ ' '
                elif col[i] == 1:
                    gobanstr += 'O' + ' '
                else:
                    gobanstr += 'X' + ' '
            gobanstr += '' + str(i+len(g[0])+1)
        else:
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
        if obtem_pedra(g,cord) not in (cria_pedra_neutra(),p): # Verifica se a pedra pertence ao jogador contrário
            cadeia_adv = obtem_cadeia(g,cord)
            cadeiaadv_livre = False
            for coord in cadeia_adv:
                for pedra in obtem_intersecoes_adjacentes(coord, obtem_ultima_intersecao(g)):
                    if obtem_pedra(g,pedra) == cria_pedra_neutra():
                        cadeiaadv_livre = True
                        break
                if cadeiaadv_livre: # Se a cadeia for livre para a execução
                    break
            if not cadeiaadv_livre: # Se a cadeia não for livre, vai remove-la
                remove_cadeia(g,cadeia_adv)
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
    '''
    Calcula os pontos que cada jogador tem no atual estado do tabuleiro goban (g)

    Parameters:
            g(tuplo): O tabuleiro de jogo goban

    Returns:
            return(tuplo): Com os inteiros correspondetes aos pontos do jogador branco e preto respetivamente
    '''
    t = obtem_territorios(g)
    terreno_branco = ()   
    terreno_preto = ()
    pontos = obtem_pedras_jogadores(g)
    for terreno in t:
        temppedras =()
        for cord in obtem_adjacentes_diferentes(g,terreno):
            if cord not in temppedras:
                temppedras += (obtem_pedra(g,cord)),
        if len(temppedras) != 0:
            if not (cria_pedra_neutra() or cria_pedra_preta() in temppedras):
                terreno_branco += (terreno)
            if not (cria_pedra_neutra() or cria_pedra_branca() in temppedras):
                terreno_preto += (terreno)
    return (pontos[0]+len(terreno_branco), pontos[1]+len(terreno_preto))


def eh_jogada_legal(g,i,p,l): 
    '''
    Verifica se uma jogada é legal ou não, se é um interseção válida, se esta se encontra vazia, se não estamos perante suícidio, 
    ou repetição (ko) - após resolução o tabuleiro ficar no mesmo estado em que se encontrava

    Parameters:
            g(tuplo): O tabuleiro de jogo goban
            i(tuplo): As coordenadas da interseção onde é executada a jogada
            p(int): O tipo de pedra que está a ser jogada (ou seja qual o jogador que está a jogar)
            l(tuplo): O tabuleiro no estado anterior á resolução da jogada
    Returns:
            return(Boolean): Vai devolver True se a jogada for legal ou Falso caso contrário
    '''
    if not eh_intersecao_valida(g,i):
        return False
    if obtem_pedra(g,i) is not cria_pedra_neutra():
        return False
    gtemp = cria_copia_goban(g)
    jogada(gtemp,i,p)
    
    if gobans_iguais(gtemp,l):
        return False
    def obtem_liberdades_cadeia(g,cadeia):
         libertades = []
         for cord in cadeia:
            adj_intersecoes = obtem_intersecoes_adjacentes(cord, obtem_ultima_intersecao(g))
            for cordadj in adj_intersecoes:
                if obtem_pedra(g, cordadj) is cria_pedra_neutra():
                    if cordadj not in libertades:
                        libertades += (cordadj),
         return libertades
    cadeia = obtem_cadeia(gtemp, i)
    liberta = obtem_liberdades_cadeia(gtemp, cadeia)

    if not liberta:  
        return False  
    
    
    return True

def turno_jogador(g,p,l):
    '''
    O turno de cada jogador, retorna False caso o jogador passe a sua vez 'P' e retorna True se o jogador introduzir um movimento legal e
    modifica destrutivamente o goban. Esta função vai pedir uma nova tentativa enquanto o jogador não passar a vez ou fornecer uma interseção legal.

    Parameters:
            g(tuplo): O tabuleiro de jogo goban
            p(int): O tipo de pedra
            l(tuplo): O estado do tabuleiro antes da resolução da jogada atual
    Returns:
            return(Boolean): Fasle caso o jogador passe a vez e True caso contrário
    '''
    inter = input("Escreva uma intersecao ou 'P' para passar ["+pedra_para_str(p)+"]:")
    while inter != 'P':
        if eh_jogada_legal(g,str_para_intersecao(inter),p,l):
            jogada(g,str_para_intersecao(inter),p)
            return True
        else:
            inter = input("Escreva uma intersecao ou 'P' para passar ["+pedra_para_str(p)+"]:")
    if inter == 'P':
        return False   
    return True


def go(g,tb,tp):
    '''
    Função principal que premite a duas pessoas o jogar um jogo de goban completo

    Parameters:
            g(int): O tamanho do tabuleiro de goban pode ser 9*9 ou 13*13 pu 19*19 - (9,13,19)
            tb(tuplo): Conjunto das interseções ocupadas por pedras brancas inicialmente
            tp(tuplo): Conjunto das interseções ocupadas por pedras pretas inicialmente
    Return:
        print(goban_para_str): Escreve no terminal a cada mudança o tabuleiro de goban
        return(Boolean): True se o jogador branco ganhar e False caso contrário

    '''
    tbinter = tuple(str_para_intersecao(i) for i in tb)
    tpinter = tuple(str_para_intersecao(i) for i in tp)

    go = ()
    goant = (cria_goban_vazio(g))
    try:
        cria_goban(g,tbinter,tpinter)
    except ValueError:
        raise ValueError('go: argumentos invalidos')
    else:
        go = cria_goban(g,tbinter,tpinter)
        brancopass = False
        pretopass = False
        i = 0

    while not (brancopass and pretopass):
        pontos = calcula_pontos(go)
        print('Branco (O) tem',pontos[0],'pontos')
        print('Preto (X) tem',pontos[1],'pontos')
        print(goban_para_str(go))
        if i % 2 == 0:
            pretopass = not turno_jogador(go, cria_pedra_preta(), goant)
        else:
            brancopass = not turno_jogador(go, cria_pedra_branca(), goant)
        goant = cria_copia_goban(go)
        i += 1
    print('Branco (O) tem',pontos[0],'pontos')
    print('Preto (X) tem',pontos[1],'pontos')
    print(goban_para_str(go))

    if pontos[0] > pontos[1]:
        return True
    return False