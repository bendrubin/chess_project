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
