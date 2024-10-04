def calcula_pontos(board):
    p_branco, p_preto =  obtem_pedras_jogadores(board)
    
    for territorio in obtem_territorios(board):
        limites = obtem_adjacentes_diferentes(board, territorio)
        if limites: #não pode ser vazio
            if all(eh_pedra_branca(obtem_pedra(board,i)) for i in limites):
                p_branco += len(territorio)
            elif all(eh_pedra_preta(obtem_pedra(board,i)) for i in limites):
                p_preto += len(territorio)
    return p_branco, p_preto #+ 0.5?