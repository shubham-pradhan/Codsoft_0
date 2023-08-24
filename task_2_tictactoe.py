import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(cell == player for cell in board[i]) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(all(cell != " " for cell in row) for row in board)

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def minimax(board, depth, maximizing_player):
    if is_winner(board, "X"):
        return 1
    if is_winner(board, "O"):
        return -1
    if is_full(board):
        return 0

    if maximizing_player:
        max_eval = -float("inf")
        for i, j in get_empty_cells(board):
            board[i][j] = "X"
            eval = minimax(board, depth + 1, False)
            board[i][j] = " "
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float("inf")
        for i, j in get_empty_cells(board):
            board[i][j] = "O"
            eval = minimax(board, depth + 1, True)
            board[i][j] = " "
            min_eval = min(min_eval, eval)
        return min_eval

def get_best_move(board):
    best_eval = -float("inf")
    best_move = None
    for i, j in get_empty_cells(board):
        board[i][j] = "X"
        eval = minimax(board, 0, False)
        board[i][j] = " "
        if eval > best_eval:
            best_eval = eval
            best_move = (i, j)
    return best_move

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe!")

    while True:
        print_board(board)

        if is_full(board):
            print("It's a draw!")
            break

        player_row = int(input("Enter row (0, 1, 2): "))
        player_col = int(input("Enter column (0, 1, 2): "))
        
        if board[player_row][player_col] != " ":
            print("Invalid move. Cell is already occupied.")
            continue
        
        board[player_row][player_col] = "O"
        
        if is_winner(board, "O"):
            print_board(board)
            print("You win!")
            break
        
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        ai_row, ai_col = get_best_move(board)
        board[ai_row][ai_col] = "X"
        
        if is_winner(board, "X"):
            print_board(board)
            print("AI wins!")
            break

if __name__ == "__main__":
    main()
