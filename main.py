# Make all import
import tools
import gameai as ai
from checkers import Piece
from checkers import Board

###########################################################
#
# Computer Project  Use AI to play checkers.
#
# Define all the functions
#   indexify(position):
#       ascii to convert alphabetic and numeric strings into coordinates.
#       return tuple
#   deindexify(row, col):
#       Use ascii tables to convert coordinates to strings.
#       return string
#   initialize(board):
#       Make a checkerboard.
#   count_pieces(board):
#       Counts the total number of black and white pieces on the board.
#       return tuple of black and white
#   get_all_moves(board, color, is_sorted = False):
#       Get all the positions of all the pieces on the board that can be moved.
#       return list of all move
#   sort_captures(all_captures,is_sorted=False):
#       Returns a sorted captures
#   get_all_captures(board, color, is_sorted = False):
#       Get the probability that all the pieces on the board can jump.
#       return sort_captures list
#   apply_move(board, move):
#       Performs actual operations and moves that move the specified pieces.
#       No return
#   apply_capture(board, capture_path):
#       Performs actual operations and jumps to move the specified pieces.
#       No return
#   get_hints(board, color, is_sorted = False):
#       Use movement and jump to get all the possibilities.
#       return tuple of move and jump
#   get_winner(board, is_sorted = False):
#       Judge the outcome of the game.
#       return the black white and draw
#   is_game_finished(board, is_sorted = False):
#       Just decide if the game is over.
#       return true or flase
#
# Define the main function
#   it is game_play_ai()
#       This is the main mechanism of the human vs. ai game play. You need to
#       implement this function by taking helps from the game_play_human() 
#       function.
#      
###########################################################

def indexify(position):
    """
Use ascii tables to convert alphabetic and numeric strings into coordinates.
    use the ord and int
return tuple
    """
    return (ord(position[0])-ord('a'),int(position[1:])-1)

def deindexify(row, col):
    """
Use ascii tables to convert coordinates to strings.
    use the ord and str
return string
    """
    return chr(row+97)+str(col+1)

def initialize(board):
    """
    This function puts white and black pieces according to the checkers
    game positions. The black pieces will be on the top three rows and
    the white pieces will be on the bottom three rows (for an 8x8 board).
    The first row for the black pieces will be placed as a2, a4, a6, ...
    etc. and the next rows will be b1, b3, b5, ... etc. For the white
    rows, the placement patterns will be opposite of those of blacks.
    This must work for any even length board size.
    """
    row = col = board.get_length()
    initrows = (row // 2) - 1
    for r in range(row - 1, row - (initrows + 1), -1):
        for c in range(0 if r % 2 == 1 else 1, col, 2):
            board.place(r, c, Piece('white'))
    for r in range(0, initrows):
        for c in range(0 if r % 2 == 1 else 1, col, 2):
            board.place(r, c, Piece())

def count_pieces(board):
    """
Counts the total number of black and white pieces on the board.
    use two for loop and three if
return tuple of black and white
    """
    row = col = board.get_length()
    black, white = 0, 0
    for r in range(row):
        for c in range(col):
            piece = board.get(r, c)
            if piece:
                if piece.is_black():
                    black += 1
                if piece.is_white():
                    white += 1
    return (black, white)

def get_all_moves(board, color, is_sorted = False):
    """
Get all the positions of all the pieces on the board that can be moved.
    use three for loop and three if
return list of all move
    """
    row = col = board.get_length()
    final_list = []
    for r in range(row):
        for c in range(col):
            piece = board.get(r, c)
            if piece:
                if piece.color() == color:
                    path_list = tools.get_moves(board, r, c, is_sorted)
                    path_start = deindexify(r, c)
                    for path in path_list:
                        final_list.append((path_start, path))
    
    if is_sorted == True:
        final_list.sort()
    return final_list

def sort_captures(all_captures,is_sorted=False):
    '''If is_sorted flag is True then the final list will be sorted by 
    the length of each sub-list and the sub-lists with the same length 
    will be sorted again with respect to the first item in corresponding 
    the sub-list, alphabetically.'''
    
    return sorted(all_captures, key = lambda x: (-len(x), x[0]))\
    if is_sorted else all_captures

def get_all_captures(board, color, is_sorted = False):
    """
Get the probability that all the pieces on the board can jump.
    use three for loop and two if
return sort_captures list
    """
    row = col = board.get_length()
    final_list = []
    for r in range(row):
        for c in range(col):
            piece = board.get(r, c)
            if piece:
                if piece.color() == color:
                    path_list = tools.get_captures(board, r, c, is_sorted)
                    for path in path_list:
                        final_list.append(path) 
    return sort_captures(final_list, is_sorted)

def apply_move(board, move):
    """
Performs actual operations and moves that move the specified pieces.
    use the if and piece and board class
No return
    
    Raise this exception below:
        raise RuntimeError("Invalid move, please type" \
                         + " \'hints\' to get suggestions.") 
    If,
        a. there is no move from move[0], i.e. use tools.get_moves() function
        to get all the moves from move[0]
        b. the destination position move[1] is not in the moves list found
            from tools.get_moves() function.            
    """
    row,col = indexify(move[0])
    row_end,col_end = indexify(move[1])
    path_list = tools.get_moves(board, row, col, is_sorted = False)
    
    if move[1] in path_list:
        piece = board.get(row, col)
        if piece.is_black() and row_end == board.get_length()-1 \
        or piece.is_white() and row_end == 0:
            piece.turn_king()
        board.remove(row, col)
        board.place(row_end, col_end, piece)
    else:
        raise RuntimeError("Invalid move, please type" \
                         + " \'hints\' to get suggestions.")

def apply_capture(board, capture_path):
    """
Performs actual operations and jumps to move the specified pieces.
    use one while loop and one if
No return
    
    Raise this exception below:
        raise RuntimeError("Invalid jump/capture, please type" \
                         + " \'hints\' to get suggestions.") 
    If,
        a. there is no jump found from any position in capture_path, i.e. use 
            tools.get_jumps() function to get all the jumps from a certain
            position in capture_path
        b. the destination position from a jump is not in the jumps list found
            from tools.get_jumps() function.            
    """
    counter = 0
    while counter < len(capture_path)-1:
        path = [capture_path[counter], capture_path[counter + 1]]
        counter += 1
        row,col = indexify(path[0])
        row_end,col_end = indexify(path[1])
        path_list = tools.get_jumps(board, row, col, is_sorted = False)
        
        if path[1] in path_list:
            piece = board.get(row, col)
            if piece.is_black() and row_end == board.get_length()-1 \
            or piece.is_white() and row_end == 0:
                piece.turn_king()
            board.remove(row, col)
            row_eat, col_eat = max(row, row_end)-1, max(col, col_end)-1
            board.remove(row_eat, col_eat)
            board.place(row_end, col_end, piece)
        else:
            raise RuntimeError("Invalid jump/capture, please type" \
                             + " \'hints\' to get suggestions.")
            
def get_hints(board, color, is_sorted = False):
    """
Use movement and jump to get all the possibilities.
    use the get_all_moves and get_all_captures
return tuple of move and jump
    """
    move = get_all_moves(board, color, is_sorted)
    jump = get_all_captures(board, color, is_sorted)
    if jump:
        return ([], jump)
    else:
        return (move, jump)
        
def get_winner(board, is_sorted = False):
    """
Judge the outcome of the game.
    use if and elif to judge and two for loop
return the black white and draw
    """
    black_hint = get_hints(board, 'black', is_sorted)
    white_hint = get_hints(board, 'white', is_sorted)
    if black_hint != ([],[]) and white_hint == ([],[]):
        return 'black'
    elif black_hint == ([],[]) and white_hint != ([],[]):
        return 'white'
    else:
        black_king,white_king = 0,0
        black, white = 0,0
        row = col = board.get_length()
        for r in range(row):
            for c in range(col):
                piece = board.get(r, c)
                if piece:
                    if piece.is_black():
                        black += 1
                        if piece.is_king():
                            black_king += 1
                    else:
                        white += 1
                        if piece.is_king():
                            white_king += 1
        if white_king == 1 and black_king == 1 and white == 1 and black == 1:
            return 'draw'
        else:
            if white > black:
                return 'white'
            elif black > white:
                return 'black'
            else:
                return 'draw'
                        
def is_game_finished(board, is_sorted = False):
    """
Just decide if the game is over.
    use one if
return true or flase
    """
    black_hint = get_hints(board, 'black', is_sorted)
    white_hint = get_hints(board, 'white', is_sorted)
    if black_hint == ([],[]) or white_hint == ([],[]):
        return True
    else:
        return False

# Some error messages to save lines.
move_error = "Invalid move, please type \'hints\' to get suggestions."
hasjump_error = "You have jumps, please type \'hints\' to get suggestions."
jump_error = "Invalid jump, please type \'hints\' to get suggestions."
hint_error = "Invalid hint number."
cmd_error = "Invalid command."

def game_play_human():
    """
    This is the main mechanism of the human vs. human game play.
    Use this function to write the game_play_ai() function.
    """    
    Piece.symbols = ['b', 'w']
    Piece.symbols_king = ['B', 'W']
    
    prompt = "[{:s}'s turn] :> "
    print(tools.banner)
   
    # Choose the color here
    (my_color, opponent_color) = tools.choose_color()
    
    # Take a board of size 8x8
    board = Board(8)
    initialize(board)
    
    # Decide on whose turn, use a variable called 'turn'.
    turn = my_color if my_color == 'black' else opponent_color
    print("Black always plays first.\n")
    
    # loop until the game is finished
    while not is_game_finished(board):
        try:
            # Count the pieces and assign into piece_count
            piece_count = count_pieces(board)
            
            print("Current board:")
            board.display(piece_count)
            
            # Get the command from user using input
            command = input(prompt.format(turn)).strip().lower()
            
            # Now decide on different commands
            if command == 'pass':
                break
            elif command == 'exit':
                break
            elif command == 'hints':
                (moves, captures) = get_hints(board, turn, True)
                if moves:
                    print("You have moves:")
                    for i, move in enumerate(moves):
                        print("\t{:d}: {:s} --> {:s}"\
                                  .format(i + 1, move[0], move[1]))
                if captures:
                    print("You have captures:")
                    for i, path in enumerate(captures):
                        print("\t{:d}: {:s}".format(i + 1, str(path)))
            else:
                command = [s.strip().lower() for s in command.split()]
                (moves, captures) = get_hints(board, turn, True)
                action = None
                if command and command[0] == 'move' and len(command) == 3:
                    if not captures:
                        action = (command[1], command[2])
                        if action in moves:
                            apply_move(board, action)
                        else:
                            raise RuntimeError(move_error)
                    else:
                        raise RuntimeError(hasjump_error)
                elif command and command[0] == 'jump' and len(command) >= 3:
                    action = command[1:]
                    if action in captures:
                        apply_capture(board, action)
                    else:
                        raise RuntimeError(jump_error)
                elif command and command[0] == 'apply' and len(command) == 2:
                    id_hint = int(command[1])
                    if moves and (1 <= id_hint <= len(moves)):
                        action = moves[id_hint - 1]
                        apply_move(board, action)
                    elif captures and (1 <= id_hint <= len(captures)):
                        action = captures[id_hint - 1]
                        apply_capture(board, action)
                    else:
                        raise ValueError(hint_error)
                else:
                    raise RuntimeError(cmd_error + tools.usage)
                print("\t{:s} played {:s}.".format(turn, str(action)))
                turn = my_color if turn == opponent_color else opponent_color
        except Exception as err:
            print("Error:", err)
    
    # The loop is over.
    piece_count = count_pieces(board)
    print("Current board:")
    board.display(piece_count)
    if command != 'pass':
        winner = get_winner(board)
        if winner != 'draw':
            diff = abs(piece_count[0] - piece_count[1])
            print("\'{:s}\' wins by {:d}! yay!!".format(winner, diff))
        else:
            print("This game ends in a draw.")
    else:
        winner = opponent_color if turn == my_color else my_color
        print("{:s} gave up! {:s} is the winner!! yay!!!".format(turn,winner))
    # --- end of game play human ---
    
def game_play_ai():
    """
    This is the main mechanism of the human vs. ai game play. You need to
    implement this function by taking helps from the game_play_human() 
    function.
    
    For a given board situation/state, you can call the ai function to get
    the next best move, like this:
        
        move = ai.get_next_move(board, turn)
        
    where the turn variable is a color 'black' or 'white', also you need to 
    import ai module as 'import gameai as ai' at the beginning of the file.
    This function will be very similar to game_play_human().
    """
    Piece.symbols = ['b', 'w']
    Piece.symbols_king = ['B', 'W']
    prompt = "[{:s}'s turn] :> "
    print(tools.banner)
   
    # Choose the color here
    (my_color, opponent_color) = tools.choose_color()
    
    # Take a board of size 8x8
    board = Board(8)
    initialize(board)
    
    # Decide on whose turn, use a variable called 'turn'.
    turn = my_color if my_color == 'black' else opponent_color
    print("Black always plays first.\n")
    
    # loop until the game is finished
    while not is_game_finished(board):
        try:
            # Count the pieces and assign into piece_count
            piece_count = count_pieces(board)
            
            print("Current board:")
            board.display(piece_count)
            
            if turn == opponent_color: # if Turn of machine
                move = ai.get_next_move(board, turn)
                if type(move) == list: # move is a move
                    apply_capture(board, move)
                if type(move) == tuple: # move is a jump
                    apply_move(board, move)
                
                print("\t{:s} played {:s}.".format(turn, str(move)))
                turn = my_color # change the turn
                continue
            # Get the command from user using input
            command = input(prompt.format(turn)).strip().lower()
            
            # Now decide on different commands
            if command == 'pass':
                break
            elif command == 'exit':
                break
            elif command == 'hints':
                (moves, captures) = get_hints(board, turn, True)
                if moves:
                    print("You have moves:")
                    for i, move in enumerate(moves):
                        print("\t{:d}: {:s} --> {:s}"\
                                  .format(i + 1, move[0], move[1]))
                if captures:
                    print("You have captures:")
                    for i, path in enumerate(captures):
                        print("\t{:d}: {:s}".format(i + 1, str(path)))
            else:
                command = [s.strip().lower() for s in command.split()]
                (moves, captures) = get_hints(board, turn, True)
                action = None
                if command and command[0] == 'move' and len(command) == 3:
                    if not captures:
                        action = (command[1], command[2])
                        if action in moves:
                            apply_move(board, action)
                        else:
                            raise RuntimeError(move_error)
                    else:
                        raise RuntimeError(hasjump_error)
                elif command and command[0] == 'jump' and len(command) >= 3:
                    action = command[1:]
                    if action in captures:
                        apply_capture(board, action)
                    else:
                        raise RuntimeError(jump_error)
                elif command and command[0] == 'apply' and len(command) == 2:
                    id_hint = int(command[1])
                    if moves and (1 <= id_hint <= len(moves)):
                        action = moves[id_hint - 1]
                        apply_move(board, action)
                    elif captures and (1 <= id_hint <= len(captures)):
                        action = captures[id_hint - 1]
                        apply_capture(board, action)
                    else:
                        raise ValueError(hint_error)
                else:
                    raise RuntimeError(cmd_error + tools.usage)
                print("\t{:s} played {:s}.".format(turn, str(action)))
                turn = my_color if turn == opponent_color else opponent_color
        except Exception as err:
            print("Error:", err)
    
    # The loop is over.
    piece_count = count_pieces(board)
    print("Current board:")
    board.display(piece_count)
    if command != 'pass':
        winner = get_winner(board)
        if winner != 'draw':
            diff = abs(piece_count[0] - piece_count[1])
            print("\'{:s}\' wins by {:d}! yay!!".format(winner, diff))
        else:
            print("This game ends in a draw.")
    else:
        winner = opponent_color if turn == my_color else my_color
        print("{:s} gave up! {:s} is the winner!! yay!!!".format(turn,winner))
    # --- end of game play ai ---

def main():
    # game_play_human()
    game_play_ai()

# main function, the program's entry point
if __name__ == "__main__":
    main()