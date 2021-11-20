import random
bord = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-", ]
game_still_going = True
winner = None
x_or_o = ["X",  "O"]
random_num = random.randint(0, 1)
random_player = x_or_o[random_num]
current_player = random_player


def display_bord():
    print(bord[0] + "|" + bord[1] + "|" + bord[2])
    print(bord[3] + "|" + bord[4] + "|" + bord[5])
    print(bord[6] + "|" + bord[7] + "|" + bord[8])


def play_game():

    display_bord()

    while game_still_going:

        handle_turn(current_player)

        check_if_game_over()

        flip_player()

    if winner == "X" or winner == "O":
        print(f'the winner is {winner}')
    elif winner is None:
        print("Tie.")


def handle_turn(player):
    print(player + ' turn.')
    position = input("choose a position from 1-9: ")

    valid = False
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input, choose a position from 1-9: ")

        position = int(position) - 1
        if bord[position] == "-":
            valid = True
        else:
            print("You cant go there. Go again.")

    bord[position] = player
    display_bord()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():
    global winner

    row_winner = check_rows()

    column_winner = check_columns()

    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return


def check_rows():
    global game_still_going

    row_1 = bord[0] == bord[1] == bord[2] != "-"
    row_2 = bord[3] == bord[4] == bord[5] != "-"
    row_3 = bord[6] == bord[7] == bord[8] != "-"
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return bord[0]
    elif row_2:
        return bord[3]
    elif row_3:
        return bord[6]
    return


def check_columns():
    global game_still_going

    column_1 = bord[0] == bord[3] == bord[6] != "-"
    column_2 = bord[1] == bord[4] == bord[7] != "-"
    column_3 = bord[2] == bord[5] == bord[8] != "-"
    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return bord[0]
    elif column_2:
        return bord[1]
    elif column_3:
        return bord[2]
    return


def check_diagonals():
    global game_still_going

    diagonals_1 = bord[0] == bord[4] == bord[8] != "-"
    diagonals_2 = bord[6] == bord[4] == bord[2] != "-"
    if diagonals_1 or diagonals_2:
        game_still_going = False
    if diagonals_1:
        return bord[0]
    elif diagonals_2:
        return bord[6]

    return


def check_if_tie():
    global game_still_going
    if "-" not in bord:
        game_still_going = False
    return


def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return


play_game()
