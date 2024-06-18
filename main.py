def print_board(board):
    """
    Function to print the current state of the tic-tac-toe board.

    Args:
    - board (list of lists): The 3x3 board represented as a list of lists.
      Each inner list represents a row of the board.

    Prints the board to the console in a visually appealing format.
    """
    for row in board:
        print(" | ".join(row))  # Print each row joined with "|"
        print("-" * 9)  # Print a line of dashes to separate rows


def is_board_full(board):
    """
    Function to check if the tic-tac-toe board is full (no empty spaces left).

    Args:
    - board (list of lists): The 3x3 board represented as a list of lists.

    Returns:
    - bool: True if the board is full (no empty spaces), False otherwise.
    """
    for row in board:
        if " " in row:  # If there is any empty space (" "), return False
            return False
    return True  # If no empty spaces found, return True


def check_win(board, player):
    """
    Function to check if the specified player has won the game.

    Args:
    - board (list of lists): The 3x3 board represented as a list of lists.
    - player (str): The player's symbol ('X' or 'O') to check for win.

    Returns:
    - bool: True if the player has won, False otherwise.
    """
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False  # If no win condition met, return False


def initialize_board():
    """
    Function to create and initialize a new 3x3 tic-tac-toe board.

    Returns:
    - list of lists: The initialized 3x3 board with empty spaces.
    """
    board = []
    for i in range(3):
        row = [" "] * 3  # Create a row with 3 empty spaces
        board.append(row)  # Add the row to the board
    return board


def make_move(board, slot, player):
    """
    Function to place a player's symbol ('X' or 'O') on the board at the specified slot.

    Args:
    - board (list of lists): The 3x3 board represented as a list of lists.
    - slot (int): The slot number (1 to 9) where the player wants to place their symbol.
    - player (str): The player's symbol ('X' or 'O') to place on the board.

    If the chosen slot is already taken, it prompts the player to enter another slot.
    """
    row = (slot - 1) // 3  # Calculate the row index based on the slot number
    col = (slot - 1) % 3  # Calculate the column index based on the slot number

    if board[row][col] == " ":  # If the slot is empty
        board[row][col] = player  # Place the player's symbol on the board
    else:
        # If the slot is already taken, prompt the player for another slot
        new_value = int(input("The number you chose is already taken. Please enter another number: "))
        row = (new_value - 1) // 3
        col = (new_value - 1) % 3
        board[row][col] = player  # Place the player's symbol on the new slot


def main():
    """
    Main function to run the tic-tac-toe game.
    """
    board = initialize_board()  # Initialize the board
    print_board(board)  # Print the initial empty board

    player_1 = "X"  # Player 1's symbol
    player_2 = "O"  # Player 2's symbol
    current_player = player_1  # Start with Player 1

    while not is_board_full(board):  # Continue while the board is not full
        slot = int(input(f"Player {current_player}, please enter a slot number from 1 to 9: "))
        make_move(board, slot, current_player)  # Make the current player's move
        print_board(board)  # Print the updated board after the move

        if check_win(board, current_player):  # Check if the current player has won
            print(f"Player {current_player} wins!")  # Print the win message
            break  # Exit the loop if there's a winner

        # Switch to the next player
        current_player = player_2 if current_player == player_1 else player_1

        if is_board_full(board) and not check_win(board, player_1) and not check_win(board, player_2):
            print("It's a draw!")  # If board is full and no one wins, it's a draw


if __name__ == "__main__":
    main()  # Run the game if this script is executed directly
