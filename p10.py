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


####### Test code ########
elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
    mouse_x, mouse_y = event.pos
    print(f"Mouse clicked at: {mouse_x}, {mouse_y}")

    # Check if the click is within the board
    if (board_offset_x <= mouse_x <= board_offset_x + square_size * 8) and (board_offset_y <= mouse_y <= board_offset_y + square_size * 8):
        x_coord = (mouse_x - board_offset_x) // square_size
        y_coord = (mouse_y - board_offset_y) // square_size
        click_coords = (int(x_coord), int(y_coord))
        print(f"Click coordinates: {click_coords}")
        
elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
    mouse_x, mouse_y = event.pos
    print(f"Mouse clicked at: {mouse_x}, {mouse_y}")

    # Check if the click is within the board
    if (board_offset_x <= mouse_x <= board_offset_x + square_size * 8) and (board_offset_y <= mouse_y <= board_offset_y + square_size * 8):
        x_coord = (mouse_x - board_offset_x) // square_size
        y_coord = (mouse_y - board_offset_y) // square_size
        click_coords = (int(x_coord), int(y_coord))
        print(f"Click coordinates: {click_coords}")

if turn_step <= 1:  # White's turn
    print(f"Turn step before processing White's turn: {turn_step}")
    if click_coords in white_locations:  # Select a white piece
        selection = white_locations.index(click_coords)
        valid_moves = check_valid_moves()  # Get valid moves for the selected piece
        print(f"Valid moves for selected piece: {valid_moves}")
        if turn_step == 0:
            turn_step = 1  # Move to "select destination" step
            print(f"Turn step updated to: {turn_step}")
    elif click_coords in valid_moves and selection != 100:  # Move the selected piece
        white_locations[selection] = click_coords
        print(f"White moved piece to: {click_coords}")
        if click_coords in black_locations:  # Capture a black piece
            black_piece = black_locations.index(click_coords)
            captured_pieces_white.append(black_pieces[black_piece])
            if black_pieces[black_piece] == 'king':  # Check for game over
                winner = 'white'
            black_pieces.pop(black_piece)
            black_locations.pop(black_piece)
        # Update valid moves and switch turn
        black_options = check_options(black_pieces, black_locations, 'black')
        white_options = check_options(white_pieces, white_locations, 'white')
        turn_step = 2  # Switch to Black's turn
        print(f"Turn step after White's move: {turn_step}")
        selection = 100
        valid_moves = []
        
if turn_step <= 1:  # White's turn
    print(f"Turn step before processing White's turn: {turn_step}")
    if click_coords in white_locations:  # Select a white piece
        selection = white_locations.index(click_coords)
        valid_moves = check_valid_moves()  # Get valid moves for the selected piece
        print(f"Valid moves for selected piece: {valid_moves}")
        if turn_step == 0:
            turn_step = 1  # Move to "select destination" step
            print(f"Turn step updated to: {turn_step}")
    elif click_coords in valid_moves and selection != 100:  # Move the selected piece
        white_locations[selection] = click_coords
        print(f"White moved piece to: {click_coords}")
        if click_coords in black_locations:  # Capture a black piece
            black_piece = black_locations.index(click_coords)
            captured_pieces_white.append(black_pieces[black_piece])
            if black_pieces[black_piece] == 'king':  # Check for game over
                winner = 'white'
            black_pieces.pop(black_piece)
            black_locations.pop(black_piece)
        # Update valid moves and switch turn
        black_options = check_options(black_pieces, black_locations, 'black')
        white_options = check_options(white_pieces, white_locations, 'white')
        turn_step = 2  # Switch to Black's turn
        print(f"Turn step after White's move: {turn_step}")
        selection = 100
        valid_moves = []
        
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
####### Test code ########