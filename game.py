import random

#GLOBAL VARIABLES
board = [' '] * 10
test_board = ['#','X','O','X','O','X','O','X','O','X']



#DISPPLAY BOARD
def display_board(board):
    print('         ')
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])  
    print('---------')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---------')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('         ')
   

# display_board(board)

# RANDOMLY SELECT WHO GOES 1ST
def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'

# PLAYER CHOOSE A MARKER X OR O
def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Which mark would you like to be? X or O: ').upper() 

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

# player_input()

# PLACE MARKER ON THE BOARD
def place_marker(board, marker, position):
     board[position] = marker



# CHECK TO SEE IF PLAYER HAS WON
def win_check(board, mark):
    return ((board[1] == board[2] == board[3] == mark) or
            (board[4] == board[5] == board[6] == mark) or
            (board[7] == board[8] == board[9] == mark) or
            (board[1] == board[4] == board[7] ==mark) or
            (board[2] == board[5] == board[8] == mark) or
            (board[3] == board[6] ==board[9] == mark) or
            (board[1] == board[5] == board[9] == mark) or
            (board[3] == board[5] == board[7] == mark))




#SPACE CHECK TO SEE IF SPACE IS AVAILABLE
def space_check(board, position):
    return board[position] == ' '

#FULL BOARD CHECK AKA DRAW
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

#Players position pick
def players_choice(board):
    position = 0

    while position not in range(1,10) or not space_check(board, position):
        position = int(input('Please select position to place marker: (1-9) '))

    return position

#REPLAY GAME?
def replay():
    ans = input('Would you like to play again? Enter yes or no: ')

    if ans == 'yes'.lower().startswith('y'):
        return True
    else:
        return False


#RUN ENTIRE GAME
while True:
    player1, player2 = player_input()
    turn = choose_first()
    print(turn + ' will go first!')

    play = input('Are you ready to play? Enter yes or no: ')

    if play == 'yes':
        run_game = True
    
    while run_game:
        if turn == 'Player 1':

            display_board(board)
            print('Player 1')
            position = players_choice(board)
            place_marker(board, player1, position)

            if win_check(board, player1):
                display_board(board)
                print('Player 1 has won!')
                run_game = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('We have a Draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            display_board(board)
            print('Player 2')
            position = players_choice(board)
            place_marker(board, player2, position)

            if win_check(board, player2):
                display_board(board)
                print('Player 1 has won!')
                run_game = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('We have a Draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break




        



