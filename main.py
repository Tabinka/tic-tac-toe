import random


def print_game_board(values):
    print(f" {values[0][0]}  |  {values[0][1]}  |  {values[0][2]}")
    print(f" {values[1][0]}  |  {values[1][1]}  |  {values[1][2]}")
    print(f" {values[2][0]}  |  {values[2][1]}  |  {values[2][2]}")


def add_value(player_character):
    print("Where do you want to input your player model? Please write row (0-2) and column (0-2)")
    row = input("Row: ")
    column = input("Column: ")
    if game_values[int(row)][int(column)] == "":
        game_values[int(row)][int(column)] = player_character
    else:
        print("You can't do that")


def add_value_bot(bot_character):
    random_column = random.randint(0, 2)
    random_row = random.randint(0, 2)
    if game_values[random_column][random_row] == "":
        game_values[random_column][random_row] = bot_character
    else:
        add_value_bot(bot_character)


def check_values(game_values, player):
    for value in game_values:
        x = 0
        for column in value:
            if column == player:
                x = x + 1
            if x == 3:
                return False
    for row in range(0, 2):
        for column in range(0, 2):
            value = game_values[row][column]
            row_check = game_values[row - 1][column]
            second_row_check = game_values[row + 1][column]
            if value == row_check and value == second_row_check and value != "":
                return False
            elif ((value == game_values[0][2] and value == game_values[1][1] and value == game_values[2][0]) or (
                    value == game_values[0][0] and value == game_values[1][1] and value == game_values[2][
                2])) and value != "":
                return False
            if '' not in game_values[0] and '' not in game_values[1] and '' not in game_values[2]:
                return False
            elif value == "":
                return True
    return True


print("Project no. 3 - Tic Tac Toe Game")

game_values = [["", "", ""], ["", "", ""], ["", "", ""]]
players = []
game = True

mode = input("Do you want to play against bot or against another player? (Choose 1 - singleplayer, choose 2 - "
             "multiplayer) ")
player = input("Choose your player character: x or o ")
players.append(player)
if player == "x":
    players.append("o")
elif player == "o":
    players.append("x")
elif mode != "1" or mode != "2" or player != "x" or player != "o":
    print("Wrong input.")
    game = False

while game:
    bot_calc = 0
    for pl in players:
        bot_calc = bot_calc + 1
        print_game_board(game_values)
        print(f"{pl} is playing now")
        if mode == "1" and bot_calc == 2:
            add_value_bot(pl)
        else:
            add_value(pl)
        if not check_values(game_values, pl):
            print(f"{pl} wins")
            game = False
            break
