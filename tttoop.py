"""TIC TAC TOE using classes for the game board and players.  Additional functions were created outside of the classes for game functionality and may be handled differently in future itterations of this script"""

class Board:

    def __init__(self):

        self.spaces = ['*',' ',' ',' ',' ',' ',' ',' ',' ',' ']

    def displayboard(self):
        print('   |   |')
        print(' ' + self.spaces[7] + ' | ' + self.spaces[8] + ' | ' + self.spaces[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.spaces[4] + ' | ' + self.spaces[5] + ' | ' + self.spaces[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.spaces[1] + ' | ' + self.spaces[2] + ' | ' + self.spaces[3])
        print('   |   |')

    def openCheck(self,space):
        return (self.spaces[space] == ' ')

    def placeMarker(self,marker,space):
        self.spaces[space] = marker

    def winCheck(self,marker):
        wincombos = [(7, 8, 9), (4, 5, 6), (1, 2, 3), (7, 4, 1), (8, 5, 2), (9, 6, 3), (7, 5, 3), (9, 5, 1)]
        matches = []
        for combo in wincombos:
            if(self.spaces[combo[0]] == marker and self.spaces[combo[1]] == marker and self.spaces[combo[2]] == marker):
                matches.append('match')
            else:
                matches.append('no')
        return 'match' in matches

    def fullCheck(self):
        return ' ' not in self.spaces




class Player:

    def __init__(self,marker):
        self.marker = marker

    def __str__(self):
        return self.marker



#player select markers
def marker_select():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input("Player 1, would you like to be Xs or Os? ").upper()
    if marker == 'X':
       return Player('X'),Player('O')
    else:
        return Player('O'),Player('X')


#ramdomly decide who goes first
import random

def first_move():
    if random.randint(0,1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


#replay function
def replay():
    return input("Would you like to play again? type YES or NO ").lower().startswith('y')

#move selection

def move_selection(board):
    position = 0
    while position not in range (1,10) or not board.openCheck(position):
        position = int(input("Please select your next move: "))
    return position


"""GAME TIME"""

print('WELCOME TO TIC TAC TOE!')

while True:
    #initiate game board and players
    gameboard = Board()
    player1,player2 = marker_select()
    print('Player 1: {}'.format(player1.marker))
    print('Player 2: {}'.format(player2.marker))

    #determine who will go first
    turn = first_move()
    print('{} will go first'.format(turn))

    #initiate game on status
    playgame = input('Are you ready to play? type YES or NO').lower()
    if playgame[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            #player 1s turn
            print("Player 1's turn! ")
            gameboard.displayboard()
            position = move_selection(gameboard)
            gameboard.placeMarker(player1.marker,position)

        #check for win
            if gameboard.winCheck(player1.marker):
                gameboard.displayboard()
                print('Player 1 Wins')
                game_on = False
            else:
        #check for Draw
                if gameboard.fullCheck():
                    gameboard.displayboard()
                    print('The Game is a Draw!')
                    break
        #switch to player 2s turn
                else:
                    turn = 'Player 2'

        else:
            print("Player 2's turn! ")
            gameboard.displayboard()
            position = move_selection(gameboard)
            gameboard.placeMarker(player2.marker,position)

            if gameboard.winCheck(player2.marker):
                gameboard.displayboard()
                print("Player 2 Wins")
                game_on = False
            else:
                if gameboard.fullCheck():
                    gameboard.displayboard()
                    print('The Game is a Draw!')
                    break

                else:
                    turn = 'Player 1'

    if not replay():
        break

