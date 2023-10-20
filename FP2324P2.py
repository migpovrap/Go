colunas = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S')
linhas = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19)

#TAD intersecao
def cria_intersecao(col,lin):
    if not (col in colunas and lin in linhas):
        raise ValueError('cria_intersecao: argumentos invalidos')
    return (col,lin)


def obtem_col(i):
    return i[0]


def obtem_lin(i):
    return i[1]


def eh_intersecao(arg):
    return type(arg) == tuple and obtem_col(arg) in colunas and obtem_lin(arg) in linhas

def intersecoes_iguais(i1,i2):
    if eh_intersecao(i1) and eh_intersecao(i2):
        return obtem_col(i1) == obtem_col(i2) and obtem_lin(i1) == obtem_lin(i2)
    return False


def intersecao_para_str(i):
    return obtem_col(i)+str(obtem_lin(i))

def str_para_intersecao(str):
    return (str[0],int(str[1:])) 

#Funções de Alto nível que estão associadas a este TAD (intersecao)
def obtem_intersecoes_adjacentes(i,l):
    #Ordem de leitura (left to right, bottom  to top)
    interadj = ()
    if colunas[colunas.index(obtem_col(i))-1] in colunas[:colunas.index(obtem_col(l))]:
        interadj += (colunas[colunas.index(obtem_col(i))-1],obtem_lin(i)),
    if obtem_lin(i)-1 <= obtem_lin(l):
        interadj += (obtem_col(i),obtem_lin(i)-1),
    if colunas[colunas.index(obtem_col(i))+1] in colunas[:colunas.index(obtem_col(l))]:
        interadj += (colunas[colunas.index(obtem_col(i))+1],obtem_lin(i)),
    if obtem_lin(i)+1 <= obtem_lin(l):
        interadj += (obtem_col(i),obtem_lin(i)+1),
    return interadj
    
def ordena_intersecoes(t):
    return tuple(sorted(t,key= lambda t: t[1]))


#TAD pedra
#Pedra [0,()] O tuplo vazio corresponde à interseção onde se localiza a pedra
#0 --> pedra branca
#1 --> pedra preta
#2 --> pedra neutra

def cria_pedra_branca():
    return [0,()]
def cria_pedra_preta():
    return [1,()]
def cria_pedra_neutra():
    return[2,()]

def eh_pedra(arg):
    return type(arg) == list and arg[0] in (0,1,3) and len(arg) == 2
def eh_pedra_branca(p):
    return p[0] == 0
def eh_pedra_preta(p):
    return p[0] == 1

def pedras_iguais(p1,p2):
    if eh_pedra(p1) and eh_pedra(p2):
        return p1[0] == p2[0]
    return False

def pedra_para_str(p):
    if p[0] == 0:
        return 'O'
    if p[0] == 1:
        return 'X'
    if p[0] == 2:
        return '.'
    
def eh_pedra_jogador(p):
    if eh_pedra_branca(p) or eh_pedra_preta(p):
        return True
    return False

