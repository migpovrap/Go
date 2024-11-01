# HLF legal move
def is_move_legal(board, pos, stone, last_board):
        
    if is_valid_intersection(board, pos) and \
        not is_player_stone(get_stone(board, pos)): #Valid intersection, free intersection
            new_board = copy_goban(board)
            move(new_board, pos, stone)
            
            # Checks suicide
            if len(get_adjacents_different(new_board, get_stone_chain(new_board, pos))) == 0:
                return False
            elif goban_equals(new_board, last_board): # Checks Ko
                return False
            else:
                return True
    return False
