#### The center of the board
if highlight_squares:
    for square in highlight_squares:
        x = board_offset_x + square[0] * square_size + square_size * 0.1  # Offset for inner perimeter
        y = board_offset_y + square[1] * square_size + square_size * 0.1  # Offset for inner perimeter
        size = square_size * 0.8  # Reduce size to fit inside the perimeter
        pygame.draw.rect(screen, 'yellow', [x, y, size, size], 3)  # Use a border width of 3

#### the perimeter of the board- but badly drawn
if highlight_squares:
    for square in highlight_squares:
        x = board_offset_x + square[0] * square_size + 2  # Slight offset from the left edge
        y = board_offset_y + square[1] * square_size + 2  # Slight offset from the top edge
        size = square_size - 4  # Reduce size to leave a small gap from the edges
        pygame.draw.rect(screen, 'yellow', [x, y, size, size], 3)  # Use a border width of 3


#### the perimeter of the board- luke warm
if highlight_squares:
    for square in highlight_squares:
        x = board_offset_x + square[0] * square_size + 3  # Slight offset from the left edge
        y = board_offset_y + square[1] * square_size + 3  # Slight offset from the top edge
        size = square_size - 6  # Reduce size to leave a small gap from the edges
        pygame.draw.rect(screen, 'yellow', [x, y, size, size], 3)  # Use a border width of 3who are thwe
        
 ###        
if highlight_squares:
    for square in highlight_squares:
        x = board_offset_x + square[0] * square_size + 3  # Offset from the left edge
        y = board_offset_y + square[1] * square_size + 3  # Offset from the top edge
        size = square_size - 6  # Reduce size to account for offsets on all sides
        pygame.draw.rect(screen, 'yellow', [x, y, size, size], 3)  # Use a border width of 3
        
if highlight_squares:
    for square in highlight_squares:
        x = board_offset_x + square[0] * square_size + 1.5  # Offset slightly inward from the left edge
        y = board_offset_y + square[1] * square_size + 1.5  # Offset slightly inward from the top edge
        size = square_size - 3  # Reduce size to account for offsets on all sides
        pygame.draw.rect(screen, 'yellow', [x, y, size, size], 2)  # Use a border width of 2
        
 # Step 2: Draw highlights
    if highlight_squares:
        for square in highlight_squares:
            x = board_offset_x + square[0] * square_size  # No offset from the left edge
            y = board_offset_y + square[1] * square_size  # No offset from the top edge
            size = square_size  # Full square size
            pygame.draw.rect(screen, 'yellow', [x + 2, y + 2, size - 4, size - 4], 3)  # Adjust for all sides


def evaluate_board():
    piece_values = {'pawn': 1.5, 'knight': 10, 'bishop': 20, 'rook': 50, 'queen': 200, 'king': 1000}
    center_squares = [(3, 3), (3, 4), (4, 3), (4, 4)]
    white_score = 0
    black_score = 0

    # Check if kings are still on the board
    if 'king' not in white_pieces:
        return float('-inf')  # White loses
    if 'king' not in black_pieces:
        return float('inf')  # Black loses

    # Piece values and pawn positioning
    white_score += sum(piece_values[piece] for piece in white_pieces)
    black_score += sum(piece_values[piece] for piece in black_pieces)
    white_score += sum(loc[1] * 0.1 for loc in white_locations if white_pieces[white_locations.index(loc)] == 'pawn')
    black_score += sum((7 - loc[1]) * 0.1 for loc in black_locations if black_pieces[black_locations.index(loc)] == 'pawn')

    # Captured pieces
    white_score += sum(piece_values[piece] for piece in captured_pieces_white)
    black_score += sum(piece_values[piece] for piece in captured_pieces_black)

    # Threats to opponent's pieces
    white_score += sum(piece_values[black_pieces[i]] for i, loc in enumerate(black_locations) if loc in [move for moves in white_options for move in moves])
    black_score += sum(piece_values[white_pieces[i]] for i, loc in enumerate(white_locations) if loc in [move for moves in black_options for move in moves])

    # King safety
    if 'king' in black_pieces:
        king_index = black_pieces.index('king')
        king_location = black_locations[king_index]
        if any(king_location in moves for moves in white_options):
            black_score -= 500  # Penalize leaving the king in danger
        else:
            black_score += 50  # Reward keeping the king safe
    if 'king' in white_pieces:
        white_king_index = white_pieces.index('king')
        white_king_location = white_locations[white_king_index]
        if any(white_king_location in moves for moves in black_options):
            black_score += 200  # Reward threatening the opponent's king

    # Control of the center
    white_score += sum(0.5 for loc in white_locations if loc in center_squares)
    black_score += sum(0.5 for loc in black_locations if loc in center_squares)

    # Piece mobility
    white_score += sum(len(moves) * 0.1 for moves in white_options)
    black_score += sum(len(moves) * 0.1 for moves in black_options)

    # Pawn structure
    white_pawn_columns = [loc[0] for loc in white_locations if white_pieces[white_locations.index(loc)] == 'pawn']
    black_pawn_columns = [loc[0] for loc in black_locations if black_pieces[black_locations.index(loc)] == 'pawn']
    white_score -= sum(0.2 for col in white_pawn_columns if white_pawn_columns.count(col) > 1)  # Penalize doubled pawns
    black_score -= sum(0.2 for col in black_pawn_columns if black_pawn_columns.count(col) > 1)  # Penalize doubled pawns

    return white_score - black_score


    else:  # Black's turn
        min_eval = float('inf')
        best_move = None
        for i, moves in enumerate(black_options):
            if not moves:
                continue
            for move in moves:
                # Simulate move
                original_position = black_locations[i]
                black_locations[i] = move
                captured_piece = None
                if move in white_locations:  # Check if a piece is captured
                    captured_index = white_locations.index(move)
                    captured_piece = white_pieces[captured_index]
                    white_pieces.pop(captured_index)
                    white_locations.pop(captured_index)

                eval, _ = minimax(depth + 1, True, alpha, beta)  # Increment depth

                # Undo move
                black_locations[i] = original_position
                if captured_piece:  # Restore captured piece
                    white_pieces.insert(captured_index, captured_piece)
                    white_locations.insert(captured_index, move)

                # Penalize losing this piece
                eval += piece_values[black_pieces[i]]

                if eval < min_eval:
                    min_eval = eval
                    best_move = (i, move)
                beta = min(beta, eval)
                if beta <= alpha:
                    break  # Prune the branch
        return min_eval, best_move