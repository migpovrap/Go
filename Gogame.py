COLUMNS = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S')
ROWS = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19)

# ADT intersection
def new_intersection(col:str,row:int) -> tuple:
    '''
    Intersection Constructor, returns an intersection if the given arguments
    meet the following conditions:
    the col is a character and the row is an integer.

    Parameters:
            col(str): A character which for the goban game in this case must\
            be between A-Z
            row(int): An integer corresponding to the row, for the goban game\
            in this case must be between 1 and 19
    Returns:
            return: the intersection

            ValueError: ('new_intersection: invalid arguments) - if the\
            arguments cannot be validated
    '''
    if isinstance(col, str) and isinstance(row, int) \
        and col in COLUMNS and row in ROWS:
        return (col, row)
    raise ValueError('new_intersection: invalid arguments')


def get_col(i:tuple) -> str:
    '''
    Function that gets columns of an intersection

    Parameters:
            i(tuple): The intersection
    Returns:
            return: The column of the intersection
    '''
    return i[0]


def get_row(i:tuple) -> int:
    '''
    Function that gets the row of an intersection

    Parameters:
            i(tuple): the intersection
    Returns:
            return: intersection row
    '''
    return i[1]


def is_intersection(arg:tuple) -> bool:
    '''
    Verifies if a arguments is a intersection.

    Parameters:
            arg(any): The argument to test
    Returns:
            return(Boolean): Returns True if it is an intersection,\
             otherwise False
    '''
    if isinstance(arg, tuple) and len(arg) == 2:
        try:
            new_intersection(get_col(arg),get_row(arg))
            return True
        except ValueError:
            pass
    return False


def equals_intersection(i1:tuple,i2:tuple) -> bool:
    '''
    Checks if two intersections are equal.

    Parameters:
            i1(tuple): the first intersection
            i2(tuple): the second intersection
    Returns:
            return(Boolean):  true if the intersections are equal, otherwise False
    '''
    return is_intersection(i1) and is_intersection(i2) and\
    get_col(i1) == get_col(i2) and get_row(i1) == get_row(i2)


def intersection_to_str(i:tuple) -> str:
    '''
    Transforms an intersection from its internal format to its externa\
    representation.

    Parameters:
            i(tuple): the intersection
    Returns:
            return(str): the string that externally represents an intersection
    '''
    return get_col(i) + str(get_row(i))

def str_to_intersection(string :str):
    '''
    Transforms the external representation of an intersection to its internal\
    representation.

    Parameters:
            string(str): string that represents the external intersection
    Returns:
            return(intersection): internal representation of the intersection\
            using the constructor
    '''
    return new_intersection(string[0], int(string[1:]))


# High level functions that are associated wiht the adt intersection
# Reading order of goban is (left to right, bottom  to top)

def get_adjacent_intersections(i:tuple, l:tuple) -> tuple:
    '''
    Gets the intersections that are adjacent to a given intersection, which\
    are located above, below, left, or right.

    Parameters:
            i(tuple): the intersection
            l(tuple): last intersection (top right corner) of the goban board\
            we are considering
    Returns:
            return(tuple): A tuple that contains the adjacent intersections\
            in reading order
    '''
    adjacent_vectors = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    adj_intersec = []

    for vec in adjacent_vectors:
        col_index = COLUMNS.index(get_col(i)) + vec[0]
        row = get_row(i) + vec[1]
        if 0 <= col_index < len(COLUMNS) and 1 <= row <= get_row(l):
            col = COLUMNS[col_index]
            if col <= get_col(l):
                adj_intersec.append(new_intersection(col, row))

    return sort_intersections(tuple(adj_intersec))


def sort_intersections(tup:tuple) -> tuple:
    '''
    Sorts the provided tuple of intersections according to the reading order\
    of the Goban board.

    Parameters:
            t(tuple): the tuple of intersections
    Returns:
            return(tuple): same tuple but with the intersections sorted
    '''
    return tuple(sorted(tup, key=lambda i: (get_row(i), get_col(i))))

# ADT stone
# n --> empty stone
# w --> white stone
# b --> black stone

def new_white_stone() -> str:
    '''
    The constructor for the white stone.

    Returns:
            return(str): internal representation of the white stone
    '''
    return 'w'

def new_black_stone() -> str:
    '''
    The constructor for the black stone.

    Returns:
            return(str): internal representation of the black stone
    '''
    return 'b'


def new_empty_stone() -> str:
    '''
    The constructor for the empty stone.

    Returns:
            return(str): internal representation of the empty stone
    '''
    return 'n'

def is_stone(arg:str) -> bool:
    '''
    Checks if the provided argument is a stone according to the internal\
    representation.

    Returns:
            return(Boolean): true if the argument is a stone, otherwise False
    '''
    return arg in (new_white_stone(), new_empty_stone(), new_black_stone())


def is_white_stone(st:str) -> bool:
    '''
    Checks if the provided argument is a white stone according to the internal\
        representation.

    Returns:
            return(Boolean):  true if the argument is a white stone, otherwise\
            False
    '''
    return st == new_white_stone()

def is_black_stone(st:str) -> bool:
    '''
    Checks if the provided argument is a black stone according to the internal\
    representation.

    Returns:
            return(Boolean): true if the argument is a black stone, otherwise False
    '''
    return st == new_black_stone()

def equals_stones(st1:str,st2:str) -> bool:
    '''
    Checks if the two provided stones are equal.

    Parameters:
            p1(int): the first stone
            p2(int): the second stone
    Returns:
            return(Boolean): true if the two stones are equal and False otherwise
    '''
    return is_stone(st1) and is_stone(st2) and ((is_white_stone(st1) and\
    is_white_stone(st2)) or (is_black_stone(st1) and is_black_stone(st2))\
    or (not is_player_stone(st1) and not is_player_stone(st2)))


def stone_to_str(st:str) -> str:
    '''
    Transforms the internal representation of a stone to its external\
    representation.

    Parameters:
            p(int): internal representation of the stone
    Returns:
            return(str): external representation of the stone
    '''
    if is_white_stone(st):
        return "O"
    if is_black_stone(st):
        return "X"
    return "."


# High level functions that are associated with ADT stone
def is_player_stone(st):
    '''
    Checks if a stone belongs to a player or is a neutral stone.

    Parameters:
            p(): the stone in question
    Returns:
            return(Boolean): true if the stone belongs to a player\
             and False if it does not
    '''
    return is_white_stone(st) or is_black_stone(st)


# ADT Goban
# The game board is represented as a tuple of lists ([],[],[])
def new_empty_goban(size:int) -> tuple:
    '''
    Creates a goban with the desired size, either 9x9, 13x13, or 19x19.

    Parameters:
            n(int): the desired size of the Goban board
    Returns:
            return(tuple): the Goban board
    '''
    if isinstance(size, int) and size in (9,13,19):
            return tuple([new_empty_stone() for i in range(size)] for i1 in range(size))
            # Generates a tuple of list with the values corresponding to the
            # internal representation of the empty goban
    raise ValueError('new_empty_goban: invalid arguments')

def new_goban(size:int, winter:tuple, binter:tuple) -> tuple:
    '''
    Creates a goban with the desired size and places it in the indicated\
    state with white and black stones.

    Parameters:
            size(int): the desired size of the Goban board
            winter(tuple): the tuple of intersections occupied by white stones
            binter(tuple): teh tuple of intersections occupied by black stones
    Returns:
            g(tuple): the Goban board in the initial state
    '''
    try:
        g = new_empty_goban(size)
    except ValueError as e:
        raise ValueError('new_goban: invalid arguments') from e
    if not isinstance(winter, tuple) or not isinstance(binter, tuple):
        raise ValueError('new_goban: invalid arguments')

    ocupied_inter = set()

    for inter in winter:
        if not is_intersection(inter) or get_row(inter) > size or get_col(inter) not in COLUMNS[:size]:
            raise ValueError('new_goban: invalid arguments')
        if inter in ocupied_inter:
            raise ValueError('new_goban: invalid arguments')
        set_stone(g, inter, new_white_stone())
        ocupied_inter.add(inter)

    for inter in binter:
        if not is_intersection(inter) or get_row(inter) > size or get_col(inter) not in COLUMNS[:size]:
            raise ValueError('new_goban: invalid arguments')
        if inter in ocupied_inter:
            raise ValueError('new_goban: invalid arguments')
        set_stone(g, inter, new_black_stone())
        ocupied_inter.add(inter)

    return g

def copy_goban(g:tuple) -> tuple:
    '''
    Creates an independent copy of the Goban board

    Parameters:
            t(tuple): the Goban board
    Returns:
            return(tuple): a deep copy of the Goban board
    '''
    return tuple([[stone for stone in row] for row in g])


def get_last_intersection(g:tuple) -> tuple:
    '''
    Gets the last intersection of a given Goban board, which is the intersection\
    at the top right corner.

    Parameters:
            g(tuple): the Goban board
    Returns:
            return(tuple): the corresponding intersection
    '''
    return new_intersection(COLUMNS[len(g)-1], len(g))


def get_stone(g:tuple,i:tuple) -> str:
    '''
    Returns the internal representation of the stone.

    Parameters:
            g(tuple): the Goban board
            i(tuple): teh intersection from which we want to get the stone
    '''
    return g[get_row(i)-1][COLUMNS.index(get_col(i))]


def get_stone_chain(g:tuple,i:tuple) -> tuple:
    '''
    Gets the chain of stones that pass through the given intersection.
    If the position is empty, returns the chain of empty positions.

    Parameters:
            g(tuple): the Goban board
            i(tuple): the intersection in question
    Returns:
            return(tuple): the tuple formed by the intersections of the chain\
            that passes through the given intersection
    '''
    st_type = get_stone(g, i)
    chain = set()
    exploring = {i}
    while exploring:
        actual = exploring.pop()
        chain.add(actual)
        for adj in get_adjacent_intersections(actual, get_last_intersection(g)):
            if adj not in chain and equals_stones(get_stone(g, adj), st_type):
                exploring.add(adj)
    return sort_intersections(tuple(chain))


def set_stone(g:tuple,i:tuple,p:str) -> tuple:
    '''
    Places the stone at a specific intersection on the Goban board.

    Parameters:
            g(tuple): the Goban board
            i(tuple): the intersection where the stone is to be placed
            p(string): the type of stone to place (the player making the move)
    Returns:
            g(tuple): destructively modifies the Goban board
    '''
    g[get_row(i)-1][COLUMNS.index(get_col(i))] = p
    return g

def remove_stone(g:tuple,i:tuple) -> tuple:
    '''
    Removes the stone at a specific intersection on the Goban board.

    Parameters:
            g(tuple): the Goban board
            i(tuple): the intersection where the stone is to be removed
    Returns:
            g(tuple): destructively modifies the Goban board
    '''
    g[get_row(i)-1][COLUMNS.index(get_col(i))] = new_empty_stone()
    return g


def remove_stone_chain(g:tuple, t:tuple) -> tuple:
    '''
    Removes a specific chain from the Goban board.

    Parameters:
            g(tuple): the Goban board
            t(tuple): the set of intersections that form the chain to be removed
    Returns:
            g(tuple): destructively modifies the Goban board
    '''
    for inter in t:
        remove_stone(g,inter)
    return g


def is_goban(arg:tuple) -> bool:
    '''
    Checks if the provided argument is a goban.

    Parameters:
            arg(tuple): argument to check if it is a goban
    Returns:
            return(Boolean): true if the argument is a goban and false otherwise
    '''
    if isinstance(arg, tuple) and len(arg) in (9, 13, 19):
        if all(isinstance(col, list) and len(col) == len(arg) for col in arg):
            if  all(is_stone(stone) for row in arg for stone in row):
                return True
    return False


def is_valid_intersection(g:tuple,i:tuple) -> bool:
    '''
    Checks if the provided arguments are valid and subsequently verifies if the\
    given intersection exists on the Goban board.

    Parameters:
            g(tuple): the Goban board
            i(tuple): the intersection to verify
    Returns:
            return(Boolean): true if the arguments are valid and the intersection\
            belongs to the Goban board, otherwise false
    '''
    return is_goban(g) and is_intersection(i) and get_col(i) in COLUMNS[:len(g)]\
    and 1 <= get_row(i) <= len(g)


def goban_equals(g1:tuple,g2:tuple) -> bool:
    '''
    Checks if the two Goban boards are equal.

    Parameters:
            g1(tuple): the first Go board
            g2(tuple): the second Go board
    Returns:
            return(Boolean): true if the two Goban boards are equal,\
            otherwise false
    '''
    if not (is_goban(g1) and is_goban(g2) and len(g1) == len(g2)):
        return False
    return all(equals_stones(get_stone(g1, new_intersection(COLUMNS[col], lin + 1)),
    get_stone(g2, new_intersection(COLUMNS[col], lin + 1)))
    for lin, row in enumerate(g1) for col, _ in enumerate(row))


def goban_to_str(g:tuple) -> str:
    '''
    Transforms the internal representation of the Goban board into its\
    external representation.

    Parameters:
            g(tuple): the Goban board
    Returns:
            return(string): external representation of the\
            Goban board
    '''
    dim = len(g)
    gobanstr = '   ' + ' '.join(COLUMNS[:dim]) + '\n'
    for i in range(dim - 1, -1, -1):
        gobanstr += f'{i+1:2} ' + ' '\
        .join(stone_to_str(get_stone(g,new_intersection(COLUMNS[col],i+1)))\
        for col in range(dim)) + f' {i+1:2}\n'
    gobanstr += '   ' + ' '.join(COLUMNS[:dim])
    return gobanstr

# High level functions associated with the ADT goban
def get_territories(g:tuple) -> tuple:
    '''
    Gets the territories that exist on a given Goban board, whether they belong\
    to a specific player or not.

    Parameters:
            g(tuple): the Goban board
    Returns:
            return(tuple): tuple formed by the tuples that contain the\
            intersections that form each territory
    '''
    terr = ()
    inter = ()
    dim = get_row(get_last_intersection(g))
    for row in range(1, dim + 1):
        for col in COLUMNS[:dim]:
            if new_intersection(col, row) not in inter:
                # Checks if the intersection has already been visited
                if equals_stones(get_stone(g, new_intersection(col, row)),\
                    new_empty_stone()):
                    nterr = get_stone_chain(g, new_intersection(col, row))
                    if nterr not in terr:
                        terr += (nterr,)
                        # Add the territory if it meets the requirements
                        inter += nterr
                        # Marks all intersections already visited,
                        # to avoid repetitions
    return tuple(sorted(terr, key=lambda t: get_row(t[0])))


def get_adjacents_different(g:tuple, t:tuple) -> tuple:
    '''
    Gets the set of intersections adjacent to a given territory.

    Parameters:
            g(tuple): the Goban board
            t(tuple): the territory in question
    Returns:
            adj(tuple): set of different adjacent intersections\
            (the boundary of the given territory)
    '''
    adj = set()
    for inter in t:
        for coord in get_adjacent_intersections(inter, get_last_intersection(g)):
            if (is_player_stone(get_stone(g, inter)) and not\
                is_player_stone(get_stone(g, coord))) or\
                (not is_player_stone(get_stone(g, inter)) and\
                is_player_stone(get_stone(g, coord))):
                adj.add(coord)
    return sort_intersections(tuple(adj))


def move(g:tuple, i:tuple, p:str) -> tuple:
    '''
    The function that is used to execute a move, will place the stone in the\
    requested position and capture the opponent's stones if necessary.

    Parameters:
            g(tuple): the Goban board
            i(tuple): the intersection where the move will be executed
            p(int): type of stone that will make the move
    Returns:
            g(tuple): Goban board itself, that as destrutively modified
    '''
    set_stone(g,i,p)
    for coord in get_adjacent_intersections(i,get_last_intersection(g)):
        if get_stone(g,coord) not in (new_empty_stone(),p):
            # Checks if the stone belongs to the opposing player
            otherplayer_chain = get_stone_chain(g,coord)
            othplacha_free = False
            for coord in otherplayer_chain:
                for pedra in get_adjacent_intersections(coord, get_last_intersection(g)):
                    if equals_stones(get_stone(g,pedra),new_empty_stone()):
                        othplacha_free = True
                        break
                if othplacha_free: # If the chain is free for execution
                    break
            if not othplacha_free: # If the chain is not free, it will be removed
                remove_stone_chain(g,otherplayer_chain)
    return g

def get_player_stones(g:tuple) -> tuple:
    '''
    Counts the number of intersections occupied by each player's stones.

    Parameters:
            g(tuple): the Goban board
    Returns:
            return(tuple): tuple containing the number of white and black\
            stones respectively (nb, np)

    '''
    dim = get_row(get_last_intersection(g))
    white_stones = sum(is_white_stone(get_stone(g, new_intersection(col, lin)))\
        for col in COLUMNS[:dim] for lin in range(1, dim + 1))
    black_stones = sum(is_black_stone(get_stone(g, new_intersection(col, lin)))\
        for col in COLUMNS[:dim] for lin in range(1, dim + 1))
    return (white_stones, black_stones)


# Aditional functions
def calculate_points(g:tuple) -> tuple:
    '''
    Calculates the points each player has in the current state of the goban board (g)

    Parameters:
            g(tuple): the goban game board

    Returns:
            return(tuple): the points of the white and black players respectively
    '''
    t = get_territories(g)
    points = get_player_stones(g)
    white_territorie = sum(len(terrain) for terrain in t if get_adjacents_different(g, terrain)\
    and all(is_white_stone(get_stone(g, coord)) for coord in get_adjacents_different(g, terrain)))
    black_territorie = sum(len(terrain) for terrain in t if get_adjacents_different(g, terrain)\
    and all(is_black_stone(get_stone(g, coord)) for coord in get_adjacents_different(g, terrain)))
    return (points[0] + white_territorie, points[1] + black_territorie)
    # Each player's points are the sum of their territories and
    # the number of stones they have in the territory


def is_move_legal(g:tuple,i:tuple,s:str,l:tuple) -> bool:
    '''
    Checks if a move is legal or not, if it is a valid intersection, if it is\
    empty, if it is not a suicide, or repetition (ko) - after resolution the\
    board remains in the same state as it was

    Parameters:
            g(tuple): the goban game board
            i(tuple): the coordinates of the intersection where the move is\
            executed
            p(str): the type of stone being moved
            l(tuple): the board in the state before the move resolution
    Returns:
            return(Boolean): true if the move is legal or false otherwise
    '''
    if not is_valid_intersection(g, i) or is_player_stone(get_stone(g, i)):
        return False

    goban_copy = copy_goban(g)
    move(goban_copy, i, s)

    # Checks for the KO state which occurs when after a move we obtain the
    # same board
    if goban_equals(goban_copy, l):
        return False

    # Checks the suicide rule
    return get_adjacents_different(goban_copy, get_stone_chain(goban_copy, i))

def player_turn(g:tuple,s:str,l:tuple) -> bool:
    '''
    Each player's turn, returns False if the player passes their turn 'P' and\
    returns True if the player makes a legal move and destructively modifies the\
    goban. This function will ask for a new attempt while the player does not\
    pass the turn or provide a legal intersection.

    Parameters:
            g(tuple): the goban game board
            p(int): type of stone
            l(tuple): the state of the board before the resolution of the\
            current move
    Returns:
            return(Boolean): false if the player passes the turn and true\
            otherwise
            g(tuple): destructively modifies the Goban board
    '''
    mensg = "Escreva uma intersecao ou 'P' para passar [" + stone_to_str(s) + "]:"
    while True:
        user_input = input(mensg)
        if user_input == 'P':
            return False
        try:
            intersecao = str_to_intersection(user_input)
            if is_move_legal(g, intersecao, s, l):
                move(g, intersecao, s)
                return True
        except ValueError:
            continue


def go(g: int, tb: 'tuple[str,...]', tp: 'tuple[str,   ]') -> bool:
    '''
    Main function that allows two people to play a complete game of goban

    Parameters:
            g(int): size of the goban board can be 9x9, 13x13, or 19x19 - (9,13,19)
            tb(tuple): intersections initially occupied by white stones
            tp(tuple): intersections initially occupied by black stones
    Return:
        print(goban_to_str): Prints the goban board to the terminal at each change
        return(Boolean): True if the white player wins, and False otherwise

    '''
    if not isinstance(tp, tuple) or not isinstance(tb, tuple):
        raise ValueError('go: invalid arguments')

    try:
        tbinter = tuple(str_to_intersection(interb) if isinstance(interb, str)\
        else interb for interb in tb)
        tpinter = tuple(str_to_intersection(interp) if isinstance(interp, str)\
        else interp for interp in tp)
        goban = new_goban(g, tbinter, tpinter)
    except ValueError as e:
        raise ValueError('go: invalid arguments') from e

    whitepass = blackpass = False
    i = 0
    initial_goban = copy_goban(goban)
    while not (whitepass and blackpass):
        white_points, black_points = calculate_points(goban)
        print(f'Branco (O) tem {white_points} pontos')
        print(f'Preto (X) tem {black_points} pontos')
        print(goban_to_str(goban))
        last_goban = copy_goban(goban)

        if i % 2 == 0:
            blackpass = not player_turn(goban, new_black_stone(), initial_goban)
        else:
            whitepass = not player_turn(goban, new_white_stone(), initial_goban)

        initial_goban = last_goban
        i += 1
    white_points, black_points = calculate_points(goban)
    print(f'Branco (O) tem {white_points} pontos')
    print(f'Preto (X) tem {black_points} pontos')
    print(goban_to_str(goban))
    return white_points >= black_points
