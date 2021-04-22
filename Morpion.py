from copy import copy
import random
#Globals variables
BOARD_EMPTY = [['_','_','_'],['_','_','_'],['_','_','_']]
PLAYER_MARK = 'X'
IA_MARK = 'O'
NULL_PLAYER_MARK = '_'

board = [['_','_','_'],['_','_','_'],['_','_','_']]

def main():
    launch_game()

def launch_game():
    init_game()
    playing = True
    while playing:
        playing = play()

def play():
    player_play()
    IA_play()
    display_board()
    return True


def player_play():
    while not try_to_make_a_move(ask_player_action(), PLAYER_MARK):
        pass
    check_victory()

def IA_play():
    #-1 because matrix start at 0
    while try_to_make_a_move(random.randint(0,8), IA_MARK) == False:
        pass
    check_victory()


def init_game():
    global board
    board = copy(BOARD_EMPTY)
    display_board()


def display_board():
    for i in reversed(range(0,3)):
        print(board[i])

def ask_player_action():
    false_to_pass = True
    while false_to_pass:
        player_coordinate = int(input('Où voulez vous jouer ? Servez vous de votre clavier numérique (1 pour en bas à gauche, 5 pour le centre) :'))
        #Check if correct move
        if 1 <= player_coordinate <= 9 :
            false_to_pass = False
    #-1 because matrix start at 0
    return player_coordinate-1


def try_to_make_a_move(position, player_mark):
    global board
    x = position//3
    y = position%3
    if board[x][y] == NULL_PLAYER_MARK:
        board[x][y] = player_mark
        return True
    print('Emplacement occupé, choisissez une autre position. ')
    return False

def check_victory():
    size_matrix = 2
    for i in range(0, size_matrix):
        for j in range(0,size_matrix):
            #horizontal and vertical victory
            if i != 0 and i != size_matrix:
                if board[i][j] == board[i+1][j] == board[i-1][j] and board[i][j] != NULL_PLAYER_MARK:
                    Victory(board[i][j])
                pass
            if j != 0 and j != size_matrix:
                if board[i][j] == board[i][j-1] == board[i][j+1] and board[i][j] != NULL_PLAYER_MARK:
                    Victory(board[i][j])
                    pass
                pass
            #diagonal victory
            if i!=0 and j!=0 and i!=size_matrix and j!=size_matrix:
                if board[i][j] == board[i-1][j-1] == board[i+1][j+1] or board[i][j] == board[i-1][j+1] == board[i+1][j-1] and board[i][j] != NULL_PLAYER_MARK:
                    Victory(board[i][j])
                    pass
            pass

    pass


def Victory(mark):
    display_board()
    if mark == PLAYER_MARK:
        print('Victoire du joueur !')
    else:
        print('Défaite, l\' ordinateur a gagné')
    exit()

main()
