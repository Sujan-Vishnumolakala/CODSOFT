print("Name : V.SUJAN")
print("")
print("Rules : ")
print("1.The game is to be played between two people (in this program between HUMAN and COMPUTER).")
print("2.One of the player chooses ‘O’ and the other ‘X’ to mark their respective cells.")
print("3.The game starts with one of the players and the game ends when one of the players has one whole row/ column/ diagonal filled with his/her respective character.")
print("‘O’ or ‘X’).")
print("4.If no one wins, then the game is said to be draw")
print(" ")

import random
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
def check_winner(board):
    for row in board:
        if row.count(row[0]) == 3 and row[0] != ' ':
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return True
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True
    return False
def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True
def get_user_move(board):
    while True:
        try:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
                return row, col
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
def get_computer_move(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                if check_winner(board):
                    board[i][j] = ' '
                    return i, j
                board[i][j] = ' '
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                if check_winner(board):
                    board[i][j] = 'O'
                    return i, j
                board[i][j] = ' '
    available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    return random.choice(available_moves)
def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    while True:
        print_board(board)
        if current_player == 'X':  
            row, col = get_user_move(board)
        else:  
            row, col = get_computer_move(board)
            print(f"Computer chooses: {row}, {col}")
        board[row][col] = current_player
        if check_winner(board):
            print_board(board)
            print(f"{current_player} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break
        else:
            current_player = 'O' if current_player == 'X' else 'X'
if __name__ == "__main__":
    main()
