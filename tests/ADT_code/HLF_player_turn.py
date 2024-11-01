
def player_turn(current, stone, last_board):
    def eh_cadeia_intercecao_ok(cad):
        return isinstance(cad,str) and ((len(cad) == 2 and 'A' <= cad[0] <= 'S' and cad[1] in '0123456789' and 1<= int(cad[1]) <= 9) \
            or (len(cad) == 3 and 'A' <= cad[0] <= 'S' and cad[1] == '1' \
                and cad[2] in '0123456789' and 1<= int(cad[1:]) <= 19)) 

    legal_move = False
    while not legal_move:
        pos = input(f"Escreva uma intersecao ou 'P' para passar [{stone_to_str(stone)}]:")
        if pos == 'P':
            return False
        elif eh_cadeia_intercecao_ok(pos):
            pos = str_to_intersection(pos)
            legal_move = is_move_legal(current, pos, stone, last_board)
            
    move(current, pos, stone)
    return True