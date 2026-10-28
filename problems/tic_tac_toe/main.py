def display_board(board):
    print()
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print()

def check_winners(board, players):
    winning_positions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for positions in winning_positions:
        if (board[positions[0]] == players and 
            board[positions[1]] == players and
            board[positions[2]] == players):
            return True

    return False

board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
players = "X"
moves = 0

print("===== Tic-Tac-Toe =====")
print("Enter a position from 1 to 9 to place your makr.")


while True:
    display_board(board)

    positions = int(input("Player " + players + ", choose a position (1-9): "))

    if positions < 1 or positions > 9:
        print("Invalid position. Choose a number from 1 to 9.")
        continue

    if board[positions - 1] == "X" or board[positions - 1] == "O":
        print("That position is already occupied. Try again.")
        continue

    board[positions - 1] = players
    moves = moves + 1

    if check_winners(board, players):
        display_board(board)
        print("Player", players, "wins!")
        break

    if moves == 9:
        display_board(board)
        print("It's a draw!")
        break

    if players == "X":
        players = "O"
    else:
        players = "X"