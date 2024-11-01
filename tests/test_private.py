import pytest
import sys
project_filename = 'Gogame.py'
ADT_CODE_PATH = './tests/ADT_code'
# from projectoFP import *

@pytest.fixture(autouse=True)
def run_around_tests():
    # Code that will run before your test, for example:
    exec(open(project_filename, encoding="utf-8").read(), globals())

    # A test function will be run at this point
    yield
    
    # Code that will run after your test, for example:
    

class TestPrivateNewIntersection:
    def test_1(self):
        with pytest.raises(ValueError) as excinfo:
            new_intersection(200, 10)
        assert "new_intersection: invalid arguments" == str(excinfo.value)
        
    def test_2(self):
        with pytest.raises(ValueError) as excinfo:
            new_intersection('B', (10,))
        assert "new_intersection: invalid arguments" == str(excinfo.value)
     
    def test_3(self):
        with pytest.raises(ValueError) as excinfo:
            new_intersection('d', 10)
        assert "new_intersection: invalid arguments" == str(excinfo.value)
        
    def test_4(self):
        with pytest.raises(ValueError) as excinfo:
            new_intersection('!', 10)
        assert "new_intersection: invalid arguments" == str(excinfo.value)
     
    def test_5(self):
        with pytest.raises(ValueError) as excinfo:
            new_intersection('CA', 10)
        assert "new_intersection: invalid arguments" == str(excinfo.value)
     
    def test_6(self):
        with pytest.raises(ValueError) as excinfo:
            new_intersection('D', '1')
        assert "new_intersection: invalid arguments" == str(excinfo.value)
        
    def test_7(self):
        with pytest.raises(ValueError) as excinfo:
            new_intersection('D', -45)
        assert "new_intersection: invalid arguments" == str(excinfo.value)

    def test_8(self):
        with pytest.raises(ValueError) as excinfo:
            new_intersection('H', 10.0)
        assert "new_intersection: invalid arguments" == str(excinfo.value)

    def test_9(self):
        with pytest.raises(ValueError) as excinfo:
            new_intersection('N', 100)
        assert "new_intersection: invalid arguments" == str(excinfo.value)
        
    def test_10(self):
        p = new_intersection('D', 13)
        assert p == p 

    def test_11(self):
        p = new_intersection('S', 19)
        assert p == p 

    def test_12(self):
        p = new_intersection('L', 11)
        assert hash(p) == hash(p)

class TestPrivateColumnIntersection:
    def test_1(self):
        p = new_intersection('C', 4)
        assert get_col(p) == 'C'


class TestPrivateRowIntersection:
    def test_1(self):
        p = new_intersection('G', 18)
        assert get_row(p) == 18


class TestPrivateIntersectionIsInter:
    def test_1(self):
        assert not is_intersection(True)

    def test_2(self):
        assert not is_intersection(27.5)
    
    def test_3(self):
        assert not is_intersection(('l', 4))

    def test_4(self):
        assert not is_intersection(('BO', 25))
    
    def test_5(self):
        assert is_intersection(new_intersection('H',19))
 


class TestPrivateisEqualsIntersection:

    def test_1(self):
        c = new_intersection('O', 7)
        assert equals_intersection(c, c)

    def test_2(self):
        c1 = new_intersection('F', 10)
        c2 = new_intersection('F', 11)
        assert not equals_intersection(c1, c2)

    def test_3(self):
        c1 = new_intersection('C', 9)
        c2 = new_intersection('D', 9)
        assert not equals_intersection(c1, c2)
    

class TestPrivateIntersectionToString:
    def test_1(self):
        c = new_intersection('E', 4)
        assert intersection_to_str(c) == 'E4' 

    def test_2(self):
        c = new_intersection('G', 14)
        assert intersection_to_str(c) == 'G14'

class TestPrivateIntersectionToCoord:
    def test_1(self):
        c = new_intersection('L', 4)
        assert equals_intersection(str_to_intersection('L4'), c)

    def test_2(self):
        assert is_intersection(str_to_intersection('M8'))

    def test_3(self):
        assert intersection_to_str(str_to_intersection('P7')) == 'P7'


class TestPrivateAdjacentIntersections:
    def test_1(self):
        c = new_intersection('R', 8)
        l = new_intersection('S', 19)
        p_viz = get_adjacent_intersections(c, l)
        assert isinstance(p_viz, tuple) and all((is_intersection(a) for a in p_viz))

    def test_2(self):
        c = new_intersection('R', 8)
        l = new_intersection('S', 19)
        p_viz = get_adjacent_intersections(c, l)
        ref = 'R7, Q8, S8, R9'
        assert ', '.join((intersection_to_str(a) for a in p_viz)) == ref

    def test_3(self):
        c = new_intersection('A', 1)
        l = new_intersection('S', 19)
        p_viz = get_adjacent_intersections(c, l)
        ref = 'B1, A2'
        assert ', '.join((intersection_to_str(a) for a in p_viz)) == ref

    def test_4(self):
        c = new_intersection('A', 7)
        l = new_intersection('I', 9)
        p_viz = get_adjacent_intersections(c, l)
        ref = 'A6, B7, A8'
        assert ', '.join((intersection_to_str(a) for a in p_viz)) == ref
        
    def test_5(self):
        c = new_intersection('S', 13)
        l = new_intersection('S', 19)
        p_viz = get_adjacent_intersections(c, l)
        ref = 'S12, R13, S14'
        assert ', '.join((intersection_to_str(a) for a in p_viz)) == ref
        
    def test_6(self):
        c = new_intersection('C', 1)
        l = new_intersection('S', 19)
        p_viz = get_adjacent_intersections(c, l)
        ref = 'B1, D1, C2'
        assert ', '.join((intersection_to_str(a) for a in p_viz)) == ref
        
    def test_7(self):
        c = new_intersection('S', 19)
        l = new_intersection('S', 19) 
        p_viz = get_adjacent_intersections(c, l)
        ref = 'S18, R19'
        assert ', '.join((intersection_to_str(a) for a in p_viz)) == ref
        
        
class TestPrivateSortIntersections:
    
    def test_1(self):
        
        t = (('G', 10), ('F', 8), ('F', 2), ('P', 13), ('R', 15), ('H', 3), ('H', 19), ('F', 16), 
            ('P', 9), ('M', 7), ('I', 16), ('G', 4), ('D', 11), ('R', 3), ('S', 12), ('S', 8), 
            ('R', 3), ('P', 3), ('O', 16), ('Q', 2), ('B', 10), ('K', 14), ('Q', 7), ('S', 16), 
            ('S', 7), ('H', 5), ('M', 4), ('F', 6), ('R', 2), ('B', 14), ('A', 17), ('L', 11), 
            ('R', 17), ('B', 12), ('E', 14), ('L', 9), ('B', 7), ('B', 14), ('R', 12), ('K', 1))


        t = tuple(new_intersection(*s) for s in t)
        ref = 'K1, F2, Q2, R2, H3, P3, R3, R3, G4, M4, H5, F6, B7, M7, Q7, S7, F8, S8, L9, P9, B10, G10, D11, L11, B12, R12, S12, P13, B14, B14, E14, K14, R15, F16, I16, O16, S16, A17, R17, H19'
        assert ', '.join((intersection_to_str(a) for a in sort_intersections(t))) == ref


    def test_2(self):
        
        t = (new_intersection('G', 10),)
        ref = 'G10'
        assert ', '.join((intersection_to_str(a) for a in sort_intersections(t))) == ref

    def test_3(self):
        t = ()
        ref = ''
        assert ', '.join((intersection_to_str(a) for a in sort_intersections(t))) == ref


class TestPrivateNewPedra:
    def test_1(self):
        assert (new_white_stone()) != (new_black_stone()) \
            and (new_white_stone()) != (new_empty_stone()) \
                and (new_black_stone()) != (new_empty_stone()) 
        
class TestPrivateStoneIsStone:
    def test_1(self):
        assert is_stone(new_white_stone()) and  is_stone(new_black_stone()) and is_stone(new_empty_stone())

    def test_2(self):
        assert not is_stone(new_intersection('B',8))
   
   
class TestPrivateStoneIsWhiteStone:
    def test_1(self):
        assert is_white_stone(new_white_stone()) and not is_white_stone(new_black_stone()) and not is_white_stone(new_empty_stone())

   
class TestPrivateStoneIsBlackStone:
    def test_1(self):
        assert not is_black_stone(new_white_stone()) and is_black_stone(new_black_stone()) and not is_black_stone(new_empty_stone())

class TestPrivateEqualsStones:
    def test_1(self):
        p1 = new_white_stone()
        p2 = new_black_stone()
        assert equals_stones(p1, p1) and equals_stones(p2, p2)

    def test_2(self):
        p1 = new_white_stone()
        p2 = new_black_stone()
        assert not equals_stones(p1, p2) 
        
    def test_3(self):
        p1 = new_white_stone()
        p2 = new_black_stone()
        assert not equals_stones(p1, new_empty_stone()) \
            and  not equals_stones(p2, new_empty_stone())

class TestPrivateStoneToString:
    def test_1(self):
        b = new_white_stone()
        p = new_black_stone()
        n = new_empty_stone()
        assert (stone_to_str(b), stone_to_str(p), stone_to_str(n)) == ('O', 'X', '.')

class TestPrivateStoneIsPlayerStone:
    def test_1(self):
        assert is_player_stone(new_white_stone()) and  is_player_stone(new_black_stone()) and not is_player_stone(new_empty_stone())


class TestPrivateNewEmptyGoban:
    def test_1(self):
        with pytest.raises(ValueError) as excinfo:
            new_empty_goban(10)
        assert "new_empty_goban: invalid arguments" == str(excinfo.value)
           
    def test_2(self):
        with pytest.raises(ValueError) as excinfo:
            new_empty_goban(13.0)
        assert "new_empty_goban: invalid arguments" == str(excinfo.value)
           
    def test_3(self):
        g1 = new_empty_goban(9)
        g2 = new_empty_goban(13)
        g3 = new_empty_goban(19)
        assert g1 == g1 and g2 == g2 and g3 == g3 
        
           
class TestPrivateNewGoban:
    def test_1(self):
        with pytest.raises(ValueError) as excinfo:
            new_goban(10, (), ())
        assert "new_goban: invalid arguments" == str(excinfo.value)
           
    def test_2(self):
        with pytest.raises(ValueError) as excinfo:
            new_goban(19.0, (), ())
        assert "new_goban: invalid arguments" == str(excinfo.value)
           
    def test_3(self):
        with pytest.raises(ValueError) as excinfo:
            new_goban(19, 19, True)
        assert "new_goban: invalid arguments" == str(excinfo.value)
         
    def test_4(self):
        with pytest.raises(ValueError) as excinfo:
            new_goban(19, [], {})
        assert "new_goban: invalid arguments" == str(excinfo.value)
             
    def test_5(self):
        with pytest.raises(ValueError) as excinfo:
            new_goban(19, (), new_intersection('A', 8))
        assert "new_goban: invalid arguments" == str(excinfo.value)
                
    def test_6(self):
        with pytest.raises(ValueError) as excinfo:
            new_goban(9, (), (new_intersection('M', 7),))
        assert "new_goban: invalid arguments" == str(excinfo.value)
        
    def test_7(self):
        with pytest.raises(ValueError) as excinfo:
            new_goban(9, (), (('Z', 99),))
        assert "new_goban: invalid arguments" == str(excinfo.value)
        
    def test_8(self):
        with pytest.raises(ValueError) as excinfo:
            new_goban(9, (), ('hello', 'world'))
        assert "new_goban: invalid arguments" == str(excinfo.value)
                   
    def test_9(self):
        with pytest.raises(ValueError) as excinfo:
            new_goban(9, (3.14,2.43), ())
        assert "new_goban: invalid arguments" == str(excinfo.value)
        
    def test_10(self):
        with pytest.raises(ValueError) as excinfo:
            new_goban(9, (new_intersection('A',1), new_intersection('A',1)), ())
        assert "new_goban: invalid arguments" == str(excinfo.value)
        
    def test_11(self):
        with pytest.raises(ValueError) as excinfo:
            new_goban(9, (new_intersection('A',1), new_intersection('A',2)), (new_intersection('B',1), new_intersection('A',1)))
        assert "new_goban: invalid arguments" == str(excinfo.value)
        
    def test_12(self):
        g = new_goban(9, (new_intersection('A',1), new_intersection('A',2)), (new_intersection('B',1), new_intersection('B',2)))
        assert g == g
        
    def test_13(self):
        g1 = new_goban(9, (), ())
        g2 = new_goban(13, (), ())
        g3 = new_goban(19, (), ())
        assert g1 == g1 and g2 == g2 and g3 == g3
        
    def test_14(self):
        assert goban_equals(new_empty_goban(9), new_goban(9, (), ()))
        
        
class TestPrivateCopyGoban:
    def test_1(self):
        c1 = new_empty_goban(19)
        c2 = copy_goban(c1)
        assert id(c1) != id(c2) and goban_equals(c1, c2)

    def test_2(self):
        c1 = new_goban(19, (), ())
        c2 = copy_goban(c1)
        assert id(c1) != id(c2) and goban_equals(c1, c2)

    def test_3(self):
        ib = new_intersection('C',1), new_intersection('C',3), new_intersection('D',4)
        ip = new_intersection('E',1), new_intersection('E',3), new_intersection('F',4)
        c1 = new_goban(13, ib, ip)
        c2 = copy_goban(c1)
        assert id(c1) != id(c2) and goban_equals(c1, c2)


class TestPrivateGetLastIntersection:
    def test_1(self):
        c = new_empty_goban(9)
        assert get_last_intersection(c) == new_intersection('I',9)
        
    def test_2(self):
        c = new_empty_goban(19)
        assert get_last_intersection(c) == new_intersection('S',19)

    def test_3(self):
        c = new_goban(13, (), ())
        assert get_last_intersection(c) == new_intersection('M',13)
        

class TestPrivateGobanGetStone:
    def test_1(self):
        g = new_empty_goban(9)
        p1 = get_stone(g, new_intersection('A',1))
        p2 = get_stone(g, new_intersection('I',9))
        assert equals_stones(p1, p2) and equals_stones(p1, new_empty_stone())
  
    def test_2(self):
        g = new_empty_goban(19)
        p1 = get_stone(g, new_intersection('A',1))
        p2 = get_stone(g, new_intersection('S',19))
        assert equals_stones(p1, p2) and equals_stones(p1, new_empty_stone())
  

    def test_3(self):
        ib = new_intersection('C',1), new_intersection('C',3), new_intersection('D',4)
        ip = new_intersection('E',1), new_intersection('E',3), new_intersection('F',4)
        g = new_goban(13, ib, ip)
 
        assert all(is_white_stone(get_stone(g, i)) for i in ib) and \
            all(is_black_stone(get_stone(g, i)) for i in ip) and \
                all((not is_player_stone(get_stone(g, new_intersection(L,N))) for L in 'LM' for N in range(1,14,2)))

class TestPrivateGobanGetStoneChain:
    def test_1(self):
        g = new_empty_goban(9)
        ref = 'A1, B1, C1, D1, E1, F1, G1, H1, I1, A2, B2, C2, D2, E2, F2, G2, H2, '\
              'I2, A3, B3, C3, D3, E3, F3, G3, H3, I3, A4, B4, C4, D4, E4, F4, G4, '\
              'H4, I4, A5, B5, C5, D5, E5, F5, G5, H5, I5, A6, B6, C6, D6, E6, F6, '\
              'G6, H6, I6, A7, B7, C7, D7, E7, F7, G7, H7, I7, A8, B8, C8, D8, E8, '\
              'F8, G8, H8, I8, A9, B9, C9, D9, E9, F9, G9, H9, I9'
        assert ref == ', '.join(intersection_to_str(i) for i in get_stone_chain(g, new_intersection('D',5)))
    def test_2(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9'
        g = new_goban(19, tuple(str_to_intersection(i) for i in ib), tuple(str_to_intersection(i) for i in ip))
        ref = 'G5'
        assert ref ==  ', '.join(intersection_to_str(i) for i in get_stone_chain(g, new_intersection('G',5)))

    def test_3(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9'
        g = new_goban(9, tuple(str_to_intersection(i) for i in ib), tuple(str_to_intersection(i) for i in ip))
        ref = 'E2, E3, E4, E5'
        assert ref ==  ', '.join(intersection_to_str(i) for i in get_stone_chain(g, new_intersection('E',3)))
        
    def test_4(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9'
        g = new_goban(13, tuple(str_to_intersection(i) for i in ib), tuple(str_to_intersection(i) for i in ip))
        ref = 'F6, F7'
        assert ref ==  ', '.join(intersection_to_str(i) for i in get_stone_chain(g, new_intersection('F',7)))
        
    def test_5(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9'
        g = new_goban(9, tuple(str_to_intersection(i) for i in ib), tuple(str_to_intersection(i) for i in ip))
        ref = 'E1, F1, G1, H1, I1, F2, G2, H2, I2, F3, G3, H3, I3, F4, G4, H4, I4, F5, H5, I5, G6, H6, I6, G7, H7, I7, H8, I8, H9, I9'
        assert ref ==  ', '.join(intersection_to_str(i) for i in get_stone_chain(g, new_intersection('G',6)))
        
    def test_6(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9'
        g = new_goban(9, tuple(str_to_intersection(i) for i in ib), tuple(str_to_intersection(i) for i in ip))
        ref = 'D2, D3, D4, D5, D6, E6, E7, E8, F8, F9'
        assert ref ==  ', '.join(intersection_to_str(i) for i in get_stone_chain(g, new_intersection('E',6)))
        
class TestPrivateGobanSetStone:
    def test_1(self):
        g1 = new_empty_goban(13)
        g2 = set_stone(g1, new_intersection('A',1), new_white_stone()) 
        assert is_white_stone(get_stone(g1, new_intersection('A',1))) and id(g1) == id(g2)

    def test_2(self):
        g = new_empty_goban(19)
        _ = set_stone(g, new_intersection('A',1), new_white_stone()) 
        _ = set_stone(g, new_intersection('A',1), new_black_stone()) 
        assert is_black_stone(get_stone(g, new_intersection('A',1)))
        
    def test_3(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9'
        g1 = new_goban(9, tuple(str_to_intersection(i) for i in ib), tuple(str_to_intersection(i) for i in ip))
        
        g2 = new_empty_goban(9)
        for i in ib: set_stone(g2, str_to_intersection(i), new_white_stone())
        for i in ip: set_stone(g2, str_to_intersection(i), new_black_stone())
        
        assert all(equals_stones(get_stone(g1, str_to_intersection(i)),get_stone(g2, str_to_intersection(i))) for i in ib + ip)


class TestPrivateGobanRemoveStone:
    def test_1(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9'
        g1 = new_goban(9, tuple(str_to_intersection(i) for i in ib), tuple(str_to_intersection(i) for i in ip))
        g2 = copy_goban(g1)
        g3 = remove_stone(g1, new_intersection('D',2))
        assert is_white_stone(get_stone(g2, new_intersection('D',2))) and not is_player_stone(get_stone(g1, new_intersection('D',2))) and id(g1) == id(g3)

    def test_2(self):
        g = new_empty_goban(13)
        _ = set_stone(g, new_intersection('A',1), new_black_stone()) 
        _ = set_stone(g, new_intersection('A',2), new_black_stone()) 
        _ = remove_stone(g, new_intersection('A',1)) 
        assert not is_player_stone(get_stone(g, new_intersection('A',1))) and is_black_stone(get_stone(g, new_intersection('A',2)))
        
    def test_3(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9'
        g1 = new_goban(9, tuple(str_to_intersection(i) for i in ib), tuple(str_to_intersection(i) for i in ip))
        
        g2 = new_empty_goban(9)
        for i in ib+ip: remove_stone(g1, str_to_intersection(i))
       
        
        assert all(equals_stones(get_stone(g1, str_to_intersection(i)),get_stone(g2, str_to_intersection(i))) for i in ib + ip)

 
class TestPrivateGobanRemoveStoneChain:
    def test_1(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9', 'B1', 'B2', 'B3', 'B4', 'A4', 'C4', 'D9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9'
        g = new_goban(9, tuple(str_to_intersection(i) for i in ib), tuple(str_to_intersection(i) for i in ip))
        
        g2 = remove_stone_chain(g, tuple(str_to_intersection(i) for i in ib[:5]))
        assert all(not is_player_stone(get_stone(g, str_to_intersection(i))) for i in ib[:5]) and id(g) == id(g2)
        
    def test_2(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9', 'B1', 'B2', 'B3', 'B4', 'A4', 'C4', 'D9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9'
        g = new_goban(9, tuple(str_to_intersection(i) for i in ib), tuple(str_to_intersection(i) for i in ip))
        
        _ = remove_stone_chain(g, get_stone_chain(g, new_intersection('D',2)))
        assert all(not is_player_stone(get_stone(g, str_to_intersection(i))) for i in ib[:-1])  
        
    def test_3(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9', 'B1', 'B2', 'B3', 'B4', 'A4', 'C4', 'D9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9'
        g = new_goban(9, tuple(str_to_intersection(i) for i in ib), tuple(str_to_intersection(i) for i in ip))
        
        _ = remove_stone_chain(g, tuple(str_to_intersection(i) for i in ib))
        _ = remove_stone_chain(g, tuple(str_to_intersection(i) for i in ip))
        assert all(not is_player_stone(get_stone(g, str_to_intersection(L+N))) for L in 'ABCDEFGHI' for N in '123456789')  
  
    def test_4(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9', 'B1', 'B2', 'B3', 'B4', 'A4', 'C4', 'D9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9'
        g = new_goban(13, tuple(str_to_intersection(i) for i in ib), tuple(str_to_intersection(i) for i in ip))
        g2 = copy_goban(g)
        _ = remove_stone_chain(g, ())
        assert all(equals_stones(get_stone(g, str_to_intersection(L+N)), get_stone(g2, str_to_intersection(L+N))) for L in 'ABCDEFGHI' for N in '123456789') and id(g) != id(g2)  
  

class TestPrivateGobanIsGoban:
    
    def test_1(self):
        assert not is_goban(False) and not is_goban(250)
    
    def test_2(self):
        assert not is_goban(()) and  not is_goban({}) and not is_goban([])
    
    def test_3(self):
        assert is_goban(new_empty_goban(19))
    
    def test_4(self):
        assert is_goban(copy_goban(new_empty_goban(13)))

    def test_5(self):
        assert is_goban(new_goban(9,(),()))
    
    def test_6(self):
        assert is_goban(copy_goban(new_goban(9,(),())))

    def test_7(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5'
        g = new_goban(13, tuple(str_to_intersection(i) for i in ib), tuple(str_to_intersection(i) for i in ip))
        assert is_goban(g)
    
    def test_8(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5'
        g = new_goban(9, tuple(str_to_intersection(i) for i in ib), tuple(str_to_intersection(i) for i in ip))
        assert is_goban(copy_goban(g))

 
class TestPrivateGobanIsValidIntersection:
    def test_1(self):
        assert not is_valid_intersection(new_empty_goban(13), new_intersection('N', 13))

    def test_2(self):
        assert is_valid_intersection(new_empty_goban(19), new_intersection('S', 19))

    def test_3(self):
        assert not is_valid_intersection(new_empty_goban(9), new_intersection('I', 10))
        
 
class TestPrivateGobanEquals:
    def test_1(self):
        c1 = new_empty_goban(9)
        c2 = new_empty_goban(9)
        assert goban_equals(c1, c2)

    def test_2(self):
        c1 = new_empty_goban(9)
        c2 = new_empty_goban(19)
        assert not goban_equals(c1, c2)

    def test_3(self):
        ib = ('D2',) 
        g1 = new_goban(13, tuple(str_to_intersection(i) for i in ib), ())
        g2 = new_goban(13, (),())
        assert not goban_equals(g1, g2)

    def test_4(self):
        ip = ('D2',) 
        g1 = new_goban(13, (), tuple(str_to_intersection(i) for i in ip))
        g2 = new_goban(13, (),())
        assert not goban_equals(g1, g2)
 
    def test_5(self):
        g1 = new_empty_goban(13)
        g2 = new_goban(13, (),())
        assert goban_equals(g1, g2)

    def test_6(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5'
        g1 = new_goban(9, tuple(str_to_intersection(i) for i in ib), tuple(str_to_intersection(i) for i in ip))
        g2 = new_goban(9, tuple(str_to_intersection(i) for i in ib), tuple(str_to_intersection(i) for i in ip[:-1]))
        assert not goban_equals(g1, g2)

    def test_7(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5'
        g1 = new_goban(9, tuple(str_to_intersection(i) for i in ib), tuple(str_to_intersection(i) for i in ip))
        g2 = new_goban(9, tuple(str_to_intersection(i) for i in ip), tuple(str_to_intersection(i) for i in ib))
        assert not goban_equals(g1, g2)


class TestPrivateGobanToString:
    def test_1(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9', 'B1', 'B2', 'B3', 'B4', 'A4', 'C4', 'D9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9'
        g = new_goban(9, tuple(str_to_intersection(i) for i in ib), tuple(str_to_intersection(i) for i in ip))
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
        assert ref == goban_to_str(g)
        
    def test_2(self):
        g = new_empty_goban(13)
        p = new_white_stone(), new_black_stone()
        for L in 'ABCDEFGHIJKLM': 
            for N in range(1,14):
                n = (ord(L) + N) % 4
                if n < 2:
                    set_stone(g, new_intersection(L,N), p[n])
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
        assert ref == goban_to_str(g)
        
    def test_3(self):
        g = new_empty_goban(19)
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
        assert ref == goban_to_str(g)

class TestPrivateGobanTerritories:
    def test_1(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9', 'B1', 'B2', 'B3', 'B4', 'A4', 'C4', 'D9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9'
        g = new_goban(9, tuple(str_to_intersection(i) for i in ib), tuple(str_to_intersection(i) for i in ip))
        ref = ('A1, A2, A3', 
               'C1, C2, C3', 
               'E1, F1, G1, H1, I1, F2, G2, H2, I2, F3, G3, H3, I3, F4, G4, H4, I4, F5, H5, I5, G6, H6, I6, G7, H7, I7, H8, I8, H9, I9', 
               'A5, B5, C5, A6, B6, C6, A7, B7, C7, D7, A8, B8, C8, D8, A9, B9, C9', 
               'E9')
        hyp = ()
        for t in get_territories(g):
            hyp +=  (', '.join(intersection_to_str(i) for i in t),)           
        assert ref == hyp
    
    def test_2(self):
        g = new_empty_goban(9)
        p = new_white_stone(), new_black_stone()
        for L in 'ABCDEFGHI': 
            for N in range(1,10):
                n = (ord(L) + N) % 2
                set_stone(g, new_intersection(L,N), p[n])
        ref = ()
        hyp = ()
        for t in get_territories(g):
            hyp +=  (', '.join(intersection_to_str(i) for i in t),)           
        assert ref == hyp
        
    
    def test_3(self):
        g = new_empty_goban(9)
        ref = ('A1, B1, C1, D1, E1, F1, G1, H1, I1, A2, B2, C2, D2, E2, F2, G2, H2, I2, A3, B3, C3, D3, E3, F3, G3, H3, I3, A4, B4, C4, D4, E4, F4, G4, H4, I4, A5, B5, C5, D5, E5, F5, G5, H5, I5, A6, B6, C6, D6, E6, F6, G6, H6, I6, A7, B7, C7, D7, E7, F7, G7, H7, I7, A8, B8, C8, D8, E8, F8, G8, H8, I8, A9, B9, C9, D9, E9, F9, G9, H9, I9',)
        hyp = ()
        for t in get_territories(g):
            hyp +=  (', '.join(intersection_to_str(i) for i in t),)           
        assert ref == hyp
        
    def test_4(self):
        g = new_empty_goban(13)
        p = new_white_stone(), new_black_stone()
        for L in 'ABCDEFGHIJKLM': 
            for N in range(1,14):
                n = (ord(L) + N) % 5
                if n < 2:
                    set_stone(g, new_intersection(L,N), p[n])
        ref = ('B1, C1, D1, A2, B2, C2, A3, B3, A4', 
               'G1, H1, I1, F2, G2, H2, E3, F3, G3, D4, E4, F4, C5, D5, E5, B6, C6, D6, A7, B7, C7, A8, B8, A9', 
               'L1, M1, K2, L2, M2, J3, K3, L3, I4, J4, K4, H5, I5, J5, G6, H6, I6, F7, G7, H7, E8, F8, G8, D9, E9, F9, C10, D10, E10, B11, C11, D11, A12, B12, C12, A13, B13', 
               'M5, L6, M6, K7, L7, M7, J8, K8, L8, I9, J9, K9, H10, I10, J10, G11, H11, I11, F12, G12, H12, E13, F13, G13', 
               'M10, L11, M11, K12, L12, M12, J13, K13, L13')
        hyp = ()
        for t in get_territories(g):
            hyp +=  (', '.join(intersection_to_str(i) for i in t),)           
        assert ref == hyp
        
    def test_5(self):
        g = new_empty_goban(19)
        p = new_white_stone(), new_black_stone()
        for L in 'ABCDEFGHIJKLMNOPQRS': 
            for N in range(1,20):
                n = (ord(L) + N) % 7
                if n < 2:
                    set_stone(g, new_intersection(L,N), p[n])
        ref = ('A1, B1, C1, D1, A2, B2, C2, A3, B3, A4', 
               'G1, H1, I1, J1, K1, F2, G2, H2, I2, J2, E3, F3, G3, H3, I3, D4, E4, F4, G4, H4, C5, D5, E5, F5, G5, B6, C6, D6, E6, F6, A7, B7, C7, D7, E7, A8, B8, C8, D8, A9, B9, C9, A10, B10, A11', 
               'N1, O1, P1, Q1, R1, M2, N2, O2, P2, Q2, L3, M3, N3, O3, P3, K4, L4, M4, N4, O4, J5, K5, L5, M5, N5, I6, J6, K6, L6, M6, H7, I7, J7, K7, L7, G8, H8, I8, J8, K8, F9, G9, H9, I9, J9, E10, F10, G10, H10, I10, D11, E11, F11, G11, H11, C12, D12, E12, F12, G12, B13, C13, D13, E13, F13, A14, B14, C14, D14, E14, A15, B15, C15, D15, A16, B16, C16, A17, B17, A18', 'S3, R4, S4, Q5, R5, S5, P6, Q6, R6, S6, O7, P7, Q7, R7, S7, N8, O8, P8, Q8, R8, M9, N9, O9, P9, Q9, L10, M10, N10, O10, P10, K11, L11, M11, N11, O11, J12, K12, L12, M12, N12, I13, J13, K13, L13, M13, H14, I14, J14, K14, L14, G15, H15, I15, J15, K15, F16, G16, H16, I16, J16, E17, F17, G17, H17, I17, D18, E18, F18, G18, H18, C19, D19, E19, F19, G19', 
               'S10, R11, S11, Q12, R12, S12, P13, Q13, R13, S13, O14, P14, Q14, R14, S14, N15, O15, P15, Q15, R15, M16, N16, O16, P16, Q16, L17, M17, N17, O17, P17, K18, L18, M18, N18, O18, J19, K19, L19, M19, N19', 
               'S17, R18, S18, Q19, R19, S19')
        hyp = ()
        for t in get_territories(g):
            hyp +=  (', '.join(intersection_to_str(i) for i in t),)           
        assert ref == hyp


class TestPrivateGobanAdjacentsDiff:
    def test_1(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9', 'B1', 'B2', 'B3', 'B4', 'A4', 'C4', 'D9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9'
        g = new_goban(9, tuple(str_to_intersection(i) for i in ib), tuple(str_to_intersection(i) for i in ip))

        t = tuple(str_to_intersection(i) for i in ('A1', 'A2', 'A3'))
        ref = 'B1, B2, B3, A4'
        hyp = ', '.join(intersection_to_str(i) for i in get_adjacents_different(g, t))
        assert ref == hyp 
        
    def test_2(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9', 'B1', 'B2', 'B3', 'B4', 'A4', 'C4', 'D9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9'
        g = new_goban(9, tuple(str_to_intersection(i) for i in ib), tuple(str_to_intersection(i) for i in ip))

        t = tuple(str_to_intersection(i) for i in ('E9', 'D8', 'D7', 'G7', 'G6', 'E1'))
        ref = 'D1, E2, G5, D6, F6, E7, F7, E8, G8, D9, F9'
        hyp = ', '.join(intersection_to_str(i) for i in get_adjacents_different(g, t))
        assert ref == hyp 
        
    def test_3(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9', 'B1', 'B2', 'B3', 'B4', 'A4', 'C4', 'D9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9'
        g = new_goban(9, tuple(str_to_intersection(i) for i in ib), tuple(str_to_intersection(i) for i in ip))

        t = tuple(str_to_intersection(i) for i in ('B1', 'B2', 'D2', 'B3', 'D3', 'A4', 'B4', 'C4', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9'))
        ref = 'A1, C1, A2, C2, A3, C3, A5, B5, C5, C6, D7, D8, E9'
        hyp = ', '.join(intersection_to_str(i) for i in get_adjacents_different(g, t))
        assert ref == hyp 
        
    def test_4(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9', 'B1', 'B2', 'B3', 'B4', 'A4', 'C4', 'D9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9'
        g = new_goban(9, tuple(str_to_intersection(i) for i in ib), tuple(str_to_intersection(i) for i in ip))

        t = tuple(str_to_intersection(i) for i in ('E2', 'E3', 'E4', 'E5'))
        ref = 'E1, F2, F3, F4, F5'
        hyp = ', '.join(intersection_to_str(i) for i in get_adjacents_different(g, t))
        assert ref == hyp 
        
    def test_5(self):
        g = new_empty_goban(13)

        t = tuple(new_intersection(L,N) for L in 'ABCDEFGHIJKLM' for N in range(1,14))
        ref = ''
        hyp = ', '.join(intersection_to_str(i) for i in get_adjacents_different(g, t))
        assert ref == hyp 
        
    def test_6(self):
        t = tuple(new_intersection(L,N) for L in 'ABCDEFGHIJKLMNOPQRS' for N in range(1,20))
        g = new_goban(19, t[::2], t[1::2])
        ref = ''
        hyp = ', '.join(intersection_to_str(i) for i in get_adjacents_different(g, t))
        assert ref == hyp 
        
class TestPrivateGobanMove:
    def test_1(self):
        ib = 'D1', 'E2', 'F2'
        ip = 'E1', 'F1'
        g = new_goban(9, tuple(str_to_intersection(i) for i in ib), tuple(str_to_intersection(i) for i in ip))
        _ = move(g, new_intersection('G',1), new_white_stone())
        ref = '   A B C D E F G H I\n 9 . . . . . . . . .  9\n 8 . . . . . . . . .  8\n 7 . . . . . . . . .  7\n 6 . . . . . . . . .  6\n 5 . . . . . . . . .  5\n 4 . . . . . . . . .  4\n 3 . . . . . . . . .  3\n 2 . . . . O O . . .  2\n 1 . . . O . . O . .  1\n   A B C D E F G H I'
        assert ref == goban_to_str(g)
        
    def test_2(self):
        ib = 'D1', 'H1', 'D2', 'I1', 'E2', 'F2', 'G2', 'H2', 'I2'
        ip = 'C1', 'C2', 'D3', 'E1', 'E3', 'F3', 'F1', 'G3', 'H3', 'I3'
        g = new_goban(9, tuple(str_to_intersection(i) for i in ib), tuple(str_to_intersection(i) for i in ip))
        _ = move(g, new_intersection('G',1), new_white_stone())
        ref = '   A B C D E F G H I\n 9 . . . . . . . . .  9\n 8 . . . . . . . . .  8\n 7 . . . . . . . . .  7\n 6 . . . . . . . . .  6\n 5 . . . . . . . . .  5\n 4 . . . . . . . . .  4\n 3 . . . X X X X X X  3\n 2 . . X O O O O O O  2\n 1 . . X O . . O O O  1\n   A B C D E F G H I'
        assert ref == goban_to_str(g)

    def test_3(self):
        ib = 'D1', 'H1', 'D2', 'I1', 'E2', 'F2', 'G2', 'H2', 'I2'
        ip = 'C1', 'C2', 'D3', 'E1', 'E3', 'F3', 'F1', 'G3', 'H3', 'I3'
        g = new_goban(9, tuple(str_to_intersection(i) for i in ib), tuple(str_to_intersection(i) for i in ip))
        _ = move(g, new_intersection('G',1), new_black_stone())
        ref = '   A B C D E F G H I\n 9 . . . . . . . . .  9\n 8 . . . . . . . . .  8\n 7 . . . . . . . . .  7\n 6 . . . . . . . . .  6\n 5 . . . . . . . . .  5\n 4 . . . . . . . . .  4\n 3 . . . X X X X X X  3\n 2 . . X . . . . . .  2\n 1 . . X . X X X . .  1\n   A B C D E F G H I'
        assert ref == goban_to_str(g)

    def test_4(self):
        t = tuple(new_intersection(L,N) for L in 'ABCDEFGHIJKLM' for N in range(1,14) if not (L == 'F' and N ==7))
        g = new_goban(13, t, ())
        _ = move(g, new_intersection('F',7), new_black_stone())
        ref = '   A B C D E F G H I J K L M\n13 . . . . . . . . . . . . . 13\n12 . . . . . . . . . . . . . 12\n11 . . . . . . . . . . . . . 11\n10 . . . . . . . . . . . . . 10\n 9 . . . . . . . . . . . . .  9\n 8 . . . . . . . . . . . . .  8\n 7 . . . . . X . . . . . . .  7\n 6 . . . . . . . . . . . . .  6\n 5 . . . . . . . . . . . . .  5\n 4 . . . . . . . . . . . . .  4\n 3 . . . . . . . . . . . . .  3\n 2 . . . . . . . . . . . . .  2\n 1 . . . . . . . . . . . . .  1\n   A B C D E F G H I J K L M'
        assert ref == goban_to_str(g)
        
    def test_5(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6',  'E8', 'F8', 'F9', 'B1', 'B2', 'B3', 'B4', 'A4', 'C4', 'D9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9', 'E7', 'D8', 'C9'
        g = new_goban(9, tuple(str_to_intersection(i) for i in ib), tuple(str_to_intersection(i) for i in ip))
        _ = move(g, new_intersection('E',9), new_black_stone())
        ref = '   A B C D E F G H I\n 9 . . X . X . X . .  9\n 8 . . . X . . X . .  8\n 7 . . . . X X . . .  7\n 6 . . . O O X . . .  6\n 5 . . . O X . X . .  5\n 4 O O O O X . . . .  4\n 3 . O . O X . . . .  3\n 2 . O . O X . . . .  2\n 1 . O . X . . . . .  1\n   A B C D E F G H I'
        assert ref == goban_to_str(g)
        
    def test_6(self):
        ib = tuple(str_to_intersection(i) \
            for i in ('A1', 'A2', 'B1', 'E4', 'E5', 'F4', 'F5', 'G6', 'G7'))
        ip = tuple(str_to_intersection(i) \
            for i in ('C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'))
        g = new_goban(9, ib, ip)
        p = new_black_stone()
        _ = move(g, new_intersection('B', 2), p)
        assert goban_to_str(g) == \
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

class TestPrivateGobanPlayerStones:

    def test_1(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9', 'B1', 'B2', 'B3', 'B4', 'A4', 'C4', 'D9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9'
        g = new_goban(9, tuple(str_to_intersection(i) for i in ib), tuple(str_to_intersection(i) for i in ip))
        ref = (17,10)
        assert ref == get_player_stones(g)
        
    def test_2(self):
        g = new_empty_goban(13)
        p = new_white_stone(), new_black_stone()
        for L in 'ABCDEFGHIJKLM': 
            for N in range(1,14):
                n = (ord(L) + N) % 4
                if n < 2:
                    set_stone(g, new_intersection(L,N), p[n])
        ref = (42,42)
        assert ref == get_player_stones(g)

    def test_3(self):
        g = new_empty_goban(9)
        p = new_white_stone(), new_black_stone()
        for L in 'ABCDEFGHI': 
            for N in range(1,10):
                n = (ord(L) + N) % 7
                if n < 3:
                    set_stone(g, new_intersection(L,N), p[(1+n)%2])
        ref = (11, 22)
        assert ref == get_player_stones(g)


class TestPrivateCalculatePoints:

    def test_1(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9', 'B1', 'B2', 'B3', 'B4', 'A4', 'C4', 'D9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9'
        g = new_goban(9, tuple(str_to_intersection(i) for i in ib), tuple(str_to_intersection(i) for i in ip))
        ref = (38,40)
        assert ref == calculate_points(g)
        
    def test_2(self):
        g = new_empty_goban(13)
        p = new_white_stone(), new_black_stone()
        for L in 'ABCDEFGHIJKLM': 
            for N in range(1,14):
                n = (ord(L) + N) % 4
                if n < 2:
                    set_stone(g, new_intersection(L,N), p[n])
        ref = (45, 43)
        assert ref == calculate_points(g)

    def test_3(self):
        g = new_empty_goban(9)
        p = new_white_stone(), new_black_stone()
        for L in 'ABCDEFGHI': 
            for N in range(1,10):
                n = (ord(L) + N) % 7
                if n < 3:
                    set_stone(g, new_intersection(L,N), p[(1+n)%2])
        ref = (11, 70)
        assert ref == calculate_points(g)

class TestPrivateIsMoveLegal:
    def test_1(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9', 'B1', 'B2', 'B3', 'B4', 'A4', 'C4', 'D9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9'
        g = new_goban(9, tuple(str_to_intersection(i) for i in ib), tuple(str_to_intersection(i) for i in ip))
        g_ant = copy_goban(g)
        assert is_move_legal(g, new_intersection('E',9), new_white_stone(), new_empty_goban(9)) and goban_equals(g, g_ant)

    def test_2(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9', 'B1', 'B2', 'B3', 'B4', 'A4', 'C4', 'D9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9'
        g = new_goban(9, tuple(str_to_intersection(i) for i in ib), tuple(str_to_intersection(i) for i in ip))
        g_ant = copy_goban(g)
        assert not is_move_legal(g, new_intersection('E',9), new_black_stone(), new_empty_goban(9)) and goban_equals(g, g_ant)

    def test_3(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9', 'C1', 'C2', 'C3', 'B4', 'A4', 'C4', 'D9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9', 'B1', 'B2', 'B3', 'A2', 'A3'
        g = new_goban(9, tuple(str_to_intersection(i) for i in ib), tuple(str_to_intersection(i) for i in ip))
        g_ant = copy_goban(g)
        assert not is_move_legal(g, new_intersection('A',1), new_black_stone(), new_empty_goban(9)) and goban_equals(g, g_ant)

    def test_4(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9', 'C1', 'C2', 'C3', 'B4', 'A4', 'C4', 'D9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9', 'B1', 'B2', 'B3', 'A2', 'A3'
        g = new_goban(9, tuple(str_to_intersection(i) for i in ib), tuple(str_to_intersection(i) for i in ip))
        g_ant = copy_goban(g)
        assert is_move_legal(g, new_intersection('A',1), new_white_stone(), new_empty_goban(9)) and goban_equals(g, g_ant)

    def test_5(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9', 'C1', 'C2', 'C3', 'B4', 'A4', 'C4', 'D9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9', 'B1', 'B2', 'B3', 'A2', 'A3'
        g = new_goban(9, tuple(str_to_intersection(i) for i in ib), tuple(str_to_intersection(i) for i in ip))
        g_ant = copy_goban(g)
        assert is_move_legal(g, new_intersection('I',1), new_black_stone(), new_empty_goban(9)) and goban_equals(g, g_ant)

    def test_6(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9', 'C1', 'C2', 'C3', 'B4', 'A4', 'C4', 'D9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9', 'B1', 'B2', 'B3', 'A2', 'A3'
        g = new_goban(19, tuple(str_to_intersection(i) for i in ib), tuple(str_to_intersection(i) for i in ip))
        g_ant = copy_goban(g)
        assert not is_move_legal(g, new_intersection('E',4), new_black_stone(), new_empty_goban(19)) and goban_equals(g, g_ant)

    def test_7(self):
        ib = 'B7', 'B8', 'C6', 'D6', 'D8', 'E7', 'E9', 'F7', 'F8', 'F9'
        ip = 'C7', 'C8', 'C9', 'D7', 'D9', 'E6', 'F5', 'F6', 'G7', 'G8'
        g = new_goban(9, tuple(str_to_intersection(i) for i in ib), tuple(str_to_intersection(i) for i in ip))
        # g_ant = copy_goban(g)
        assert is_move_legal(g, new_intersection('E',8), new_black_stone(), new_empty_goban(9)) 

    def test_8(self):
        ib = 'B7', 'B8', 'C6', 'D6', 'D8', 'E7', 'E9', 'F7', 'F8', 'F9'
        ip = 'C7', 'C8', 'C9', 'D7', 'D9', 'E6', 'F5', 'F6', 'G7', 'G8'
        g = new_goban(9, tuple(str_to_intersection(i) for i in ib), tuple(str_to_intersection(i) for i in ip))
        g_ant = copy_goban(g)
        _ = move(g, new_intersection('E',8), new_black_stone())
        assert not is_move_legal(g, new_intersection('E',7), new_white_stone(), g_ant) 


class TestPrivatePlayerTurn:
    def test_1(self):
        g = new_empty_goban(9)
        ref = (True, "Escreva uma intersecao ou 'P' para passar [X]:")
        assert offline_player_turn(g, new_black_stone(), new_empty_goban(9), 'A1\n') == ref and is_black_stone(get_stone(g, new_intersection('A',1)))

    def test_2(self):
        g = new_empty_goban(19)
        ref = (True, "Escreva uma intersecao ou 'P' para passar [O]:Escreva uma intersecao ou 'P' para passar [O]:Escreva uma intersecao ou 'P' para passar [O]:Escreva uma intersecao ou 'P' para passar [O]:")
        assert offline_player_turn(g, new_white_stone(), new_empty_goban(19), 'L\n?1\nAA1\nA2\n') == ref and is_white_stone(get_stone(g, new_intersection('A',2)))

    def test_3(self):
        g = new_empty_goban(13)
        ref = (True, "Escreva uma intersecao ou 'P' para passar [O]:Escreva uma intersecao ou 'P' para passar [O]:Escreva uma intersecao ou 'P' para passar [O]:Escreva uma intersecao ou 'P' para passar [O]:")
        assert offline_player_turn(g, new_white_stone(), new_empty_goban(13), 'D99\nALO\nA?\nI8\n') == ref and is_white_stone(get_stone(g, new_intersection('I',8)))

    def test_4(self):
        g = new_empty_goban(9)
        ref = (False, "Escreva uma intersecao ou 'P' para passar [X]:Escreva uma intersecao ou 'P' para passar [X]:Escreva uma intersecao ou 'P' para passar [X]:Escreva uma intersecao ou 'P' para passar [X]:")
        assert offline_player_turn(g, new_black_stone(), new_empty_goban(9), 'd7\nA13\nb13\nP\n') == ref 

    def test_5(self):
        g = new_empty_goban(19)
        ref = (True, "Escreva uma intersecao ou 'P' para passar [X]:")
        assert offline_player_turn(g, new_black_stone(), new_empty_goban(9), 'N14\n') == ref 

    def test_6(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9', 'C1', 'C2', 'C3', 'B4', 'A4', 'C4', 'D9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9', 'B1', 'B2', 'B3', 'A2', 'A3'
        g = new_goban(9, tuple(str_to_intersection(i) for i in ib), tuple(str_to_intersection(i) for i in ip))
        ref = (True, "Escreva uma intersecao ou 'P' para passar [X]:Escreva uma intersecao ou 'P' para passar [X]:Escreva uma intersecao ou 'P' para passar [X]:")
        cad = '   A B C D E F G H I\n 9 . . . O . O X . .  9\n 8 . . . . O O X . .  8\n 7 . . . . O X . . .  7\n 6 . . . O O X . . .  6\n 5 . . . O X X X . .  5\n 4 O O O O X . . . .  4\n 3 X X O O X . . . .  3\n 2 X X O O X . . . .  2\n 1 . X O X . . . . .  1\n   A B C D E F G H I'
        assert offline_player_turn(g, new_black_stone(), new_empty_goban(9), 'E9\nA1\nF5\n') == ref and cad == goban_to_str(g)

    def test_7(self):
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9', 'C1', 'C2', 'C3', 'B4', 'A4', 'C4', 'D9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9', 'B1', 'B2', 'B3', 'A2', 'A3'
        g = new_goban(9, tuple(str_to_intersection(i) for i in ib), tuple(str_to_intersection(i) for i in ip))
        ref = (True, "Escreva uma intersecao ou 'P' para passar [O]:Escreva uma intersecao ou 'P' para passar [O]:")
        cad = '   A B C D E F G H I\n 9 . . . O . O X . .  9\n 8 . . . . O O X . .  8\n 7 . . . . O X . . .  7\n 6 . . . O O X . . .  6\n 5 . . . O X . X . .  5\n 4 O O O O X . . . .  4\n 3 . . O O X . . . .  3\n 2 . . O O X . . . .  2\n 1 O . O X . . . . .  1\n   A B C D E F G H I'
        assert offline_player_turn(g, new_white_stone(), new_empty_goban(9), 'A2\nA1\n') == ref and cad == goban_to_str(g)
        
    def test_8(self):
        ib = 'B7', 'B8', 'C6', 'D6', 'D8', 'E7', 'E9', 'F7', 'F8', 'F9'
        ip = 'C7', 'C8', 'C9', 'D7', 'D9', 'E6', 'F5', 'F6', 'G7', 'G8'
        g = new_goban(9, tuple(str_to_intersection(i) for i in ib), tuple(str_to_intersection(i) for i in ip))
        g_ant = copy_goban(g)
        _ = offline_player_turn(g, new_black_stone(), new_empty_goban(9), 'E8\n')
        ref1 = '   A B C D E F G H I\n 9 . . X X O O . . .  9\n 8 . O X . X O X . .  8\n 7 . O X X O O X . .  7\n 6 . . O O X X . . .  6\n 5 . . . . . X . . .  5\n 4 . . . . . . . . .  4\n 3 . . . . . . . . .  3\n 2 . . . . . . . . .  2\n 1 . . . . . . . . .  1\n   A B C D E F G H I'
        hyp1 = goban_to_str(g)
        _ = offline_player_turn(g, new_white_stone(), g_ant, 'D8\nG6\n')
        ref2 = '   A B C D E F G H I\n 9 . . X X O O . . .  9\n 8 . O X . X O X . .  8\n 7 . O X X O O X . .  7\n 6 . . O O X X O . .  6\n 5 . . . . . X . . .  5\n 4 . . . . . . . . .  4\n 3 . . . . . . . . .  3\n 2 . . . . . . . . .  2\n 1 . . . . . . . . .  1\n   A B C D E F G H I'
        assert ref1 == hyp1  and ref2 == goban_to_str(g)

    def test_9(self):
        ib = 'B7', 'B8', 'C6', 'D6', 'D8', 'E7', 'E9', 'F7', 'F8', 'F9'
        ip = 'C7', 'C8', 'C9', 'D7', 'D9', 'E6', 'F5', 'F6', 'G7', 'G8'
        g = new_goban(9, tuple(str_to_intersection(i) for i in ib), tuple(str_to_intersection(i) for i in ip))
        _ = offline_player_turn(g, new_white_stone(), new_empty_goban(9), 'E10\nE8\n')
        ref = '   A B C D E F G H I\n 9 . . X X O O . . .  9\n 8 . O X O O O X . .  8\n 7 . O X X O O X . .  7\n 6 . . O O X X . . .  6\n 5 . . . . . X . . .  5\n 4 . . . . . . . . .  4\n 3 . . . . . . . . .  3\n 2 . . . . . . . . .  2\n 1 . . . . . . . . .  1\n   A B C D E F G H I'
        assert ref == goban_to_str(g)

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
        assert "go: invalid arguments" == str(excinfo.value)
        
    def test_2(self):
        with pytest.raises(ValueError) as excinfo:
            go(25, (), ())
        assert "go: invalid arguments" == str(excinfo.value)

    def test_3(self):
        with pytest.raises(ValueError) as excinfo:
            go(9, True, 5)
        assert "go: invalid arguments" == str(excinfo.value)
        
    def test_4(self):
        with pytest.raises(ValueError) as excinfo:
            go(9, [], {})
        assert "go: invalid arguments" == str(excinfo.value)

    def test_5(self):
        with pytest.raises(ValueError) as excinfo:
            go(9, ('ola',), ('adeus',))
        assert "go: invalid arguments" == str(excinfo.value)

    def test_6(self):
        with pytest.raises(ValueError) as excinfo:
            go(9, (6,), (45,))
        assert "go: invalid arguments" == str(excinfo.value)

    def test_7(self):
        with pytest.raises(ValueError) as excinfo:
            go(9, ('A11',), ())
        assert "go: invalid arguments" == str(excinfo.value)

    def test_8(self):
        with pytest.raises(ValueError) as excinfo:
            go(9, ('A7',), ('ZZ8',))
        assert "go: invalid arguments" == str(excinfo.value)

    def test_9(self):
        with pytest.raises(ValueError) as excinfo:
            go(9, ('A7', 35), ('B8',))
        assert "go: invalid arguments" == str(excinfo.value)

    def test_10(self):
        with pytest.raises(ValueError) as excinfo:
            go(9, ('A7', 'B5', 'C4'), ('B8', 'A8', 'B5'))
        assert "go: invalid arguments" == str(excinfo.value)


class TestPrivateADTIntersection:
    
    # score = 0.5

    def test_1(self):
        exec(open(f'{ADT_CODE_PATH}/ADT_intersection.py', encoding="utf-8").read(), globals())
        c = new_intersection('A', 2)
        l = new_intersection('S',19)
        ref = ('A1', 'B2', 'A3')
        assert ref == tuple(intersection_to_str(i) for i in get_adjacent_intersections(c, l))
        
    def test_2(self):
        exec(open(f'{ADT_CODE_PATH}/ADT_intersection.py', encoding="utf-8").read(), globals())
        tup = (new_intersection('A',1), new_intersection('A',3), new_intersection('B',1), new_intersection('B',2))
        assert ('A1', 'B1', 'B2', 'A3') == tuple(intersection_to_str(i) for i in sort_intersections(tup))
        
class TestPrivateTADPedra:
    # score 0.25
    def test_1(self):
        exec(open(f'{ADT_CODE_PATH}/ADT_stone.py', encoding="utf-8").read(), globals())
        assert is_player_stone(new_white_stone()) and  is_player_stone(new_black_stone()) and not is_player_stone(new_empty_stone())
   
class TestPrivateADTGoban:

    # score = 1.0
    def test_1(self):
            exec(open(f'{ADT_CODE_PATH}/TF_intersection.py', encoding="utf-8").read(), globals())
            exec(open(f'{ADT_CODE_PATH}/TF_stone.py', encoding="utf-8").read(), globals())
            g1 = new_empty_goban(9)
            g2 = copy_goban(g1)
            assert id(g1) != id(g2) and goban_equals(g1, g2)
            
    def test_2(self):
        exec(open(f'{ADT_CODE_PATH}/TF_intersection.py', encoding="utf-8").read(), globals())
        exec(open(f'{ADT_CODE_PATH}/TF_stone.py', encoding="utf-8").read(), globals())
        ib = 'B7', 'B8', 'C6', 'D6', 'D8', 'E7', 'E9', 'F7', 'F8', 'F9'
        ip = 'C7', 'C8', 'C9', 'D7', 'D9', 'E6', 'F5', 'F6', 'G7', 'G8'
        g1 = new_goban(9, tuple(str_to_intersection(i) for i in ib), tuple(str_to_intersection(i) for i in ip))
        g2 = copy_goban(g1)
        assert id(g1) != id(g2) and goban_equals(g1, g2)

    def test_3(self):
        exec(open(f'{ADT_CODE_PATH}/TF_intersection.py', encoding="utf-8").read(), globals())
        exec(open(f'{ADT_CODE_PATH}/TF_stone.py', encoding="utf-8").read(), globals())
        ib = new_intersection('C',1), new_intersection('C',3), new_intersection('D',4)
        ip = new_intersection('E',1), new_intersection('E',3), new_intersection('F',4)
        g = new_goban(13, ib, ip)
 
        assert all(is_white_stone(get_stone(g, i)) for i in ib) and \
            all(is_black_stone(get_stone(g, i)) for i in ip) and \
                all((not is_player_stone(get_stone(g, new_intersection(L,N))) for L in 'LM' for N in range(1,14,2)))

    def test_4(self):
        exec(open(f'{ADT_CODE_PATH}/TF_intersection.py', encoding="utf-8").read(), globals())
        exec(open(f'{ADT_CODE_PATH}/TF_stone.py', encoding="utf-8").read(), globals())
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9'
        g = new_goban(9, tuple(str_to_intersection(i) for i in ib), tuple(str_to_intersection(i) for i in ip))
        ref = 'E2, E3, E4, E5'
        assert ref ==  ', '.join(intersection_to_str(i) for i in get_stone_chain(g, new_intersection('E',3)))
        
    def test_5(self):
        exec(open(f'{ADT_CODE_PATH}/TF_intersection.py', encoding="utf-8").read(), globals())
        exec(open(f'{ADT_CODE_PATH}/TF_stone.py', encoding="utf-8").read(), globals())
        g = new_empty_goban(13)
        _ = set_stone(g, new_intersection('A',1), new_black_stone()) 
        _ = set_stone(g, new_intersection('A',2), new_black_stone()) 
        _ = remove_stone(g, new_intersection('A',1)) 
        assert not is_player_stone(get_stone(g, new_intersection('A',1))) and is_black_stone(get_stone(g, new_intersection('A',2)))
      
    def test_6(self):
        exec(open(f'{ADT_CODE_PATH}/TF_intersection.py', encoding="utf-8").read(), globals())
        exec(open(f'{ADT_CODE_PATH}/TF_stone.py', encoding="utf-8").read(), globals())
        g = new_empty_goban(13)
        _ = set_stone(g, new_intersection('A',1), new_black_stone()) 
        _ = set_stone(g, new_intersection('A',2), new_black_stone()) 
        _ = remove_stone(g, new_intersection('A',1)) 
        assert is_goban(g) and is_goban(copy_goban(g))
          
    def test_7(self):
        exec(open(f'{ADT_CODE_PATH}/TF_intersection.py', encoding="utf-8").read(), globals())
        exec(open(f'{ADT_CODE_PATH}/TF_stone.py', encoding="utf-8").read(), globals())
        
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9', 'B1', 'B2', 'B3', 'B4', 'A4', 'C4', 'D9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9'
        g = new_goban(9, tuple(str_to_intersection(i) for i in ib), tuple(str_to_intersection(i) for i in ip))
        
        g2 = remove_stone_chain(g, tuple(str_to_intersection(i) for i in ib[:5]))
        assert all(not is_player_stone(get_stone(g, str_to_intersection(i))) for i in ib[:5]) and id(g) == id(g2)
  

    def test_8(self):
        exec(open(f'{ADT_CODE_PATH}/TF_intersection.py', encoding="utf-8").read(), globals())
        exec(open(f'{ADT_CODE_PATH}/TF_stone.py', encoding="utf-8").read(), globals()) 
        assert not is_valid_intersection(new_empty_goban(13), new_intersection('N', 13)) and is_valid_intersection(new_empty_goban(19), new_intersection('S', 19))
        
        
    def test_9(self):
        exec(open(f'{ADT_CODE_PATH}/TF_intersection.py', encoding="utf-8").read(), globals())
        exec(open(f'{ADT_CODE_PATH}/TF_stone.py', encoding="utf-8").read(), globals())
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9', 'B1', 'B2', 'B3', 'B4', 'A4', 'C4', 'D9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9'
        g = new_goban(9, tuple(str_to_intersection(i) for i in ib), tuple(str_to_intersection(i) for i in ip))
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
        assert ref == goban_to_str(g)

    def test_10(self):
        exec(open(f'{ADT_CODE_PATH}/TF_intersection.py', encoding="utf-8").read(), globals())
        exec(open(f'{ADT_CODE_PATH}/TF_stone.py', encoding="utf-8").read(), globals())
        g = new_empty_goban(13)
        g2 = copy_goban(g)
        _ = set_stone(g, new_intersection('A',2), new_black_stone())  
        assert is_black_stone(get_stone(g, new_intersection('A',2))) and not is_player_stone(get_stone(g2, new_intersection('A',2)))
    
    def test_11(self):
        exec(open(f'{ADT_CODE_PATH}/TF_intersection.py', encoding="utf-8").read(), globals())
        exec(open(f'{ADT_CODE_PATH}/TF_stone.py', encoding="utf-8").read(), globals())
        ib = 'D2', 'D3', 'D4', 'D5', 'D6', 'E6', 'E7', 'E8', 'F8', 'F9', 'B1', 'B2', 'B3', 'B4', 'A4', 'C4', 'D9'
        ip = 'D1', 'E2', 'E3', 'E4', 'E5', 'F6', 'F7', 'G5', 'G8', 'G9'
        g1 = new_goban(9, tuple(str_to_intersection(i) for i in ib), tuple(str_to_intersection(i) for i in ip))
        g2 = new_goban(9, tuple(str_to_intersection(i) for i in ib), tuple(str_to_intersection(i) for i in ip))
        
        assert goban_equals(g1, g2)
    
class TestPrivateADTGobanHLF:
    
    # score = 0.75
    def test_1(self):
        exec(open(f'{ADT_CODE_PATH}/TF_intersection.py', encoding="utf-8").read(), globals())
        exec(open(f'{ADT_CODE_PATH}/TF_stone.py', encoding="utf-8").read(), globals())      
        exec(open(f'{ADT_CODE_PATH}/ADT_goban.py', encoding="utf-8").read(), globals())    
        
        g = new_empty_goban(9)
        b, p = new_white_stone(), new_black_stone()
        ib = 'C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'
        ip = 'E4', 'E5', 'F4', 'F5', 'G6', 'G7'
        for i in ib: set_stone(g, str_to_intersection(i), b)
        for i in ip: set_stone(g, str_to_intersection(i), p)
        cad = get_stone_chain(g, new_intersection('F',5))
        liberdades = get_adjacents_different(g, cad)
        assert tuple(intersection_to_str(i) for i in liberdades) == ('E3', 'F3', 'G4', 'D5', 'G5', 'E6', 'F6')
        
        
    def test_2(self):
        exec(open(f'{ADT_CODE_PATH}/TF_intersection.py', encoding="utf-8").read(), globals())
        exec(open(f'{ADT_CODE_PATH}/TF_stone.py', encoding="utf-8").read(), globals())      
        exec(open(f'{ADT_CODE_PATH}/ADT_goban.py', encoding="utf-8").read(), globals())      
             
        g = new_empty_goban(9)
        b, p = new_white_stone(), new_black_stone()
        ib = 'C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'
        ip = 'E4', 'E5', 'F4', 'F5', 'G6', 'G7'
        for i in ib: set_stone(g, str_to_intersection(i), b)
        for i in ip: set_stone(g, str_to_intersection(i), p)
        terr = get_territories(g)
        assert tuple(intersection_to_str(i) for i in terr[0]) == ('A1', 'B1', 'A2', 'B2')

    def test_3(self):
        exec(open(f'{ADT_CODE_PATH}/TF_intersection.py', encoding="utf-8").read(), globals())
        exec(open(f'{ADT_CODE_PATH}/TF_stone.py', encoding="utf-8").read(), globals())      
        exec(open(f'{ADT_CODE_PATH}/ADT_goban.py', encoding="utf-8").read(), globals())   
        
        g = new_empty_goban(9)
        b, p = new_white_stone(), new_black_stone()
        ib = 'C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'
        ip = 'E4', 'E5', 'F4', 'F5', 'G6', 'G7'
        for i in ib: set_stone(g, str_to_intersection(i), b)
        for i in ip: set_stone(g, str_to_intersection(i), p)
        assert get_player_stones(g) == (8, 6)
           
        
    def test_4(self):
        exec(open(f'{ADT_CODE_PATH}/TF_intersection.py', encoding="utf-8").read(), globals())
        exec(open(f'{ADT_CODE_PATH}/TF_stone.py', encoding="utf-8").read(), globals())      
        exec(open(f'{ADT_CODE_PATH}/ADT_goban.py', encoding="utf-8").read(), globals()) 
        
        ib = tuple(str_to_intersection(i) \
            for i in ('C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'))
        ip = tuple(str_to_intersection(i) \
            for i in ('A1', 'A2', 'B1', 'E4', 'E5', 'F4', 'F5', 'G6', 'G7'))
        g = new_goban(9, ib, ip)
        b = new_white_stone()
        _ = move(g, new_intersection('B', 2), b)
        assert goban_to_str(g) == \
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


class TestPrivateADTCalculatePoints:
    # score = 0.5
    def test_1(self):
        exec(open(f'{ADT_CODE_PATH}/TF_intersection.py', encoding="utf-8").read(), globals())
        exec(open(f'{ADT_CODE_PATH}/TF_stone.py', encoding="utf-8").read(), globals())      
        exec(open(f'{ADT_CODE_PATH}/TF_goban.py', encoding="utf-8").read(), globals()) 
        ib = tuple(str_to_intersection(i) for i in ('C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'))
        ip = tuple(str_to_intersection(i) for i in ('E4', 'E5', 'F4', 'F5', 'G6', 'G7'))
        g = new_goban(9, ib, ip)
        assert calculate_points(g) == (12, 6)
 
class TestPrivateADTLegalMove:
    # score = 0.5
    def test_1(self):
        exec(open(f'{ADT_CODE_PATH}/TF_intersection.py', encoding="utf-8").read(), globals())
        exec(open(f'{ADT_CODE_PATH}/TF_stone.py', encoding="utf-8").read(), globals())      
        exec(open(f'{ADT_CODE_PATH}/TF_goban.py', encoding="utf-8").read(), globals()) 
        
        ib = tuple(str_to_intersection(i) for i in ('C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'))
        ip = tuple(str_to_intersection(i) for i in ('A1', 'A2', 'B1', 'E4', 'E5', 'F4', 'F5', 'G6', 'G7'))
        g = new_goban(9, ib, ip)
        l = new_empty_goban(9)
        b, p = new_white_stone(), new_black_stone()
        assert not is_move_legal(g, new_intersection('B', 2), p, l)
 
class TestPrivateADTPlayerTurn:
    # score = 0.5
    def test_1(self):
        exec(open(f'{ADT_CODE_PATH}/TF_intersection.py', encoding="utf-8").read(), globals())
        exec(open(f'{ADT_CODE_PATH}/TF_stone.py', encoding="utf-8").read(), globals())      
        exec(open(f'{ADT_CODE_PATH}/TF_goban.py', encoding="utf-8").read(), globals()) 
        exec(open(f'{ADT_CODE_PATH}/HLF_legal_move.py', encoding="utf-8").read(), globals()) 
        
        ib = tuple(str_to_intersection(i) for i in ('C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'))
        ip = tuple(str_to_intersection(i) for i in ('A1', 'A2', 'B1', 'E4', 'E5', 'F4', 'F5', 'G6', 'G7'))
        g = new_goban(9, ib, ip)
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
        assert ref == offline_player_turn(g, new_black_stone(), new_empty_goban(9), 'B10\nB2\nG5\n') and (goban_to_str(g) == goban_str)

             
class TestPrivateADTGo:

    def test_1(self):
        exec(open(f'{ADT_CODE_PATH}/TF_intersection.py', encoding="utf-8").read(), globals())
        exec(open(f'{ADT_CODE_PATH}/TF_stone.py', encoding="utf-8").read(), globals())      
        exec(open(f'{ADT_CODE_PATH}/TF_goban.py', encoding="utf-8").read(), globals()) 
        exec(open(f'{ADT_CODE_PATH}/HLF_legal_move.py', encoding="utf-8").read(), globals()) 
        exec(open(f'{ADT_CODE_PATH}/HLF_calculate_points.py', encoding="utf-8").read(), globals()) 
        exec(open(f'{ADT_CODE_PATH}/HLF_player_turn.py', encoding="utf-8").read(), globals()) 
        
        input_str = 'A1\nB1\nB2\nA2\nA1\nA3\nA1\nC1\nE5\nP\nP\n'
        assert go_offline(9, (), (), input_str) == (False, REF_GO_PUBLIC_JOGO1)
        
    def test_2(self):
        exec(open(f'{ADT_CODE_PATH}/TF_intersection.py', encoding="utf-8").read(), globals())
        exec(open(f'{ADT_CODE_PATH}/TF_stone.py', encoding="utf-8").read(), globals())      
        exec(open(f'{ADT_CODE_PATH}/TF_goban.py', encoding="utf-8").read(), globals()) 
        exec(open(f'{ADT_CODE_PATH}/HLF_legal_move.py', encoding="utf-8").read(), globals()) 
        exec(open(f'{ADT_CODE_PATH}/HLF_calculate_points.py', encoding="utf-8").read(), globals()) 
        exec(open(f'{ADT_CODE_PATH}/HLF_player_turn.py', encoding="utf-8").read(), globals()) 
    
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


def offline_player_turn(board, pedra, last, input_jogo):
    oldstdin = sys.stdin
    sys.stdin = ReplaceStdIn(input_handle=input_jogo)
    
    oldstdout, newstdout = sys.stdout,  ReplaceStdOut()
    sys.stdout = newstdout

    try:
        res = player_turn(board, pedra, last)
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
