#simple game of tic tac toe between two players


#function to display the game board
def display_board(board):
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' ')
    print('---|---|---')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' ')
    print('---|---|---')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' ')
    print('   |   |   ')




#function for player selection
def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input("Player 1, would you like to be 'X' or 'O': ").upper()
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

#funtion to place players move on the game board
def place_marker(board,marker,position):
    board[position] = marker

#function to check if a player has won

def win_check(board,marker):
    return((board[7] == marker and board[8] == marker and board[9] == marker) or
           (board[4] == marker and board[5] == marker and board[6] == marker) or
           (board[1] == marker and board[2] == marker and board[3] == marker) or
           (board[7] == marker and board[4] == marker and board[1] == marker) or
           (board[8] == marker and board[5] == marker and board[2] == marker) or
           (board[9] == marker and board[6] == marker and board[3] == marker) or
           (board[7] == marker and board[5] == marker and board[3] == marker) or
           (board[9] == marker and board[5] == marker and board[1] == marker))


#function to randomly choose which player goes first
import random

def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

#function to check if position on board is available
def space_check(board,position):
   return board[position] == ' '

#function to check if the game board is full
def full_board_check(board):
    for i in range (1,10):
        if space_check(board,i):
            return False
    return True


#function that allows a player to select their move and place their marker on the board

def player_choice(board):
    selection = 0
    while not (selection > 0 and selection < 10) or not space_check(board,selection):
        selection = int(input('please select a space 1-9: '))
    return selection

#fucntion to give the players the option to play again
def replay():
    return input("Would you like to play again? type YES or NO").lower().startswith('y')

'''GAME TIME'''

print('Welcome to Tic Tac Toe!')

while True:
    gameBoard = [' '] * 10

    player_1_marker, player_2_marker = player_input()
    turn = choose_first()
    print('{} will go first'.format(turn))

    play_game = input('Are you ready to play, YES or NO').lower()
    if play_game[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            print('Player 1 turn')
            display_board(gameBoard)
            position = player_choice(gameBoard)
            place_marker(gameBoard,player_1_marker,position)

            if win_check(gameBoard, player_1_marker):
                display_board(gameBoard)
                print('Congratulations Player 1, you won the game!')
                game_on = False
            else:
                if full_board_check(gameBoard):
                    display_board(gameBoard)
                    print('The game is a Draw')
                    break
                else:
                    turn = 'Player 2'

        else:
            print('Player 2 turn')
            display_board(gameBoard)
            position = player_choice(gameBoard)
            place_marker(gameBoard, player_2_marker, position)

            if win_check(gameBoard, player_2_marker):
                display_board(gameBoard)
                print('Congratulations Player 2, you won the game!')
                game_on = False
            else:
                if full_board_check(gameBoard):
                    display_board(gameBoard)
                    print('The game is a Draw')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break