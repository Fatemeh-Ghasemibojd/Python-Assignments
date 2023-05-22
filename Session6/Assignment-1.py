def show():
    for row in game_board:
        for cell in row:
            print(cell, end="")
        print()

def check_win_player1():
     
    if game_board[0][0]=="x" and game_board[0][1]=="x" and game_board[0][2]=="x":
        print("player1 wins")
    elif game_board[1][0]=="x" and game_board[1][1]=="x" and game_board[1][2]=="x":
        print("player1 wins")
    elif game_board[2][0]=="x" and game_board[2][1]=="x" and game_board[2][2]=="x":
        print("player1 wins")
    elif game_board[0][0]=="x" and game_board[1][0]=="x" and game_board[2][0]=="x":
        print("player1 wins")
    elif game_board[0][1]=="x" and game_board[1][1]=="x" and game_board[2][1]=="x":
        print("player1 wins")
    elif game_board[0][2]=="x" and game_board[1][2]=="x" and game_board[2][2]=="x":
        print("player1 wins")
    elif game_board[0][0]=="x" and game_board[1][1]=="x" and game_board[2][2]=="x":
        print("player1 wins")
    elif  game_board[0][2]=="x" and game_board[1][1]=="x" and game_board[2][0]=="x":
        print("player1 wins")

          
def check_win_player2():
     
    if game_board[0][0]=="O" and game_board[0][1]=="O" and game_board[0][2]=="O":
        print("player2 wins")
    elif game_board[1][0]=="O" and game_board[1][1]=="O" and game_board[1][2]=="O":
        print("player2 wins")
    elif game_board[2][0]=="O" and game_board[2][1]=="O" and game_board[2][2]=="O":
        print("player2 wins")
    elif game_board[0][0]=="O" and game_board[1][0]=="O" and game_board[2][0]=="O":
        print("player2 wins")
    elif game_board[0][1]=="O" and game_board[1][1]=="O" and game_board[2][1]=="O":
        print("player2 wins")
    elif game_board[0][2]=="O" and game_board[1][2]=="O" and game_board[2][2]=="O":
        print("player2 wins")
    elif game_board[0][0]=="O" and game_board[1][1]=="O" and game_board[2][2]=="O":
        print("player2 wins")
    elif  game_board[0][2]=="O" and game_board[1][1]=="O" and game_board[2][0]=="O":
        print("player2 wins")


game_board = [["-","-","-"],
              ["-","-","-"],
              ["-","-","-"]]
show()

while True:
    print("player1")
    while True:
        row = int(input("Enter row: "))
        col = int(input("Enter col: "))
        if 0 <= row <= 2 and 0 <= col <= 2: 
            if game_board[row][col] == "-":
                game_board[row][col] = "X"
                break
            else:
                print("Select another cell")
        else:
            print("select in 0-2")
    show()
    check_win_player1()

    print("player2")
    while True:
        row = int(input("Enter row: "))
        col = int(input("Enter col: "))
        if 0 <= row <= 2 and 0 <= col <= 2:
            if game_board[row][col] == "-":
                game_board[row][col] = "O"
                break
            else:
                print("Select another cell")
        else:
            print("select in 0-2")
    show()
    check_win_player2()
