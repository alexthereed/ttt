'''game of tic tac toe between two players'''

#display game board
def display_board(board):
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' ')
    print('   |   |   ')
    print('---|---|---')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' ')
    print('   |   |   ')
    print('---|---|---')
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' ')
    print('   |   |   ')


#function for player selection
def player_marker_select():
    marker = ''
    while not(marker =='X' or marker =='O'):
        marker = input("Player 1, would you like to be Xs or Os? ").upper()
    if marker == 'X':
        return 'X','O'
    else:
        return 'O','X'

#funtion to place players move on the game board
def place_marker(board,marker,position):
    board[position] = marker

#function to check if a player has won by getting three in a row
def win_check(board,marker):
    wincombos =[(7,8,9),(4,5,6),(1,2,3),(7,4,1),(8,5,2),(9,6,3),(7,5,3),(9,5,1)]
    matches = []
    for combo in wincombos:
        if(board[combo[0]] == marker and board[combo[1]] == marker and board[combo[2]] == marker):
           matches.append('match')
        else:
            matches.append('no')
    return ('match' in matches)


#function to randomly choose which player goes first
import random

def first_move():
    if random.randint(0,1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

#function to check if position on board is available
def free_space_check(board,position):
    return board[position] == ' '

#function to check if the game board is full
def full_check(board):
    return ' ' not in board


#function that allows a player to select their move and place their marker on the board
def move_select(board):
    position = 0
    while position not in range(1,10) or not free_space_check(board,position):
        position = int(input("Please make your next move "))
    return position

#fucntion to give the players the option to play again
def replay():
    return input('Would you like to play again? type YES or NO').lower().startswith('y')

'''GAME TIME'''

print('WELCOME TO TIC TAC TOE')
while True:
    #initialize game board
    game_board = ['*',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    #determine markers for both players
    player1_marker,player2_marker=player_marker_select()
    print('Player 1: {}'.format(player1_marker))
    print('Player 2: {}'.format(player2_marker))
    #pick who is going to go first
    turn = first_move()
    print('{} will go first'.format(turn))

    #prompt players if they are ready to play the game
    play_game = input("Are you ready to play? YES or NO: ").lower()
    if play_game[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        #player 1's turn
        if turn == 'Player 1':
            print("Player 1's turn")
            display_board(game_board)
            position = move_select(game_board)
            place_marker(game_board,player1_marker,position)

            #check for a win
            if win_check(game_board,player1_marker):
                display_board(game_board)
                print('Congratulations Player 1, you won the game!')
                game_on = False
            else:
                #check for a draw
                if full_check(game_board):
                    display_board(game_board)
                    print('The game is a draw')
                    break
                else:
                    #switch to player 2's turn
                    turn = 'Player 2'

        else:
            #player 2's turn
            print("Player 2's turn")
            display_board(game_board)
            position = move_select(game_board)
            place_marker(game_board,player2_marker,position)

            #check for a win
            if win_check(game_board,player2_marker):
                print("Congratulations Player 2, you won the game!")
                game_on = False
            else:
                #check for a draw
                if full_check(game_board):
                    display_board(game_board)
                    print('The game is a draw')
                    break
                else:
                    #switch to player 1's turn
                    turn = 'Player 1'
    #option to play again after game has been concluded
    if not replay():
        break