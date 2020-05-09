import random

board_list = [1,2,3,4,5,6,7,8,9]

def gameboard():
    k = 0
    print("\n")
    for i in range(1, 4):
        for j in range(2):
            if (board_list[k] == 'X' or board_list[k] == 'O'):
                print(f" {board_list[k]} |", end="")
            else:
                print("   |", end="")
            k += 1
        
        if (board_list[k] == 'X' or board_list[k] == 'O'):
            print(f" {board_list[k]} ")
        else:
            print("   ")
        k += 1

        if not (i % 3 == 0):
            print("--- --- ---")
    print("\n")

def turn_available():
    temp_lst = board_list.copy()
    xvalues = temp_lst.count('X')
    ovalues = temp_lst.count('O')

    if xvalues > 0:
        while not (xvalues == 0):
            temp_lst.remove('X')
            xvalues -= 1
    if ovalues > 0:
        while not (ovalues == 0):
            temp_lst.remove("O")
            ovalues -= 1
    return temp_lst

def winner_P():
    if board_list[0] == 'X' and board_list[1] == 'X' and board_list[2] == 'X':
        return True
    elif board_list[3] == 'X' and board_list[4] == 'X' and board_list[5] == 'X':
        return True
    elif board_list[6] == 'X' and board_list[7] == 'X' and board_list[8] == 'X':
        return True
    elif board_list[0] == 'X' and board_list[3] == 'X' and board_list[6] == 'X':
        return True
    elif board_list[1] == 'X' and board_list[4] == 'X' and board_list[7] == 'X':
        return True
    elif board_list[2] == 'X' and board_list[5] == 'X' and board_list[8] == 'X':
        return True
    elif board_list[0] == 'X' and board_list[4] == 'X' and board_list[8] == 'X':
        return True
    elif board_list[2] == 'X' and board_list[4] == 'X' and board_list[6] == 'X':
        return True
    else:
       return False

def winner_C():
    if board_list[0] == 'O' and board_list[1] == 'O' and board_list[2] == 'O':
        return True
    elif board_list[3] == 'O' and board_list[4] == 'O' and board_list[5] == 'O':
        return True
    elif board_list[6] == 'O' and board_list[7] == 'O' and board_list[8] == 'O':
        return True
    elif board_list[0] == 'O' and board_list[3] == 'O' and board_list[6] == 'O':
        return True
    elif board_list[1] == 'O' and board_list[4] == 'O' and board_list[7] == 'O':
        return True
    elif board_list[2] == 'O' and board_list[5] == 'O' and board_list[8] == 'O':
        return True
    elif board_list[0] == 'O' and board_list[4] == 'O' and board_list[8] == 'O':
        return True
    elif board_list[2] == 'O' and board_list[4] == 'O' and board_list[6] == 'O':
        return True
    else:
        return False
    
def turn(p1, p2):
    turn = int(input(f"{player1} make a turn: "))
    while not (turn in board_list):
        turn = int(input(f"Choose empty spot: {player1} make a turn: "))
    board_list[turn-1] = 'X'
    game_over = winner_P()   #to check if player 1 win the game
    if (game_over == True):
        gameboard()
        print(f"WINNER is ..... {p1}")

    temp_lst = turn_available()
    if len(temp_lst) > 0 and game_over == False:
        turn = random.choice(temp_lst)
        board_list[turn-1] = 'O'
        game_over = winner_C()

        if (game_over == True):
            gameboard()
            print(f"WINNER is ..... {p2}")

    return game_over

def play(p1, p2):
    gameboard()
    game_over = False
    temp_lst = turn_available()
    turn_count = len(temp_lst)

    while (turn_count > 0 and game_over == False):
        game_over = turn(p1, p2)

        if game_over == False:
            gameboard()
            temp_lst = turn_available()
            turn_count = len(temp_lst)

    if turn_count == 0 and game_over == False:
        print("Game is TIE.....")

##################### MAIN GAME AREA ##################

print("\n\n === WELCOME TO TIC TAC TOE === \n\n")
player1 = input("Enter your name: ")
player2 = "Computer"

print(f"\nPlayer 1 is \"{player1}\" and Player 2 is \"{player2}\"\n")

play(player1, player2)

