
import pygame




def generate_legal_moves(pieces, locations, turn):
    all_moves_list = check_options(pieces, locations, turn)
    all_moves = []
    for i, piece_moves in enumerate(all_moves_list):
        start_pos = locations[i]
        for end_pos in piece_moves:
            all_moves.append((start_pos[0], start_pos[1], end_pos[0], end_pos[1]))
    return all_moves


def apply_move(pieces, locations, move):
    from_x, from_y, to_x, to_y = move
    start = (from_x, from_y)
    end = (to_x, to_y)

    if start in locations:
        i = locations.index(start)
        # Capture if another piece is at the destination
        if end in locations:
            j = locations.index(end)
            del pieces[j]
            del locations[j]
            # Adjust index if deleted piece was before the moving one
            if j < i:
                i -= 1
        locations[i] = end

def game_over(pieces, locations):
    return 'king' not in pieces
