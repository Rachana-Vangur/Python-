matrix = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

game_on = True


def symbol_choice():
    choice = input("Enter the symbol you like (X or O)").upper()
    if choice == "X":
        print("You have choosen X \nand the other player is O\n")
        return "X"
    elif choice == "O":
        print("You have choosen O \nand the other player is X\n")
        return "O"
    else:
        print("Invalid symbol")
        exit()


def check_position(position, player_sym):
    while position not in range(1, 10):
        print("Position not in range. Try another position")
        exit()

    # ele[col][row]
    col = (position - 1) // 3
    row = (position - 1) % 3

    if matrix[col][row] == "X" or matrix[col][row] == "O":
        print("This position is already occupied")
        return

    else:
        matrix[col][row] = player_sym

    return 0


def check_match(player_sym):
    for i in range(0, 3):
        if all(cell == player_sym for cell in matrix[i]):
            return True

    i = 0
    if all(matrix[i][i] == player_sym for i in range(0, 3)):
        return True
    if all(matrix[j][i] == player_sym for j in range(0, 3)):
        return True
    if all(matrix[i][2 - i] == player_sym for i in range(0, 3)):
        return True

    return False


def flip_player(player_sym):
    if player_sym == "X":
        player_sym = "O"
    else:
        player_sym = "X"

    return player_sym


def board_complete():
    count = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if matrix[i][j] == "X" or matrix[i][j] == "O":
                count += 1
    if count == 9:
        return True
    return False


while game_on:

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            print(matrix[i][j], end=" ")
        print("\n")
    player_sym = symbol_choice()

    not_end = True
    while not_end:
        position = int(input("Enter the position you want to insert: \n"))
        check_position(position, player_sym)
        check_match(player_sym)

        # player_sym = flip_player(player_sym)

        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                print(matrix[i][j], end=" ")
            print("\n")
        if check_match(player_sym) == True:
            print(f"Player {player_sym} won the match")
            not_end = False

        player_sym = flip_player(player_sym)
        if board_complete():
            print("It is a TIE")
            break
    go_on = input("Do you want to play another game? (Y / N)").upper()
    if go_on == "N":
        game_on = False


print("Exiting the game")
