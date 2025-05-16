# Debug print to check the reset state
print(f"Game Reset: \nWhite Pieces: {white_pieces}\nWhite Locations: {white_locations}\n"
      f"Black Pieces: {black_pieces}\nBlack Locations: {black_locations}") is the error here yes or no?


if event.key == pygame.K_RETURN:
    game_over = False
    winner = ''
    white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                    'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
    white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                       (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
    black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                    'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
    black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                       (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
    captured_pieces_white = []
    captured_pieces_black = []
    turn_step = 0
    selection = 100
    valid_moves = []

    # Debug print to check the reset state
    print(f"Game Reset: \nWhite Pieces: {white_pieces}\nWhite Locations: {white_locations}\n"
          f"Black Pieces: {black_pieces}\nBlack Locations: {black_locations}") here yes or no?
