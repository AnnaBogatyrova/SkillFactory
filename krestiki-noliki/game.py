desk = []
playerX = "X"
playerO = "O"


def begin():
    print("""You are playing the famous game "Krestiki-Noliki"
    Each player need to try to make a line faster than opponent
     Have a luck!
     ----------------------------------------------------------""")
    global desk
    desk = [["-" for i in range(3)] for j in range(3)]
    desk.insert(0, [" ", "1", "2", "3"])
    for n in range(1, 4):
        desk[n].insert(0, n)
        desk[n].insert(4, "")


def print_desk():
    global desk
    print("The current state of desk is:")
    for i in range(4):
        print_value = desk[i]
        print(*print_value, sep=" | ")
        print("----------------")


def user_input(player):
    global desk
    print(f"Player {player} make your choice:\n")
    x = input("Choose the column - ")
    y = input("Choose the row - ")
    if not x.isdigit() or not y.isdigit():
        print("\nPlease enter only digits. Try again\n")
        return False
    else:
        x, y = int(x), int(y)
    if x in range(1, 4) and y in range(1, 4):
        if desk[y][x] == "-":
            desk[y][x] = player
            return True
        else:
            print("\nYou choose non empty cell.Try again\n")
            return False
    else:
        print("\nYou enter wrong adress.Try again\n")
        return False


def check_line(player):
    draw = 0
    for i in range(1, 4):
        if desk[i][1] == desk[i][2] == desk[i][3] == player or desk[1][i] == desk[2][i] == desk[3][i] == player:
            print(f"\n-----------------\nPlayer {player} win!\n-----------------\n")
            return True
        for j in range(1, 4):
            if desk[i][j] == "-":
                draw += 1
    if not draw:
        print("_________\n No steps forward! No one wins!\n___________")
        return True
    return False


def win_check(player):
    win = check_line(player)
    if win:
        return win
    elif desk[1][1] == desk[2][2] == desk[3][3] == player or desk[1][3] == desk[2][2] == desk[3][1] == player:
        print(f"\n-----------------\nPlayer {player} win!\n-----------------\n")
        win = True
        return win
    else:
        return win


def game():
    begin()
    turn = True
    win = False
    player = ""
    step = 1
    print_desk()
    while turn:
        if step % 2 == 0:
            player = playerO
        else:
            player = playerX
        turn = user_input(player)
        if turn:
            win = win_check(player)
            print("\n")
            print_desk()
            step += 1
            if win: turn = False
        else:
            turn = True


while True:
    game()
    if input("\n\n Enter 1 if you want to play again: \n") != "1":
        print("Goodbye!")
        break
