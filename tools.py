import copy
import main
"""
This file contains some basic functions for the checkers game implementation.
The functions are:
    a. get_moves()
    b. get_jumps()
    c. get_captures()
    d. search_path()
    e. choose_color()
This file also contains two string constants to be used in the main() function.
"""

def get_moves(board, row, col, is_sorted = False):
    """
    This function returns moves for a given single piece at row,col position.
    This function returns a list of valid moves in terms of string positions,
    like 'a1', 'b4' etc. The rules are follows:
        a. All the move(s) must be inside the board.
        b. If the given row, col position has no piece (i.e. empty), this
            function returns an empty list.
        c. If the piece is not a king then it will return a list of at most 
            two diagonal positions. For a black piece, the diagonals will be 
            bottom-left and bottom-right. For a white, they will be top-left 
            and top-right.
        d. If the piece is a king, then it will return a list of at most 
            four diagonal positions. Irrespective of color, the diagonals 
            will be bottom and top, left and right.
        e. By default, is_sorted flag is set to False, if it's True then
            the final returning list must be sorted. Remember that the list
            is a list of string positions.
    """
    down, up = [(+1, -1), (+1, +1)], [(-1, -1), (-1, +1)]
    length = board.get_length()
    piece = board.get(row, col)
    if piece:
        bottom = [main.deindexify(row + x, col + y) for (x, y) in down \
                      if (0 <= (row + x) < length) \
                          and (0 <= (col + y) < length) \
                          and board.is_free(row + x, col + y)]
        top = [main.deindexify(row + x, col + y) for (x, y) in up \
                   if (0 <= (row + x) < length) \
                       and (0 <= (col + y) < length) \
                       and board.is_free(row + x, col + y)]
        return (sorted(bottom + top) if piece.is_king() else \
                (sorted(bottom) if piece.is_black() else sorted(top))) \
                    if is_sorted else (bottom + top if piece.is_king() else \
                                       (bottom if piece.is_black() else top))
    return []

def get_jumps(board, row, col, is_sorted = False):
    """
    This function is very similar to the get_moves() function. This function
    lists all the capture for a single piece on the board located at the row,
    col position. To capture the piece needs to "jump". A checker may move 
    more than one space if they can jump one of the opponent's checker pieces 
    which is located immediately in their diagonal vicinity and onto a free 
    space. This function returns a list of valid captures in terms of string 
    positions, like 'a1', 'b4' etc. The rules are follows:
        a. All the captures(s) must be inside the board.
        b. If the given row, col position has no piece (i.e. empty), this
            function returns an empty list.
        c. To make a jump, there must be an opponent piece on the immediate
            diagonal.
        d. If the piece is not a king then it will return a list of at most 
            two diagonal positions. For a black piece, the diagonals will be 
            bottom-left and bottom-right.
        e. If the piece is a king, then it will return a list of at most 
            four diagonal positions. Irrespective of color, the diagonals 
            will be bottom and top, left and right.
        f. By default, is_sorted flag is set to False, if it's True then
            the final returning list must be sorted. Remember that the list
            is a list of string positions.
    """
    down, up = [(+1, -1), (+1, +1)], [(-1, -1), (-1, +1)]
    length = board.get_length()
    piece = board.get(row, col)
    if piece:
        bottom = \
            [main.deindexify(row + 2 * x, col + 2 * y) for (x, y) in down \
             if (0 <= (row + 2 * x) < length) \
                 and (0 <= (col + 2 * y) < length) \
                 and board.is_free(row + 2 * x, col + 2 * y) \
                 and (not board.is_free(row + x, col + y)) \
                 and (board.get(row + x, col + y).color() != piece.color())]
        top = \
            [main.deindexify(row + 2 * x, col + 2 * y) for (x, y) in up \
             if (0 <= (row + 2 * x) < length) \
                 and (0 <= (col + 2 * y) < length) \
                 and board.is_free(row + 2 * x, col + 2 * y) \
                 and (not board.is_free(row + x, col + y)) \
                 and (board.get(row + x, col + y).color() != piece.color())]
        return (sorted(bottom + top) if piece.is_king() else \
                (sorted(bottom) if piece.is_black() else sorted(top))) \
                    if is_sorted else (bottom + top if piece.is_king() else \
                                       (bottom if piece.is_black() else top))
    return []

def search_path(board, row, col, path, paths, is_sorted = False):
    """
    This function recursive builds all capturing paths started at a certain
    row/col position. 
    """
    path.append(main.deindexify(row, col))
    jumps = get_jumps(board, row, col, is_sorted)
    if not jumps:
        paths.append(path)
    else:
        for position in jumps:
            (row_to, col_to) = main.indexify(position)
            piece = copy.copy(board.get(row, col))
            board.remove(row, col)
            board.place(row_to, col_to, piece)
            if (piece.color() == 'black' \
                and row_to == board.get_length() - 1) \
                    or (piece.color() == 'white' \
                        and row_to == 0) \
                            and (not piece.is_king()):
                                piece.turn_king()
            row_mid = row + 1 if row_to > row else row - 1
            col_mid = col + 1 if col_to > col else col - 1
            capture = board.get(row_mid, col_mid)
            board.remove(row_mid, col_mid)
            search_path(board, row_to, col_to, copy.copy(path), paths)
            board.place(row_mid, col_mid, capture)
            board.remove(row_to, col_to)
            board.place(row, col, piece)
            
def get_captures(board, row, col, is_sorted = False):
    """
    This function finds all capturing paths started at a certain row/col
    position on the board. If there is no capture from the given row/col,
    this function will return an empty list [].
    """
    paths = []
    board_ = copy.copy(board)
    search_path(board_, row, col, [], paths, is_sorted)
    if len(paths) == 1 and len(paths[0]) == 1:
        paths = []
    return paths

def choose_color():
    """
    This function asks for a color inside a loop until a valid color name  i.e. 
    'black'/'white' is entered. If a wrong color or an arbitrary string is 
    entered, it will print an error message. Once it receives a correct color 
    assignment, it will store those color values in to two variables called 
    'my_color' and 'opponent_color' and return them as a tuple 
    (my_color, opponent_color).
    
    Some useful print/prompt strings:
        For prompting: "Pick a color: "
        Error message: "Wrong color, type only \'black\' or \'white\', try again."
        Final decision: "You are \'{:s}\' and your opponent is \'{:s}\'."
    """
    my_color = ''
    opponent_color = ''
    while True:
        my_color = input("Pick a color: ").lower()
        if my_color == 'black' or my_color == 'white':
            break
        else:
            print("Wrong color, type only \'black\' or \'white\', try again.")
    opponent_color = 'black' if my_color == 'white' else 'white'
    print("You are \'{:s}\' and your opponent is \'{:s}\'."\
            .format(my_color, opponent_color))
    return (my_color, opponent_color)

banner = """
  ____ _               _                     
 / ___| |__   ___  ___| | _____ _ __ ___    
| |   | '_ \ / _ \/ __| |/ / _ \ '__/ __|    
| |___| | | |  __/ (__|   <  __/ |  \__ \    
 \____|_| |_|\___|\___|_|\_\___|_|  |___/    

Developed by The TianTian Inc.
About The AI
Michigan State University
East Lansing, MI, USA.
"""

usage = """
    Usage:
        pass:       give up, admit defeat and exit the game
        exit:       exit the game
        hints:      shows suggestions
        move x y:   moves a piece from x to y
        jump x y:   jumps a piece from x to y
        apply n:    executes n-th suggestion from current hints
"""
