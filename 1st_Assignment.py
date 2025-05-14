"""
Assignment 1: Tic-Tac-Toe Implementation
"""

def tic_tac_toe():
    board = [' ' for _ in range(9)]
    player = 'X'
    
    def check_win():
        # Check rows, columns, and diagonals
        win_positions = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), 
                        (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        for pos in win_positions:
            if board[pos[0]] == board[pos[1]] == board[pos[2]] != ' ':
                return True
        return False
    
    def print_board():
        for i in range(0, 9, 3):
            print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
            if i < 6: print("---------")
    
    while ' ' in board and not check_win():
        print_board()
        try:
            move = int(input(f"Player {player}, choose position (1-9): ")) - 1
            if 0 <= move < 9 and board[move] == ' ':
                board[move] = player
                player = 'O' if player == 'X' else 'X'
            else:
                print("Invalid move, try again.")
        except ValueError:
            print("Please enter a number.")
    
    print_board()
    if check_win():
        print(f"Player {('O' if player=='X' else 'X')} wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    tic_tac_toe()