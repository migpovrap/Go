COLUNAS = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S')
LINHAS = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19)

#TAD intersecao
def cria_intersecao(col:str,lin:int) -> tuple:
    '''
    Construtor de Interseção, devolve uma interseção caso os argumentos dados cumpram as seguintes validades,
    a col seja um caracter e a lin seja um inteiro.

    Parameters:
            col(str): Um caracter que para o jogo do goban neste caso tem de ser entre A-Z
            lin(int): Um inteiro que corresponde a linha, para o jogo goban neste caso tem de ser entre 1 e 19
    Returns:
            return: devolve a interseção 
            ValueError: ('cria_intersecao: argumentos invalidos) - caso os argumentos não possam ser validados

    '''
    if type(col) == str and type(lin) == int:
            if col in COLUNAS and lin in LINHAS:
                return (col,lin)
            else:
                raise ValueError('cria_intersecao: argumentos invalidos')
    else:
        raise ValueError('cria_intersecao: argumentos invalidos')
              

def obtem_col(i:tuple) -> str: 
    '''
    Função para obter a coluna de uma interseção

    Parameters:
            i(tuple): A interseção
    Returns:
            return: Devolve a clouna da interseção
    '''
    return i[0]


def obtem_lin(i:tuple) -> int:
    '''
    Função para obter a linha de uma interseção

    Parameters:
            i(tuple): A interseção
    Returns:
            return: Devolve a linha da interseção
    '''
    return i[1]


def eh_intersecao(arg) -> bool:
    '''
    Determina se um determinado argumento é uma interseção ou não.

    Parameters:
            arg(any): O argumento a testar
    Returns:
            return(Boolean): Caso se trate de uma interseção vai devolver True em caso contrário Falso
    '''
    if type(arg) == tuple or (type(arg) == str and len(arg) == 2):
        try:
            cria_intersecao(obtem_col(arg),obtem_lin(arg))
        except ValueError:
            return False
        else:
            return True
    else:
        return False   
    
    

def intersecoes_iguais(i1:tuple,i2:tuple) -> bool:
    '''
    Verifica se duas interseções são iguais.

    Parameters:
            i1(tuplo): A primeira interseção
            i2(tuplo): A segunda interseção
    Returns:
            return(Boolean): Se as interseções forem iguais devolve True caso contrário devolve Falso
    '''
    if eh_intersecao(i1) and eh_intersecao(i2):
        return obtem_col(i1) == obtem_col(i2) and obtem_lin(i1) == obtem_lin(i2)
    return False


def intersecao_para_str(i:tuple) -> str:
    '''
    Transoforma uma interseção no seu formato interno para a sua representação externa.

    Parameters:
            i(tuplo): Uma interseção
    Returns:
            return(str): Devolve a string que representa externamente uma interseção
    '''
    return obtem_col(i)+str(obtem_lin(i))


def str_para_intersecao(str:str):
    '''
    Transforma a representação externa de uma interseção na representação interna.

    Parameters:
            str(string): A string que representa a externa de uma interseção
    Returns:
            return(intersecao): A representação interna da interseção usando o construtor
    '''
    return cria_intersecao(str[0],int(str[1:])) 


#Funções de Alto nível que estão associadas a este TAD (intersecao)
#Ordem de leitura (left to right, bottom  to top)

def obtem_intersecoes_adjacentes(i,l):
    '''
    Obtem as interseções que se encontram nas posições adjacentes a uma detreminada interseção, sendo que estas de encontram para cima, baixo, esquerda ou direita.

    Parameters:
            i(tupel): A interseção 
            l(tuple): A última interseção(canto superior direito) do tabuleiro de goban que estamos a considerar
    Returns:
            return(tupel): Um tuplo que contem as interseções adjacentes por ordem de leitura
    '''
    interadj = ()
    if obtem_col(l) not in COLUNAS: # Se a letra não se encontrar nas permitadas (A-S), devolve vazio
        return ()
    if obtem_col(i) in COLUNAS[:COLUNAS.index(obtem_col(l))+1] and obtem_lin(i) in range(1,obtem_lin(l)+1): #Ve se a interseção dada se encontra dentro do atual goban, tamanho estabelecido pela interseção do canto superior direito
        if 0 < obtem_lin(i)+1 <= obtem_lin(l): #Verifica se a interseção a cima se enontra nos limites estabelecidos por l
            interadj += (cria_intersecao(obtem_col(i),obtem_lin(i)+1)),
        if 0 < obtem_lin(i)-1 <= obtem_lin(l): #Verifica se a interseção em baixo se enontra nos limites estabelecidos por l
            interadj += (cria_intersecao(obtem_col(i),obtem_lin(i)-1)),
        if 0 <= COLUNAS.index(obtem_col(i))+1  <= COLUNAS.index(obtem_col(l)): #Verifica se a interseção a direita se encontra dentro dos limites de l 
            interadj += (cria_intersecao(COLUNAS[COLUNAS.index(obtem_col(i))+1],obtem_lin(i))),
        if 0 <= COLUNAS.index(obtem_col(i))-1 <= COLUNAS.index(obtem_col(l)): #Verifica se a interseção a esquerda se encontra dentro dos limites de l 
            interadj += (cria_intersecao(COLUNAS[COLUNAS.index(obtem_col(i))-1],obtem_lin(i))),
    return ordena_intersecoes(interadj)
    
def ordena_intersecoes(t):
    '''
    Ordena o tuplo fornecido de interseções de acordo com a ordem de leitura do tabuleiro de Goban.

    Parameters:
            t(tuplo): O tuplo de interseções
    Returns:
            return(tuplo): O mesmo tuplo mas com as interseções ordenadas
    '''
    return tuple(sorted((sorted(t,key= lambda t: t[0])), key= lambda i: i[1]))


#TAD pedra
#0 --> pedra neutro
#1 --> pedra branco
#2 --> pedra preto

def cria_pedra_branca() -> int:
    '''
    O construtor da pedra branca.

    Returns:
            return(int): A repersentação interna da pedra branca
    '''
    return 1

def cria_pedra_preta() -> int:
    '''
    O construtor da pedra preta.

    Returns:
            return(int): A repersentação interna da pedra preta
    '''
    return 2

def cria_pedra_neutra() -> int:
    '''
    O construtor da pedra neutra.

    Returns:
            return(int): A repersentação interna da pedra neutra
    '''
    return 0

def eh_pedra(arg:int) -> bool:
    '''
    Verifica se o argumento fornecido é uma pedra de acordo com a representação interna

    Returns:
            return(Boolean): Devolve True se o argumento for uma pedra e False caso contrário 
    '''
    return type(arg) == int and arg in (0,1,2)

def eh_pedra_branca(p:int) -> bool:
    '''
    Verifica se o argumento fornecido é uma pedra branca de acordo com a representação interna

    Returns:
            return(Boolean): Devolve True se o argumento for uma pedra branca e False caso contrário 
    '''
    return p == 1

def eh_pedra_preta(p:int) -> bool:
    '''
    Verifica se o argumento fornecido é uma pedra preta de acordo com a representação interna

    Returns:
            return(Boolean): Devolve True se o argumento for uma pedra preta e False caso contrário 
    '''
    return p== 2

def pedras_iguais(p1:int,p2:int) -> bool:
    '''
    Verifica se as duas pedras fornecidas são iguais.

    Parameters:
            p1(int): A primeira pedra
            p2(int): A segunda pedra
    Returns:
            return(Boolean): Devolve True se as duas pedras forem iguais e False caso contrário
    '''
    if eh_pedra(p1) and eh_pedra(p2):
        return p1 == p2
    return False

def pedra_para_str(p:int) -> str:
    '''
    Transforma a representação interna de pedra para a representação externa de pedra.

    Parameters:
            p(int): A representação interna da pedra
    Returns:
            pedras(string): A representação externa da pedra
    '''
    pedras = {
        0:'.',
        1:'O',
        2:'X'
    }
    return pedras[p]

#Funções de Alto nível que estão associadas a este TAD (pedra)
def eh_pedra_jogador(p):
    '''
    Verifica se uma pedra pertence a um jogador ou é um pedra neutra.

    Parameters:
            p(): A pedra em questão
    Returns:
            return(Boolean): Devolve True caso a pedra pertenca a um jogador e False caso não pertenca
    '''
    return eh_pedra_branca(p) or eh_pedra_preta(p)
   


#TAD goban
#O tabuleiro vai ser representado por uma tuplo de listas ([],[],[])
def cria_goban_vazio(n:int):
    '''
    Cria um goban com o tamanho pertendido, seja 9x9, 13,13 ou 19x19.

    Parameters:
            n(int): O tamanho do tabuleiro de Goban pertendido
    Returns:
            return(tuple): O tabuleiro de Goban
    '''
    if type(n) == int and n in (9,13,19):
        return tuple([0 for i in range(n)] for i1 in range(n)) #Gera um tuplo de listas com os valores correspondentes a representação interna do goban
    else:
        raise ValueError('cria_goban_vazio: argumento invalido')

def cria_goban(n:int,ib:tuple,ip:tuple):
    '''
    Cria um goban com o tamanho pretendido e coloca-o no estado indicado com pedras brancas de pretas.

    Parameters:
            n(int): O tamanho do tabuleiro de Goban pertendido
            ib(tuple): O tuplo das interseções ocupadas por pedras brancas
            ip(tuple):  O tuplo das interseções ocupadas por pedras pretas
    '''
    try:
        cria_goban_vazio(n)
    except ValueError:
        raise ValueError('cria_goban: argumentos invalidos')
    else:
        g = cria_goban_vazio(n)
        if  not type(ib) == tuple:
            raise ValueError('cria_goban: argumentos invalidos')
        intervist = () # As interseções ja visitadas(de forma a detetar se a mesma interseção existe várias vezes)
        for inter in ib:
            if inter in ip or inter in intervist:
                raise ValueError('cria_goban: argumentos invalidos')
            else:
                if not (eh_intersecao(inter) and obtem_lin(inter) <= n and obtem_col(inter) in COLUNAS[:n]): #Verifica se é uma interseção e se encontra dentro do goban estabelecido
                    raise ValueError('cria_goban: argumentos invalidos')
                g[COLUNAS.index(obtem_col(inter))][obtem_lin(inter)-1] = cria_pedra_branca()
            intervist += (inter),
        if not type(ip) == tuple:
            raise ValueError('cria_goban: argumentos invalidos')
        intervist = () # As interseções ja visitadas(de forma a detetar se a mesma interseção existe várias vezes)
        for inter in ip:
            if inter in ib or inter in intervist:
                raise ValueError('cria_goban: argumentos invalidos')
            else:
                if not (eh_intersecao(inter) and obtem_lin(inter) <= n and obtem_col(inter) in COLUNAS[:n]): #Verifica se é uma interseção e se encontra dentro do goban estabelecido
                    raise ValueError('cria_goban: argumentos invalidos')
                g[COLUNAS.index(obtem_col(inter))][obtem_lin(inter)-1] = cria_pedra_preta()
            intervist += (inter),
    return g

def cria_copia_goban(t):
    '''
    Cria uma cópia independe do tabuleiro de Goban

    Parameters:
            t(tuple): O Tabuleiro de Goban
    Returns:
            return(tuple): Uma cópia independente do tabuleiro de Goban
    '''
    tcopy = []
    for l in t:
        tcopy += [l.copy()]
    return tuple(tcopy)

def obtem_ultima_intersecao(g) -> tuple:
    '''
    Obtem a última interseção de um determinado tabuleiro de Goban, ou seja a interseção do canto superior direito.

    Parameters:
            g(tuple): O tabuleiro de Goban
    Returns:
            return(tuple): A interseção correspondente
    '''
    return (COLUNAS[len(g)-1],len(g[-1]))

def obtem_pedra(g,i):
    '''
    Devolve a representação interna da pedra.

    Parameters:
            g(tuple): O tabuleiro de Goban
            i(tuple): A interseção da qual queremos obter a pedra
    '''
    return (g[COLUNAS.index(obtem_col(i))][obtem_lin(i)-1])


def obtem_cadeia(g,i):
    '''
    Obtem a cadeia de pedras que passam pela interseção dada, caso a posição se encontre vazia
    devolve a cadeia de posições livres.

    Parameters:
            g(tuplo): O tabuleiro de Goban
            i(tuplo): A interseção em questão
    Returns:
            return(tuplo): O tuplo formando pelas interseções da cadeia que passa na interseção fornecida

    '''
    tipo = g[COLUNAS.index(obtem_col(i))][obtem_lin(i)-1] # o tipo de pedra da interseção pretendida
    igual, inter, cadeia= (i,), (), ()
    while len(igual) > 0: 
        testcoord = igual[-1] 
        cadeia += (testcoord,)
        interigualtemp = ()
        for el in obtem_intersecoes_adjacentes(testcoord,obtem_ultima_intersecao(g)):
            if el not in inter and pedras_iguais(g[COLUNAS.index(obtem_col(el))][obtem_lin(el)-1],tipo):
                interigualtemp += (el,)
                inter += (el,) #As interseções que cumprem os requesitos
        igual = igual[:-1] + interigualtemp # A interseção que foi testada é retirada e adiciona-se as próximas que cumpriam os requesitos
    cadeiafinal = []
    for el in cadeia:
        if el not in cadeiafinal: # Retira elementos repeditos da cadeia
            cadeiafinal += [el]
    return tuple(ordena_intersecoes(cadeiafinal)) 


def coloca_pedra(g,i,p):
    '''
    Coloca a pedra numa derterminada interseção no tabuleiro de Goban.

    Parameters:
            g(tuplo): O Tabuleiro de Goban
            i(tuplo): A interseção onde colocar a pedra
            p(int): O tipo de pedra a colocar, ou seja o jogador que efetua a ação
    Returns:
            g(tuplo): Vai modificar destrutivamente o Tabuleiro de Goban
    '''
    g[COLUNAS.index(obtem_col(i))][obtem_lin(i)-1] = p
    return g


def remove_pedra(g,i,):
    '''
    Remove a pedra numa derterminada interseção no tabuleiro de Goban.

    Parameters:
            g(tuplo): O Tabuleiro de Goban
            i(tuplo): A interseção onde remover a pedra
    Returns:
            g(tuplo): Vai modificar destrutivamente o Tabuleiro de Goban
    '''
    g[COLUNAS.index(obtem_col(i))][obtem_lin(i)-1] = 0
    return g


def remove_cadeia(g,t):
    '''
    Remove uma determinada cadeia do tabuleiro de Goban.

    Parameters:
            g(tuplo): O Tabuleiro de Goban
            t(tuplo): O conjunto de interseções que formam a cadeia a ser removida
    Returns:
            g(tuplo): Vai modificar destrutivamente o Tabuleiro de Goban
    '''
    for inter in t:
        remove_pedra(g,inter)
    return g


def eh_goban(arg) -> bool:
    '''
    Verifica se o argumento fornecido é um goban.

    Parameters:
            arg(tuple): O argumento para verificar se se trata de um goban
    Returns:
            return(Boolean): Devolve True se o argumento for um goban e False em caso contrário
    '''
    if type(arg) == tuple and type(arg[0]) == list:
        if len(arg) in (9,13,19) and len(arg[0]) in (9,13,19):
            for col in range(len(arg)):
                if len(arg[col]) == len(arg[col-1]):
                    if len(arg) == len(arg[col]):
                        for el in arg[col]:
                            if el in (0,1,2):
                                return True
    return False


def eh_intersecao_valida(g,i) -> bool:
    '''
    Verifica se os argumentos fornecidos são válidos e posteriormente verifica se a interseção fornecida existe no Tabuleiro de Goban.

    Parameters:
            g(tuple): O tabuleiro de Goban
            i(tuple): A interseção para testar
    Returns:
            return(Boolean): Devolve True caso os argumentos sejam válidos e a interseção pertenca ao tabuleiro de goban e False em caso contrário
    '''
    if eh_goban(g) and eh_intersecao(i):
        if COLUNAS.index(obtem_col(i)) in range(len(g)) and obtem_lin(i)-1 in range(len(g[COLUNAS.index(obtem_col(i))])):
            return True
    return False


def gobans_iguais(g1,g2) -> bool:
    '''
    Verifica se os dois Goban são iguais.

    Parameters:
            g1(tuplo): O primeiro tabuleiro de Go
            g2(tuplo): O segundo tabuleiro de Go
    Returns:
            return(Boolean): Devolve True se os dois Gobans forem iguais e False em caso contrário
    '''
    if eh_goban(g1) and eh_goban(g2):
        if len(g1) == len(g2):
            for icol in range(len(g1)):
                for irow in range(len(g1[icol])):
                    if not pedras_iguais(g1[icol][irow], g2[icol][irow]):
                        return False
        else:
            return False
    else:
        return False
    return True
               

def goban_para_str(g) -> str:
    '''
    Transforma a representação interna do tabuleiro de goban na representação externa.

    Parameters:
            g(tuple): O tabuleiro de Goban
    Returns:
            return(string): A representação externa do tabuleiro de Gobans
    '''
    gobanstr = '  '
    for icol in range(len(g)): #Adiciona as letras das colunas na parte de cima
        gobanstr += ' ' + COLUNAS[icol]
    i = -1
    gobanstr += '\n'
    while i >= -len(g[0]):
        if (i+len(g[0])+1) > 9: # Para quando o valor da linha é maior que 9 a formatação é diferente 
            gobanstr += str(i+len(g[0])+1)+' ' #Adiciona o número da linha e os espaços necessários
            for col in g:
                if pedras_iguais(col[i], cria_pedra_neutra()):
                    gobanstr += pedra_para_str(col[i])+ ' ' #Adiciona a pedra correspondente
                elif pedras_iguais(col[i], cria_pedra_branca()):
                    gobanstr += pedra_para_str(col[i]) + ' '
                else:
                    gobanstr += pedra_para_str(col[i]) + ' '
            gobanstr += '' + str(i+len(g[0])+1) 
        else: # Quando o valor da linha é menor ou igual a 9
            gobanstr += ' ' + str(i+len(g[0])+1) + ' ' #Adiciona o número da linha e os espaços necessários 
            for col in g:
                if pedras_iguais(col[i],cria_pedra_neutra()):
                    gobanstr += pedra_para_str(col[i]) + ' ' #Adiciona a pedra correspondente
                elif pedras_iguais(col[i], cria_pedra_branca()):
                    gobanstr += pedra_para_str(col[i]) + ' '
                else:
                    gobanstr += pedra_para_str(col[i]) + ' '
            gobanstr += ' ' + str(i+len(g[0])+1)
        gobanstr += '\n'
        i -= 1
    gobanstr += '  '
    for icol in range(len(g)): #Adiciona as letras das colunas na parte de baixo
        gobanstr += ' ' + COLUNAS[icol]
    return gobanstr


#Funções de Alto nível que estão associadas a este TAD (goban)
def obtem_territorios(g) -> tuple:
    '''
    Obtem os territórios que existem num determinado tabuleiro de Goban, quer pertenção a um determinado jogador ou não.

    Parameters:
            g(tuple): O tabuleiro de goban
    Returns:
            return(tuple): Um tuplo formado pelos tuplos que cotém as interseções que formam cada território
    '''
    terr = ()
    inter = ()
    for icol in range(len(g)):
        for irow in range(len(g[icol])):
            if cria_intersecao(COLUNAS[icol],irow+1) not in inter: #Verifica se a interseção já foi visitada
                if pedras_iguais(g[icol][irow], cria_pedra_neutra()):
                    nterr = obtem_cadeia(g,cria_intersecao(COLUNAS[icol],irow+1))
                    if nterr not in terr:
                        terr += (nterr,) #Adiciona o terreno se este cumpre os requesitos
                        inter += nterr #Marca todas as interseções já visitadas, para não existirem repetições
    
    return tuple(sorted(terr, key= lambda i: i[0][1] ))  #Tem de ser ordenado no interrior por ordem de leitura e no exterior por menor para maior


def obtem_adjacentes_diferentes(g,t) -> tuple:
    '''
    Obtem o conjunto de interseções adjacentes a um determinado território.

    Parameters:
            g(tuplo): O tabuleiro de Goban
            t(tuplo): O território em questão
    Returns:
            adj(tuplo): O conjunto das interseções adjacentes diferentes ou seja a fronteira do determinado território
    '''
    adj = ()
    for inter in t:
        if eh_pedra_jogador(obtem_pedra(g,inter)): #Para quando é uma pedra pertencente a um jogador
            for cord in obtem_intersecoes_adjacentes(inter, obtem_ultima_intersecao(g)):
                if obtem_pedra(g,cord) not in (cria_pedra_branca(), cria_pedra_preta()):
                    if cord not in adj:
                        adj+= (cord),
        if not eh_pedra_jogador(obtem_pedra(g,inter)): #Para quando é uma interseção livre, perdra neutra
            for cord in obtem_intersecoes_adjacentes(inter, obtem_ultima_intersecao(g)):
                 if obtem_pedra(g,cord) in (cria_pedra_branca(), cria_pedra_preta()):
                    if cord not in adj:
                        adj+= (cord),
    return ordena_intersecoes(adj)


def jogada(g,i,p):
     '''
     A função que é usada para executar uma jogada, vai colocar a pedra na posição pedida e efetuar a captura das pedras inimigas se necessário.

     Parameters:
            g(tuplo): O tabuleiro do Goban
            i(tuplo): A interseção onde vai ser excutada a jogada
            p(int): O tipo de pedra que vai efetuar a jogada
    Returns:
            g(tuplo): Devolve o próprio tabuleiro Goban, modificando-o de forma destrutiva
     '''
     coloca_pedra(g,i,p)  
     for cord in obtem_intersecoes_adjacentes(i,obtem_ultima_intersecao(g)):
        if obtem_pedra(g,cord) not in (cria_pedra_neutra(),p): # Verifica se a pedra pertence ao jogador contrário
            cadeia_adv = obtem_cadeia(g,cord)
            cadeiaadv_livre = False
            for coord in cadeia_adv:
                for pedra in obtem_intersecoes_adjacentes(coord, obtem_ultima_intersecao(g)):
                    if pedras_iguais(obtem_pedra(g,pedra),cria_pedra_neutra()):
                        cadeiaadv_livre = True
                        break
                if cadeiaadv_livre: # Se a cadeia for livre para a execução
                    break
            if not cadeiaadv_livre: # Se a cadeia não for livre, vai remove-la
                remove_cadeia(g,cadeia_adv)
     return g
         

def obtem_pedras_jogadores(g) -> tuple:
    '''
    Vai contar o número de interseções ocupadas por pedras de cada jogador.

    Parameters:
            g(tuplo): O tabuleiro de Goban
    Returns:
            return(tuplo): Um tuplo que contém o número de pedras do jogador branco e preto respetivamente (nb,np)

    '''
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
def calcula_pontos(g) -> tuple:
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
    return (pontos[0]+len(terreno_branco), pontos[1]+len(terreno_preto)) #Os pontos de cada jogador são a soma dos seus terrenos e do número de pedras que têm no território


def eh_jogada_legal(g,i,p,l) -> bool: 
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
    def obtem_liberdades_cadeia(g,cadeia): #Função auxiliar para obter as liberdades de cada cadeia, se não tiver liberdades a lista devolvida é vazia
         libertades = []
         for cord in cadeia:
            adj_intersecoes = obtem_intersecoes_adjacentes(cord, obtem_ultima_intersecao(g))
            for cordadj in adj_intersecoes:
                if obtem_pedra(g, cordadj) == cria_pedra_neutra():
                    if cordadj not in libertades:
                        libertades += (cordadj),
         return libertades
    if not obtem_liberdades_cadeia(gtemp, obtem_cadeia(gtemp, i)):  # Se a lista libedades estiver vazia então esta fica sem liberdades e a jogada é ilegal retona False
        return False  
    return True


def turno_jogador(g,p,l) -> bool:
    '''
    O turno de cada jogador, retorna False caso o jogador passe a sua vez 'P' e retorna True se o jogador introduzir um movimento legal e
    modifica destrutivamente o goban. Esta função vai pedir uma nova tentativa enquanto o jogador não passar a vez ou fornecer uma interseção legal.

    Parameters:
            g(tuplo): O tabuleiro de jogo goban
            p(int): O tipo de pedra
            l(tuplo): O estado do tabuleiro antes da resolução da jogada atual
    Returns:
            return(Boolean): Fasle caso o jogador passe a vez e True caso contrário
            g(tuplo): Modifica destrutivamente o tabuleiro de Goban
    '''
    inter = input("Escreva uma intersecao ou 'P' para passar ["+pedra_para_str(p)+"]:")
    while inter != 'P':
        try:
            str_para_intersecao(inter)
        except ValueError:
            inter = input("Escreva uma intersecao ou 'P' para passar ["+pedra_para_str(p)+"]:")
        else:
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
    try:
       tbinter =  tuple(str_para_intersecao(i) for i in tb)
       tpinter = tuple(str_para_intersecao(i) for i in tp)
    except (ValueError, IndexError,TypeError):
        raise ValueError('go: argumentos invalidos')
    else:
        go = ()
        try:
            cria_goban_vazio(g)
        except ValueError:
            raise ValueError('go: argumentos invalidos')
        else:
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
            if i % 2 == 0: # Determinar qual o jogador que joga a seguir (começã no zero, então par preto, impar branco)
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