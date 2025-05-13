def explore_moves(board, depth):
    if depth == 0 or game_over(board):
        return evaluate(board)

    best_score = -infinity if current_player_is_maximizing(board) else infinity

    for move in generate_legal_moves(board):
        new_board = apply_move(board, move)
        score = explore_moves(new_board, depth - 1)

        if current_player_is_maximizing(board):
            best_score = max(best_score, score)
        else:
            best_score = min(best_score, score)

    return best_score

def evaluate_board(board):
    # This function scores the board from the AI's perspective.
    # You’ll fill this in later.
    return 0
def minimax(board, depth, maximizing_player):
    if depth == 0 or game_over(board):
        return evaluate_board(board)

    if maximizing_player:
        max_eval = float('-inf')
        for move in generate_legal_moves(board):
            new_board = apply_move(board, move)
            eval = minimax(new_board, depth - 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in generate_legal_moves(board):
            new_board = apply_move(board, move)
            eval = minimax(new_board, depth - 1, True)
            min_eval = min(min_eval, eval)
        return min_eval



def check_valid_moves():
    if turn_step < 2:
        print(f"Checking valid moves for White. Turn step: {turn_step}")
        options_list = white_options
    else:
        print(f"Checking valid moves for Black. Turn step: {turn_step}")
        options_list = black_options
    valid_options = options_list[selection]
    print(f"Valid moves for selection {selection}: {valid_options}")
    return valid_options

def check_valid_moves():
    if turn_step < 2:
        print(f"Checking valid moves for White. Turn step: {turn_step}")
        options_list = white_options
    else:
        print(f"Checking valid moves for Black. Turn step: {turn_step}")
        options_list = black_options
    valid_options = options_list[selection]
    print(f"Valid moves for selection {selection}: {valid_options}")
    return valid_options


if turn_step == 2:  # Black's turn
    print(f"Turn step before processing Black's turn: {turn_step}")
    _, best_move = minimax(depth=3, is_maximizing=True, white_pieces=white_pieces, white_locations=white_locations, black_pieces=black_pieces, black_locations=black_locations)
    
    if best_move:
        piece_index, move = best_move
        print(f"AI chose move: {best_move}")
        black_locations[piece_index] = move
        if move in white_locations:
            captured_index = white_locations.index(move)
            captured_piece = white_pieces.pop(captured_index)
            white_locations.pop(captured_index)
            captured_pieces_black.append(captured_piece)

        black_options = check_options(black_pieces, black_locations, 'black')
        white_options = check_options(white_pieces, white_locations, 'white')
        turn_step = 0  # Switch to White's turn
        print(f"Turn step after Black's move: {turn_step}")

    # Check if the game is over
    if game_is_over(white_pieces, black_pieces):
        print("Game over detected.")
        game_over = True
        break
    
    
if turn_step == 2:  # Black's turn
    print(f"Turn step before processing Black's turn: {turn_step}")
    _, best_move = minimax(depth=3, is_maximizing=True, white_pieces=white_pieces, white_locations=white_locations, black_pieces=black_pieces, black_locations=black_locations)
    
    if best_move:
        piece_index, move = best_move
        print(f"AI chose move: {best_move}")
        black_locations[piece_index] = move
        if move in white_locations:
            captured_index = white_locations.index(move)
            captured_piece = white_pieces.pop(captured_index)
            white_locations.pop(captured_index)
            captured_pieces_black.append(captured_piece)

        black_options = check_options(black_pieces, black_locations, 'black')
        white_options = check_options(white_pieces, white_locations, 'white')
        turn_step = 0  # Switch to White's turn
        print(f"Turn step after Black's move: {turn_step}")

    # Check if the game is over
    if game_is_over(white_pieces, black_pieces):
        print("Game over detected.")
        game_over = True
        break
    
    
    
    