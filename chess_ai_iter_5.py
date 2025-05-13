### PART 1:
import pygame

# Initialize Pygame
pygame.init()

# Set up the screen with an initial default size and make it resizable
WIDTH, HEIGHT = 800, 800
SIDE_PANEL_WIDTH = int(WIDTH * 0.25)  # 25% of total width
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Resizable Chessboard")

# Fonts (keep them defined as needed)
font = pygame.font.Font('freesansbold.ttf', 20)
medium_font = pygame.font.Font('freesansbold.ttf', 40)
big_font = pygame.font.Font('freesansbold.ttf', 50)

# Setup for game loop
timer = pygame.time.Clock()
fps = 60

### PART 2: # game variables and images

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

# 0 - whites turn no selection: 1-whites turn piece selected: 
# 2- black turn no selection, 3 - black turn piece selected
# Turn and game state
turn_step = 0  # 0: White's turn, no selection; 1: White's turn, piece selected; etc.
print(f"Turn step at start of loop: {turn_step}")
selection = 100  # No piece selected
valid_moves = []  # No valid moves initially
winner = ''  # No winner at the start
game_over = False  # Game is not over

# Move tracking
max_moves = 12  # Set a maximum number of moves to prevent infinite loops
move_count = 0  # Initialize move counter

# Board dimensions
board_area_width = int(WIDTH * 0.75)
square_size = min(board_area_width // 8, (HEIGHT - 100) // 8)
piece_size = square_size * 0.8
board_offset_x = 0
board_offset_y = (HEIGHT - 100 - (square_size * 8)) // 2



# Placeholder for move options
black_options = []  # Will be initialized later
white_options = []  # Will be initialized later
# Counter for animations
counter = 0

### PART 3: # load in game piece images 

black_queen = pygame.image.load(r'C:\Users\benjy\OneDrive\Desktop\py_pro\black queen.png')
black_queen = pygame.transform.scale(black_queen, (80, 80))
black_queen_small = pygame.transform.scale(black_queen, (45, 45))

black_king = pygame.image.load(r'C:\Users\benjy\OneDrive\Desktop\py_pro\black king.png')
black_king = pygame.transform.scale(black_king, (80, 80))
black_king_small = pygame.transform.scale(black_king, (45, 45))

black_bishop = pygame.image.load(r'C:\Users\benjy\OneDrive\Desktop\py_pro\black bishop.png')
black_bishop = pygame.transform.scale(black_bishop, (80, 80))
black_bishop_small = pygame.transform.scale(black_bishop, (45, 45))

black_knight = pygame.image.load(r'C:\Users\benjy\OneDrive\Desktop\py_pro\black knight.png')
black_knight = pygame.transform.scale(black_knight, (80, 80))
black_knight_small = pygame.transform.scale(black_knight, (45, 45))

black_rook = pygame.image.load(r'C:\Users\benjy\OneDrive\Desktop\py_pro\black rook.png')
black_rook = pygame.transform.scale(black_rook, (80, 80))
black_rook_small = pygame.transform.scale(black_rook, (45, 45))

black_pawn = pygame.image.load(r'C:\Users\benjy\OneDrive\Desktop\py_pro\black pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (65, 65))
black_pawn_small = pygame.transform.scale(black_pawn, (45, 45))

white_queen = pygame.image.load(r'C:\Users\benjy\OneDrive\Desktop\py_pro\white queen.png')
white_queen = pygame.transform.scale(white_queen, (80, 80))
white_queen_small = pygame.transform.scale(white_queen, (45, 45))

white_king = pygame.image.load(r'C:\Users\benjy\OneDrive\Desktop\py_pro\white king.png')
white_king = pygame.transform.scale(white_king, (80, 80))
white_king_small = pygame.transform.scale(white_king, (45, 45))

white_bishop = pygame.image.load(r'C:\Users\benjy\OneDrive\Desktop\py_pro\white bishop.png')
white_bishop = pygame.transform.scale(white_bishop, (80, 80))
white_bishop_small = pygame.transform.scale(white_bishop, (45, 45))

white_knight = pygame.image.load(r'C:\Users\benjy\OneDrive\Desktop\py_pro\white knight.png')
white_knight = pygame.transform.scale(white_knight, (80, 80))
white_knight_small = pygame.transform.scale(white_knight, (45, 45))

white_rook = pygame.image.load(r'C:\Users\benjy\OneDrive\Desktop\py_pro\white rook.png')
white_rook = pygame.transform.scale(white_rook, (80, 80))
white_rook_small = pygame.transform.scale(white_rook, (45, 45))

white_pawn = pygame.image.load(r'C:\Users\benjy\OneDrive\Desktop\py_pro\white pawn.png')
white_pawn = pygame.transform.scale(white_pawn, (65, 65))
white_pawn_small = pygame.transform.scale(white_pawn, (45, 45))

white_images = [white_pawn, white_queen, white_king, white_knight, 
white_rook, white_bishop]
small_white_images = [white_pawn_small, white_queen_small, white_king_small, 
white_knight_small, white_rook_small, white_bishop_small]
black_images = [black_pawn, black_queen, black_king, black_knight, 
black_rook, black_bishop]
small_black_images = [black_pawn_small, black_queen_small, black_king_small, 
black_knight_small, black_rook_small, black_bishop_small]

piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']

counter = 0
winner = ''
game_over = False


### PART 4: (resizing with side panel)

def draw_board(square_size, board_offset_x, board_offset_y, width, height, turn_step):
    print(f"Rendering status text for turn_step: {turn_step}")
    # Calculate font size based on window size
    font_size = max(int(height * 0.03), 24)  # Adjust font size dynamically
    big_font = pygame.font.Font(None, font_size)  # Update the font size
    medium_font = pygame.font.Font(None, font_size // 2)  # For the forfeit button    
    
    # Draw main board squares
    for row in range(8):
        for col in range(8):
            color = 'light gray' if (row + col) % 2 == 0 else 'dark gray'
            pygame.draw.rect(screen, color, 
                [board_offset_x + col * square_size, board_offset_y + row * square_size, square_size, square_size])

    # Draw grid lines
    for i in range(9):
        pygame.draw.line(screen, 'black', 
            (board_offset_x + i * square_size, board_offset_y), 
            (board_offset_x + i * square_size, board_offset_y + 8 * square_size), 2)
        pygame.draw.line(screen, 'black', 
            (board_offset_x, board_offset_y + i * square_size), 
            (board_offset_x + 8 * square_size, board_offset_y + i * square_size), 2)

    # Draw bottom panel
    pygame.draw.rect(screen, 'gray', [0, height - 100, width, 100])
    pygame.draw.rect(screen, 'gold', [0, height - 100, width, 100], 5)

    # Draw right side panel
    pygame.draw.rect(screen, 'gold', [board_offset_x + 8 * square_size, 0, width - (board_offset_x + 8 * square_size), height], 5)

    # Draw status text
    status_text = ['White: Select a Piece to Move!', 'White: Select a Destination!',
                   'Black: Select a Piece to Move!', 'Black: Select a Destination!']
    screen.blit(big_font.render(status_text[turn_step], True, 'black'), (20, height - 80))
    print(f"Rendering status text for turn_step: {turn_step}")



# draw pieces on the board

# Images for white and black pieces
white_images = [white_pawn, white_queen, white_king, white_knight, 
                white_rook, white_bishop]
black_images = [black_pawn, black_queen, black_king, black_knight, 
                black_rook, black_bishop]

# List of piece names (for indexing)
piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']

counter = 0
winner = ''
game_over = False

# draw main game board
### PART 5: drawing the pieces. 

# Function to draw the pieces on the main board
def draw_pieces(square_size, piece_size, board_offset_x, board_offset_y):
    print(f"Drawing pieces: White - {white_locations}, Black - {black_locations}")
    # Draw white pieces
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        piece_image = pygame.transform.scale(white_images[index], (int(piece_size), int(piece_size)))
        screen.blit(piece_image, (board_offset_x + white_locations[i][0] * square_size + (square_size - piece_size) // 2,
                                  board_offset_y + white_locations[i][1] * square_size + (square_size - piece_size) // 2))

    # Draw black pieces
    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        piece_image = pygame.transform.scale(black_images[index], (int(piece_size), int(piece_size)))
        screen.blit(piece_image, (board_offset_x + black_locations[i][0] * square_size + (square_size - piece_size) // 2,
                                  board_offset_y + black_locations[i][1] * square_size + (square_size - piece_size) // 2))

    # Draw captured pieces (white and black) in the captured area
    draw_captured(square_size, piece_size, board_offset_x, board_offset_y, WIDTH, HEIGHT)

    # Handle red and blue dots (valid moves and selected pieces)
    if selection != 100:  # Assuming selection holds the index of the selected piece
        valid_moves = check_valid_moves()  # This will return a list of valid moves
        for move in valid_moves:
            move_x, move_y = move
            pygame.draw.circle(screen, 'red', (board_offset_x + move_x * square_size + square_size // 2, 
                                                board_offset_y + move_y * square_size + square_size // 2), piece_size // 6)
        
    if turn_step >= 2:  # Check if it's time to highlight the selected piece (based on your turn logic)
        print(f"Rendering status text for turn_step: {turn_step}")
        if selection != 100:
            pygame.draw.rect(screen, 'blue', [board_offset_x + white_locations[selection][0] * square_size + (square_size - piece_size) // 2,
                                              board_offset_y + white_locations[selection][1] * square_size + (square_size - piece_size) // 2,
                                              piece_size, piece_size], 2)




### PART 6:
# checking all valid pieces on the board
def check_options(pieces, locations, turn):
    moves_list = []
    all_moves_list = []
    for i in range(len(pieces)):
        location = locations[i]
        piece = pieces[i]

        # Validate location
        if location is None:
            print(f"Invalid location for piece {piece} at index {i}: {location}")
            continue

        if piece == 'pawn':
            moves_list = check_pawn(location, turn)
        elif piece == 'rook':
            moves_list = check_rook(location, turn)
        elif piece == 'bishop':
            moves_list = check_bishop(location, turn)
        elif piece == 'knight':
            moves_list = check_knight(location, turn)
        elif piece == 'king':
            moves_list = check_king(location, turn)
        elif piece == 'queen':
            moves_list = check_queen(location, turn)
        all_moves_list.append(moves_list)
    print(f"Options for {turn}: {all_moves_list}")
    return all_moves_list

### PART 7:
# checking all valid moves for king
def check_king(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    # 8 squares to check for kings, they can go one square any direction
    targets = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list

### PART 8:
# check queen valid moves
def check_queen(position, color):
    moves_list = check_bishop(position, color)
    second_list = check_rook(position, color)
    for i in range(len(second_list)):
        moves_list.append(second_list[i])
    return moves_list

### PART 9:
# checking all valid moves for pawn

def check_pawn(position, color):
    moves_list = []
    if color == 'white':
        # Move forward one step
        if (position[0], position[1] + 1) not in white_locations and \
            (position[0], position[1] + 1) not in black_locations and position[1] < 7:
            moves_list.append((position[0], position[1] + 1))
        # Move forward two steps if on starting position
        if (position[0], position[1] + 2) not in white_locations and \
            (position[0], position[1] + 2) not in black_locations and position[1] == 1:
            moves_list.append((position[0], position[1] + 2))
        # Capture diagonally right
        if (position[0] + 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] + 1, position[1] + 1))
        # Capture diagonally left
        if (position[0] - 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] - 1, position[1] + 1))

    else:  # color == 'black'
        # Move forward one step
        if (position[0], position[1] - 1) not in white_locations and \
            (position[0], position[1] - 1) not in black_locations and position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
        # Move forward two steps if on starting position
        if (position[0], position[1] - 2) not in white_locations and \
            (position[0], position[1] - 2) not in black_locations and position[1] == 6:
            moves_list.append((position[0], position[1] - 2))
        # Capture diagonally right
        if (position[0] + 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] + 1, position[1] - 1))
        # Capture diagonally left
        if (position[0] - 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] - 1, position[1] - 1))
    return moves_list

### PART 10
# valide moves for bishop
def check_bishop(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    for i in range(4):  # up-right, up-left, down-right, down-left
        path = True
        chain = 1
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list
### PART 11:
# checking all valid moves for rook
def check_rook(position, color):
        moves_list = []
        if color == 'white':
            enemies_list = black_locations
            friends_list = white_locations
        else:
            friends_list = black_locations
            enemies_list = white_locations
        for i in range(4):  # down, up, right, left
            path = True
            chain = 1
            if i == 0:
                x = 0
                y = 1
            elif i == 1:
                x = 0
                y = -1
            elif i == 2:
                x = 1
                y = 0
            else:
                x = -1
                y = 0
            while path:
                if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                    moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                    if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                        path = False
                    chain += 1
                else:
                    path = False
        return moves_list
    
### PART 12:
# check valid knight moves
def check_knight(position, color):
    if position is None:
        print("Invalid position passed to check_knight.")
        return []

    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations

    # 8 squares to check for knights
    targets = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list



### PART 13:
# check for valid moves for just selected piece
def check_valid_moves():
    # Point 1: Print selection and turn_step
    print(f"Selection: {selection}, Turn step: {turn_step}")

    if turn_step < 2:
        print(f"Checking valid moves for White. Turn step: {turn_step}")
        options_list = white_options
    else:
        print(f"Checking valid moves for Black. Turn step: {turn_step}")
        options_list = black_options

    # Point 2: Print white_options and black_options
    print(f"White options: {white_options}")
    print(f"Black options: {black_options}")

    # Point 3: Check and print valid_options
    valid_options = options_list[selection]
    print(f"Valid moves for selection {selection}: {valid_options}")

    return valid_options

### PART 14: (updated) - draw_valid function
def draw_valid(valid_moves, square_size, board_offset_x, board_offset_y):
    # Loop through each valid move and draw a circle at the correct position
    for move in valid_moves:
        move_x, move_y = move
        # Adjust position based on the new offsets and size, ensuring the circle appears centered in the square
        pygame.draw.circle(screen, 'red', 
                           (board_offset_x + move_x * square_size + square_size // 2, 
                            board_offset_y + move_y * square_size + square_size // 2), square_size // 12)



### PART 15: Draw captured pieces with dynamic resizing and fixed minimum width for the panel
def draw_captured(square_size, piece_size, board_offset_x, board_offset_y, WIDTH, HEIGHT):
    # Minimum width for the captured pieces section to remain visible
    min_panel_width = square_size * 2  # Ensure the panel never shrinks too small

    # Calculate x positions for the white and black captured pieces
    x_white = board_offset_x + square_size * 8 + square_size // 4
    x_black = x_white + square_size
    
    # Make sure the panel doesn't shrink beyond the min width
    if x_black + min_panel_width > WIDTH:
        x_black = WIDTH - min_panel_width

    spacing = piece_size * 1.1  # Dynamic spacing based on piece size
    y_start = board_offset_y

    # Draw white captured pieces
    for i, captured_piece in enumerate(captured_pieces_white):
        index = piece_list.index(captured_piece)
        y = y_start + i * spacing
        resized_piece = pygame.transform.scale(small_black_images[index], (int(piece_size), int(piece_size)))
        screen.blit(resized_piece, (x_white, y))

    # Draw black captured pieces
    for i, captured_piece in enumerate(captured_pieces_black):
        index = piece_list.index(captured_piece)
        y = y_start + i * spacing
        resized_piece = pygame.transform.scale(small_white_images[index], (int(piece_size), int(piece_size)))
        screen.blit(resized_piece, (x_black, y))





### PART 16: the rules for putting a king in check, and winning the game
def draw_check(square_size, board_offset_x, board_offset_y):
    if turn_step < 2:
        print(f"Rendering status text for turn_step: {turn_step}")
        if 'king' in white_pieces:
            king_index = white_pieces.index('king')
            king_location = white_locations[king_index]
            for i in range(len(black_options)):
                if king_location in black_options[i]:
                    if counter < 15:
                        x = board_offset_x + king_location[0] * square_size + 1
                        y = board_offset_y + king_location[1] * square_size + 1
                        pygame.draw.rect(screen, 'dark red', [x, y, square_size, square_size], 5)
    else:
        if 'king' in black_pieces:
            king_index = black_pieces.index('king')
            king_location = black_locations[king_index]
            for i in range(len(white_options)):
                if king_location in white_options[i]:
                    if counter < 15:
                        x = board_offset_x + king_location[0] * square_size + 1
                        y = board_offset_y + king_location[1] * square_size + 1
                        pygame.draw.rect(screen, 'dark blue', [x, y, square_size, square_size], 5)


def draw_game_over():
    pygame.draw.rect(screen, 'black', [200, 200, 400, 70])
    screen.blit(font.render(f'{winner} won the game!', True, 'white'), (210, 210))
    screen.blit(font.render(f'Press ENTER to Restart!', True, 'white'), (210, 240))

print(f"Black locations: {black_locations}")
print(f"White locations: {white_locations}")
black_options = check_options(black_pieces, black_locations, 'black')
white_options = check_options(white_pieces, white_locations, 'white')

### PART 17: AI evaluation function and minimax algorithm
def evaluate_board(white_pieces, white_locations, black_pieces, black_locations):
    piece_values = {'pawn': 1, 'knight': 3, 'bishop': 3, 'rook': 5, 'queen': 9, 'king': 1000}
    white_score = sum(piece_values[p] for p in white_pieces)
    black_score = sum(piece_values[p] for p in black_pieces)
    return black_score - white_score  # Higher is better for black (AI)

def game_is_over(white_pieces, black_pieces):
    global black_options, white_options  # Ensure options are updated globally
    black_options = check_options(black_pieces, black_locations, 'black')
    white_options = check_options(white_pieces, white_locations, 'white')

    if 'king' not in white_pieces or 'king' not in black_pieces:
        print("Game over: A king is missing.")
        return True
    if not any(white_options) and turn_step < 2:  # No valid moves for White
        print("Game over: White has no valid moves. Stalemate or invalid state.")
        return True
    if not any(black_options) and turn_step >= 2:  # No valid moves for Black
        print("Game over: Black has no valid moves. Stalemate or invalid state.")
        return True
    return False

def get_all_moves(pieces, locations, color):
    options = []
    for i, piece in enumerate(pieces):
        # Validate piece index
        if i >= len(locations):
            print(f"Invalid piece index in get_all_moves: {i}, locations: {locations}")
            continue

        # Temporarily update selection/turn_step for move generation
        original_selection = selection
        original_turn = turn_step
        print(f"Rendering status text for turn_step: {turn_step}")
        globals()['selection'] = i
        globals()['turn_step'] = 2 if color == 'black' else 0
        print(f"Rendering status text for turn_step: {turn_step}")
        moves = check_valid_moves()
        globals()['selection'] = original_selection
        globals()['turn_step'] = original_turn
        print(f"Rendering status text for turn_step: {turn_step}")

        for move in moves:
            options.append((i, move))
    print(f"Generated moves for {color}: {options}")
    return options
def is_king_in_check(pieces, locations, enemy_options, color):
    """Check if the king of the given color is in check."""
    if 'king' not in pieces:
        return False  # No king, game over
    king_index = pieces.index('king')
    king_location = locations[king_index]
    for moves in enemy_options:
        if king_location in moves:
            return True
    return False

def simulate_move(pieces, locations, opponent_pieces, opponent_locations, piece_index, move):
    if piece_index < 0 or piece_index >= len(locations):
        print(f"Invalid piece_index in simulate_move: {piece_index}, locations: {locations}")
        return None, None

    print(f"Simulating move: piece_index={piece_index}, move={move}, locations={locations}")
    original_pos = locations[piece_index]
    captured_piece = None

    # Handle capturing an opponent's piece
    if move in opponent_locations:
        captured_index = opponent_locations.index(move)
        captured_piece = (opponent_pieces[captured_index], captured_index)
        opponent_pieces.pop(captured_index)
        opponent_locations[captured_index] = (-1, -1)  # Replace with placeholder

    # Update the piece's location
    locations[piece_index] = move
    print(f"After simulating move: locations={locations}")

    return original_pos, captured_piece

def undo_move(pieces, locations, opponent_pieces, opponent_locations, piece_index, move, original_pos=None, captured_piece=None):
    if piece_index < 0 or piece_index >= len(locations):
        print(f"Invalid piece_index in undo_move: {piece_index}, locations: {locations}")
        return

    print(f"Undoing move: piece_index={piece_index}, move={move}, original_pos={original_pos}, locations={locations}")
    # Restore the piece's original position
    if original_pos is not None:
        locations[piece_index] = original_pos
    else:
        print(f"Warning: original_pos is None for piece_index={piece_index}")

    # Restore the captured piece, if any
    if captured_piece:
        opponent_pieces.insert(captured_piece[1], captured_piece[0])
        opponent_locations[captured_piece[1]] = move
    print(f"After undoing move: locations={locations}")

def minimax(depth, is_maximizing, white_pieces, white_locations, black_pieces, black_locations):
    print(f"Minimax called at depth {depth} with {'Black' if is_maximizing else 'White'}'s turn")

    # Base case: game over or maximum depth reached
    if game_is_over(white_pieces, black_pieces) or depth == 0:
        score = evaluate_board(white_pieces, white_locations, black_pieces, black_locations)
        print(f"Evaluating board at depth {depth}: {score}")
        return score, None

    # Get all possible moves for the current player
    all_moves = get_all_moves(black_pieces if is_maximizing else white_pieces,
                              black_locations if is_maximizing else white_locations,
                              'black' if is_maximizing else 'white')
    print(f"All moves for {'Black' if is_maximizing else 'White'}: {all_moves}")

    # If no valid moves, check for stalemate or checkmate
    if not all_moves:
        if is_maximizing:
            if is_king_in_check(black_pieces, black_locations, check_options(white_pieces, white_locations, 'white'), 'black'):
                return -float('inf'), None  # Black is checkmated
            else:
                return 0, None  # Stalemate
        else:
            if is_king_in_check(white_pieces, white_locations, check_options(black_pieces, black_locations, 'black'), 'white'):
                return float('inf'), None  # White is checkmated
            else:
                return 0, None  # Stalemate

    # Initialize variables
    best_score = -float('inf') if is_maximizing else float('inf')
    best_move = None

    # Iterate through all possible moves
    for piece_index, move in all_moves:
        print(f"Processing move: piece_index={piece_index}, move={move}, locations={white_locations if not is_maximizing else black_locations}")
        # Simulate the move
        if is_maximizing:
            simulate_move(black_pieces, black_locations, white_pieces, white_locations, piece_index, move)
        else:
            simulate_move(white_pieces, white_locations, black_pieces, black_locations, piece_index, move)

        # Recursively call minimax
        score, _ = minimax(depth - 1, not is_maximizing, white_pieces, white_locations, black_pieces, black_locations)

        # Undo the move
        if is_maximizing:
            undo_move(black_pieces, black_locations, white_pieces, white_locations, piece_index, move)
        else:
            undo_move(white_pieces, white_locations, black_pieces, black_locations, piece_index, move)

        # Update the best score and move
        if is_maximizing:
            if score > best_score:
                best_score = score
                best_move = (piece_index, move)
        else:
            if score < best_score:
                best_score = score
                best_move = (piece_index, move)

    print(f"Best move for {'Black' if is_maximizing else 'White'} at depth {depth}: {best_move} with score {best_score}")
    return best_score, best_move

### PART 18: the main game loop
# Initial definitions outside the loop
board_area_width = int(WIDTH * 0.75)
square_size = min(board_area_width // 8, (HEIGHT - 100) // 8)
piece_size = square_size * 0.8
board_offset_x = 0
board_offset_y = (HEIGHT - 100 - (square_size * 8)) // 2
max_moves = 50  # Set a maximum number of moves to prevent infinite loops
move_count = 0

# Main game loop
# Main game loop
run = True
while run:
    # Ensure turn_step is valid
    if turn_step not in [0, 1, 2, 3]:
        print(f"Invalid turn_step detected: {turn_step}. Resetting to 0.")
        turn_step = 0

    move_count += 1
    if move_count > max_moves:
        print("Maximum move limit reached. Ending game to prevent infinite loop.")
        game_over = True
        break

    print(f"Turn step at start of loop: {turn_step}")
    timer.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            mouse_x, mouse_y = event.pos
            x_coord = (mouse_x - board_offset_x) // square_size
            y_coord = (mouse_y - board_offset_y) // square_size
            print(f"Mouse clicked at: {mouse_x}, {mouse_y}")

            # Check if the click is within the board
            if (board_offset_x <= mouse_x <= board_offset_x + square_size * 8) and (board_offset_y <= mouse_y <= board_offset_y + square_size * 8):
                if 0 <= x_coord <= 7 and 0 <= y_coord <= 7:
                    click_coords = (int(x_coord), int(y_coord))
                    print(f"Valid board coordinates: {click_coords}")
                else:
                    print(f"Invalid board coordinates: ({x_coord}, {y_coord})")
                    click_coords = None  # Reset invalid clicks
                print(f"Click coordinates: {click_coords}")

                if turn_step <= 1:  # White's turn
                    if click_coords in white_locations:  # Select a white piece
                        selection = white_locations.index(click_coords)
                        valid_moves = check_valid_moves()  # Get valid moves for the selected piece
                        if valid_moves:  # Ensure there are valid moves
                            turn_step = 1  # Move to "select destination" step
                            print(f"Piece selected at {click_coords}. Valid moves: {valid_moves}")
                        else:
                            print("No valid moves for the selected piece.")
                    if click_coords in valid_moves and selection != 100:  # Move the selected piece
                        white_locations[selection] = click_coords
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
                        turn_step = 2 if turn_step == 1 else 0  # Switch to Black's turn
                        selection = 100
                        valid_moves = []

        elif event.type == pygame.KEYDOWN and game_over:
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
                print(f"Turn step after game reset: {turn_step}")
                selection = 100
                valid_moves = []
                black_options = check_options(black_pieces, black_locations, 'black')
                white_options = check_options(white_pieces, white_locations, 'white')

    # Check for game over
    if game_is_over(white_pieces, black_pieces):
        print("Game over detected.")
        game_over = True
        break

    # Draw the game state
    screen.fill('dark green')
    draw_board(square_size, board_offset_x, board_offset_y, WIDTH, HEIGHT, turn_step)
    print(f"Rendering status text for turn_step: {turn_step}")
    draw_pieces(square_size, piece_size, board_offset_x, board_offset_y)
    draw_captured(square_size, piece_size, board_offset_x, board_offset_y, WIDTH, HEIGHT)
    draw_check(square_size, board_offset_x, board_offset_y)

    if selection != 100:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves, square_size, board_offset_x, board_offset_y)

    if winner != '':
        game_over = True
        draw_game_over()

    pygame.display.flip()

pygame.quit()