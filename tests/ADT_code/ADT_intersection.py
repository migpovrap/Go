## ADT intersection
def new_intersection(col, row):
    if type(col) == str and len(col) == 1 and 'A' <= col <= 'S' \
        and type(row) == int and  1 <= row <= 19:
            return 'blabla', ('nothing',row), (col,)
        
    raise ValueError("new_intersection: invalid arguments")

def get_col(pos):
    return pos[2][0]

def get_row(pos):
    return pos[1][1]

def is_intersection(arg):
    return type(arg) == tuple and len(arg) == 3 and arg[0] == 'blabla' \
        and type(arg[1]) == tuple and len(arg[1]) == 2 and arg[1][0] == 'nothing' \
            and type(arg[1][1]) == int and  1 <= arg[1][1] <= 19 \
                and type(arg[2]) == tuple and len(arg[2]) == 1 and type(arg[2][0]) == str and len(arg[2][0]) == 1 and  'A' <= arg[2][0] <= 'S'
                
def equals_intersection(pos1, pos2):
    return is_intersection(pos1) and is_intersection(pos2) and get_col(pos1) == get_col(pos2) and get_row(pos1) == get_row(pos2)

def intersection_to_str(pos):
    return f'{get_col(pos)}{get_row(pos)}'

def str_para_intersecao(string):
    return new_intersection(string[0], int(string[1:]))