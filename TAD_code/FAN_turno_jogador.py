
def turno_jogador(current, pedra, last_board):
    def eh_cadeia_intercecao_ok(cad):
        return isinstance(cad,str) and ((len(cad) == 2 and 'A' <= cad[0] <= 'S' and cad[1] in '0123456789' and 1<= int(cad[1]) <= 9) \
            or (len(cad) == 3 and 'A' <= cad[0] <= 'S' and cad[1] == '1' \
                and cad[2] in '0123456789' and 1<= int(cad[1:]) <= 19)) 

    jogada_legal = False
    while not jogada_legal:
        pos = input(f"Escreva uma intersecao ou 'P' para passar [{pedra_para_str(pedra)}]:")
        if pos == 'P':
            return False
        elif eh_cadeia_intercecao_ok(pos):
            pos = str_para_intersecao(pos)
            jogada_legal = eh_jogada_legal(current, pos, pedra, last_board)
            
    jogada(current, pos, pedra)
    return True