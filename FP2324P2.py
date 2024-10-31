from ast import cmpop


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
    if isinstance(col, str) and type(lin) == int and col in COLUNAS and lin in LINHAS:
        return (col, lin)
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


def eh_intersecao(arg:tuple) -> bool:
    '''
    Determina se um determinado argumento é uma interseção ou não.

    Parameters:
            arg(any): O argumento a testar
    Returns:
            return(Boolean): Caso se trate de uma interseção vai devolver True em caso contrário Falso
    '''
    if isinstance(arg, tuple) and len(arg) == 2:
        try:
            cria_intersecao(obtem_col(arg),obtem_lin(arg))
            return True
        except ValueError:
            pass
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
    return eh_intersecao(i1) and eh_intersecao(i2) and obtem_col(i1) == obtem_col(i2) and obtem_lin(i1) == obtem_lin(i2)


def intersecao_para_str(i:tuple) -> str:
    '''
    Transoforma uma interseção no seu formato interno para a sua representação externa.

    Parameters:
            i(tuplo): Uma interseção
    Returns:
            return(str): Devolve a string que representa externamente uma interseção
    '''
    return obtem_col(i) + str(obtem_lin(i))

def str_para_intersecao(string :str):
    '''
    Transforma a representação externa de uma interseção na representação interna.

    Parameters:
            str(string): A string que representa a externa de uma interseção
    Returns:
            return(intersecao): A representação interna da interseção usando o construtor
    '''
    return cria_intersecao(string[0], int(string[1:]))


#Funções de Alto nível que estão associadas a este TAD (intersecao)
#Ordem de leitura (left to right, bottom  to top)

def obtem_intersecoes_adjacentes(i, l):
    '''
    Obtem as interseções que se encontram nas posições adjacentes a uma detreminada interseção, sendo que estas de encontram para cima, baixo, esquerda ou direita.

    Parameters:
            i(tuple): A interseção
            l(tuple): A última interseção(canto superior direito) do tabuleiro de goban que estamos a considerar
    Returns:
            return(tupel): Um tuplo que contem as interseções adjacentes por ordem de leitura
    '''
    vec_adjacente = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    inter_adj = []

    for vec in vec_adjacente:
        col_index = COLUNAS.index(obtem_col(i)) + vec[0]
        lin = obtem_lin(i) + vec[1]
        if 0 <= col_index < len(COLUNAS) and 1 <= lin <= obtem_lin(l):
            col = COLUNAS[col_index]
            if col <= obtem_col(l):
                inter_adj.append(cria_intersecao(col, lin))

    return ordena_intersecoes(tuple(inter_adj))
    
def ordena_intersecoes(t):
    '''
    Ordena o tuplo fornecido de interseções de acordo com a ordem de leitura do tabuleiro de Goban.

    Parameters:
            t(tuplo): O tuplo de interseções
    Returns:
            return(tuplo): O mesmo tuplo mas com as interseções ordenadas
    '''
    return tuple(sorted(t, key=lambda i: (obtem_lin(i), obtem_col(i))))

#TAD pedra
#n --> pedra neutro
#w --> pedra branca
#b --> pedra preta

def cria_pedra_branca() -> str:
    '''
    O construtor da pedra branca.

    Returns:
            return(int): A repersentação interna da pedra branca
    '''
    return 'w'

def cria_pedra_preta() -> str:
    '''
    O construtor da pedra preta.

    Returns:
            return(int): A repersentação interna da pedra preta
    '''
    return 'b'


def cria_pedra_neutra() -> str:
    '''
    O construtor da pedra neutra.

    Returns:
            return(int): A repersentação interna da pedra neutra
    '''
    return 'n'

def eh_pedra(arg:str) -> bool:
    '''
    Verifica se o argumento fornecido é uma pedra de acordo com a representação interna

    Returns:
            return(Boolean): Devolve True se o argumento for uma pedra e False caso contrário
    '''
    return arg in (cria_pedra_branca(), cria_pedra_neutra(), cria_pedra_preta())


def eh_pedra_branca(p:str) -> bool:
    '''
    Verifica se o argumento fornecido é uma pedra branca de acordo com a representação interna

    Returns:
            return(Boolean): Devolve True se o argumento for uma pedra branca e False caso contrário
    '''
    return p == cria_pedra_branca()

def eh_pedra_preta(p:str) -> bool:
    '''
    Verifica se o argumento fornecido é uma pedra preta de acordo com a representação interna

    Returns:
            return(Boolean): Devolve True se o argumento for uma pedra preta e False caso contrário
    '''
    return p == cria_pedra_preta()

def pedras_iguais(p1:str,p2:str) -> bool:
    '''
    Verifica se as duas pedras fornecidas são iguais.

    Parameters:
            p1(int): A primeira pedra
            p2(int): A segunda pedra
    Returns:
            return(Boolean): Devolve True se as duas pedras forem iguais e False caso contrário
    '''
    return eh_pedra(p1) and eh_pedra(p2) and ((eh_pedra_branca(p1) and eh_pedra_branca(p2)) or (eh_pedra_preta(p1) and eh_pedra_preta(p2)) or (not eh_pedra_jogador(p1) and not eh_pedra_jogador(p2)))


def pedra_para_str(p:str) -> str:
    '''
    Transforma a representação interna de pedra para a representação externa de pedra.

    Parameters:
            p(int): A representação interna da pedra
    Returns:
            pedras(string): A representação externa da pedra
    '''
    if eh_pedra_branca(p):
        return "O"
    if eh_pedra_preta(p):
        return "X"
    return "."


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
    if isinstance(n, int) and n in (9,13,19):
            return tuple([cria_pedra_neutra() for i in range(n)] for i1 in range(n)) #Gera um tuplo de listas com os valores correspondentes a representação interna do goban
    raise ValueError('cria_goban_vazio: argumento invalido')

def cria_goban(n:int, ib:tuple, ip:tuple):
    '''
    Cria um goban com o tamanho pretendido e coloca-o no estado indicado com pedras brancas e pretas.

    Parameters:
            n(int): O tamanho do tabuleiro de Goban pretendido
            ib(tuple): O tuplo das interseções ocupadas por pedras brancas
            ip(tuple): O tuplo das interseções ocupadas por pedras pretas
    Returns:
            g(tuple): O tabuleiro de Goban no estado inicial
    '''
    try:
        g = cria_goban_vazio(n)
    except ValueError as e:
        raise ValueError('cria_goban: argumentos invalidos') from e
    if not isinstance(ib, tuple) or not isinstance(ip, tuple):
        raise ValueError('cria_goban: argumentos invalidos')

    intersecoes_ocupadas = set()

    for inter in ib:
        if not eh_intersecao(inter) or obtem_lin(inter) > n or obtem_col(inter) not in COLUNAS[:n]:
            raise ValueError('cria_goban: argumentos invalidos')
        if inter in intersecoes_ocupadas:
            raise ValueError('cria_goban: argumentos invalidos')
        coloca_pedra(g, inter, cria_pedra_branca())
        intersecoes_ocupadas.add(inter)

    for inter in ip:
        if not eh_intersecao(inter) or obtem_lin(inter) > n or obtem_col(inter) not in COLUNAS[:n]:
            raise ValueError('cria_goban: argumentos invalidos')
        if inter in intersecoes_ocupadas:
            raise ValueError('cria_goban: argumentos invalidos')
        coloca_pedra(g, inter, cria_pedra_preta())
        intersecoes_ocupadas.add(inter)

    return g

def cria_copia_goban(g):
    '''
    Cria uma cópia independe do tabuleiro de Goban

    Parameters:
            t(tuple): O Tabuleiro de Goban
    Returns:
            return(tuple): Uma cópia independente do tabuleiro de Goban
    '''
    return tuple([[pedra for pedra in linha] for linha in t])


def obtem_ultima_intersecao(g) -> tuple:
    '''
    Obtem a última interseção de um determinado tabuleiro de Goban, ou seja a interseção do canto superior direito.

    Parameters:
            g(tuple): O tabuleiro de Goban
    Returns:
            return(tuple): A interseção correspondente
    '''
    return cria_intersecao(COLUNAS[len(g)-1], len(g))


def obtem_pedra(g,i):
    '''
    Devolve a representação interna da pedra.

    Parameters:
            g(tuple): O tabuleiro de Goban
            i(tuple): A interseção da qual queremos obter a pedra
    '''
    return g[obtem_lin(i)-1][COLUNAS.index(obtem_col(i))]


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
    tipo = obtem_pedra(g, i)
    cadeia = set()
    a_explorar = {i}
    while a_explorar:
        atual = a_explorar.pop()
        cadeia.add(atual)
        for adj in obtem_intersecoes_adjacentes(atual, obtem_ultima_intersecao(g)):
            if adj not in cadeia and pedras_iguais(obtem_pedra(g, adj), tipo):
                a_explorar.add(adj)
    return ordena_intersecoes(tuple(cadeia))



def coloca_pedra(g,i,p):
    '''
    Coloca a pedra numa derterminada interseção no tabuleiro de Goban.

    Parameters:
            g(tuplo): O Tabuleiro de Goban
            i(tuplo): A interseção onde colocar a pedra
            p(string): O tipo de pedra a colocar, ou seja o jogador que efetua a ação
    Returns:
            g(tuplo): Vai modificar destrutivamente o Tabuleiro de Goban
    '''
    g[obtem_lin(i)-1][COLUNAS.index(obtem_col(i))] = p
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
    g[obtem_lin(i)-1][COLUNAS.index(obtem_col(i))] = cria_pedra_neutra()
    return g


def remove_cadeia(g:tuple, t:tuple) -> tuple:
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


def eh_goban(arg:tuple) -> bool:
    '''
    Verifica se o argumento fornecido é um goban.

    Parameters:
            arg(tuple): O argumento para verificar se se trata de um goban
    Returns:
            return(Boolean): Devolve True se o argumento for um goban e False em caso contrário
    '''
    if isinstance(arg, tuple) and len(arg) in (9, 13, 19):
        if all(isinstance(col, list) and len(col) == len(arg) for col in arg):
            if  all(eh_pedra(pedra) for lin in arg for pedra in lin):
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
    return eh_goban(g) and eh_intersecao(i) and obtem_col(i) in COLUNAS[:len(g)] and 1 <= obtem_lin(i) <= len(g)


def gobans_iguais(g1,g2) -> bool:
    '''
    Verifica se os dois Goban são iguais.

    Parameters:
            g1(tuplo): O primeiro tabuleiro de Go
            g2(tuplo): O segundo tabuleiro de Go
    Returns:
            return(Boolean): Devolve True se os dois Gobans forem iguais e False em caso contrário
    '''
    if not (eh_goban(g1) and eh_goban(g2) and len(g1) == len(g2)):
        return False
    return all(pedras_iguais(obtem_pedra(g1, cria_intersecao(COLUNAS[col], lin + 1)),
    obtem_pedra(g2, cria_intersecao(COLUNAS[col], lin + 1)))
    for lin, row in enumerate(g1) for col, _ in enumerate(row))


def goban_para_str(g) -> str:
    '''
    Transforma a representação interna do tabuleiro de goban na representação externa.

    Parameters:
            g(tuple): O tabuleiro de Goban
    Returns:
            return(string): A representação externa do tabuleiro de Gobans
    '''
    dimensao = len(g)
    gobanstr = '   ' + ' '.join(COLUNAS[:dimensao]) + '\n'
    for i in range(dimensao - 1, -1, -1):
        gobanstr += f'{i+1:2} ' + ' '.join(pedra_para_str(obtem_pedra(g,cria_intersecao(COLUNAS[col],i+1))) for col in range(dimensao)) + f' {i+1:2}\n'
    gobanstr += '   ' + ' '.join(COLUNAS[:dimensao])
    return gobanstr

#Funções de Alto nível que estão associadas a este TAD (goban)
def obtem_territorios(g:tuple) -> tuple:
    '''
    Obtem os territórios que existem num determinado tabuleiro de Goban, quer pertenção a um determinado jogador ou não.

    Parameters:
            g(tuple): O tabuleiro de goban
    Returns:
            return(tuple): Um tuplo formado pelos tuplos que cotém as interseções que formam cada território
    '''
    terr = ()
    inter = ()
    dim = obtem_lin(obtem_ultima_intersecao(g))
    for lin in range(1, dim + 1):
        for col in COLUNAS[:dim]:
            if cria_intersecao(col, lin) not in inter:  # Verifica se a interseção já foi visitada
                if pedras_iguais(obtem_pedra(g, cria_intersecao(col, lin)), cria_pedra_neutra()):
                    nterr = obtem_cadeia(g, cria_intersecao(col, lin))
                    if nterr not in terr:
                        terr += (nterr,)  # Adiciona o terreno se este cumpre os requesitos
                        inter += nterr  # Marca todas as interseções já visitadas, para não existirem repetições
    return tuple(sorted(terr, key=lambda t: obtem_lin(t[0])))


def obtem_adjacentes_diferentes(g, t) -> tuple:
    '''
    Obtem o conjunto de interseções adjacentes a um determinado território.

    Parameters:
            g(tuplo): O tabuleiro de Goban
            t(tuplo): O território em questão
    Returns:
            adj(tuplo): O conjunto das interseções adjacentes diferentes ou seja a fronteira do determinado território
    '''
    adj = set()
    for inter in t:
        for cord in obtem_intersecoes_adjacentes(inter, obtem_ultima_intersecao(g)):
            if (eh_pedra_jogador(obtem_pedra(g, inter)) and not eh_pedra_jogador(obtem_pedra(g, cord))) or \
                (not eh_pedra_jogador(obtem_pedra(g, inter)) and eh_pedra_jogador(obtem_pedra(g, cord))):
                adj.add(cord)
    return ordena_intersecoes(tuple(adj))


def jogada(g, i, p):
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
    dimensao = obtem_lin(obtem_ultima_intersecao(g))
    pedras_brancas = sum(eh_pedra_branca(obtem_pedra(g, cria_intersecao(col, lin))) for col in COLUNAS[:dimensao] for lin in range(1, dimensao + 1))
    pedras_pretas = sum(eh_pedra_preta(obtem_pedra(g, cria_intersecao(col, lin))) for col in COLUNAS[:dimensao] for lin in range(1, dimensao + 1))
    return (pedras_brancas, pedras_pretas)


#Funções adicionais
def calcula_pontos(g:tuple) -> tuple:
    '''
    Calcula os pontos que cada jogador tem no atual estado do tabuleiro goban (g)

    Parameters:
            g(tuplo): O tabuleiro de jogo goban

    Returns:
            return(tuplo): Com os inteiros correspondetes aos pontos do jogador branco e preto respetivamente
    '''
    t = obtem_territorios(g)
    pontos = obtem_pedras_jogadores(g)
    terreno_branco = sum(len(terreno) for terreno in t if obtem_adjacentes_diferentes(g, terreno) and all(eh_pedra_branca(obtem_pedra(g, cord)) for cord in obtem_adjacentes_diferentes(g, terreno)))
    terreno_preto = sum(len(terreno) for terreno in t if obtem_adjacentes_diferentes(g, terreno) and all(eh_pedra_preta(obtem_pedra(g, cord)) for cord in obtem_adjacentes_diferentes(g, terreno)))
    return (pontos[0] + terreno_branco, pontos[1] + terreno_preto)
#Os pontos de cada jogador são a soma dos seus terrenos e do número de pedras que têm no território


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
    if not eh_intersecao_valida(g, i) or eh_pedra_jogador(obtem_pedra(g, i)):
        return False

    copia_goban = cria_copia_goban(g)
    jogada(copia_goban, i, p)

    # Verifica a o estado KO's que acontece qunado apos uma jogada obtemos o mesmo tabuleiro
    if gobans_iguais(copia_goban, l):
        return False

    # Verifica a regra do suicidio
    return obtem_adjacentes_diferentes(copia_goban, obtem_cadeia(copia_goban, i))

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
    mensg = "Escreva uma intersecao ou 'P' para passar [" + pedra_para_str(p) + "]:"
    while True:
        input_utilizador = input(mensg)
        if input_utilizador == 'P':
            return False
        try:
            intersecao = str_para_intersecao(input_utilizador)
            if eh_jogada_legal(g, intersecao, p, l):
                jogada(g, intersecao, p)
                return True
        except ValueError:
            continue


def go(g: int, tb: 'tuple[str,...]', tp: 'tuple[str,   ]') -> bool:
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
    if not isinstance(tp, tuple) or not isinstance(tb, tuple):
        raise ValueError('go: argumentos invalidos')

    try:
        tbinter = tuple(str_para_intersecao(interb) if isinstance(interb, str) else interb for interb in tb)
        tpinter = tuple(str_para_intersecao(interp) if isinstance(interp, str) else interp for interp in tp)
        goban = cria_goban(g, tbinter, tpinter)
        goant = cria_copia_goban(goban)
    except ValueError as e:
        raise ValueError('go: argumentos invalidos') from e

    brancopass = pretopass = False
    i = 0

    while not (brancopass and pretopass):
        pontos_branco, pontos_preto = calcula_pontos(goban)
        print(f'Branco (O) tem {pontos_branco} pontos')
        print(f'Preto (X) tem {pontos_preto} pontos')
        print(goban_para_str(goban))

        if i % 2 == 0:
            pretopass = not turno_jogador(goban, cria_pedra_preta(), goant)
        else:
            brancopass = not turno_jogador(goban, cria_pedra_branca(), goant)

        goant = cria_copia_goban(goban)
        i += 1

    pontos_branco, pontos_preto = calcula_pontos(goban)
    print(f'Branco (O) tem {pontos_branco} pontos')
    print(f'Preto (X) tem {pontos_preto} pontos')
    print(goban_para_str(goban))

    return pontos_branco >= pontos_preto
