import sys
import os

# Add the parent directory to the Python path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)
import FP2324P2 as fp


#print('Test for function intersecao_para_str')
#print(fp.intersecao_para_str(('A',2)))
#print(type(fp.intersecao_para_str(('A',2))))

#print('Test for function str_para_intersecao')
#print(fp.str_para_intersecao('A12'))
#print(type(fp.str_para_intersecao('A12')))

#i1 = fp.cria_intersecao('A',2)
#print(tuple(fp.intersecao_para_str(i) for i in fp.obtem_intersecoes_adjacentes(i1,fp.cria_intersecao('S',19))))
#print(fp.obtem_intersecoes_adjacentes(i1,('S',19)))

#tup = (fp.cria_intersecao('A',1),fp.cria_intersecao('A',3),fp.cria_intersecao('B',1),fp.cria_intersecao('B',2))
#print(fp.ordena_intersecoes(tup))
#print(tuple(fp.intersecao_para_str(i) for i in fp.ordena_intersecoes(tup)))


#tab[0][3] = 1
#rint(tab)
#print(len(tab))
#print(len(tab[0]))

#tabcopy = fp.cria_copia_goban(tab)
#tabcopy[0][3] = 1
#print(tab)
#print(tabcopy)

#print(fp.obtem_ultima_intersecao(tab))
#print(fp.obtem_pedra(tab,('A',4)))
#tab = fp.cria_goban_vazio(9)
#tab[0][2] = 1
#tab[1][2] = 1
#tab[2][2] = 1
#tab[2][1] = 1
#tab[2][0] = 1
#tab[3][3] = 1
#tab[3][2] = 1
#tab[3][1] = 1
#tab[6][8] = 2
#tab[6][7] = 2
#tab[6][6] = 2
#tab[7][6] = 2
#tab[8][6] = 2
#print(fp.obtem_cadeia(tab,('H',8)))
#print(tab)
#print(fp.obtem_cadeia(tab,('A',4)))
#print(fp.goban_para_str(tab))
#ter =fp.obtem_territorios(tab)
#print(tuple(fp.intersecao_para_str(i) for i in fp.obtem_adjacentes_differentes(tab,ter[0])))
#print(fp.obtem_pedras_jogadores(tab))
 

#g = fp.cria_goban_vazio(9)
#b, p = fp.cria_pedra_branca(), fp.cria_pedra_preta()
#ib = 'C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'
#ip = 'E4', 'E5', 'F4', 'F5', 'G6', 'G7'
#for i in ib: fp.coloca_pedra(g, fp.str_para_intersecao(i), b)
#for i in ip: fp.coloca_pedra(g, fp.str_para_intersecao(i), p)
#terr = fp.obtem_territorios(g)
#print(fp.goban_para_str(g),terr[0])
#border = fp.obtem_adjacentes_diferentes(g, terr[0])
#print(tuple(fp.intersecao_para_str(i) for i in border))

#ib = tuple(fp.str_para_intersecao(i) \
#for i in ('C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'))
#ip = tuple(fp.str_para_intersecao(i) \
#for i in ('A1', 'A2', 'B1', 'E4', 'E5', 'F4', 'F5', 'G6', 'G7'))
#g = fp.cria_goban(9, ib, ip)
#b = fp.cria_pedra_branca()
#print(fp.jogada(g, fp.cria_intersecao('B', 2), b))
#print(fp.goban_para_str(g))

#ib = tuple(fp.str_para_intersecao(i) for i in ('C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'))
#ip = tuple(fp.str_para_intersecao(i) for i in ('E4', 'E5', 'F4', 'F5', 'G6', 'G7'))
#g = fp.cria_goban(9, ib, ip)
#print(fp.goban_para_str(g))
#print(fp.calcula_pontos(g))


#ib = tuple(fp.str_para_intersecao(i) for i in ('C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'))
#ip = tuple(fp.str_para_intersecao(i) for i in ('A1', 'A2', 'B1', 'E4', 'E5', 'F4', 'F5', 'G6', 'G7'))
#g = fp.cria_goban(9, ib, ip)
#l = fp.cria_goban_vazio(9)
#b, p = fp.cria_pedra_branca(), fp.cria_pedra_preta()
#print(fp.eh_jogada_legal(g, fp.cria_intersecao('B', 2), p, l))

#ib = tuple(fp.str_para_intersecao(i) for i in ('C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'))
#ip = tuple(fp.str_para_intersecao(i) for i in ('A1', 'A2', 'B1', 'E4', 'E5', 'F4', 'F5', 'G6', 'G7'))
#g = fp.cria_goban(9, ib, ip)
#l = fp.cria_goban_vazio(9)
#b, p = fp.cria_pedra_branca(), fp.cria_pedra_preta()
#print(fp.eh_jogada_legal(g, fp.cria_intersecao('B', 2), p, l))


#ib = tuple(fp.str_para_intersecao(i) for i in ('C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'))
#print(fp.turno_jogador(g, fp.cria_pedra_preta(),fp.cria_goban_vazio(9)))
#ip = tuple(fp.str_para_intersecao(i) for i in ('A1', 'A2', 'B1', 'E4', 'E5', 'F4', 'F5', 'G6', 'G7'))
#print(fp.go(9, ib, ip))

#ib = tuple(fp.str_para_intersecao(i) for i in ('C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'))
#ip = tuple(fp.str_para_intersecao(i) for i in ('E4', 'E5', 'F4', 'F5', 'G6', 'G7'))
#g = fp.cria_goban(9, ib, ip)

#print(fp.calcula_pontos(g))

#ib = tuple(fp.str_para_intersecao(i) for i in ('C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'))
#ip = tuple(fp.str_para_intersecao(i) for i in ('A1', 'A2', 'B1', 'E4', 'E5', 'F4', 'F5', 'G6', 'G7'))
#g = fp.cria_goban(9, ib, ip)
#l = fp.cria_goban_vazio(9)
#b, p = fp.cria_pedra_branca(), fp.cria_pedra_preta()
#ref = \

#print(fp.eh_jogada_legal(g, fp.cria_intersecao('B', 2), p, l))
#print(fp.eh_jogada_legal(g, fp.cria_intersecao('B', 2), b, l))
#print(fp.goban_para_str(g))


#print(fp.go(9,(),()))
#print(fp.calcula_pontos(fp.cria_goban(9,(),())))
#print(fp.obtem_pedras_jogadores(fp.cria_goban(9,(),())))
#print(fp.obtem_territorios(fp.cria_goban(9,(),())))

#ib = 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'B3', 'I3', 'B4', 'D4', 'E4', 'F4', 'B5', 'D5', 'G5', 'I5', 'B6', 'D6', 'E6', 'F6', 'G6', 'I6', 'C7', 'I7', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8', 'I8'
#ip = 'C3', 'D3', 'E3', 'F3', 'G3', 'C4', 'G4', 'H4', 'C5', 'H5', 'C6', 'H6', 'D7', 'E7', 'F7', 'G7', 'H7'
#print(fp.go(9,ib,ip))
#tbinter = tuple(fp.str_para_intersecao(i) for i in ib)
#tpinter = tuple(fp.str_para_intersecao(i) for i in ip)
#print(tbinter)

#print(fp.cria_intersecao('A',1.0))
#print(fp.obtem_intersecoes_adjacentes(('R',9),('I',9)))
#
#print(fp.cria_goban(9,(('I',8)),()))

#COLUNAS = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S')
#i1 = fp.cria_intersecao('A', 2)
#print(tuple(fp.intersecao_para_str(i) for i in fp.obtem_intersecoes_adjacentes(i1, fp.cria_intersecao('S',19))))
#print(fp.obtem_intersecoes_adjacentes(i1, fp.cria_intersecao('S',19)))

#print(fp.cria_goban(9,(),()))







#def remove_cadeia(g,t):
#    '''
#    Remove uma determinada cadeia do tabuleiro de Goban.
#    Parameters:
#            g(tuplo): O Tabuleiro de Goban
#            t(tuplo): O conjunto de interseções que formam a cadeia a ser removida
#    Returns:
#            g(tuplo): Vai modificar destrutivamente o Tabuleiro de Goban
#    '''
#    for inter in t:
#        g[fp.COLUNAS.index(fp.obtem_col(inter))][fp.obtem_lin(inter)-1] = 0
#    return g



#g12 = ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

#g1 = ([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0])

#g2 = ([0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 2, 2, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0])
#print(fp.eh_goban(g))

#print(fp.gobans_iguais(g1,g12))

#print(fp.go(9,(),()))

#print(fp.obtem_adjacentes_diferentes(g))

#print(fp.cria_intersecao('A',True))

#print(fp.obtem_intersecoes_adjacentes(('B',2),('S',19)))


#ip = ("B1","A2","B2","A4","B4","C4","D4","D3","D2","D1","F1")
#ib = ("F2","F3","F4","F5","F6","E6","D6","C6","B6","A6","A8","B8","C8","D8","E8","F8","G8","H8","H7","H6","H5","H4","H3","H2","H1","I9","G7","E5","C3")
#ip = tuple(fp.str_para_intersecao(x) for x in ip)
#ib = tuple(fp.str_para_intersecao(x) for x in ib)
#g = fp.cria_goban(9,ib,ip)

#print(fp.obtem_territorios(g))
#print(fp.go(9,((2),),()))


#print('   A B C D E F G H I\n 9 . . . O . O X . .  9\n 8 . . . . O O X . .  8\n 7 . . . . O X . . .  7\n 6 . . . O O X . . .  6\n 5 . . . O X . X . .  5\n 4 O O O O X . . . .  4\n 3 . O . O X . . . .  3\n 2 . O . O X . . . .  2\n 1 . O . X . . . . .  1\n   A B C D E F G H I')
#print('   A B C D E F G H I\n 9 . . . X . X X . .  9\n 8 . . . . X X X . .  8\n 7 . . . . X X . . .  7\n 6 . . . X X X . . .  6\n 5 . . . X X . X . .  5\n 4 X X X X X . . . .  4\n 3 . X . X X . . . .  3\n 2 . X . X X . . . .  2\n 1 . X . X . . . . .  1\n   A B C D E F G H I')

#print('\nSegundo Error\n')

#print('   A B C D E F G H I\n 9 . . . . . . . . .  9\n 8 . . . . . . . . .  8\n 7 . . . . . . X . .  7\n 6 . . . . . . X . .  6\n 5 . . . . X X . . .  5\n 4 . . . . X X . . .  4\n 3 . . . . . . . . .  3\n 2 . . . . . . . . .  2\n 1 . . . . . . . . .  1\n   A B C D E F G H I')
#print('   A B C D E F G H I\n 9 . . . . . . . . .  9\n 8 . . . . . . . . .  8\n 7 . . . . . . X . .  7\n 6 . . . . . . X . .  6\n 5 . . . . X X . . .  5\n 4 . . . O X X . . .  4\n 3 O O O O . . . . .  3\n 2 . O O O . . . . .  2\n 1 . . O . . . . . .  1\n   A B C D E F G H I')


#print(fp.obtem_cadeia(fp.cria_goban_vazio(9),('R',9)))

#ib = tuple(fp.str_para_intersecao(i) for i in ('C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'))
#ip = tuple(fp.str_para_intersecao(i) for i in ('E4', 'E5', 'F4', 'F5', 'G6', 'G7'))
#g = fp.cria_goban(9, ib, ip)

#print(fp.calcula_pontos(g))

# O que a minha função dá
#print("Branco (O) tem 18 pontos\nPreto (X) tem 23 pontos\n   A B C D E F G H I\n 9 . . X X O O . . .  9\n 8 . O X O . O X . .  8\n 7 . O X X O O X . .  7\n 6 . . O O X X . . .  6\n 5 O O . . . . . . .  5\n 4 . . X X X . . . .  4\n 3 O O O O O X . . .  3\n 2 X X X X . X . . .  2\n 1 X X X X . X . . .  1\n   A B C D E F G H I\nEscreva uma intersecao ou 'P' para passar [X]:Branco (O) tem 16 pontos\nPreto (X) tem 25 pontos\n   A B C D E F G H I\n 9 . . X X O O . . .  9\n 8 . O X . X O X . .  8\n 7 . O X X O O X . .  7\n 6 . . O O X X . . .  6\n 5 O O . . . . . . .  5\n 4 . . X X X . . . .  4\n 3 O O O O O X . . .  3\n 2 X X X X . X . . .  2\n 1 X X X X . X . . .  1\n   A B C D E F G H I\nEscreva uma intersecao ou 'P' para passar [O]:Escreva uma intersecao ou 'P' para passar [O]:Branco (O) tem 17 pontos\nPreto (X) tem 25 pontos\n   A B C D E F G H I\n 9 . . X X O O . . .  9\n 8 . O X . X O X . .  8\n 7 . O X X O O X . .  7\n 6 . . O O X X . . .  6\n 5 O O . . . . . . .  5\n 4 . . X X X . . . .  4\n 3 O O O O O X . . .  3\n 2 X X X X O X . . .  2\n 1 X X X X . X . . .  1\n   A B C D E F G H I\nEscreva uma intersecao ou 'P' para passar [X]:Branco (O) tem 17 pontos\nPreto (X) tem 26 pontos\n   A B C D E F G H I\n 9 . . X X O O . . .  9\n 8 . O X . X O X . .  8\n 7 . O X X O O X . .  7\n 6 . . O O X X . . .  6\n 5 O O . . . . . . .  5\n 4 . . X X X . . . .  4\n 3 O O O O O X . . .  3\n 2 X X X X O X . . .  2\n 1 X X X X X X . . .  1\n   A B C D E F G H I\nEscreva uma intersecao ou 'P' para passar [O]:Branco (O) tem 19 pontos\nPreto (X) tem 24 pontos\n   A B C D E F G H I\n 9 . . X X O O . . .  9\n 8 . O X O . O X . .  8\n 7 . O X X O O X . .  7\n 6 . . O O X X . . .  6\n 5 O O . . . . . . .  5\n 4 . . X X X . . . .  4\n 3 O O O O O X . . .  3\n 2 X X X X O X . . .  2\n 1 X X X X X X . . .  1\n   A B C D E F G H I\nEscreva uma intersecao ou 'P' para passar [X]:Escreva uma intersecao ou 'P' para passar [X]:Branco (O) tem 19 pontos\nPreto (X) tem 25 pontos\n   A B C D E F G H I\n 9 . . X X O O . . .  9\n 8 . O X O . O X . .  8\n 7 . O X X O O X . .  7\n 6 . . O O X X . . .  6\n 5 O O . . . . . . .  5\n 4 . X X X X . . . .  4\n 3 O O O O O X . . .  3\n 2 X X X X O X . . .  2\n 1 X X X X X X . . .  1\n   A B C D E F G H I\nEscreva uma intersecao ou 'P' para passar [O]:Branco (O) tem 20 pontos\nPreto (X) tem 25 pontos\n   A B C D E F G H I\n 9 . . X X O O . . .  9\n 8 . O X O . O X . .  8\n 7 . O X X O O X . .  7\n 6 . . O O X X . . .  6\n 5 O O . . . . . . .  5\n 4 O X X X X . . . .  4\n 3 O O O O O X . . .  3\n 2 X X X X O X . . .  2\n 1 X X X X X X . . .  1\n   A B C D E F G H I\nEscreva uma intersecao ou 'P' para passar [X]:Branco (O) tem 18 pontos\nPreto (X) tem 27 pontos\n   A B C D E F G H I\n 9 . . X X O O . . .  9\n 8 . O X . X O X . .  8\n 7 . O X X O O X . .  7\n 6 . . O O X X . . .  6\n 5 O O . . . . . . .  5\n 4 O X X X X . . . .  4\n 3 O O O O O X . . .  3\n 2 X X X X O X . . .  2\n 1 X X X X X X . . .  1\n   A B C D E F G H I\nEscreva uma intersecao ou 'P' para passar [O]:Branco (O) tem 18 pontos\nPreto (X) tem 27 pontos\n   A B C D E F G H I\n 9 . . X X O O . . .  9\n 8 . O X . X O X . .  8\n 7 . O X X O O X . .  7\n 6 . . O O X X . . .  6\n 5 O O . . . . . . .  5\n 4 O X X X X . . . .  4\n 3 O O O O O X . . .  3\n 2 X X X X O X . . .  2\n 1 X X X X X X . . .  1\n   A B C D E F G H I\nEscreva uma intersecao ou 'P' para passar [X]:Branco (O) tem 18 pontos\nPreto (X) tem 27 pontos\n   A B C D E F G H I\n 9 . . X X O O . . .  9\n 8 . O X . X O X . .  8\n 7 . O X X O O X . .  7\n 6 . . O O X X . . .  6\n 5 O O . . . . . . .  5\n 4 O X X X X . . . .  4\n 3 O O O O O X . . .  3\n 2 X X X X O X . . .  2\n 1 X X X X X X . . .  1\n   A B C D E F G H I\n")
# O que o sor esperava
#print("Branco (O) tem 18 pontos\nPreto (X) tem 23 pontos\n   A B C D E F G H I\n 9 . . X X O O . . .  9\n 8 . O X O . O X . .  8\n 7 . O X X O O X . .  7\n 6 . . O O X X . . .  6\n 5 O O . . . . . . .  5\n 4 . . X X X . . . .  4\n 3 O O O O O X . . .  3\n 2 X X X X . X . . .  2\n 1 X X X X . X . . .  1\n   A B C D E F G H I\nEscreva uma intersecao ou 'P' para passar [X]:Branco (O) tem 16 pontos\nPreto (X) tem 25 pontos\n   A B C D E F G H I\n 9 . . X X O O . . .  9\n 8 . O X . X O X . .  8\n 7 . O X X O O X . .  7\n 6 . . O O X X . . .  6\n 5 O O . . . . . . .  5\n 4 . . X X X . . . .  4\n 3 O O O O O X . . .  3\n 2 X X X X . X . . .  2\n 1 X X X X . X . . .  1\n   A B C D E F G H I\nEscreva uma intersecao ou 'P' para passar [O]:Branco (O) tem 18 pontos\nPreto (X) tem 23 pontos\n   A B C D E F G H I\n 9 . . X X O O . . .  9\n 8 . O X O . O X . .  8\n 7 . O X X O O X . .  7\n 6 . . O O X X . . .  6\n 5 O O . . . . . . .  5\n 4 . . X X X . . . .  4\n 3 O O O O O X . . .  3\n 2 X X X X . X . . .  2\n 1 X X X X . X . . .  1\n   A B C D E F G H I\nEscreva uma intersecao ou 'P' para passar [X]:Branco (O) tem 18 pontos\nPreto (X) tem 25 pontos\n   A B C D E F G H I\n 9 . . X X O O . . .  9\n 8 . O X O . O X . .  8\n 7 . O X X O O X . .  7\n 6 . . O O X X . . .  6\n 5 O O . . . . . . .  5\n 4 . . X X X . . . .  4\n 3 O O O O O X . . .  3\n 2 X X X X X X . . .  2\n 1 X X X X . X . . .  1\n   A B C D E F G H I\nEscreva uma intersecao ou 'P' para passar [O]:Escreva uma intersecao ou 'P' para passar [O]:Escreva uma intersecao ou 'P' para passar [O]:Branco (O) tem 18 pontos\nPreto (X) tem 25 pontos\n   A B C D E F G H I\n 9 . . X X O O . . .  9\n 8 . O X O O O X . .  8\n 7 . O X X O O X . .  7\n 6 . . O O X X . . .  6\n 5 O O . . . . . . .  5\n 4 . . X X X . . . .  4\n 3 O O O O O X . . .  3\n 2 X X X X X X . . .  2\n 1 X X X X . X . . .  1\n   A B C D E F G H I\nEscreva uma intersecao ou 'P' para passar [X]:Branco (O) tem 18 pontos\nPreto (X) tem 26 pontos\n   A B C D E F G H I\n 9 . . X X O O . . .  9\n 8 . O X O O O X . .  8\n 7 . O X X O O X . .  7\n 6 . . O O X X . . .  6\n 5 O O . . . . . . .  5\n 4 . X X X X . . . .  4\n 3 O O O O O X . . .  3\n 2 X X X X X X . . .  2\n 1 X X X X . X . . .  1\n   A B C D E F G H I\nEscreva uma intersecao ou 'P' para passar [O]:Branco (O) tem 19 pontos\nPreto (X) tem 26 pontos\n   A B C D E F G H I\n 9 . . X X O O . . .  9\n 8 . O X O O O X . .  8\n 7 . O X X O O X . .  7\n 6 . . O O X X . . .  6\n 5 O O . . . . . . .  5\n 4 O X X X X . . . .  4\n 3 O O O O O X . . .  3\n 2 X X X X X X . . .  2\n 1 X X X X . X . . .  1\n   A B C D E F G H I\nEscreva uma intersecao ou 'P' para passar [X]:Escreva uma intersecao ou 'P' para passar [X]:Branco (O) tem 19 pontos\nPreto (X) tem 26 pontos\n   A B C D E F G H I\n 9 . . X X O O . . .  9\n 8 . O X O O O X . .  8\n 7 . O X X O O X . .  7\n 6 . . O O X X . . .  6\n 5 O O . . . . . . .  5\n 4 O X X X X . . . .  4\n 3 O O O O O X . . .  3\n 2 X X X X X X . . .  2\n 1 X X X X . X . . .  1\n   A B C D E F G H I\nEscreva uma intersecao ou 'P' para passar [O]:Branco (O) tem 19 pontos\nPreto (X) tem 26 pontos\n   A B C D E F G H I\n 9 . . X X O O . . .  9\n 8 . O X O O O X . .  8\n 7 . O X X O O X . .  7\n 6 . . O O X X . . .  6\n 5 O O . . . . . . .  5\n 4 O X X X X . . . .  4\n 3 O O O O O X . . .  3\n 2 X X X X X X . . .  2\n 1 X X X X . X . . .  1\n   A B C D E F G H I\n")

#ib = ('A3','A5','B3','B5','B7','B8','C3','C6','D3','D6','D8','E3','E7','E9','F7','F8','F9')
#ip = ('A1','B1','C1','D1','F1','C4','D4','E4','E6','F6','A2','B2','C2','D2','F2','F3','C7','D7','G7','C8','G8','C9','D9')
#print(fp.go(9,ib,ip))

#print(fp.eh_goban(((['A',[1],2],1),True)))

ib = 'B7', 'B8', 'C6', 'D6', 'D8', 'E7', 'E9', 'F7', 'F8', 'F9', 'A5', 'B5', 'A3', 'B3', 'C3', 'D3', 'E3'
ip = 'C7', 'C8', 'C9', 'D7', 'D9', 'E6', 'F6', 'G7', 'G8', 'C4', 'D4', 'E4', 'A1', 'B1', 'C1', 'D1', 'F1', 'A2', 'B2', 'C2', 'D2', 'F2', 'F3'
fp.go(9,ib, ip)

#'E8\nD8\nE2\nE1\nD8\nE8\nB4\nA4\nE8\nP\nP\n'