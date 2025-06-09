# Day 25
# Project-25 = The Tic-Tac-Toe Game Project
def create_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def print_board(b):
    print("\n  1   2   3")  # column headers
    for i, row in enumerate(b, start=1):
        print(i, " | ".join(row))
        if i < 3:
            print("  " + "---+---+---")

def check_winner(b, player):
    # Rows, columns, diagonals
    return any(all(cell == player for cell in row) for row in b) or \
           any(all(b[r][c] == player for r in range(3)) for c in range(3)) or \
           all(b[i][i] == player for i in range(3)) or \
           all(b[i][2-i] == player for i in range(3))

def board_full(b):
    return all(cell != " " for row in b for cell in row)

def tic_tac_toe():
    board = create_board()
    current = "X"
    while True:
        print_board(board)
        move = input(f"Player {current}, enter row and col (e.g. 2 3), or 'q' to quit: ").split()
        if not move:
            continue
        if move[0].lower() == "q":
            print("Game aborted.")
            return

        if len(move) != 2 or not all(m.isdigit() for m in move):
            print("Invalid input. Use two numbers 1–3.")
            continue

        r, c = map(int, move)
        if not (1 <= r <= 3 and 1 <= c <= 3):
            print("Row and column must be 1, 2, or 3.")
            continue
        if board[r-1][c-1] != " ":
            print("That cell is already occupied.")
            continue

        board[r-1][c-1] = current

        if check_winner(board, current):
            print_board(board)
            print(f"🎉 Player {current} wins!")
            return
        if board_full(board):
            print_board(board)
            print("🤝 It's a draw!")
            return

        current = "O" if current == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
