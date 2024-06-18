def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True


def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def initialize_board():
    board = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(" ")
        board.append(row)
    return board


def make_move(board ,slot ,player,):
    row = (slot - 1) // 3
    col = (slot - 1) % 3
    if board[row][col] == " ":
        board[row][col] = player
    else:
        new_value = int(input("The number you chose is already taken. Please enter another number: "))
        row = (new_value - 1) // 3
        col = (new_value - 1) % 3
        board[row][col] = player


def main():
    board = initialize_board()
    print_board(board)

    player_1 = "X"
    player_2 = "O"
    current_player = player_1

    while not is_board_full(board):
        slot = int(input(f"Player {current_player}, please enter a slot number from 1 to 9: "))
        make_move(board, slot, current_player)
        print_board(board)

        if check_win(board, current_player):
            print(f"Player {current_player} wins!")
            break
        current_player = player_2 if current_player == player_1 else player_1
        if is_board_full(board) and not check_win(board, player_1) and not check_win(board, player_2):
            print("It's a draw!")


main()
