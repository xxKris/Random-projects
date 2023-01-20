import os

# The Tic-Tac-Toe board
board = [" " for x in range(9)]

# The player's marker
player = "X"

# The winning combinations
winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

# The game loop
while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("""
    Tic-Tac-Toe
    ==========
    0 | 1 | 2
    ---------
    3 | 4 | 5
    ---------
    6 | 7 | 8
    """)
    print("Player {}'s turn.".format(player))
    print("\n".join(" ".join(board[i:i+3]) for i in range(0, len(board), 3)))
    choice = int(input("Choose a spot: "))
    if board[choice] == " ":
        board[choice] = player
    else:
        print("That spot is taken. Try again.")
        continue
    for x, y, z in winning_combinations:
        if board[x] == board[y] == board[z] and board[x] != " ":
            print("Player {} wins!".format(player))
            exit()
    if "_" not in board:
        print("It's a tie!")
        exit()
    if player == "X":
        player = "O"
    else:
        player = "X"
