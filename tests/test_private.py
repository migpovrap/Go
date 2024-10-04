import pytest
import sys
project_filename = 'FP2324P2.py'
TAD_CODE_PATH = './TAD_code'
# from projectoFP import *

@pytest.fixture(autouse=True)
def run_around_tests():
    # Code that will run before your test, for example:
    exec(open(project_filename, encoding="utf-8").read(), globals())

    # A test function will be run at this point
    yield
    
    # Code that will run after your test, for example:
    

class TestPrivateIntersecaoCria:
    def test_1(self):
        with pytest.raises(ValueError) as excinfo:
            cria_intersecao(200, 10)
        assert "cria_intersecao: argumentos invalidos" == str(excinfo.value)
        
    def test_2(self):
        with pytest.raises(ValueError) as excinfo:
            cria_intersecao('B', (10,))
        assert "cria_intersecao: argumentos invalidos" == str(excinfo.value)
     
    def test_3(self):
        with pytest.raises(ValueError) as excinfo:
            cria_intersecao('d', 10)
        assert "cria_intersecao: argumentos invalidos" == str(excinfo.value)
        
    def test_4(self):
        with pytest.raises(ValueError) as excinfo:
            cria_intersecao('!', 10)
        assert "cria_intersecao: argumentos invalidos" == str(excinfo.value)
     
    def test_5(self):
        with pytest.raises(ValueError) as excinfo:
            cria_intersecao('CA', 10)
        assert "cria_intersecao: argumentos invalidos" == str(excinfo.value)
     
    def test_6(self):
        with pytest.raises(ValueError) as excinfo:
            cria_intersecao('D', '1')
        assert "cria_intersecao: argumentos invalidos" == str(excinfo.value)
        
    def test_7(self):
        with pytest.raises(ValueError) as excinfo:
            cria_intersecao('D', -45)
        assert "cria_intersecao: argumentos invalidos" == str(excinfo.value)

    def test_8(self):
        with pytest.raises(ValueError) as excinfo:
            cria_intersecao('H', 10.0)
        assert "cria_intersecao: argumentos invalidos" == str(excinfo.value)

    def test_9(self):
        with pytest.raises(ValueError) as excinfo:
            cria_intersecao('N', 100)
        assert "cria_intersecao: argumentos invalidos" == str(excinfo.value)
        
    def test_10(self):
        p = cria_intersecao('D', 13)
        assert p == p 

    def test_11(self):
        p = cria_intersecao('S', 19)
        assert p == p 

    def test_12(self):
        p = cria_intersecao('L', 11)
        assert hash(p) == hash(p)

class TestPrivateIntersecaoColuna:
    def test_1(self):
        p = cria_intersecao('C', 4)
        assert obtem_col(p) == 'C'


class TestPrivateIntersecaoLinha:
    def test_1(self):
        p = cria_intersecao('G', 18)
        assert obtem_lin(p) == 18


class TestPrivateIntersecaoEhInter:
    def test_1(self):
        assert not eh_intersecao(True)

    def test_2(self):
        assert not eh_intersecao(27.5)
    
    def test_3(self):
        assert not eh_intersecao(('l', 4))

    def test_4(self):
        assert not eh_intersecao(('BO', 25))
    
    def test_5(self):
        assert eh_intersecao(cria_intersecao('H',19))
 


class TestPrivateIntersecaoIguais:

    def test_1(self):
        c = cria_intersecao('O', 7)
        assert intersecoes_iguais(c, c)

    def test_2(self):
        c1 = cria_intersecao('F', 10)
        c2 = cria_intersecao('F', 11)
        assert not intersecoes_iguais(c1, c2)

    def test_3(self):
        c1 = cria_intersecao('C', 9)
        c2 = cria_intersecao('D', 9)
        assert not intersecoes_iguais(c1, c2)
    

class TestPrivateIntersecaoToString:
    def test_1(self):
        c = cria_intersecao('E', 4)
        assert intersecao_para_str(c) == 'E4' 

    def test_2(self):
        c = cria_intersecao('G', 14)
        assert intersecao_para_str(c) == 'G14'

class TestPrivateIntersecaoToCoord:
    def test_1(self):
        c = cria_intersecao('L', 4)
        assert intersecoes_iguais(str_para_intersecao('L4'), c)

    def test_2(self):
        assert eh_intersecao(str_para_intersecao('M8'))

    def test_3(self):
        assert intersecao_para_str(str_para_intersecao('P7')) == 'P7'


class TestPrivateIntersecaoAdjacentes:
    def test_1(self):
        c = cria_intersecao('R', 8)
        l = cria_intersecao('S', 19)
        p_viz = obtem_intersecoes_adjacentes(c, l)
        assert isinstance(p_viz, tuple) and all((eh_intersecao(a) for a in p_viz))

    def test_2(self):
        c = cria_intersecao('R', 8)
        l = cria_intersecao('S', 19)
        p_viz = obtem_intersecoes_adjacentes(c, l)
        ref = 'R7, Q8, S8, R9'
        assert ', '.join((intersecao_para_str(a) for a in p_viz)) == ref

    def test_3(self):
        c = cria_intersecao('A', 1)
        l = cria_intersecao('S', 19)
        p_viz = obtem_intersecoes_adjacentes(c, l)
        ref = 'B1, A2'
        assert ', '.join((intersecao_para_str(a) for a in p_viz)) == ref

    def test_4(self):
        c = cria_intersecao('A', 7)
        l = cria_intersecao('I', 9)
        p_viz = obtem_intersecoes_adjacentes(c, l)
        ref = 'A6, B7, A8'
        assert ', '.join((intersecao_para_str(a) for a in p_viz)) == ref
        
    def test_5(self):
        c = cria_intersecao('S', 13)
        l = cria_intersecao('S', 19)
        p_viz = obtem_intersecoes_adjacentes(c, l)
        ref = 'S12, R13, S14'
        assert ', '.join((intersecao_para_str(a) for a in p_viz)) == ref
        
    def test_6(self):
        c = cria_intersecao('C', 1)
        l = cria_intersecao('S', 19)
        p_viz = obtem_intersecoes_adjacentes(c, l)
        ref = 'B1, D1, C2'
        assert ', '.join((intersecao_para_str(a) for a in p_viz)) == ref
        
    def test_7(self):
        c = cria_intersecao('S', 19)
        l = cria_intersecao('S', 19) 
        p_viz = obtem_intersecoes_adjacentes(c, l)
        ref = 'S18, R19'
        assert ', '.join((intersecao_para_str(a) for a in p_viz)) == ref
        
        
class TestPrivateIntersecaoOrdena:
    
    def test_1(self):
        
        t = (('G', 10), ('F', 8), ('F', 2), ('P', 13), ('R', 15), ('H', 3), ('H', 19), ('F', 16), 
            ('P', 9), ('M', 7), ('I', 16), ('G', 4), ('D', 11), ('R', 3), ('S', 12), ('S', 8), 
            ('R', 3), ('P', 3), ('O', 16), ('Q', 2), ('B', 10), ('K', 14), ('Q', 7), ('S', 16), 
            ('S', 7), ('H', 5), ('M', 4), ('F', 6), ('R', 2), ('B', 14), ('A', 17), ('L', 11), 
            ('R', 17), ('B', 12), ('E', 14), ('L', 9), ('B', 7), ('B', 14), ('R', 12), ('K', 1))


        t = tuple(cria_intersecao(*s) for s in t)
        ref = 'K1, F2, Q2, R2, H3, P3, R3, R3, G4, M4, H5, F6, B7, M7, Q7, S7, F8, S8, L9, P9, B10, G10, D11, L11, B12, R12, S12, P13, B14, B14, E14, K14, R15, F16, I16, O16, S16, A17, R17, H19'
        assert ', '.join((intersecao_para_str(a) for a in ordena_intersecoes(t))) == ref


    def test_2(self):
        
        t = (cria_intersecao('G', 10),)
        ref = 'G10'
        assert ', '.join((intersecao_para_str(a) for a in ordena_intersecoes(t))) == ref

    def test_3(self):
        t = ()
        ref = ''
        assert ', '.join((intersecao_para_str(a) for a in ordena_intersecoes(t))) == ref


class TestPrivatePedraCria:
    def test_1(self):
        assert (cria_pedra_branca()) != (cria_pedra_preta()) \
            and (cria_pedra_branca()) != (cria_pedra_neutra()) \
                and (cria_pedra_preta()) != (cria_pedra_neutra()) 
        
class TestPrivatePedraEhPedra:
    def test_1(self):
        assert eh_pedra(cria_pedra_branca()) and  eh_pedra(cria_pedra_preta()) and eh_pedra(cria_pedra_neutra())

    def test_2(self):
        assert not eh_pedra(cria_intersecao('B',8))
   
   
class TestPrivatePedraEhPedraBranca:
    def test_1(self):
        assert eh_pedra_branca(cria_pedra_branca()) and not eh_pedra_branca(cria_pedra_preta()) and not eh_pedra_branca(cria_pedra_neutra())

   
class TestPrivatePedraEhPedraPreta:
    def test_1(self):
        assert not eh_pedra_preta(cria_pedra_branca()) and eh_pedra_preta(cria_pedra_preta()) and not eh_pedra_preta(cria_pedra_neutra())

class TestPrivatePedraIguais:
    def test_1(self):
        p1 = cria_pedra_branca()
        p2 = cria_pedra_preta()
        assert pedras_iguais(p1, p1) and pedras_iguais(p2, p2)

    def test_2(self):
        p1 = cria_pedra_branca()
        p2 = cria_pedra_preta()
        assert not pedras_iguais(p1, p2) 
        
    def test_3(self):
        p1 = cria_pedra_branca()
        p2 = cria_pedra_preta()
        assert not pedras_iguais(p1, cria_pedra_neutra()) \
            and  not pedras_iguais(p2, cria_pedra_neutra())

class TestPrivatePedraToString:
    def test_1(self):
        b = cria_pedra_branca()
        p = cria_pedra_preta()
        n = cria_pedra_neutra()
        assert (pedra_para_str(b), pedra_para_str(p), pedra_para_str(n)) == ('O', 'X', '.')

class TestPrivatePedraEhPedraJogador:
    def test_1(self):
        assert eh_pedra_jogador(cria_pedra_branca()) and  eh_pedra_jogador(cria_pedra_preta()) and not eh_pedra_jogador(cria_pedra_neutra())


class TestPrivateGobanCriaVazio:
    def test_1(self):
        with pytest.raises(ValueError) as excinfo:
            cria_goban_vazio(10)
        assert "cria_goban_vazio: argumento invalido" == str(excinfo.value)
           
    def test_2(self):
        with pytest.raises(ValueError) as excinfo:
            cria_goban_vazio(13.0)
        assert "cria_goban_vazio: argumento invalido" == str(excinfo.value)
           
    def test_3(self):
        g1 = cria_goban_vazio(9)
        g2 = cria_goban_vazio(13)
        g3 = cria_goban_vazio(19)
        assert g1 == g1 and g2 == g2 and g3 == g3 
        
           
class TestPrivateGobanCria:
    def test_1(self):
        with pytest.raises(ValueError) as excinfo:
            cria_goban(10, (), ())
        assert "cria_goban: argumentos invalidos" == str(excinfo.value)
           
    def test_2(self):
        with pytest.raises(ValueError) as excinfo:
            cria_goban(19.0, (), ())
        assert "cria_goban: argumentos invalidos" == str(excinfo.value)
           
    def test_3(self):
        with pytest.raises(ValueError) as excinfo:
            cria_goban(19, 19, True)
        assert "cria_goban: argumentos invalidos" == str(excinfo.value)
         
    def test_4(self):
        with pytest.raises(ValueError) as excinfo:
            cria_goban(19, [], {})
        assert "cria_goban: argumentos invalidos" == str(excinfo.value)
             
    def test_5(self):
        with pytest.raises(ValueError) as excinfo:
            cria_goban(19, (), cria_intersecao('A', 8))
        assert "cria_goban: argumentos invalidos" == str(excinfo.value)
                
    def test_6(self):
        with pytest.raises(ValueError) as excinfo:
            cria_goban(9, (), (cria_intersecao('M', 7),))
        assert "cria_goban: argumentos invalidos" == str(excinfo.value)
        
    def test_7(self):
        with pytest.raises(ValueError) as excinfo:
            cria_goban(9, (), (('Z', 99),))
        assert "cria_goban: argumentos invalidos" == str(excinfo.value)
        
    def test_8(self):
        with pytest.raises(ValueError) as excinfo:
            cria_goban(9, (), ('hello', 'world'))
        assert "cria_goban: argumentos invalidos" == str(excinfo.value)
                   
    def test_9(self):
        with pytest.raises(ValueError) as excinfo:
            cria_goban(9, (3.14,2.43), ())
        assert "cria_goban: argumentos invalidos" == str(excinfo.value)
        
    def test_10(self):
        with pytest.raises(ValueError) as excinfo:
            cria_goban(9, (cria_intersecao('A',1), cria_intersecao('A',1)), ())
        assert "cria_goban: argumentos invalidos" == str(excinfo.value)
        
    def test_11(self):
        with pytest.raises(ValueError) as excinfo:
            cria_goban(9, (cria_intersecao('A',1), cria_intersecao('A',2)), (cria_intersecao('B',1), cria_intersecao('A',1)))
        assert "cria_goban: argumentos invalidos" == str(excinfo.value)
        
    def test_12(self):
        g = cria_goban(9, (cria_intersecao('A',1), cria_intersecao('A',2)), (cria_intersecao('B',1), cria_intersecao('B',2)))
        assert g == g
        
    def test_13(self):
        g1 = cria_goban(9, (), ())
        g2 = cria_goban(13, (), ())
        g3 = cria_goban(19, (), ())
        assert g1 == g1 and g2 == g2 and g3 == g3
        
    def test_14(self):
        assert gobans_iguais(cria_goban_vazio(9), cria_goban(9, (), ()))
        
        
class TestPrivateGobanCriaCopia:
    def test_1(self):
        c1 = cria_goban_vazio(19)
        c2 = cria_copia_goban(c1)
        assert id(c1) != id(c2) and gobans_iguais(c1, c2)

    def test_2(self):
        c1 = cria_goban(19, (), ())
        c2 = cria_copia_goban(c1)
        assert id(c1) != id(c2) and gobans_iguais(c1, c2)

    def test_3(self):
        ib = cria_intersecao('C',1), cria_intersecao('C',3), cria_intersecao('D',4)
        ip = cria_intersecao('E',1), cria_intersecao('E',3), cria_intersecao('F',4)
        c1 = cria_goban(13, ib, ip)
        c2 = cria_copia_goban(c1)
        assert id(c1) != id(c2) and gobans_iguais(c1, c2)


class TestPrivateGobanObtemUltimaInt:
    def test_1(self):
        c = cria_goban_vazio(9)
        assert obtem_ultima_intersecao(c) == cria_intersecao('I',9)
        
    def test_2(self):
        c = cria_goban_vazio(19)
        assert obtem_ultima_intersecao(c) == cria_intersecao('S',19)

    def test_3(self):
        c = cria_goban(13, (), ())
        assert obtem_ultima_intersecao(c) == cria_intersecao('M',13)
        

class TestPrivateGobanObtemPedra:
    def test_1(self):
        g = cria_goban_vazio(9)
        p1 = obtem_pedra(g, cria_intersecao('A',1))
        p2 = obtem_pedra(g, cria_intersecao('I',9))
        assert pedras_iguais(p1, p2) and pedras_iguais(p1, cria_pedra_neutra())
  
    def test_2(self):
        g = cria_goban_vazio(19)
        p1 = obtem_pedra(g, cria_intersecao('A',1))
        p2 = obtem_pedra(g, cria_intersecao('S',19))
        assert pedras_iguais(p1, p2) and pedras_iguais(p1, cria_pedra_neutra())
  

    def test_3(self):
        ib = cria_intersecao('C',1), cria_intersecao('C',3), cria_intersecao('D',4)
        ip = cria_intersecao('E',1), cria_intersecao('E',3), cria_intersecao('F',4)
        g = cria_goban(13, ib, ip)
 
        assert all(eh_pedra_branca(obtem_pedra(g, i)) for i in ib) and \
            all(eh_pedra_preta(obtem_pedra(g, i)) for i in ip) and \
                all((not eh_pedra_jogador(obtem_pedra(g, cria_intersecao(L,N))) for L in 'LM' for N in range(1,14,2)))

class TestPrivateGobanObtemCadeia:
    def test_1(self):
        g = cria_goban_vazio(9)
        ref = 'A1, B1, C1, D1, E1, F1, G1, H1, I1, A2, B2, C2, D2, E2, F2, G2, H2, '\
              'I2, A3, B3, C3, D3, E3, F3, G3, H3, I3, A4, B4, C4, D4, E4, F4, G4, '\
              'H4, I4, A5, B5, C5, D5, E5, F5, G5, H5, I5, A6, B6, C6, D6, E6, F6, '\
              'G6, H6, I6, A7, B7, C7, D7, E7, F7, G7, H7, I7, A8, B8, C8, D8, E8, '\
              'F8, G8, H8, I8, A9, B9, C9, D9, E9, F9, G9, H9, I9'
        assert ref == ', '.join(intersecao_para_str(i) for i in obtem_cadeia(g, cria_intersecao('D',5)))
    def test_2(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9'
        g = cria_goban(19, tuple(str_para_intersecao(i) for i in ib), tuple(str_para_intersecao(i) for i in ip))
        ref = 'G5'
        assert ref ==  ', '.join(intersecao_para_str(i) for i in obtem_cadeia(g, cria_intersecao('G',5)))

    def test_3(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9'
        g = cria_goban(9, tuple(str_para_intersecao(i) for i in ib), tuple(str_para_intersecao(i) for i in ip))
        ref = 'E2, E3, E4, E5'
        assert ref ==  ', '.join(intersecao_para_str(i) for i in obtem_cadeia(g, cria_intersecao('E',3)))
        
    def test_4(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9'
        g = cria_goban(13, tuple(str_para_intersecao(i) for i in ib), tuple(str_para_intersecao(i) for i in ip))
        ref = 'F6, F7'
        assert ref ==  ', '.join(intersecao_para_str(i) for i in obtem_cadeia(g, cria_intersecao('F',7)))
        
    def test_5(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9'
        g = cria_goban(9, tuple(str_para_intersecao(i) for i in ib), tuple(str_para_intersecao(i) for i in ip))
        ref = 'E1, F1, G1, H1, I1, F2, G2, H2, I2, F3, G3, H3, I3, F4, G4, H4, I4, F5, H5, I5, G6, H6, I6, G7, H7, I7, H8, I8, H9, I9'
        assert ref ==  ', '.join(intersecao_para_str(i) for i in obtem_cadeia(g, cria_intersecao('G',6)))
        
    def test_6(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9'
        g = cria_goban(9, tuple(str_para_intersecao(i) for i in ib), tuple(str_para_intersecao(i) for i in ip))
        ref = 'D2, D3, D4, D5, D6, E6, E7, E8, F8, F9'
        assert ref ==  ', '.join(intersecao_para_str(i) for i in obtem_cadeia(g, cria_intersecao('E',6)))
        
class TestPrivateGobanColocaPedra:
    def test_1(self):
        g1 = cria_goban_vazio(13)
        g2 = coloca_pedra(g1, cria_intersecao('A',1), cria_pedra_branca()) 
        assert eh_pedra_branca(obtem_pedra(g1, cria_intersecao('A',1))) and id(g1) == id(g2)

    def test_2(self):
        g = cria_goban_vazio(19)
        _ = coloca_pedra(g, cria_intersecao('A',1), cria_pedra_branca()) 
        _ = coloca_pedra(g, cria_intersecao('A',1), cria_pedra_preta()) 
        assert eh_pedra_preta(obtem_pedra(g, cria_intersecao('A',1)))
        
    def test_3(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9'
        g1 = cria_goban(9, tuple(str_para_intersecao(i) for i in ib), tuple(str_para_intersecao(i) for i in ip))
        
        g2 = cria_goban_vazio(9)
        for i in ib: coloca_pedra(g2, str_para_intersecao(i), cria_pedra_branca())
        for i in ip: coloca_pedra(g2, str_para_intersecao(i), cria_pedra_preta())
        
        assert all(pedras_iguais(obtem_pedra(g1, str_para_intersecao(i)),obtem_pedra(g2, str_para_intersecao(i))) for i in ib + ip)


class TestPrivateGobanRemovePedra:
    def test_1(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9'
        g1 = cria_goban(9, tuple(str_para_intersecao(i) for i in ib), tuple(str_para_intersecao(i) for i in ip))
        g2 = cria_copia_goban(g1)
        g3 = remove_pedra(g1, cria_intersecao('D',2))
        assert eh_pedra_branca(obtem_pedra(g2, cria_intersecao('D',2))) and not eh_pedra_jogador(obtem_pedra(g1, cria_intersecao('D',2))) and id(g1) == id(g3)

    def test_2(self):
        g = cria_goban_vazio(13)
        _ = coloca_pedra(g, cria_intersecao('A',1), cria_pedra_preta()) 
        _ = coloca_pedra(g, cria_intersecao('A',2), cria_pedra_preta()) 
        _ = remove_pedra(g, cria_intersecao('A',1)) 
        assert not eh_pedra_jogador(obtem_pedra(g, cria_intersecao('A',1))) and eh_pedra_preta(obtem_pedra(g, cria_intersecao('A',2)))
        
    def test_3(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9'
        g1 = cria_goban(9, tuple(str_para_intersecao(i) for i in ib), tuple(str_para_intersecao(i) for i in ip))
        
        g2 = cria_goban_vazio(9)
        for i in ib+ip: remove_pedra(g1, str_para_intersecao(i))
       
        
        assert all(pedras_iguais(obtem_pedra(g1, str_para_intersecao(i)),obtem_pedra(g2, str_para_intersecao(i))) for i in ib + ip)

 
class TestPrivateGobanRemoveCadeia:
    def test_1(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9', 'B1', 'B2', 'B3', 'B4', 'A4', 'C4', 'D9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9'
        g = cria_goban(9, tuple(str_para_intersecao(i) for i in ib), tuple(str_para_intersecao(i) for i in ip))
        
        g2 = remove_cadeia(g, tuple(str_para_intersecao(i) for i in ib[:5]))
        assert all(not eh_pedra_jogador(obtem_pedra(g, str_para_intersecao(i))) for i in ib[:5]) and id(g) == id(g2)
        
    def test_2(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9', 'B1', 'B2', 'B3', 'B4', 'A4', 'C4', 'D9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9'
        g = cria_goban(9, tuple(str_para_intersecao(i) for i in ib), tuple(str_para_intersecao(i) for i in ip))
        
        _ = remove_cadeia(g, obtem_cadeia(g, cria_intersecao('D',2)))
        assert all(not eh_pedra_jogador(obtem_pedra(g, str_para_intersecao(i))) for i in ib[:-1])  
        
    def test_3(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9', 'B1', 'B2', 'B3', 'B4', 'A4', 'C4', 'D9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9'
        g = cria_goban(9, tuple(str_para_intersecao(i) for i in ib), tuple(str_para_intersecao(i) for i in ip))
        
        _ = remove_cadeia(g, tuple(str_para_intersecao(i) for i in ib))
        _ = remove_cadeia(g, tuple(str_para_intersecao(i) for i in ip))
        assert all(not eh_pedra_jogador(obtem_pedra(g, str_para_intersecao(L+N))) for L in 'ABCDEFGHI' for N in '123456789')  
  
    def test_4(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9', 'B1', 'B2', 'B3', 'B4', 'A4', 'C4', 'D9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9'
        g = cria_goban(13, tuple(str_para_intersecao(i) for i in ib), tuple(str_para_intersecao(i) for i in ip))
        g2 = cria_copia_goban(g)
        _ = remove_cadeia(g, ())
        assert all(pedras_iguais(obtem_pedra(g, str_para_intersecao(L+N)), obtem_pedra(g2, str_para_intersecao(L+N))) for L in 'ABCDEFGHI' for N in '123456789') and id(g) != id(g2)  
  

class TestPrivateGobanEhGoban:
    
    def test_1(self):
        assert not eh_goban(False) and not eh_goban(250)
    
    def test_2(self):
        assert not eh_goban(()) and  not eh_goban({}) and not eh_goban([])
    
    def test_3(self):
        assert eh_goban(cria_goban_vazio(19))
    
    def test_4(self):
        assert eh_goban(cria_copia_goban(cria_goban_vazio(13)))

    def test_5(self):
        assert eh_goban(cria_goban(9,(),()))
    
    def test_6(self):
        assert eh_goban(cria_copia_goban(cria_goban(9,(),())))

    def test_7(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5'
        g = cria_goban(13, tuple(str_para_intersecao(i) for i in ib), tuple(str_para_intersecao(i) for i in ip))
        assert eh_goban(g)
    
    def test_8(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5'
        g = cria_goban(9, tuple(str_para_intersecao(i) for i in ib), tuple(str_para_intersecao(i) for i in ip))
        assert eh_goban(cria_copia_goban(g))

 
class TestPrivateGobanEhIntValida:
    def test_1(self):
        assert not eh_intersecao_valida(cria_goban_vazio(13), cria_intersecao('N', 13))

    def test_2(self):
        assert eh_intersecao_valida(cria_goban_vazio(19), cria_intersecao('S', 19))

    def test_3(self):
        assert not eh_intersecao_valida(cria_goban_vazio(9), cria_intersecao('I', 10))
        
 
class TestPrivateGobanIguais:
    def test_1(self):
        c1 = cria_goban_vazio(9)
        c2 = cria_goban_vazio(9)
        assert gobans_iguais(c1, c2)

    def test_2(self):
        c1 = cria_goban_vazio(9)
        c2 = cria_goban_vazio(19)
        assert not gobans_iguais(c1, c2)

    def test_3(self):
        ib = ('D2',) 
        g1 = cria_goban(13, tuple(str_para_intersecao(i) for i in ib), ())
        g2 = cria_goban(13, (),())
        assert not gobans_iguais(g1, g2)

    def test_4(self):
        ip = ('D2',) 
        g1 = cria_goban(13, (), tuple(str_para_intersecao(i) for i in ip))
        g2 = cria_goban(13, (),())
        assert not gobans_iguais(g1, g2)
 
    def test_5(self):
        g1 = cria_goban_vazio(13)
        g2 = cria_goban(13, (),())
        assert gobans_iguais(g1, g2)

    def test_6(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5'
        g1 = cria_goban(9, tuple(str_para_intersecao(i) for i in ib), tuple(str_para_intersecao(i) for i in ip))
        g2 = cria_goban(9, tuple(str_para_intersecao(i) for i in ib), tuple(str_para_intersecao(i) for i in ip[:-1]))
        assert not gobans_iguais(g1, g2)

    def test_7(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5'
        g1 = cria_goban(9, tuple(str_para_intersecao(i) for i in ib), tuple(str_para_intersecao(i) for i in ip))
        g2 = cria_goban(9, tuple(str_para_intersecao(i) for i in ip), tuple(str_para_intersecao(i) for i in ib))
        assert not gobans_iguais(g1, g2)


class TestPrivateGobanToString:
    def test_1(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9', 'B1', 'B2', 'B3', 'B4', 'A4', 'C4', 'D9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9'
        g = cria_goban(9, tuple(str_para_intersecao(i) for i in ib), tuple(str_para_intersecao(i) for i in ip))
        ref = ('   A B C D E F G H I\n'
               ' 9 . . . O . O X . .  9\n'
               ' 8 . . . . O O X . .  8\n'
               ' 7 . . . . O X . . .  7\n'
               ' 6 . . . O O X . . .  6\n'
               ' 5 . . . O X . X . .  5\n'
               ' 4 O O O O X . . . .  4\n'
               ' 3 . O . O X . . . .  3\n'
               ' 2 . O . O X . . . .  2\n'
               ' 1 . O . X . . . . .  1\n'
               '   A B C D E F G H I')
        assert ref == goban_para_str(g)
        
    def test_2(self):
        g = cria_goban_vazio(13)
        p = cria_pedra_branca(), cria_pedra_preta()
        for L in 'ABCDEFGHIJKLM': 
            for N in range(1,14):
                n = (ord(L) + N) % 4
                if n < 2:
                    coloca_pedra(g, cria_intersecao(L,N), p[n])
        ref = ('   A B C D E F G H I J K L M\n'
               '13 . . O X . . O X . . O X . 13\n'
               '12 X . . O X . . O X . . O X 12\n'
               '11 O X . . O X . . O X . . O 11\n'
               '10 . O X . . O X . . O X . . 10\n'
               ' 9 . . O X . . O X . . O X .  9\n'
               ' 8 X . . O X . . O X . . O X  8\n'
               ' 7 O X . . O X . . O X . . O  7\n'
               ' 6 . O X . . O X . . O X . .  6\n'
               ' 5 . . O X . . O X . . O X .  5\n'
               ' 4 X . . O X . . O X . . O X  4\n'
               ' 3 O X . . O X . . O X . . O  3\n'
               ' 2 . O X . . O X . . O X . .  2\n'
               ' 1 . . O X . . O X . . O X .  1\n'
               '   A B C D E F G H I J K L M')
        assert ref == goban_para_str(g)
        
    def test_3(self):
        g = cria_goban_vazio(19)
        ref = ('   A B C D E F G H I J K L M N O P Q R S\n'
               '19 . . . . . . . . . . . . . . . . . . . 19\n'
               '18 . . . . . . . . . . . . . . . . . . . 18\n'
               '17 . . . . . . . . . . . . . . . . . . . 17\n'
               '16 . . . . . . . . . . . . . . . . . . . 16\n'
               '15 . . . . . . . . . . . . . . . . . . . 15\n'
               '14 . . . . . . . . . . . . . . . . . . . 14\n'
               '13 . . . . . . . . . . . . . . . . . . . 13\n'
               '12 . . . . . . . . . . . . . . . . . . . 12\n'
               '11 . . . . . . . . . . . . . . . . . . . 11\n'
               '10 . . . . . . . . . . . . . . . . . . . 10\n'
               ' 9 . . . . . . . . . . . . . . . . . . .  9\n'
               ' 8 . . . . . . . . . . . . . . . . . . .  8\n'
               ' 7 . . . . . . . . . . . . . . . . . . .  7\n'
               ' 6 . . . . . . . . . . . . . . . . . . .  6\n'
               ' 5 . . . . . . . . . . . . . . . . . . .  5\n'
               ' 4 . . . . . . . . . . . . . . . . . . .  4\n'
               ' 3 . . . . . . . . . . . . . . . . . . .  3\n'
               ' 2 . . . . . . . . . . . . . . . . . . .  2\n'
               ' 1 . . . . . . . . . . . . . . . . . . .  1\n'
               '   A B C D E F G H I J K L M N O P Q R S')
        assert ref == goban_para_str(g)

class TestPrivateGobanTerritorios:
    def test_1(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9', 'B1', 'B2', 'B3', 'B4', 'A4', 'C4', 'D9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9'
        g = cria_goban(9, tuple(str_para_intersecao(i) for i in ib), tuple(str_para_intersecao(i) for i in ip))
        ref = ('A1, A2, A3', 
               'C1, C2, C3', 
               'E1, F1, G1, H1, I1, F2, G2, H2, I2, F3, G3, H3, I3, F4, G4, H4, I4, F5, H5, I5, G6, H6, I6, G7, H7, I7, H8, I8, H9, I9', 
               'A5, B5, C5, A6, B6, C6, A7, B7, C7, D7, A8, B8, C8, D8, A9, B9, C9', 
               'E9')
        hyp = ()
        for t in obtem_territorios(g):
            hyp +=  (', '.join(intersecao_para_str(i) for i in t),)           
        assert ref == hyp
    
    def test_2(self):
        g = cria_goban_vazio(9)
        p = cria_pedra_branca(), cria_pedra_preta()
        for L in 'ABCDEFGHI': 
            for N in range(1,10):
                n = (ord(L) + N) % 2
                coloca_pedra(g, cria_intersecao(L,N), p[n])
        ref = ()
        hyp = ()
        for t in obtem_territorios(g):
            hyp +=  (', '.join(intersecao_para_str(i) for i in t),)           
        assert ref == hyp
        
    
    def test_3(self):
        g = cria_goban_vazio(9)
        ref = ('A1, B1, C1, D1, E1, F1, G1, H1, I1, A2, B2, C2, D2, E2, F2, G2, H2, I2, A3, B3, C3, D3, E3, F3, G3, H3, I3, A4, B4, C4, D4, E4, F4, G4, H4, I4, A5, B5, C5, D5, E5, F5, G5, H5, I5, A6, B6, C6, D6, E6, F6, G6, H6, I6, A7, B7, C7, D7, E7, F7, G7, H7, I7, A8, B8, C8, D8, E8, F8, G8, H8, I8, A9, B9, C9, D9, E9, F9, G9, H9, I9',)
        hyp = ()
        for t in obtem_territorios(g):
            hyp +=  (', '.join(intersecao_para_str(i) for i in t),)           
        assert ref == hyp
        
    def test_4(self):
        g = cria_goban_vazio(13)
        p = cria_pedra_branca(), cria_pedra_preta()
        for L in 'ABCDEFGHIJKLM': 
            for N in range(1,14):
                n = (ord(L) + N) % 5
                if n < 2:
                    coloca_pedra(g, cria_intersecao(L,N), p[n])
        ref = ('B1, C1, D1, A2, B2, C2, A3, B3, A4', 
               'G1, H1, I1, F2, G2, H2, E3, F3, G3, D4, E4, F4, C5, D5, E5, B6, C6, D6, A7, B7, C7, A8, B8, A9', 
               'L1, M1, K2, L2, M2, J3, K3, L3, I4, J4, K4, H5, I5, J5, G6, H6, I6, F7, G7, H7, E8, F8, G8, D9, E9, F9, C10, D10, E10, B11, C11, D11, A12, B12, C12, A13, B13', 
               'M5, L6, M6, K7, L7, M7, J8, K8, L8, I9, J9, K9, H10, I10, J10, G11, H11, I11, F12, G12, H12, E13, F13, G13', 
               'M10, L11, M11, K12, L12, M12, J13, K13, L13')
        hyp = ()
        for t in obtem_territorios(g):
            hyp +=  (', '.join(intersecao_para_str(i) for i in t),)           
        assert ref == hyp
        
    def test_5(self):
        g = cria_goban_vazio(19)
        p = cria_pedra_branca(), cria_pedra_preta()
        for L in 'ABCDEFGHIJKLMNOPQRS': 
            for N in range(1,20):
                n = (ord(L) + N) % 7
                if n < 2:
                    coloca_pedra(g, cria_intersecao(L,N), p[n])
        ref = ('A1, B1, C1, D1, A2, B2, C2, A3, B3, A4', 
               'G1, H1, I1, J1, K1, F2, G2, H2, I2, J2, E3, F3, G3, H3, I3, D4, E4, F4, G4, H4, C5, D5, E5, F5, G5, B6, C6, D6, E6, F6, A7, B7, C7, D7, E7, A8, B8, C8, D8, A9, B9, C9, A10, B10, A11', 
               'N1, O1, P1, Q1, R1, M2, N2, O2, P2, Q2, L3, M3, N3, O3, P3, K4, L4, M4, N4, O4, J5, K5, L5, M5, N5, I6, J6, K6, L6, M6, H7, I7, J7, K7, L7, G8, H8, I8, J8, K8, F9, G9, H9, I9, J9, E10, F10, G10, H10, I10, D11, E11, F11, G11, H11, C12, D12, E12, F12, G12, B13, C13, D13, E13, F13, A14, B14, C14, D14, E14, A15, B15, C15, D15, A16, B16, C16, A17, B17, A18', 'S3, R4, S4, Q5, R5, S5, P6, Q6, R6, S6, O7, P7, Q7, R7, S7, N8, O8, P8, Q8, R8, M9, N9, O9, P9, Q9, L10, M10, N10, O10, P10, K11, L11, M11, N11, O11, J12, K12, L12, M12, N12, I13, J13, K13, L13, M13, H14, I14, J14, K14, L14, G15, H15, I15, J15, K15, F16, G16, H16, I16, J16, E17, F17, G17, H17, I17, D18, E18, F18, G18, H18, C19, D19, E19, F19, G19', 
               'S10, R11, S11, Q12, R12, S12, P13, Q13, R13, S13, O14, P14, Q14, R14, S14, N15, O15, P15, Q15, R15, M16, N16, O16, P16, Q16, L17, M17, N17, O17, P17, K18, L18, M18, N18, O18, J19, K19, L19, M19, N19', 
               'S17, R18, S18, Q19, R19, S19')
        hyp = ()
        for t in obtem_territorios(g):
            hyp +=  (', '.join(intersecao_para_str(i) for i in t),)           
        assert ref == hyp


class TestPrivateGobanAdjacentesDif:
    def test_1(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9', 'B1', 'B2', 'B3', 'B4', 'A4', 'C4', 'D9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9'
        g = cria_goban(9, tuple(str_para_intersecao(i) for i in ib), tuple(str_para_intersecao(i) for i in ip))

        t = tuple(str_para_intersecao(i) for i in ('A1', 'A2', 'A3'))
        ref = 'B1, B2, B3, A4'
        hyp = ', '.join(intersecao_para_str(i) for i in obtem_adjacentes_diferentes(g, t))
        assert ref == hyp 
        
    def test_2(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9', 'B1', 'B2', 'B3', 'B4', 'A4', 'C4', 'D9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9'
        g = cria_goban(9, tuple(str_para_intersecao(i) for i in ib), tuple(str_para_intersecao(i) for i in ip))

        t = tuple(str_para_intersecao(i) for i in ('E9', 'D8', 'D7', 'G7', 'G6', 'E1'))
        ref = 'D1, E2, G5, D6, F6, E7, F7, E8, G8, D9, F9'
        hyp = ', '.join(intersecao_para_str(i) for i in obtem_adjacentes_diferentes(g, t))
        assert ref == hyp 
        
    def test_3(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9', 'B1', 'B2', 'B3', 'B4', 'A4', 'C4', 'D9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9'
        g = cria_goban(9, tuple(str_para_intersecao(i) for i in ib), tuple(str_para_intersecao(i) for i in ip))

        t = tuple(str_para_intersecao(i) for i in ('B1', 'B2', 'D2', 'B3', 'D3', 'A4', 'B4', 'C4', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9'))
        ref = 'A1, C1, A2, C2, A3, C3, A5, B5, C5, C6, D7, D8, E9'
        hyp = ', '.join(intersecao_para_str(i) for i in obtem_adjacentes_diferentes(g, t))
        assert ref == hyp 
        
    def test_4(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9', 'B1', 'B2', 'B3', 'B4', 'A4', 'C4', 'D9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9'
        g = cria_goban(9, tuple(str_para_intersecao(i) for i in ib), tuple(str_para_intersecao(i) for i in ip))

        t = tuple(str_para_intersecao(i) for i in ('E2', 'E3', 'E4', 'E5'))
        ref = 'E1, F2, F3, F4, F5'
        hyp = ', '.join(intersecao_para_str(i) for i in obtem_adjacentes_diferentes(g, t))
        assert ref == hyp 
        
    def test_5(self):
        g = cria_goban_vazio(13)

        t = tuple(cria_intersecao(L,N) for L in 'ABCDEFGHIJKLM' for N in range(1,14))
        ref = ''
        hyp = ', '.join(intersecao_para_str(i) for i in obtem_adjacentes_diferentes(g, t))
        assert ref == hyp 
        
    def test_6(self):
        t = tuple(cria_intersecao(L,N) for L in 'ABCDEFGHIJKLMNOPQRS' for N in range(1,20))
        g = cria_goban(19, t[::2], t[1::2])
        ref = ''
        hyp = ', '.join(intersecao_para_str(i) for i in obtem_adjacentes_diferentes(g, t))
        assert ref == hyp 
        
class TestPrivateGobanJogada:
    def test_1(self):
        ib = 'D1', 'E2', 'F2'
        ip = 'E1', 'F1'
        g = cria_goban(9, tuple(str_para_intersecao(i) for i in ib), tuple(str_para_intersecao(i) for i in ip))
        _ = jogada(g, cria_intersecao('G',1), cria_pedra_branca())
        ref = '   A B C D E F G H I\n 9 . . . . . . . . .  9\n 8 . . . . . . . . .  8\n 7 . . . . . . . . .  7\n 6 . . . . . . . . .  6\n 5 . . . . . . . . .  5\n 4 . . . . . . . . .  4\n 3 . . . . . . . . .  3\n 2 . . . . O O . . .  2\n 1 . . . O . . O . .  1\n   A B C D E F G H I'
        assert ref == goban_para_str(g)
        
    def test_2(self):
        ib = 'D1', 'H1', 'D2', 'I1', 'E2', 'F2', 'G2', 'H2', 'I2'
        ip = 'C1', 'C2', 'D3', 'E1', 'E3', 'F3', 'F1', 'G3', 'H3', 'I3'
        g = cria_goban(9, tuple(str_para_intersecao(i) for i in ib), tuple(str_para_intersecao(i) for i in ip))
        _ = jogada(g, cria_intersecao('G',1), cria_pedra_branca())
        ref = '   A B C D E F G H I\n 9 . . . . . . . . .  9\n 8 . . . . . . . . .  8\n 7 . . . . . . . . .  7\n 6 . . . . . . . . .  6\n 5 . . . . . . . . .  5\n 4 . . . . . . . . .  4\n 3 . . . X X X X X X  3\n 2 . . X O O O O O O  2\n 1 . . X O . . O O O  1\n   A B C D E F G H I'
        assert ref == goban_para_str(g)

    def test_3(self):
        ib = 'D1', 'H1', 'D2', 'I1', 'E2', 'F2', 'G2', 'H2', 'I2'
        ip = 'C1', 'C2', 'D3', 'E1', 'E3', 'F3', 'F1', 'G3', 'H3', 'I3'
        g = cria_goban(9, tuple(str_para_intersecao(i) for i in ib), tuple(str_para_intersecao(i) for i in ip))
        _ = jogada(g, cria_intersecao('G',1), cria_pedra_preta())
        ref = '   A B C D E F G H I\n 9 . . . . . . . . .  9\n 8 . . . . . . . . .  8\n 7 . . . . . . . . .  7\n 6 . . . . . . . . .  6\n 5 . . . . . . . . .  5\n 4 . . . . . . . . .  4\n 3 . . . X X X X X X  3\n 2 . . X . . . . . .  2\n 1 . . X . X X X . .  1\n   A B C D E F G H I'
        assert ref == goban_para_str(g)

    def test_4(self):
        t = tuple(cria_intersecao(L,N) for L in 'ABCDEFGHIJKLM' for N in range(1,14) if not (L == 'F' and N ==7))
        g = cria_goban(13, t, ())
        _ = jogada(g, cria_intersecao('F',7), cria_pedra_preta())
        ref = '   A B C D E F G H I J K L M\n13 . . . . . . . . . . . . . 13\n12 . . . . . . . . . . . . . 12\n11 . . . . . . . . . . . . . 11\n10 . . . . . . . . . . . . . 10\n 9 . . . . . . . . . . . . .  9\n 8 . . . . . . . . . . . . .  8\n 7 . . . . . X . . . . . . .  7\n 6 . . . . . . . . . . . . .  6\n 5 . . . . . . . . . . . . .  5\n 4 . . . . . . . . . . . . .  4\n 3 . . . . . . . . . . . . .  3\n 2 . . . . . . . . . . . . .  2\n 1 . . . . . . . . . . . . .  1\n   A B C D E F G H I J K L M'
        assert ref == goban_para_str(g)
        
    def test_5(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6',  'E8', 'F8', 'F9', 'B1', 'B2', 'B3', 'B4', 'A4', 'C4', 'D9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9', 'E7', 'D8', 'C9'
        g = cria_goban(9, tuple(str_para_intersecao(i) for i in ib), tuple(str_para_intersecao(i) for i in ip))
        _ = jogada(g, cria_intersecao('E',9), cria_pedra_preta())
        ref = '   A B C D E F G H I\n 9 . . X . X . X . .  9\n 8 . . . X . . X . .  8\n 7 . . . . X X . . .  7\n 6 . . . O O X . . .  6\n 5 . . . O X . X . .  5\n 4 O O O O X . . . .  4\n 3 . O . O X . . . .  3\n 2 . O . O X . . . .  2\n 1 . O . X . . . . .  1\n   A B C D E F G H I'
        assert ref == goban_para_str(g)
        
    def test_6(self):
        ib = tuple(str_para_intersecao(i) \
            for i in ('A1', 'A2', 'B1', 'E4', 'E5', 'F4', 'F5', 'G6', 'G7'))
        ip = tuple(str_para_intersecao(i) \
            for i in ('C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'))
        g = cria_goban(9, ib, ip)
        p = cria_pedra_preta()
        _ = jogada(g, cria_intersecao('B', 2), p)
        assert goban_para_str(g) == \
"""   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . . . O . .  7
 6 . . . . . . O . .  6
 5 . . . . O O . . .  5
 4 . . . X O O . . .  4
 3 X X X X . . . . .  3
 2 . X X X . . . . .  2
 1 . . X . . . . . .  1
   A B C D E F G H I"""

class TestPrivateGobanPedrasJogadores:

    def test_1(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9', 'B1', 'B2', 'B3', 'B4', 'A4', 'C4', 'D9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9'
        g = cria_goban(9, tuple(str_para_intersecao(i) for i in ib), tuple(str_para_intersecao(i) for i in ip))
        ref = (17,10)
        assert ref == obtem_pedras_jogadores(g)
        
    def test_2(self):
        g = cria_goban_vazio(13)
        p = cria_pedra_branca(), cria_pedra_preta()
        for L in 'ABCDEFGHIJKLM': 
            for N in range(1,14):
                n = (ord(L) + N) % 4
                if n < 2:
                    coloca_pedra(g, cria_intersecao(L,N), p[n])
        ref = (42,42)
        assert ref == obtem_pedras_jogadores(g)

    def test_3(self):
        g = cria_goban_vazio(9)
        p = cria_pedra_branca(), cria_pedra_preta()
        for L in 'ABCDEFGHI': 
            for N in range(1,10):
                n = (ord(L) + N) % 7
                if n < 3:
                    coloca_pedra(g, cria_intersecao(L,N), p[(1+n)%2])
        ref = (11, 22)
        assert ref == obtem_pedras_jogadores(g)


class TestPrivateCalculaPontos:

    def test_1(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9', 'B1', 'B2', 'B3', 'B4', 'A4', 'C4', 'D9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9'
        g = cria_goban(9, tuple(str_para_intersecao(i) for i in ib), tuple(str_para_intersecao(i) for i in ip))
        ref = (38,40)
        assert ref == calcula_pontos(g)
        
    def test_2(self):
        g = cria_goban_vazio(13)
        p = cria_pedra_branca(), cria_pedra_preta()
        for L in 'ABCDEFGHIJKLM': 
            for N in range(1,14):
                n = (ord(L) + N) % 4
                if n < 2:
                    coloca_pedra(g, cria_intersecao(L,N), p[n])
        ref = (45, 43)
        assert ref == calcula_pontos(g)

    def test_3(self):
        g = cria_goban_vazio(9)
        p = cria_pedra_branca(), cria_pedra_preta()
        for L in 'ABCDEFGHI': 
            for N in range(1,10):
                n = (ord(L) + N) % 7
                if n < 3:
                    coloca_pedra(g, cria_intersecao(L,N), p[(1+n)%2])
        ref = (11, 70)
        assert ref == calcula_pontos(g)

class TestPrivateJogadaLegal:
    def test_1(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9', 'B1', 'B2', 'B3', 'B4', 'A4', 'C4', 'D9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9'
        g = cria_goban(9, tuple(str_para_intersecao(i) for i in ib), tuple(str_para_intersecao(i) for i in ip))
        g_ant = cria_copia_goban(g)
        assert eh_jogada_legal(g, cria_intersecao('E',9), cria_pedra_branca(), cria_goban_vazio(9)) and gobans_iguais(g, g_ant)

    def test_2(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9', 'B1', 'B2', 'B3', 'B4', 'A4', 'C4', 'D9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9'
        g = cria_goban(9, tuple(str_para_intersecao(i) for i in ib), tuple(str_para_intersecao(i) for i in ip))
        g_ant = cria_copia_goban(g)
        assert not eh_jogada_legal(g, cria_intersecao('E',9), cria_pedra_preta(), cria_goban_vazio(9)) and gobans_iguais(g, g_ant)

    def test_3(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9', 'C1', 'C2', 'C3', 'B4', 'A4', 'C4', 'D9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9', 'B1', 'B2', 'B3', 'A2', 'A3'
        g = cria_goban(9, tuple(str_para_intersecao(i) for i in ib), tuple(str_para_intersecao(i) for i in ip))
        g_ant = cria_copia_goban(g)
        assert not eh_jogada_legal(g, cria_intersecao('A',1), cria_pedra_preta(), cria_goban_vazio(9)) and gobans_iguais(g, g_ant)

    def test_4(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9', 'C1', 'C2', 'C3', 'B4', 'A4', 'C4', 'D9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9', 'B1', 'B2', 'B3', 'A2', 'A3'
        g = cria_goban(9, tuple(str_para_intersecao(i) for i in ib), tuple(str_para_intersecao(i) for i in ip))
        g_ant = cria_copia_goban(g)
        assert eh_jogada_legal(g, cria_intersecao('A',1), cria_pedra_branca(), cria_goban_vazio(9)) and gobans_iguais(g, g_ant)

    def test_5(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9', 'C1', 'C2', 'C3', 'B4', 'A4', 'C4', 'D9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9', 'B1', 'B2', 'B3', 'A2', 'A3'
        g = cria_goban(9, tuple(str_para_intersecao(i) for i in ib), tuple(str_para_intersecao(i) for i in ip))
        g_ant = cria_copia_goban(g)
        assert eh_jogada_legal(g, cria_intersecao('I',1), cria_pedra_preta(), cria_goban_vazio(9)) and gobans_iguais(g, g_ant)

    def test_6(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9', 'C1', 'C2', 'C3', 'B4', 'A4', 'C4', 'D9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9', 'B1', 'B2', 'B3', 'A2', 'A3'
        g = cria_goban(19, tuple(str_para_intersecao(i) for i in ib), tuple(str_para_intersecao(i) for i in ip))
        g_ant = cria_copia_goban(g)
        assert not eh_jogada_legal(g, cria_intersecao('E',4), cria_pedra_preta(), cria_goban_vazio(19)) and gobans_iguais(g, g_ant)

    def test_7(self):
        ib = 'B7', 'B8', 'C6', 'D6', 'D8', 'E7', 'E9', 'F7', 'F8', 'F9'
        ip = 'C7', 'C8', 'C9', 'D7', 'D9', 'E6', 'F5', 'F6', 'G7', 'G8'
        g = cria_goban(9, tuple(str_para_intersecao(i) for i in ib), tuple(str_para_intersecao(i) for i in ip))
        # g_ant = cria_copia_goban(g)
        assert eh_jogada_legal(g, cria_intersecao('E',8), cria_pedra_preta(), cria_goban_vazio(9)) 

    def test_8(self):
        ib = 'B7', 'B8', 'C6', 'D6', 'D8', 'E7', 'E9', 'F7', 'F8', 'F9'
        ip = 'C7', 'C8', 'C9', 'D7', 'D9', 'E6', 'F5', 'F6', 'G7', 'G8'
        g = cria_goban(9, tuple(str_para_intersecao(i) for i in ib), tuple(str_para_intersecao(i) for i in ip))
        g_ant = cria_copia_goban(g)
        _ = jogada(g, cria_intersecao('E',8), cria_pedra_preta())
        assert not eh_jogada_legal(g, cria_intersecao('E',7), cria_pedra_branca(), g_ant) 


class TestPrivateTurnoJogador:
    def test_1(self):
        g = cria_goban_vazio(9)
        ref = (True, "Escreva uma intersecao ou 'P' para passar [X]:")
        assert turno_jogador_offline(g, cria_pedra_preta(), cria_goban_vazio(9), 'A1\n') == ref and eh_pedra_preta(obtem_pedra(g, cria_intersecao('A',1)))

    def test_2(self):
        g = cria_goban_vazio(19)
        ref = (True, "Escreva uma intersecao ou 'P' para passar [O]:Escreva uma intersecao ou 'P' para passar [O]:Escreva uma intersecao ou 'P' para passar [O]:Escreva uma intersecao ou 'P' para passar [O]:")
        assert turno_jogador_offline(g, cria_pedra_branca(), cria_goban_vazio(19), 'L\n?1\nAA1\nA2\n') == ref and eh_pedra_branca(obtem_pedra(g, cria_intersecao('A',2)))

    def test_3(self):
        g = cria_goban_vazio(13)
        ref = (True, "Escreva uma intersecao ou 'P' para passar [O]:Escreva uma intersecao ou 'P' para passar [O]:Escreva uma intersecao ou 'P' para passar [O]:Escreva uma intersecao ou 'P' para passar [O]:")
        assert turno_jogador_offline(g, cria_pedra_branca(), cria_goban_vazio(13), 'D99\nALO\nA?\nI8\n') == ref and eh_pedra_branca(obtem_pedra(g, cria_intersecao('I',8)))

    def test_4(self):
        g = cria_goban_vazio(9)
        ref = (False, "Escreva uma intersecao ou 'P' para passar [X]:Escreva uma intersecao ou 'P' para passar [X]:Escreva uma intersecao ou 'P' para passar [X]:Escreva uma intersecao ou 'P' para passar [X]:")
        assert turno_jogador_offline(g, cria_pedra_preta(), cria_goban_vazio(9), 'd7\nA13\nb13\nP\n') == ref 

    def test_5(self):
        g = cria_goban_vazio(19)
        ref = (True, "Escreva uma intersecao ou 'P' para passar [X]:")
        assert turno_jogador_offline(g, cria_pedra_preta(), cria_goban_vazio(9), 'N14\n') == ref 

    def test_6(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9', 'C1', 'C2', 'C3', 'B4', 'A4', 'C4', 'D9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9', 'B1', 'B2', 'B3', 'A2', 'A3'
        g = cria_goban(9, tuple(str_para_intersecao(i) for i in ib), tuple(str_para_intersecao(i) for i in ip))
        ref = (True, "Escreva uma intersecao ou 'P' para passar [X]:Escreva uma intersecao ou 'P' para passar [X]:Escreva uma intersecao ou 'P' para passar [X]:")
        cad = '   A B C D E F G H I\n 9 . . . O . O X . .  9\n 8 . . . . O O X . .  8\n 7 . . . . O X . . .  7\n 6 . . . O O X . . .  6\n 5 . . . O X X X . .  5\n 4 O O O O X . . . .  4\n 3 X X O O X . . . .  3\n 2 X X O O X . . . .  2\n 1 . X O X . . . . .  1\n   A B C D E F G H I'
        assert turno_jogador_offline(g, cria_pedra_preta(), cria_goban_vazio(9), 'E9\nA1\nF5\n') == ref and cad == goban_para_str(g)

    def test_7(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9', 'C1', 'C2', 'C3', 'B4', 'A4', 'C4', 'D9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9', 'B1', 'B2', 'B3', 'A2', 'A3'
        g = cria_goban(9, tuple(str_para_intersecao(i) for i in ib), tuple(str_para_intersecao(i) for i in ip))
        ref = (True, "Escreva uma intersecao ou 'P' para passar [O]:Escreva uma intersecao ou 'P' para passar [O]:")
        cad = '   A B C D E F G H I\n 9 . . . O . O X . .  9\n 8 . . . . O O X . .  8\n 7 . . . . O X . . .  7\n 6 . . . O O X . . .  6\n 5 . . . O X . X . .  5\n 4 O O O O X . . . .  4\n 3 . . O O X . . . .  3\n 2 . . O O X . . . .  2\n 1 O . O X . . . . .  1\n   A B C D E F G H I'
        assert turno_jogador_offline(g, cria_pedra_branca(), cria_goban_vazio(9), 'A2\nA1\n') == ref and cad == goban_para_str(g)
        
    def test_8(self):
        ib = 'B7', 'B8', 'C6', 'D6', 'D8', 'E7', 'E9', 'F7', 'F8', 'F9'
        ip = 'C7', 'C8', 'C9', 'D7', 'D9', 'E6', 'F5', 'F6', 'G7', 'G8'
        g = cria_goban(9, tuple(str_para_intersecao(i) for i in ib), tuple(str_para_intersecao(i) for i in ip))
        g_ant = cria_copia_goban(g)
        _ = turno_jogador_offline(g, cria_pedra_preta(), cria_goban_vazio(9), 'E8\n')
        ref1 = '   A B C D E F G H I\n 9 . . X X O O . . .  9\n 8 . O X . X O X . .  8\n 7 . O X X O O X . .  7\n 6 . . O O X X . . .  6\n 5 . . . . . X . . .  5\n 4 . . . . . . . . .  4\n 3 . . . . . . . . .  3\n 2 . . . . . . . . .  2\n 1 . . . . . . . . .  1\n   A B C D E F G H I'
        hyp1 = goban_para_str(g)
        _ = turno_jogador_offline(g, cria_pedra_branca(), g_ant, 'D8\nG6\n')
        ref2 = '   A B C D E F G H I\n 9 . . X X O O . . .  9\n 8 . O X . X O X . .  8\n 7 . O X X O O X . .  7\n 6 . . O O X X O . .  6\n 5 . . . . . X . . .  5\n 4 . . . . . . . . .  4\n 3 . . . . . . . . .  3\n 2 . . . . . . . . .  2\n 1 . . . . . . . . .  1\n   A B C D E F G H I'
        assert ref1 == hyp1  and ref2 == goban_para_str(g)

    def test_9(self):
        ib = 'B7', 'B8', 'C6', 'D6', 'D8', 'E7', 'E9', 'F7', 'F8', 'F9'
        ip = 'C7', 'C8', 'C9', 'D7', 'D9', 'E6', 'F5', 'F6', 'G7', 'G8'
        g = cria_goban(9, tuple(str_para_intersecao(i) for i in ib), tuple(str_para_intersecao(i) for i in ip))
        _ = turno_jogador_offline(g, cria_pedra_branca(), cria_goban_vazio(9), 'E10\nE8\n')
        ref = '   A B C D E F G H I\n 9 . . X X O O . . .  9\n 8 . O X O O O X . .  8\n 7 . O X X O O X . .  7\n 6 . . O O X X . . .  6\n 5 . . . . . X . . .  5\n 4 . . . . . . . . .  4\n 3 . . . . . . . . .  3\n 2 . . . . . . . . .  2\n 1 . . . . . . . . .  1\n   A B C D E F G H I'
        assert ref == goban_para_str(g)

class TestPrivateGo:
    def test_1(self):
        assert (True, REF_GO_JOGO1) == go_offline(19, (), (), 'S1\nR1\nP\nS2\nO17\nP\nP\n') 
        
    def test_2(self):
        assert (False, REF_GO_JOGO2) == go_offline(13, (), (), 'A3\nA2\nB2\nA1\nC1\nB1\nA3\nA4\nB1\nP\nP\n')
        
    def test_3(self):
        ib = 'B7', 'B8', 'C6', 'D6', 'D8', 'E7', 'E9', 'F7', 'F8', 'F9', 'A5', 'B5', 'A3', 'B3', 'C3', 'D3', 'E3'
        ip = 'C7', 'C8', 'C9', 'D7', 'D9', 'E6', 'F6', 'G7', 'G8', 'C4', 'D4', 'E4', 'A1', 'B1', 'C1', 'D1', 'F1', 'A2', 'B2', 'C2', 'D2', 'F2', 'F3'
        assert  (False, REF_GO_JOGO3) == go_offline(9, ib, ip, 'E8\nD8\nE2\nE1\nD8\nE8\nB4\nA4\nE8\nP\nP\n')

    def test_4(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9', 'B1', 'B2', 'B3', 'B4', 'A4', 'C4', 'D9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9'
        assert (False, REF_GO_JOGO4) == go_offline(9, ib, ip, 'C1\nC2\nE1\nD8\nD7\nC7\nP\nP\n') 

class TestPrivateGoExceptions:
    def test_1(self):
        with pytest.raises(ValueError) as excinfo:
            go('ola', (), ())
        assert "go: argumentos invalidos" == str(excinfo.value)
        
    def test_2(self):
        with pytest.raises(ValueError) as excinfo:
            go(25, (), ())
        assert "go: argumentos invalidos" == str(excinfo.value)

    def test_3(self):
        with pytest.raises(ValueError) as excinfo:
            go(9, True, 5)
        assert "go: argumentos invalidos" == str(excinfo.value)
        
    def test_4(self):
        with pytest.raises(ValueError) as excinfo:
            go(9, [], {})
        assert "go: argumentos invalidos" == str(excinfo.value)

    def test_5(self):
        with pytest.raises(ValueError) as excinfo:
            go(9, ('ola',), ('adeus',))
        assert "go: argumentos invalidos" == str(excinfo.value)

    def test_6(self):
        with pytest.raises(ValueError) as excinfo:
            go(9, (6,), (45,))
        assert "go: argumentos invalidos" == str(excinfo.value)

    def test_7(self):
        with pytest.raises(ValueError) as excinfo:
            go(9, ('A11',), ())
        assert "go: argumentos invalidos" == str(excinfo.value)

    def test_8(self):
        with pytest.raises(ValueError) as excinfo:
            go(9, ('A7',), ('ZZ8',))
        assert "go: argumentos invalidos" == str(excinfo.value)

    def test_9(self):
        with pytest.raises(ValueError) as excinfo:
            go(9, ('A7', 35), ('B8',))
        assert "go: argumentos invalidos" == str(excinfo.value)

    def test_10(self):
        with pytest.raises(ValueError) as excinfo:
            go(9, ('A7', 'B5', 'C4'), ('B8', 'A8', 'B5'))
        assert "go: argumentos invalidos" == str(excinfo.value)


class TestPrivateTADIntersecao:
    
    # score = 0.5

    def test_1(self):
        exec(open(f'{TAD_CODE_PATH}/TAD_intersecao.py', encoding="utf-8").read(), globals())
        c = cria_intersecao('A', 2)
        l = cria_intersecao('S',19)
        ref = ('A1', 'B2', 'A3')
        assert ref == tuple(intersecao_para_str(i) for i in obtem_intersecoes_adjacentes(c, l))
        
    def test_2(self):
        exec(open(f'{TAD_CODE_PATH}/TAD_intersecao.py', encoding="utf-8").read(), globals())
        tup = (cria_intersecao('A',1), cria_intersecao('A',3), cria_intersecao('B',1), cria_intersecao('B',2))
        assert ('A1', 'B1', 'B2', 'A3') == tuple(intersecao_para_str(i) for i in ordena_intersecoes(tup))
        
class TestPrivateTADPedra:
    # score 0.25
    def test_1(self):
        exec(open(f'{TAD_CODE_PATH}/TAD_pedra.py', encoding="utf-8").read(), globals())
        assert eh_pedra_jogador(cria_pedra_branca()) and  eh_pedra_jogador(cria_pedra_preta()) and not eh_pedra_jogador(cria_pedra_neutra())
   
class TestPrivateTADGoban:

    # score = 1.0
    def test_1(self):
            exec(open(f'{TAD_CODE_PATH}/TF_intersecao.py', encoding="utf-8").read(), globals())
            exec(open(f'{TAD_CODE_PATH}/TF_pedra.py', encoding="utf-8").read(), globals())
            g1 = cria_goban_vazio(9)
            g2 = cria_copia_goban(g1)
            assert id(g1) != id(g2) and gobans_iguais(g1, g2)
            
    def test_2(self):
        exec(open(f'{TAD_CODE_PATH}/TF_intersecao.py', encoding="utf-8").read(), globals())
        exec(open(f'{TAD_CODE_PATH}/TF_pedra.py', encoding="utf-8").read(), globals())
        ib = 'B7', 'B8', 'C6', 'D6', 'D8', 'E7', 'E9', 'F7', 'F8', 'F9'
        ip = 'C7', 'C8', 'C9', 'D7', 'D9', 'E6', 'F5', 'F6', 'G7', 'G8'
        g1 = cria_goban(9, tuple(str_para_intersecao(i) for i in ib), tuple(str_para_intersecao(i) for i in ip))
        g2 = cria_copia_goban(g1)
        assert id(g1) != id(g2) and gobans_iguais(g1, g2)

    def test_3(self):
        exec(open(f'{TAD_CODE_PATH}/TF_intersecao.py', encoding="utf-8").read(), globals())
        exec(open(f'{TAD_CODE_PATH}/TF_pedra.py', encoding="utf-8").read(), globals())
        ib = cria_intersecao('C',1), cria_intersecao('C',3), cria_intersecao('D',4)
        ip = cria_intersecao('E',1), cria_intersecao('E',3), cria_intersecao('F',4)
        g = cria_goban(13, ib, ip)
 
        assert all(eh_pedra_branca(obtem_pedra(g, i)) for i in ib) and \
            all(eh_pedra_preta(obtem_pedra(g, i)) for i in ip) and \
                all((not eh_pedra_jogador(obtem_pedra(g, cria_intersecao(L,N))) for L in 'LM' for N in range(1,14,2)))

    def test_4(self):
        exec(open(f'{TAD_CODE_PATH}/TF_intersecao.py', encoding="utf-8").read(), globals())
        exec(open(f'{TAD_CODE_PATH}/TF_pedra.py', encoding="utf-8").read(), globals())
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9'
        g = cria_goban(9, tuple(str_para_intersecao(i) for i in ib), tuple(str_para_intersecao(i) for i in ip))
        ref = 'E2, E3, E4, E5'
        assert ref ==  ', '.join(intersecao_para_str(i) for i in obtem_cadeia(g, cria_intersecao('E',3)))
        
    def test_5(self):
        exec(open(f'{TAD_CODE_PATH}/TF_intersecao.py', encoding="utf-8").read(), globals())
        exec(open(f'{TAD_CODE_PATH}/TF_pedra.py', encoding="utf-8").read(), globals())
        g = cria_goban_vazio(13)
        _ = coloca_pedra(g, cria_intersecao('A',1), cria_pedra_preta()) 
        _ = coloca_pedra(g, cria_intersecao('A',2), cria_pedra_preta()) 
        _ = remove_pedra(g, cria_intersecao('A',1)) 
        assert not eh_pedra_jogador(obtem_pedra(g, cria_intersecao('A',1))) and eh_pedra_preta(obtem_pedra(g, cria_intersecao('A',2)))
      
    def test_6(self):
        exec(open(f'{TAD_CODE_PATH}/TF_intersecao.py', encoding="utf-8").read(), globals())
        exec(open(f'{TAD_CODE_PATH}/TF_pedra.py', encoding="utf-8").read(), globals())
        g = cria_goban_vazio(13)
        _ = coloca_pedra(g, cria_intersecao('A',1), cria_pedra_preta()) 
        _ = coloca_pedra(g, cria_intersecao('A',2), cria_pedra_preta()) 
        _ = remove_pedra(g, cria_intersecao('A',1)) 
        assert eh_goban(g) and eh_goban(cria_copia_goban(g))
          
    def test_7(self):
        exec(open(f'{TAD_CODE_PATH}/TF_intersecao.py', encoding="utf-8").read(), globals())
        exec(open(f'{TAD_CODE_PATH}/TF_pedra.py', encoding="utf-8").read(), globals())
        
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9', 'B1', 'B2', 'B3', 'B4', 'A4', 'C4', 'D9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9'
        g = cria_goban(9, tuple(str_para_intersecao(i) for i in ib), tuple(str_para_intersecao(i) for i in ip))
        
        g2 = remove_cadeia(g, tuple(str_para_intersecao(i) for i in ib[:5]))
        assert all(not eh_pedra_jogador(obtem_pedra(g, str_para_intersecao(i))) for i in ib[:5]) and id(g) == id(g2)
  

    def test_8(self):
        exec(open(f'{TAD_CODE_PATH}/TF_intersecao.py', encoding="utf-8").read(), globals())
        exec(open(f'{TAD_CODE_PATH}/TF_pedra.py', encoding="utf-8").read(), globals()) 
        assert not eh_intersecao_valida(cria_goban_vazio(13), cria_intersecao('N', 13)) and eh_intersecao_valida(cria_goban_vazio(19), cria_intersecao('S', 19))
        
        
    def test_9(self):
        exec(open(f'{TAD_CODE_PATH}/TF_intersecao.py', encoding="utf-8").read(), globals())
        exec(open(f'{TAD_CODE_PATH}/TF_pedra.py', encoding="utf-8").read(), globals())
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9', 'B1', 'B2', 'B3', 'B4', 'A4', 'C4', 'D9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9'
        g = cria_goban(9, tuple(str_para_intersecao(i) for i in ib), tuple(str_para_intersecao(i) for i in ip))
        ref = ('   A B C D E F G H I\n'
               ' 9 . . . O . O X . .  9\n'
               ' 8 . . . . O O X . .  8\n'
               ' 7 . . . . O X . . .  7\n'
               ' 6 . . . O O X . . .  6\n'
               ' 5 . . . O X . X . .  5\n'
               ' 4 O O O O X . . . .  4\n'
               ' 3 . O . O X . . . .  3\n'
               ' 2 . O . O X . . . .  2\n'
               ' 1 . O . X . . . . .  1\n'
               '   A B C D E F G H I')
        assert ref == goban_para_str(g)

    def test_10(self):
        exec(open(f'{TAD_CODE_PATH}/TF_intersecao.py', encoding="utf-8").read(), globals())
        exec(open(f'{TAD_CODE_PATH}/TF_pedra.py', encoding="utf-8").read(), globals())
        g = cria_goban_vazio(13)
        g2 = cria_copia_goban(g)
        _ = coloca_pedra(g, cria_intersecao('A',2), cria_pedra_preta())  
        assert eh_pedra_preta(obtem_pedra(g, cria_intersecao('A',2))) and not eh_pedra_jogador(obtem_pedra(g2, cria_intersecao('A',2)))
    
    def test_11(self):
        exec(open(f'{TAD_CODE_PATH}/TF_intersecao.py', encoding="utf-8").read(), globals())
        exec(open(f'{TAD_CODE_PATH}/TF_pedra.py', encoding="utf-8").read(), globals())
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9', 'B1', 'B2', 'B3', 'B4', 'A4', 'C4', 'D9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9'
        g1 = cria_goban(9, tuple(str_para_intersecao(i) for i in ib), tuple(str_para_intersecao(i) for i in ip))
        g2 = cria_goban(9, tuple(str_para_intersecao(i) for i in ib), tuple(str_para_intersecao(i) for i in ip))
        
        assert gobans_iguais(g1, g2)
    
class TestPrivateTADGobanFAN:
    
    # score = 0.75
    def test_1(self):
        exec(open(f'{TAD_CODE_PATH}/TF_intersecao.py', encoding="utf-8").read(), globals())
        exec(open(f'{TAD_CODE_PATH}/TF_pedra.py', encoding="utf-8").read(), globals())      
        exec(open(f'{TAD_CODE_PATH}/TAD_goban.py', encoding="utf-8").read(), globals())    
        
        g = cria_goban_vazio(9)
        b, p = cria_pedra_branca(), cria_pedra_preta()
        ib = 'C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'
        ip = 'E4', 'E5', 'F4', 'F5', 'G6', 'G7'
        for i in ib: coloca_pedra(g, str_para_intersecao(i), b)
        for i in ip: coloca_pedra(g, str_para_intersecao(i), p)
        cad = obtem_cadeia(g, cria_intersecao('F',5))
        liberdades = obtem_adjacentes_diferentes(g, cad)
        assert tuple(intersecao_para_str(i) for i in liberdades) == ('E3', 'F3', 'G4', 'D5', 'G5', 'E6', 'F6')
        
        
    def test_2(self):
        exec(open(f'{TAD_CODE_PATH}/TF_intersecao.py', encoding="utf-8").read(), globals())
        exec(open(f'{TAD_CODE_PATH}/TF_pedra.py', encoding="utf-8").read(), globals())      
        exec(open(f'{TAD_CODE_PATH}/TAD_goban.py', encoding="utf-8").read(), globals())      
             
        g = cria_goban_vazio(9)
        b, p = cria_pedra_branca(), cria_pedra_preta()
        ib = 'C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'
        ip = 'E4', 'E5', 'F4', 'F5', 'G6', 'G7'
        for i in ib: coloca_pedra(g, str_para_intersecao(i), b)
        for i in ip: coloca_pedra(g, str_para_intersecao(i), p)
        terr = obtem_territorios(g)
        assert tuple(intersecao_para_str(i) for i in terr[0]) == ('A1', 'B1', 'A2', 'B2')

    def test_3(self):
        exec(open(f'{TAD_CODE_PATH}/TF_intersecao.py', encoding="utf-8").read(), globals())
        exec(open(f'{TAD_CODE_PATH}/TF_pedra.py', encoding="utf-8").read(), globals())      
        exec(open(f'{TAD_CODE_PATH}/TAD_goban.py', encoding="utf-8").read(), globals())   
        
        g = cria_goban_vazio(9)
        b, p = cria_pedra_branca(), cria_pedra_preta()
        ib = 'C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'
        ip = 'E4', 'E5', 'F4', 'F5', 'G6', 'G7'
        for i in ib: coloca_pedra(g, str_para_intersecao(i), b)
        for i in ip: coloca_pedra(g, str_para_intersecao(i), p)
        assert obtem_pedras_jogadores(g) == (8, 6)
           
        
    def test_4(self):
        exec(open(f'{TAD_CODE_PATH}/TF_intersecao.py', encoding="utf-8").read(), globals())
        exec(open(f'{TAD_CODE_PATH}/TF_pedra.py', encoding="utf-8").read(), globals())      
        exec(open(f'{TAD_CODE_PATH}/TAD_goban.py', encoding="utf-8").read(), globals()) 
        
        ib = tuple(str_para_intersecao(i) \
            for i in ('C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'))
        ip = tuple(str_para_intersecao(i) \
            for i in ('A1', 'A2', 'B1', 'E4', 'E5', 'F4', 'F5', 'G6', 'G7'))
        g = cria_goban(9, ib, ip)
        b = cria_pedra_branca()
        _ = jogada(g, cria_intersecao('B', 2), b)
        assert goban_para_str(g) == \
"""   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . . . X . .  7
 6 . . . . . . X . .  6
 5 . . . . X X . . .  5
 4 . . . O X X . . .  4
 3 O O O O . . . . .  3
 2 . O O O . . . . .  2
 1 . . O . . . . . .  1
   A B C D E F G H I"""     


class TestPrivateTADCalculaPontos:
    # score = 0.5
    def test_1(self):
        exec(open(f'{TAD_CODE_PATH}/TF_intersecao.py', encoding="utf-8").read(), globals())
        exec(open(f'{TAD_CODE_PATH}/TF_pedra.py', encoding="utf-8").read(), globals())      
        exec(open(f'{TAD_CODE_PATH}/TF_goban.py', encoding="utf-8").read(), globals()) 
        ib = tuple(str_para_intersecao(i) for i in ('C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'))
        ip = tuple(str_para_intersecao(i) for i in ('E4', 'E5', 'F4', 'F5', 'G6', 'G7'))
        g = cria_goban(9, ib, ip)
        assert calcula_pontos(g) == (12, 6)
 
class TestPrivateTADJogadaLegal:
    # score = 0.5
    def test_1(self):
        exec(open(f'{TAD_CODE_PATH}/TF_intersecao.py', encoding="utf-8").read(), globals())
        exec(open(f'{TAD_CODE_PATH}/TF_pedra.py', encoding="utf-8").read(), globals())      
        exec(open(f'{TAD_CODE_PATH}/TF_goban.py', encoding="utf-8").read(), globals()) 
        
        ib = tuple(str_para_intersecao(i) for i in ('C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'))
        ip = tuple(str_para_intersecao(i) for i in ('A1', 'A2', 'B1', 'E4', 'E5', 'F4', 'F5', 'G6', 'G7'))
        g = cria_goban(9, ib, ip)
        l = cria_goban_vazio(9)
        b, p = cria_pedra_branca(), cria_pedra_preta()
        assert not eh_jogada_legal(g, cria_intersecao('B', 2), p, l)
 
class TestPrivateTADTurnoJogador:
    # score = 0.5
    def test_1(self):
        exec(open(f'{TAD_CODE_PATH}/TF_intersecao.py', encoding="utf-8").read(), globals())
        exec(open(f'{TAD_CODE_PATH}/TF_pedra.py', encoding="utf-8").read(), globals())      
        exec(open(f'{TAD_CODE_PATH}/TF_goban.py', encoding="utf-8").read(), globals()) 
        exec(open(f'{TAD_CODE_PATH}/FAN_jogada_legal.py', encoding="utf-8").read(), globals()) 
        
        ib = tuple(str_para_intersecao(i) for i in ('C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'))
        ip = tuple(str_para_intersecao(i) for i in ('A1', 'A2', 'B1', 'E4', 'E5', 'F4', 'F5', 'G6', 'G7'))
        g = cria_goban(9, ib, ip)
        goban_str = \
"""   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . . . X . .  7
 6 . . . . . . X . .  6
 5 . . . . X X X . .  5
 4 . . . O X X . . .  4
 3 O O O O . . . . .  3
 2 X . O O . . . . .  2
 1 X X O . . . . . .  1
   A B C D E F G H I"""
        ref = (True, "Escreva uma intersecao ou 'P' para passar [X]:Escreva uma intersecao ou 'P' para passar [X]:Escreva uma intersecao ou 'P' para passar [X]:")
        assert ref == turno_jogador_offline(g, cria_pedra_preta(), cria_goban_vazio(9), 'B10\nB2\nG5\n') and (goban_para_str(g) == goban_str)

             
class TestPrivateTADGo:

    def test_1(self):
        exec(open(f'{TAD_CODE_PATH}/TF_intersecao.py', encoding="utf-8").read(), globals())
        exec(open(f'{TAD_CODE_PATH}/TF_pedra.py', encoding="utf-8").read(), globals())      
        exec(open(f'{TAD_CODE_PATH}/TF_goban.py', encoding="utf-8").read(), globals()) 
        exec(open(f'{TAD_CODE_PATH}/FAN_jogada_legal.py', encoding="utf-8").read(), globals()) 
        exec(open(f'{TAD_CODE_PATH}/FAN_calcula_pontos.py', encoding="utf-8").read(), globals()) 
        exec(open(f'{TAD_CODE_PATH}/FAN_turno_jogador.py', encoding="utf-8").read(), globals()) 
        
        input_str = 'A1\nB1\nB2\nA2\nA1\nA3\nA1\nC1\nE5\nP\nP\n'
        assert go_offline(9, (), (), input_str) == (False, REF_GO_PUBLIC_JOGO1)
        
    def test_2(self):
        exec(open(f'{TAD_CODE_PATH}/TF_intersecao.py', encoding="utf-8").read(), globals())
        exec(open(f'{TAD_CODE_PATH}/TF_pedra.py', encoding="utf-8").read(), globals())      
        exec(open(f'{TAD_CODE_PATH}/TF_goban.py', encoding="utf-8").read(), globals()) 
        exec(open(f'{TAD_CODE_PATH}/FAN_jogada_legal.py', encoding="utf-8").read(), globals()) 
        exec(open(f'{TAD_CODE_PATH}/FAN_calcula_pontos.py', encoding="utf-8").read(), globals()) 
        exec(open(f'{TAD_CODE_PATH}/FAN_turno_jogador.py', encoding="utf-8").read(), globals()) 
    
        ib = 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'B3', 'I3', 'B4', 'D4', 'E4', 'F4', 'B5', 'D5', 'G5', 'I5', 'B6', 'D6', 'E6', 'F6', 'G6', 'I6', 'C7', 'I7', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8', 'I8'
        ip = 'C3', 'D3', 'E3', 'F3', 'G3', 'C4', 'G4', 'H4', 'C5', 'H5', 'C6', 'H6', 'D7', 'E7', 'F7', 'G7', 'H7'
        assert go_offline(9, ib, ip, 'E5\nF5\nE5\nP\nP\n') == (True, REF_GO_PUBLIC_JOGO2)
     
   
### AUXILIAR CODE NECESSARY TO REPLACE STANDARD INPUT 
class ReplaceStdIn:
    def __init__(self, input_handle):
        self.input = input_handle.split('\n')
        self.line = 0

    def readline(self):
        if len(self.input) == self.line:
            return ''
        result = self.input[self.line]
        self.line += 1
        return result

class ReplaceStdOut:
    def __init__(self):
        self.output = ''

    def write(self, s):
        self.output += s
        return len(s)

    def flush(self):
        return 


def turno_jogador_offline(board, pedra, last, input_jogo):
    oldstdin = sys.stdin
    sys.stdin = ReplaceStdIn(input_handle=input_jogo)
    
    oldstdout, newstdout = sys.stdout,  ReplaceStdOut()
    sys.stdout = newstdout

    try:
        res = turno_jogador(board, pedra, last)
        text = newstdout.output
        return res, text
    except ValueError as e:
        raise e
    finally:
        sys.stdin = oldstdin
        sys.stdout = oldstdout

def go_offline(n, ib, ip, input_jogo):
    oldstdin = sys.stdin
    sys.stdin = ReplaceStdIn(input_handle=input_jogo)
    
    oldstdout, newstdout = sys.stdout,  ReplaceStdOut()
    sys.stdout = newstdout

    try:
        res = go(n, ib, ip)
        text = newstdout.output
        return res, text
    except ValueError as e:
        raise e
    finally:
        sys.stdin = oldstdin
        sys.stdout = oldstdout

REF_GO_JOGO1 = \
"""Branco (O) tem 0 pontos
Preto (X) tem 0 pontos
   A B C D E F G H I J K L M N O P Q R S
19 . . . . . . . . . . . . . . . . . . . 19
18 . . . . . . . . . . . . . . . . . . . 18
17 . . . . . . . . . . . . . . . . . . . 17
16 . . . . . . . . . . . . . . . . . . . 16
15 . . . . . . . . . . . . . . . . . . . 15
14 . . . . . . . . . . . . . . . . . . . 14
13 . . . . . . . . . . . . . . . . . . . 13
12 . . . . . . . . . . . . . . . . . . . 12
11 . . . . . . . . . . . . . . . . . . . 11
10 . . . . . . . . . . . . . . . . . . . 10
 9 . . . . . . . . . . . . . . . . . . .  9
 8 . . . . . . . . . . . . . . . . . . .  8
 7 . . . . . . . . . . . . . . . . . . .  7
 6 . . . . . . . . . . . . . . . . . . .  6
 5 . . . . . . . . . . . . . . . . . . .  5
 4 . . . . . . . . . . . . . . . . . . .  4
 3 . . . . . . . . . . . . . . . . . . .  3
 2 . . . . . . . . . . . . . . . . . . .  2
 1 . . . . . . . . . . . . . . . . . . .  1
   A B C D E F G H I J K L M N O P Q R S
Escreva uma intersecao ou 'P' para passar [X]:Branco (O) tem 0 pontos
Preto (X) tem 361 pontos
   A B C D E F G H I J K L M N O P Q R S
19 . . . . . . . . . . . . . . . . . . . 19
18 . . . . . . . . . . . . . . . . . . . 18
17 . . . . . . . . . . . . . . . . . . . 17
16 . . . . . . . . . . . . . . . . . . . 16
15 . . . . . . . . . . . . . . . . . . . 15
14 . . . . . . . . . . . . . . . . . . . 14
13 . . . . . . . . . . . . . . . . . . . 13
12 . . . . . . . . . . . . . . . . . . . 12
11 . . . . . . . . . . . . . . . . . . . 11
10 . . . . . . . . . . . . . . . . . . . 10
 9 . . . . . . . . . . . . . . . . . . .  9
 8 . . . . . . . . . . . . . . . . . . .  8
 7 . . . . . . . . . . . . . . . . . . .  7
 6 . . . . . . . . . . . . . . . . . . .  6
 5 . . . . . . . . . . . . . . . . . . .  5
 4 . . . . . . . . . . . . . . . . . . .  4
 3 . . . . . . . . . . . . . . . . . . .  3
 2 . . . . . . . . . . . . . . . . . . .  2
 1 . . . . . . . . . . . . . . . . . . X  1
   A B C D E F G H I J K L M N O P Q R S
Escreva uma intersecao ou 'P' para passar [O]:Branco (O) tem 1 pontos
Preto (X) tem 1 pontos
   A B C D E F G H I J K L M N O P Q R S
19 . . . . . . . . . . . . . . . . . . . 19
18 . . . . . . . . . . . . . . . . . . . 18
17 . . . . . . . . . . . . . . . . . . . 17
16 . . . . . . . . . . . . . . . . . . . 16
15 . . . . . . . . . . . . . . . . . . . 15
14 . . . . . . . . . . . . . . . . . . . 14
13 . . . . . . . . . . . . . . . . . . . 13
12 . . . . . . . . . . . . . . . . . . . 12
11 . . . . . . . . . . . . . . . . . . . 11
10 . . . . . . . . . . . . . . . . . . . 10
 9 . . . . . . . . . . . . . . . . . . .  9
 8 . . . . . . . . . . . . . . . . . . .  8
 7 . . . . . . . . . . . . . . . . . . .  7
 6 . . . . . . . . . . . . . . . . . . .  6
 5 . . . . . . . . . . . . . . . . . . .  5
 4 . . . . . . . . . . . . . . . . . . .  4
 3 . . . . . . . . . . . . . . . . . . .  3
 2 . . . . . . . . . . . . . . . . . . .  2
 1 . . . . . . . . . . . . . . . . . O X  1
   A B C D E F G H I J K L M N O P Q R S
Escreva uma intersecao ou 'P' para passar [X]:Branco (O) tem 1 pontos
Preto (X) tem 1 pontos
   A B C D E F G H I J K L M N O P Q R S
19 . . . . . . . . . . . . . . . . . . . 19
18 . . . . . . . . . . . . . . . . . . . 18
17 . . . . . . . . . . . . . . . . . . . 17
16 . . . . . . . . . . . . . . . . . . . 16
15 . . . . . . . . . . . . . . . . . . . 15
14 . . . . . . . . . . . . . . . . . . . 14
13 . . . . . . . . . . . . . . . . . . . 13
12 . . . . . . . . . . . . . . . . . . . 12
11 . . . . . . . . . . . . . . . . . . . 11
10 . . . . . . . . . . . . . . . . . . . 10
 9 . . . . . . . . . . . . . . . . . . .  9
 8 . . . . . . . . . . . . . . . . . . .  8
 7 . . . . . . . . . . . . . . . . . . .  7
 6 . . . . . . . . . . . . . . . . . . .  6
 5 . . . . . . . . . . . . . . . . . . .  5
 4 . . . . . . . . . . . . . . . . . . .  4
 3 . . . . . . . . . . . . . . . . . . .  3
 2 . . . . . . . . . . . . . . . . . . .  2
 1 . . . . . . . . . . . . . . . . . O X  1
   A B C D E F G H I J K L M N O P Q R S
Escreva uma intersecao ou 'P' para passar [O]:Branco (O) tem 361 pontos
Preto (X) tem 0 pontos
   A B C D E F G H I J K L M N O P Q R S
19 . . . . . . . . . . . . . . . . . . . 19
18 . . . . . . . . . . . . . . . . . . . 18
17 . . . . . . . . . . . . . . . . . . . 17
16 . . . . . . . . . . . . . . . . . . . 16
15 . . . . . . . . . . . . . . . . . . . 15
14 . . . . . . . . . . . . . . . . . . . 14
13 . . . . . . . . . . . . . . . . . . . 13
12 . . . . . . . . . . . . . . . . . . . 12
11 . . . . . . . . . . . . . . . . . . . 11
10 . . . . . . . . . . . . . . . . . . . 10
 9 . . . . . . . . . . . . . . . . . . .  9
 8 . . . . . . . . . . . . . . . . . . .  8
 7 . . . . . . . . . . . . . . . . . . .  7
 6 . . . . . . . . . . . . . . . . . . .  6
 5 . . . . . . . . . . . . . . . . . . .  5
 4 . . . . . . . . . . . . . . . . . . .  4
 3 . . . . . . . . . . . . . . . . . . .  3
 2 . . . . . . . . . . . . . . . . . . O  2
 1 . . . . . . . . . . . . . . . . . O .  1
   A B C D E F G H I J K L M N O P Q R S
Escreva uma intersecao ou 'P' para passar [X]:Branco (O) tem 3 pontos
Preto (X) tem 1 pontos
   A B C D E F G H I J K L M N O P Q R S
19 . . . . . . . . . . . . . . . . . . . 19
18 . . . . . . . . . . . . . . . . . . . 18
17 . . . . . . . . . . . . . . X . . . . 17
16 . . . . . . . . . . . . . . . . . . . 16
15 . . . . . . . . . . . . . . . . . . . 15
14 . . . . . . . . . . . . . . . . . . . 14
13 . . . . . . . . . . . . . . . . . . . 13
12 . . . . . . . . . . . . . . . . . . . 12
11 . . . . . . . . . . . . . . . . . . . 11
10 . . . . . . . . . . . . . . . . . . . 10
 9 . . . . . . . . . . . . . . . . . . .  9
 8 . . . . . . . . . . . . . . . . . . .  8
 7 . . . . . . . . . . . . . . . . . . .  7
 6 . . . . . . . . . . . . . . . . . . .  6
 5 . . . . . . . . . . . . . . . . . . .  5
 4 . . . . . . . . . . . . . . . . . . .  4
 3 . . . . . . . . . . . . . . . . . . .  3
 2 . . . . . . . . . . . . . . . . . . O  2
 1 . . . . . . . . . . . . . . . . . O .  1
   A B C D E F G H I J K L M N O P Q R S
Escreva uma intersecao ou 'P' para passar [O]:Branco (O) tem 3 pontos
Preto (X) tem 1 pontos
   A B C D E F G H I J K L M N O P Q R S
19 . . . . . . . . . . . . . . . . . . . 19
18 . . . . . . . . . . . . . . . . . . . 18
17 . . . . . . . . . . . . . . X . . . . 17
16 . . . . . . . . . . . . . . . . . . . 16
15 . . . . . . . . . . . . . . . . . . . 15
14 . . . . . . . . . . . . . . . . . . . 14
13 . . . . . . . . . . . . . . . . . . . 13
12 . . . . . . . . . . . . . . . . . . . 12
11 . . . . . . . . . . . . . . . . . . . 11
10 . . . . . . . . . . . . . . . . . . . 10
 9 . . . . . . . . . . . . . . . . . . .  9
 8 . . . . . . . . . . . . . . . . . . .  8
 7 . . . . . . . . . . . . . . . . . . .  7
 6 . . . . . . . . . . . . . . . . . . .  6
 5 . . . . . . . . . . . . . . . . . . .  5
 4 . . . . . . . . . . . . . . . . . . .  4
 3 . . . . . . . . . . . . . . . . . . .  3
 2 . . . . . . . . . . . . . . . . . . O  2
 1 . . . . . . . . . . . . . . . . . O .  1
   A B C D E F G H I J K L M N O P Q R S
Escreva uma intersecao ou 'P' para passar [X]:Branco (O) tem 3 pontos
Preto (X) tem 1 pontos
   A B C D E F G H I J K L M N O P Q R S
19 . . . . . . . . . . . . . . . . . . . 19
18 . . . . . . . . . . . . . . . . . . . 18
17 . . . . . . . . . . . . . . X . . . . 17
16 . . . . . . . . . . . . . . . . . . . 16
15 . . . . . . . . . . . . . . . . . . . 15
14 . . . . . . . . . . . . . . . . . . . 14
13 . . . . . . . . . . . . . . . . . . . 13
12 . . . . . . . . . . . . . . . . . . . 12
11 . . . . . . . . . . . . . . . . . . . 11
10 . . . . . . . . . . . . . . . . . . . 10
 9 . . . . . . . . . . . . . . . . . . .  9
 8 . . . . . . . . . . . . . . . . . . .  8
 7 . . . . . . . . . . . . . . . . . . .  7
 6 . . . . . . . . . . . . . . . . . . .  6
 5 . . . . . . . . . . . . . . . . . . .  5
 4 . . . . . . . . . . . . . . . . . . .  4
 3 . . . . . . . . . . . . . . . . . . .  3
 2 . . . . . . . . . . . . . . . . . . O  2
 1 . . . . . . . . . . . . . . . . . O .  1
   A B C D E F G H I J K L M N O P Q R S
"""

REF_GO_JOGO2 = \
"""Branco (O) tem 0 pontos
Preto (X) tem 0 pontos
   A B C D E F G H I J K L M
13 . . . . . . . . . . . . . 13
12 . . . . . . . . . . . . . 12
11 . . . . . . . . . . . . . 11
10 . . . . . . . . . . . . . 10
 9 . . . . . . . . . . . . .  9
 8 . . . . . . . . . . . . .  8
 7 . . . . . . . . . . . . .  7
 6 . . . . . . . . . . . . .  6
 5 . . . . . . . . . . . . .  5
 4 . . . . . . . . . . . . .  4
 3 . . . . . . . . . . . . .  3
 2 . . . . . . . . . . . . .  2
 1 . . . . . . . . . . . . .  1
   A B C D E F G H I J K L M
Escreva uma intersecao ou 'P' para passar [X]:Branco (O) tem 0 pontos
Preto (X) tem 169 pontos
   A B C D E F G H I J K L M
13 . . . . . . . . . . . . . 13
12 . . . . . . . . . . . . . 12
11 . . . . . . . . . . . . . 11
10 . . . . . . . . . . . . . 10
 9 . . . . . . . . . . . . .  9
 8 . . . . . . . . . . . . .  8
 7 . . . . . . . . . . . . .  7
 6 . . . . . . . . . . . . .  6
 5 . . . . . . . . . . . . .  5
 4 . . . . . . . . . . . . .  4
 3 X . . . . . . . . . . . .  3
 2 . . . . . . . . . . . . .  2
 1 . . . . . . . . . . . . .  1
   A B C D E F G H I J K L M
Escreva uma intersecao ou 'P' para passar [O]:Branco (O) tem 1 pontos
Preto (X) tem 1 pontos
   A B C D E F G H I J K L M
13 . . . . . . . . . . . . . 13
12 . . . . . . . . . . . . . 12
11 . . . . . . . . . . . . . 11
10 . . . . . . . . . . . . . 10
 9 . . . . . . . . . . . . .  9
 8 . . . . . . . . . . . . .  8
 7 . . . . . . . . . . . . .  7
 6 . . . . . . . . . . . . .  6
 5 . . . . . . . . . . . . .  5
 4 . . . . . . . . . . . . .  4
 3 X . . . . . . . . . . . .  3
 2 O . . . . . . . . . . . .  2
 1 . . . . . . . . . . . . .  1
   A B C D E F G H I J K L M
Escreva uma intersecao ou 'P' para passar [X]:Branco (O) tem 1 pontos
Preto (X) tem 2 pontos
   A B C D E F G H I J K L M
13 . . . . . . . . . . . . . 13
12 . . . . . . . . . . . . . 12
11 . . . . . . . . . . . . . 11
10 . . . . . . . . . . . . . 10
 9 . . . . . . . . . . . . .  9
 8 . . . . . . . . . . . . .  8
 7 . . . . . . . . . . . . .  7
 6 . . . . . . . . . . . . .  6
 5 . . . . . . . . . . . . .  5
 4 . . . . . . . . . . . . .  4
 3 X . . . . . . . . . . . .  3
 2 O X . . . . . . . . . . .  2
 1 . . . . . . . . . . . . .  1
   A B C D E F G H I J K L M
Escreva uma intersecao ou 'P' para passar [O]:Branco (O) tem 2 pontos
Preto (X) tem 2 pontos
   A B C D E F G H I J K L M
13 . . . . . . . . . . . . . 13
12 . . . . . . . . . . . . . 12
11 . . . . . . . . . . . . . 11
10 . . . . . . . . . . . . . 10
 9 . . . . . . . . . . . . .  9
 8 . . . . . . . . . . . . .  8
 7 . . . . . . . . . . . . .  7
 6 . . . . . . . . . . . . .  6
 5 . . . . . . . . . . . . .  5
 4 . . . . . . . . . . . . .  4
 3 X . . . . . . . . . . . .  3
 2 O X . . . . . . . . . . .  2
 1 O . . . . . . . . . . . .  1
   A B C D E F G H I J K L M
Escreva uma intersecao ou 'P' para passar [X]:Branco (O) tem 2 pontos
Preto (X) tem 166 pontos
   A B C D E F G H I J K L M
13 . . . . . . . . . . . . . 13
12 . . . . . . . . . . . . . 12
11 . . . . . . . . . . . . . 11
10 . . . . . . . . . . . . . 10
 9 . . . . . . . . . . . . .  9
 8 . . . . . . . . . . . . .  8
 7 . . . . . . . . . . . . .  7
 6 . . . . . . . . . . . . .  6
 5 . . . . . . . . . . . . .  5
 4 . . . . . . . . . . . . .  4
 3 X . . . . . . . . . . . .  3
 2 O X . . . . . . . . . . .  2
 1 O . X . . . . . . . . . .  1
   A B C D E F G H I J K L M
Escreva uma intersecao ou 'P' para passar [O]:Escreva uma intersecao ou 'P' para passar [O]:Escreva uma intersecao ou 'P' para passar [O]:Branco (O) tem 3 pontos
Preto (X) tem 3 pontos
   A B C D E F G H I J K L M
13 . . . . . . . . . . . . . 13
12 . . . . . . . . . . . . . 12
11 . . . . . . . . . . . . . 11
10 . . . . . . . . . . . . . 10
 9 . . . . . . . . . . . . .  9
 8 . . . . . . . . . . . . .  8
 7 . . . . . . . . . . . . .  7
 6 . . . . . . . . . . . . .  6
 5 . . . . . . . . . . . . .  5
 4 O . . . . . . . . . . . .  4
 3 X . . . . . . . . . . . .  3
 2 O X . . . . . . . . . . .  2
 1 O . X . . . . . . . . . .  1
   A B C D E F G H I J K L M
Escreva uma intersecao ou 'P' para passar [X]:Branco (O) tem 1 pontos
Preto (X) tem 6 pontos
   A B C D E F G H I J K L M
13 . . . . . . . . . . . . . 13
12 . . . . . . . . . . . . . 12
11 . . . . . . . . . . . . . 11
10 . . . . . . . . . . . . . 10
 9 . . . . . . . . . . . . .  9
 8 . . . . . . . . . . . . .  8
 7 . . . . . . . . . . . . .  7
 6 . . . . . . . . . . . . .  6
 5 . . . . . . . . . . . . .  5
 4 O . . . . . . . . . . . .  4
 3 X . . . . . . . . . . . .  3
 2 . X . . . . . . . . . . .  2
 1 . X X . . . . . . . . . .  1
   A B C D E F G H I J K L M
Escreva uma intersecao ou 'P' para passar [O]:Branco (O) tem 1 pontos
Preto (X) tem 6 pontos
   A B C D E F G H I J K L M
13 . . . . . . . . . . . . . 13
12 . . . . . . . . . . . . . 12
11 . . . . . . . . . . . . . 11
10 . . . . . . . . . . . . . 10
 9 . . . . . . . . . . . . .  9
 8 . . . . . . . . . . . . .  8
 7 . . . . . . . . . . . . .  7
 6 . . . . . . . . . . . . .  6
 5 . . . . . . . . . . . . .  5
 4 O . . . . . . . . . . . .  4
 3 X . . . . . . . . . . . .  3
 2 . X . . . . . . . . . . .  2
 1 . X X . . . . . . . . . .  1
   A B C D E F G H I J K L M
Escreva uma intersecao ou 'P' para passar [X]:Branco (O) tem 1 pontos
Preto (X) tem 6 pontos
   A B C D E F G H I J K L M
13 . . . . . . . . . . . . . 13
12 . . . . . . . . . . . . . 12
11 . . . . . . . . . . . . . 11
10 . . . . . . . . . . . . . 10
 9 . . . . . . . . . . . . .  9
 8 . . . . . . . . . . . . .  8
 7 . . . . . . . . . . . . .  7
 6 . . . . . . . . . . . . .  6
 5 . . . . . . . . . . . . .  5
 4 O . . . . . . . . . . . .  4
 3 X . . . . . . . . . . . .  3
 2 . X . . . . . . . . . . .  2
 1 . X X . . . . . . . . . .  1
   A B C D E F G H I J K L M
"""

REF_GO_JOGO3 = \
"""Branco (O) tem 18 pontos
Preto (X) tem 23 pontos
   A B C D E F G H I
 9 . . X X O O . . .  9
 8 . O X O . O X . .  8
 7 . O X X O O X . .  7
 6 . . O O X X . . .  6
 5 O O . . . . . . .  5
 4 . . X X X . . . .  4
 3 O O O O O X . . .  3
 2 X X X X . X . . .  2
 1 X X X X . X . . .  1
   A B C D E F G H I
Escreva uma intersecao ou 'P' para passar [X]:Branco (O) tem 16 pontos
Preto (X) tem 25 pontos
   A B C D E F G H I
 9 . . X X O O . . .  9
 8 . O X . X O X . .  8
 7 . O X X O O X . .  7
 6 . . O O X X . . .  6
 5 O O . . . . . . .  5
 4 . . X X X . . . .  4
 3 O O O O O X . . .  3
 2 X X X X . X . . .  2
 1 X X X X . X . . .  1
   A B C D E F G H I
Escreva uma intersecao ou 'P' para passar [O]:Escreva uma intersecao ou 'P' para passar [O]:Branco (O) tem 17 pontos
Preto (X) tem 25 pontos
   A B C D E F G H I
 9 . . X X O O . . .  9
 8 . O X . X O X . .  8
 7 . O X X O O X . .  7
 6 . . O O X X . . .  6
 5 O O . . . . . . .  5
 4 . . X X X . . . .  4
 3 O O O O O X . . .  3
 2 X X X X O X . . .  2
 1 X X X X . X . . .  1
   A B C D E F G H I
Escreva uma intersecao ou 'P' para passar [X]:Branco (O) tem 17 pontos
Preto (X) tem 26 pontos
   A B C D E F G H I
 9 . . X X O O . . .  9
 8 . O X . X O X . .  8
 7 . O X X O O X . .  7
 6 . . O O X X . . .  6
 5 O O . . . . . . .  5
 4 . . X X X . . . .  4
 3 O O O O O X . . .  3
 2 X X X X O X . . .  2
 1 X X X X X X . . .  1
   A B C D E F G H I
Escreva uma intersecao ou 'P' para passar [O]:Branco (O) tem 19 pontos
Preto (X) tem 24 pontos
   A B C D E F G H I
 9 . . X X O O . . .  9
 8 . O X O . O X . .  8
 7 . O X X O O X . .  7
 6 . . O O X X . . .  6
 5 O O . . . . . . .  5
 4 . . X X X . . . .  4
 3 O O O O O X . . .  3
 2 X X X X O X . . .  2
 1 X X X X X X . . .  1
   A B C D E F G H I
Escreva uma intersecao ou 'P' para passar [X]:Escreva uma intersecao ou 'P' para passar [X]:Branco (O) tem 19 pontos
Preto (X) tem 25 pontos
   A B C D E F G H I
 9 . . X X O O . . .  9
 8 . O X O . O X . .  8
 7 . O X X O O X . .  7
 6 . . O O X X . . .  6
 5 O O . . . . . . .  5
 4 . X X X X . . . .  4
 3 O O O O O X . . .  3
 2 X X X X O X . . .  2
 1 X X X X X X . . .  1
   A B C D E F G H I
Escreva uma intersecao ou 'P' para passar [O]:Branco (O) tem 20 pontos
Preto (X) tem 25 pontos
   A B C D E F G H I
 9 . . X X O O . . .  9
 8 . O X O . O X . .  8
 7 . O X X O O X . .  7
 6 . . O O X X . . .  6
 5 O O . . . . . . .  5
 4 O X X X X . . . .  4
 3 O O O O O X . . .  3
 2 X X X X O X . . .  2
 1 X X X X X X . . .  1
   A B C D E F G H I
Escreva uma intersecao ou 'P' para passar [X]:Branco (O) tem 18 pontos
Preto (X) tem 27 pontos
   A B C D E F G H I
 9 . . X X O O . . .  9
 8 . O X . X O X . .  8
 7 . O X X O O X . .  7
 6 . . O O X X . . .  6
 5 O O . . . . . . .  5
 4 O X X X X . . . .  4
 3 O O O O O X . . .  3
 2 X X X X O X . . .  2
 1 X X X X X X . . .  1
   A B C D E F G H I
Escreva uma intersecao ou 'P' para passar [O]:Branco (O) tem 18 pontos
Preto (X) tem 27 pontos
   A B C D E F G H I
 9 . . X X O O . . .  9
 8 . O X . X O X . .  8
 7 . O X X O O X . .  7
 6 . . O O X X . . .  6
 5 O O . . . . . . .  5
 4 O X X X X . . . .  4
 3 O O O O O X . . .  3
 2 X X X X O X . . .  2
 1 X X X X X X . . .  1
   A B C D E F G H I
Escreva uma intersecao ou 'P' para passar [X]:Branco (O) tem 18 pontos
Preto (X) tem 27 pontos
   A B C D E F G H I
 9 . . X X O O . . .  9
 8 . O X . X O X . .  8
 7 . O X X O O X . .  7
 6 . . O O X X . . .  6
 5 O O . . . . . . .  5
 4 O X X X X . . . .  4
 3 O O O O O X . . .  3
 2 X X X X O X . . .  2
 1 X X X X X X . . .  1
   A B C D E F G H I
"""

REF_GO_JOGO4 = \
"""Branco (O) tem 38 pontos
Preto (X) tem 40 pontos
   A B C D E F G H I
 9 . . . O . O X . .  9
 8 . . . . O O X . .  8
 7 . . . . O X . . .  7
 6 . . . O O X . . .  6
 5 . . . O X . X . .  5
 4 O O O O X . . . .  4
 3 . O . O X . . . .  3
 2 . O . O X . . . .  2
 1 . O . X . . . . .  1
   A B C D E F G H I
Escreva uma intersecao ou 'P' para passar [X]:Branco (O) tem 38 pontos
Preto (X) tem 41 pontos
   A B C D E F G H I
 9 . . . O . O X . .  9
 8 . . . . O O X . .  8
 7 . . . . O X . . .  7
 6 . . . O O X . . .  6
 5 . . . O X . X . .  5
 4 O O O O X . . . .  4
 3 . O . O X . . . .  3
 2 . O . O X . . . .  2
 1 . O X X . . . . .  1
   A B C D E F G H I
Escreva uma intersecao ou 'P' para passar [O]:Branco (O) tem 40 pontos
Preto (X) tem 41 pontos
   A B C D E F G H I
 9 . . . O . O X . .  9
 8 . . . . O O X . .  8
 7 . . . . O X . . .  7
 6 . . . O O X . . .  6
 5 . . . O X . X . .  5
 4 O O O O X . . . .  4
 3 . O . O X . . . .  3
 2 . O O O X . . . .  2
 1 . O X X . . . . .  1
   A B C D E F G H I
Escreva uma intersecao ou 'P' para passar [X]:Branco (O) tem 40 pontos
Preto (X) tem 41 pontos
   A B C D E F G H I
 9 . . . O . O X . .  9
 8 . . . . O O X . .  8
 7 . . . . O X . . .  7
 6 . . . O O X . . .  6
 5 . . . O X . X . .  5
 4 O O O O X . . . .  4
 3 . O . O X . . . .  3
 2 . O O O X . . . .  2
 1 . O X X X . . . .  1
   A B C D E F G H I
Escreva uma intersecao ou 'P' para passar [O]:Branco (O) tem 40 pontos
Preto (X) tem 41 pontos
   A B C D E F G H I
 9 . . . O . O X . .  9
 8 . . . O O O X . .  8
 7 . . . . O X . . .  7
 6 . . . O O X . . .  6
 5 . . . O X . X . .  5
 4 O O O O X . . . .  4
 3 . O . O X . . . .  3
 2 . O O O X . . . .  2
 1 . O X X X . . . .  1
   A B C D E F G H I
Escreva uma intersecao ou 'P' para passar [X]:Branco (O) tem 24 pontos
Preto (X) tem 42 pontos
   A B C D E F G H I
 9 . . . O . O X . .  9
 8 . . . O O O X . .  8
 7 . . . X O X . . .  7
 6 . . . O O X . . .  6
 5 . . . O X . X . .  5
 4 O O O O X . . . .  4
 3 . O . O X . . . .  3
 2 . O O O X . . . .  2
 1 . O X X X . . . .  1
   A B C D E F G H I
Escreva uma intersecao ou 'P' para passar [O]:Branco (O) tem 40 pontos
Preto (X) tem 41 pontos
   A B C D E F G H I
 9 . . . O . O X . .  9
 8 . . . O O O X . .  8
 7 . . O . O X . . .  7
 6 . . . O O X . . .  6
 5 . . . O X . X . .  5
 4 O O O O X . . . .  4
 3 . O . O X . . . .  3
 2 . O O O X . . . .  2
 1 . O X X X . . . .  1
   A B C D E F G H I
Escreva uma intersecao ou 'P' para passar [X]:Branco (O) tem 40 pontos
Preto (X) tem 41 pontos
   A B C D E F G H I
 9 . . . O . O X . .  9
 8 . . . O O O X . .  8
 7 . . O . O X . . .  7
 6 . . . O O X . . .  6
 5 . . . O X . X . .  5
 4 O O O O X . . . .  4
 3 . O . O X . . . .  3
 2 . O O O X . . . .  2
 1 . O X X X . . . .  1
   A B C D E F G H I
Escreva uma intersecao ou 'P' para passar [O]:Branco (O) tem 40 pontos
Preto (X) tem 41 pontos
   A B C D E F G H I
 9 . . . O . O X . .  9
 8 . . . O O O X . .  8
 7 . . O . O X . . .  7
 6 . . . O O X . . .  6
 5 . . . O X . X . .  5
 4 O O O O X . . . .  4
 3 . O . O X . . . .  3
 2 . O O O X . . . .  2
 1 . O X X X . . . .  1
   A B C D E F G H I
"""

REF_GO_PUBLIC_JOGO1 = \
"""Branco (O) tem 0 pontos
Preto (X) tem 0 pontos
   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . . . . . .  7
 6 . . . . . . . . .  6
 5 . . . . . . . . .  5
 4 . . . . . . . . .  4
 3 . . . . . . . . .  3
 2 . . . . . . . . .  2
 1 . . . . . . . . .  1
   A B C D E F G H I
Escreva uma intersecao ou 'P' para passar [X]:Branco (O) tem 0 pontos
Preto (X) tem 81 pontos
   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . . . . . .  7
 6 . . . . . . . . .  6
 5 . . . . . . . . .  5
 4 . . . . . . . . .  4
 3 . . . . . . . . .  3
 2 . . . . . . . . .  2
 1 X . . . . . . . .  1
   A B C D E F G H I
Escreva uma intersecao ou 'P' para passar [O]:Branco (O) tem 1 pontos
Preto (X) tem 1 pontos
   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . . . . . .  7
 6 . . . . . . . . .  6
 5 . . . . . . . . .  5
 4 . . . . . . . . .  4
 3 . . . . . . . . .  3
 2 . . . . . . . . .  2
 1 X O . . . . . . .  1
   A B C D E F G H I
Escreva uma intersecao ou 'P' para passar [X]:Branco (O) tem 1 pontos
Preto (X) tem 2 pontos
   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . . . . . .  7
 6 . . . . . . . . .  6
 5 . . . . . . . . .  5
 4 . . . . . . . . .  4
 3 . . . . . . . . .  3
 2 . X . . . . . . .  2
 1 X O . . . . . . .  1
   A B C D E F G H I
Escreva uma intersecao ou 'P' para passar [O]:Branco (O) tem 3 pontos
Preto (X) tem 1 pontos
   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . . . . . .  7
 6 . . . . . . . . .  6
 5 . . . . . . . . .  5
 4 . . . . . . . . .  4
 3 . . . . . . . . .  3
 2 O X . . . . . . .  2
 1 . O . . . . . . .  1
   A B C D E F G H I
Escreva uma intersecao ou 'P' para passar [X]:Escreva uma intersecao ou 'P' para passar [X]:Branco (O) tem 3 pontos
Preto (X) tem 2 pontos
   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . . . . . .  7
 6 . . . . . . . . .  6
 5 . . . . . . . . .  5
 4 . . . . . . . . .  4
 3 X . . . . . . . .  3
 2 O X . . . . . . .  2
 1 . O . . . . . . .  1
   A B C D E F G H I
Escreva uma intersecao ou 'P' para passar [O]:Branco (O) tem 3 pontos
Preto (X) tem 2 pontos
   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . . . . . .  7
 6 . . . . . . . . .  6
 5 . . . . . . . . .  5
 4 . . . . . . . . .  4
 3 X . . . . . . . .  3
 2 O X . . . . . . .  2
 1 O O . . . . . . .  1
   A B C D E F G H I
Escreva uma intersecao ou 'P' para passar [X]:Branco (O) tem 0 pontos
Preto (X) tem 81 pontos
   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . . . . . .  7
 6 . . . . . . . . .  6
 5 . . . . . . . . .  5
 4 . . . . . . . . .  4
 3 X . . . . . . . .  3
 2 . X . . . . . . .  2
 1 . . X . . . . . .  1
   A B C D E F G H I
Escreva uma intersecao ou 'P' para passar [O]:Branco (O) tem 1 pontos
Preto (X) tem 6 pontos
   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . . . . . .  7
 6 . . . . . . . . .  6
 5 . . . . O . . . .  5
 4 . . . . . . . . .  4
 3 X . . . . . . . .  3
 2 . X . . . . . . .  2
 1 . . X . . . . . .  1
   A B C D E F G H I
Escreva uma intersecao ou 'P' para passar [X]:Branco (O) tem 1 pontos
Preto (X) tem 6 pontos
   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . . . . . .  7
 6 . . . . . . . . .  6
 5 . . . . O . . . .  5
 4 . . . . . . . . .  4
 3 X . . . . . . . .  3
 2 . X . . . . . . .  2
 1 . . X . . . . . .  1
   A B C D E F G H I
Escreva uma intersecao ou 'P' para passar [O]:Branco (O) tem 1 pontos
Preto (X) tem 6 pontos
   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . . . . . .  7
 6 . . . . . . . . .  6
 5 . . . . O . . . .  5
 4 . . . . . . . . .  4
 3 X . . . . . . . .  3
 2 . X . . . . . . .  2
 1 . . X . . . . . .  1
   A B C D E F G H I
"""
    
REF_GO_PUBLIC_JOGO2 = \
"""Branco (O) tem 62 pontos
Preto (X) tem 17 pontos
   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . O O O O O O O  8
 7 . . O X X X X X O  7
 6 . O X O O O O X O  6
 5 . O X O . . O X O  5
 4 . O X O O O X X .  4
 3 . O X X X X X . O  3
 2 . . O O O O O O .  2
 1 . . . . . . . . .  1
   A B C D E F G H I
Escreva uma intersecao ou 'P' para passar [X]:Branco (O) tem 60 pontos
Preto (X) tem 18 pontos
   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . O O O O O O O  8
 7 . . O X X X X X O  7
 6 . O X O O O O X O  6
 5 . O X O X . O X O  5
 4 . O X O O O X X .  4
 3 . O X X X X X . O  3
 2 . . O O O O O O .  2
 1 . . . . . . . . .  1
   A B C D E F G H I
Escreva uma intersecao ou 'P' para passar [O]:Branco (O) tem 62 pontos
Preto (X) tem 17 pontos
   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . O O O O O O O  8
 7 . . O X X X X X O  7
 6 . O X O O O O X O  6
 5 . O X O . O O X O  5
 4 . O X O O O X X .  4
 3 . O X X X X X . O  3
 2 . . O O O O O O .  2
 1 . . . . . . . . .  1
   A B C D E F G H I
Escreva uma intersecao ou 'P' para passar [X]:Branco (O) tem 51 pontos
Preto (X) tem 28 pontos
   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . O O O O O O O  8
 7 . . O X X X X X O  7
 6 . O X . . . . X O  6
 5 . O X . X . . X O  5
 4 . O X . . . X X .  4
 3 . O X X X X X . O  3
 2 . . O O O O O O .  2
 1 . . . . . . . . .  1
   A B C D E F G H I
Escreva uma intersecao ou 'P' para passar [O]:Branco (O) tem 51 pontos
Preto (X) tem 28 pontos
   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . O O O O O O O  8
 7 . . O X X X X X O  7
 6 . O X . . . . X O  6
 5 . O X . X . . X O  5
 4 . O X . . . X X .  4
 3 . O X X X X X . O  3
 2 . . O O O O O O .  2
 1 . . . . . . . . .  1
   A B C D E F G H I
Escreva uma intersecao ou 'P' para passar [X]:Branco (O) tem 51 pontos
Preto (X) tem 28 pontos
   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . O O O O O O O  8
 7 . . O X X X X X O  7
 6 . O X . . . . X O  6
 5 . O X . X . . X O  5
 4 . O X . . . X X .  4
 3 . O X X X X X . O  3
 2 . . O O O O O O .  2
 1 . . . . . . . . .  1
   A B C D E F G H I
"""
