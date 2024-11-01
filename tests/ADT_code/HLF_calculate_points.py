def calculate_points(board):
    white_s, black_s =  get_player_stones(board)
    
    for territorie in get_territories(board):
        limits = get_adjacents_different(board, territorie)
        if limits: #não pode ser vazio
            if all(is_white_stone(get_stone(board,i)) for i in limits):
                white_s += len(territorie)
            elif all(is_black_stone(get_stone(board,i)) for i in limits):
                black_s += len(territorie)
    return white_s, black_s #+ 0.5?