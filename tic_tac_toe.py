board = {i: ' ' for i in range(1, 10)}

def print_board():
    print(f"{board[1]}|{board[2]}|{board[3]}")
    print("-+-+-")
    print(f"{board[4]}|{board[5]}|{board[6]}")
    print("-+-+-")
    print(f"{board[7]}|{board[8]}|{board[9]}\n")

def is_space_free(pos):
    return board[pos] == ' '

def check_win():
    win_conditions = [
        (1,2,3), (4,5,6), (7,8,9),   # Rows
        (1,4,7), (2,5,8), (3,6,9),   # Columns
        (1,5,9), (3,5,7)             # Diagonals
    ]
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] != ' ':
            return True
    return False

def check_draw():
    return all(space != ' ' for space in board.values())

def insert_letter(letter, position):
    if is_space_free(position):
        board[position] = letter
        print_board()
        if check_win():
            print(f"{'Bot' if letter == 'X' else 'You'} wins!")
            return True
        elif check_draw():
            print("Draw!")
            return True
        return False
    else:
        print("Position taken, please pick a different position.")
        return False

def player_move():
    while True:
        try:
            position = int(input("Enter position for O (1-9): "))
            if position in board and insert_letter('O', position):
                return True
            elif position in board:
                return False
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def comp_move():
    best_score = -float('inf')
    best_move = None

    for key in board.keys():
        if board[key] == ' ':
            board[key] = 'X'
            score = minimax(False)
            board[key] = ' '
            if score > best_score:
                best_score = score
                best_move = key

    insert_letter('X', best_move)

def minimax(is_maximizing):
    if check_win():
        return 1 if not is_maximizing else -1
    if check_draw():
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for key in board.keys():
            if board[key] == ' ':
                board[key] = 'X'
                score = minimax(False)
                board[key] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for key in board.keys():
            if board[key] == ' ':
                board[key] = 'O'
                score = minimax(True)
                board[key] = ' '
                best_score = min(score, best_score)
        return best_score

def play_game():
    print_board()
    while True:
        comp_move()
        if check_win() or check_draw():
            break
        if player_move():
            break

if __name__ == "__main__":
    play_game()
