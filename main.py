




def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def initialize_board():
    # Create an empty list to hold the rows of the board
    board = []

    # Loop 3 times to create each row
    for i in range(3):
        # Create a row list with 3 empty strings
        row = []
        for j in range(3):
            row.append(" ")
        # Add the row to the board
        board.append(row)

    # Print the resulting board
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

    slot_1 = int(input("Player 1, you have 'X'. Please enter a slot number from 1 to 9 to place your 'X': "))
    make_move(board, slot_1, "X")
    print_board(board)
    slot_2 = int(input("Player 2, you have 'O'. Please enter a slot number from 1 to 9 to place your 'O': "))
    make_move(board, slot_2, "O")
    print_board(board)

print(main())
