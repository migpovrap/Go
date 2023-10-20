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

tup = (fp.cria_intersecao('A',1),fp.cria_intersecao('A',3),fp.cria_intersecao('B',1),fp.cria_intersecao('B',2))
print(fp.ordena_intersecoes(tup))
print(tuple(fp.intersecao_para_str(i) for i in fp.ordena_intersecoes(tup)))