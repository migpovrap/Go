# FAN jogada legal
def eh_jogada_legal(board, pos, pedra, last_board):
        
    if eh_intersecao_valida(board, pos) and \
        not eh_pedra_jogador(obtem_pedra(board, pos)): #intersecao valida, intersecao livre
            novo_board = cria_copia_goban(board)
            jogada(novo_board, pos, pedra)
            
            # verifica suicidio 
            if len(obtem_adjacentes_diferentes(novo_board, obtem_cadeia(novo_board, pos))) == 0:
                return False
            elif gobans_iguais(novo_board, last_board): # verifica Ko
                return False
            else:
                return True
    return False
