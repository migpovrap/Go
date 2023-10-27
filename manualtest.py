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


ib = tuple(fp.str_para_intersecao(i) for i in ('C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'))
#print(fp.turno_jogador(g, fp.cria_pedra_preta(),fp.cria_goban_vazio(9)))
ip = tuple(fp.str_para_intersecao(i) for i in ('A1', 'A2', 'B1', 'E4', 'E5', 'F4', 'F5', 'G6', 'G7'))
print(fp.go(9, ib, ip))

