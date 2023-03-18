""" THIS GAME WORKS"""
def initialize_game():
    global winner
    global turn
    global numbers
    global row1
    global row2
    global row3

    winner = 0
    turn = 0
    numbers = [' ','1', '2', '3']
    row1 = ['a', '-', '-', '-']
    row2 = ['b', '-', '-', '-']
    row3 = ['c', '-', '-', '-']

    board = [numbers, row1, row2, row3]

    for x in board:
        print(x)


def which_player():
    global marker
    if turn % 2 == 0:
        marker = 'x'
    else:
        marker = 'o'


def get_choice():
    global coord
    coord = input('Where would you like to place your marker? Enter as coordinates (ex. a1.)')


def place_marker():
    row = coord[0]
    column = coord[1]
    if row == 'a':
        if column == '1':
            row1[1] = marker
        if column == '2':
            row1[2] = marker
        if column == '3':
            row1[3] = marker
    if row == 'b':
        if column == '1':
            row2[1] = marker
        if column == '2':
            row2[2] = marker
        if column == '3':
            row2[3] = marker
    if row == 'c':
        if column == '1':
            row3[1] = marker
        if column == '2':
            row3[2] = marker
        if column == '3':
            row3[3] = marker


def new_board():
    board = [numbers, row1, row2, row3]

    for x in board:
        print(x)


def check_winner():
    global winner
    if (row1[1] == row1[2] == row1[3] != '-') or (row2[1] == row2[2] == row2[3] != '-') or (row3[1] == row3[2] == row3[3] != '-') or (row1[1] == row2[1] == row3[1] != '-') or (row1[2] == row2[2] == row3[2] != '-') or (row1[3] == row2[3] == row3[3] != '-') or (row1[1] == row2[2] == row3[3] != '-') or (row1[3] == row2[2] == row3[1] != '-'):
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!WINNER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        winner = 1
        return winner


def execute_turn():
    global turn
    which_player()
    get_choice()
    place_marker()
    turn = turn + 1
    new_board()
    check_winner()
    """ """


def run_game():
    #global winner
    initialize_game()

    x = 0
    while x == 0:
        execute_turn()
        if winner == 1:
            x = 1


run_game()