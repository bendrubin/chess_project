### PART 1
import pygame


# Initialize Pygame
pygame.init()

# Set up the screen with a default size (WIDTH, HEIGHT) and make it resizable
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
# Set the window caption
pygame.display.set_caption("Resizable Chessboard")
# Fonts (keep them defined as needed)
font = pygame.font.Font('freesansbold.ttf', 20)
medium_font = pygame.font.Font('freesansbold.ttf', 40)
big_font = pygame.font.Font('freesansbold.ttf', 50)
timer = pygame.time.Clock()
fps = 60

### PART 2
# game variables and images

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
turn_step = 0
selection = 100    
valid_moves = []

### PART 3
# load in game piece images 

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

### PART 4 (updated)

def draw_board(square_size, board_offset_x, board_offset_y):
    for row in range(8):
        for col in range(8):
            color = 'light gray' if (row + col) % 2 == 0 else 'dark gray'
            pygame.draw.rect(screen, color, 
                [board_offset_x + col * square_size, board_offset_y + row * square_size, square_size, square_size])
    for i in range(9):
        pygame.draw.line(screen, 'black', 
            (board_offset_x + i * square_size, board_offset_y), 
            (board_offset_x + i * square_size, board_offset_y + 8 * square_size), 2)
        pygame.draw.line(screen, 'black', 
            (board_offset_x, board_offset_y + i * square_size), 
            (board_offset_x + 8 * square_size, board_offset_y + i * square_size), 2)



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
### PART 5 drawing the pieces. 

def draw_pieces(square_size, piece_size, board_offset_x, board_offset_y):
    # Draw white pieces
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        if white_pieces[i] == 'pawn':
            piece_image = pygame.transform.scale(white_pawn, (int(piece_size), int(piece_size)))
        else:
            piece_image = pygame.transform.scale(white_images[index], (int(piece_size), int(piece_size)))
        screen.blit(piece_image, (board_offset_x + white_locations[i][0] * square_size + (square_size - piece_size) // 2,
                                  board_offset_y + white_locations[i][1] * square_size + (square_size - piece_size) // 2))

    # Draw black pieces
    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        if black_pieces[i] == 'pawn':
            piece_image = pygame.transform.scale(black_pawn, (int(piece_size), int(piece_size)))
        else:
            piece_image = pygame.transform.scale(black_images[index], (int(piece_size), int(piece_size)))
        screen.blit(piece_image, (board_offset_x + black_locations[i][0] * square_size + (square_size - piece_size) // 2,
                                  board_offset_y + black_locations[i][1] * square_size + (square_size - piece_size) // 2))


    # Handle red and blue dots (valid moves and selected pieces)
    if selection != 100:  # Assuming selection holds the index of the selected piece
        valid_moves = check_valid_moves()  # This will return a list of valid moves
        for move in valid_moves:
            move_x, move_y = move
            pygame.draw.circle(screen, 'red', (board_offset_x + move_x * square_size + square_size // 2, 
                                                board_offset_y + move_y * square_size + square_size // 2), piece_size // 6)
        
    if turn_step >= 2:  # Check if it's time to highlight the selected piece (based on your turn logic)
        if selection != 100:
            pygame.draw.rect(screen, 'blue', [board_offset_x + white_locations[selection][0] * square_size + (square_size - piece_size) // 2,
                                              board_offset_y + white_locations[selection][1] * square_size + (square_size - piece_size) // 2,
                                              piece_size, piece_size], 2)



### PART 6A
# checking all valid pieces on the board
def check_options(pieces, locations, turn):
    moves_list = []
    all_moves_list = []
    for i in range((len(pieces))):  # Iterate through each piece
        location = locations[i]
        piece = pieces[i]
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
        all_moves_list.append(moves_list)  # Add moves for each piece to the list
    return all_moves_list 

### PART 6B
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

### PART 6C
# check queen valid moves
def check_queen(position, color):
    moves_list = check_bishop(position, color)
    second_list = check_rook(position, color)
    for i in range(len(second_list)):
        moves_list.append(second_list[i])
    return moves_list

### PART 6D
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

### PART 6E
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
### PART 6F
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
    
### PART 6G
# check valid knight moves
def check_knight(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    # 8 squares to check for knights, they can go two squares in one direction and one in another
    targets = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list

### PART 7
# check for valid moves for just selected piece
def check_valid_moves():
    if turn_step < 2:
        options_list = white_options
    else:
        options_list = black_options
    valid_options = options_list[selection]
    return valid_options

### PART 8 (updated) - draw_valid function

def draw_valid(valid_moves, square_size, board_offset_x, board_offset_y):
    # Loop through each valid move and draw a circle at the correct position
    for move in valid_moves:
        move_x, move_y = move
        # Adjust position based on the new offsets and size, ensuring the circle appears centered in the square
        pygame.draw.circle(screen, 'red', 
                           (board_offset_x + move_x * square_size + square_size // 2, 
                            board_offset_y + move_y * square_size + square_size // 2), square_size // 6)


### PART 9
# draw captured pieces on side of screen
def draw_captured():
    for i in range(len(captured_pieces_white)):
        captured_piece = captured_pieces_white[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_black_images[index], (825, 5 + 50 * i))
    for i in range(len(captured_pieces_black)):
        captured_piece = captured_pieces_black[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_white_images[index], (925, 5 + 50 * i))


### PART 10: the rules for putting a king in check, and winning the game
def draw_check():
    if turn_step < 2:
        if 'king' in white_pieces:
            king_index = white_pieces.index('king')
            king_location = white_locations[king_index]
            for i in range(len(black_options)):
                if king_location in black_options[i]:
                    if counter < 15:
                        pygame.draw.rect(screen, 'dark red', [white_locations[king_index][0] * 100 + 1,
                                                              white_locations[king_index][1] * 100 + 1, 100, 100], 5)
    else:
        if 'king' in black_pieces:
            king_index = black_pieces.index('king')
            king_location = black_locations[king_index]
            for i in range(len(white_options)):
                if king_location in white_options[i]:
                    if counter < 15:
                        pygame.draw.rect(screen, 'dark blue', [black_locations[king_index][0] * 100 + 1,
                                                               black_locations[king_index][1] * 100 + 1, 100, 100], 5)

def draw_game_over():
    pygame.draw.rect(screen, 'black', [200, 200, 400, 70])
    screen.blit(font.render(f'{winner} won the game!', True, 'white'), (210, 210))
    screen.blit(font.render(f'Press ENTER to Restart!', True, 'white'), (210, 240))


black_options = check_options(black_pieces, black_locations, 'black')
white_options = check_options(white_pieces, white_locations, 'white')

### PART 11: the main game loop
### PART 11 (corrected full game loop)

run = True
while run:
    timer.tick(fps)

    # Dynamically calculate the square size and board offsets
    square_size = min(WIDTH, HEIGHT) // 8
    piece_size = square_size * 0.8  # 80% of square
    board_offset_x = (WIDTH - (square_size * 8)) // 2
    board_offset_y = (HEIGHT - (square_size * 8)) // 2

    if counter < 30:
        counter += 1
    else:
        counter = 0

    screen.fill('dark gray')
    draw_board(square_size, board_offset_x, board_offset_y)
    draw_pieces(square_size, piece_size, board_offset_x, board_offset_y)
    draw_captured()
    draw_check()

    if selection != 100:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves, square_size, board_offset_x, board_offset_y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.w, event.h
            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            mouse_x, mouse_y = event.pos

            # Check if click is inside the board
            if (board_offset_x <= mouse_x <= board_offset_x + square_size * 8) and (board_offset_y <= mouse_y <= board_offset_y + square_size * 8):
                x_coord = (mouse_x - board_offset_x) // square_size
                y_coord = (mouse_y - board_offset_y) // square_size
                click_coords = (int(x_coord), int(y_coord))

                if turn_step <= 1:
                    if click_coords == (8, 8) or click_coords == (9, 8):
                        winner = 'black'
                    if click_coords in white_locations:
                        selection = white_locations.index(click_coords)
                        if turn_step == 0:
                            turn_step = 1
                    if click_coords in valid_moves and selection != 100:
                        white_locations[selection] = click_coords
                        if click_coords in black_locations:
                            black_piece = black_locations.index(click_coords)
                            captured_pieces_white.append(black_pieces[black_piece])
                            if black_pieces[black_piece] == 'king':
                                winner = 'white'
                            black_pieces.pop(black_piece)
                            black_locations.pop(black_piece)
                        black_options = check_options(black_pieces, black_locations, 'black')
                        white_options = check_options(white_pieces, white_locations, 'white')
                        turn_step = 2
                        selection = 100
                        valid_moves = []

                else:
                    if click_coords == (8, 8) or click_coords == (9, 8):
                        winner = 'white'
                    if click_coords in black_locations:
                        selection = black_locations.index(click_coords)
                        if turn_step == 2:
                            turn_step = 3
                    if click_coords in valid_moves and selection != 100:
                        black_locations[selection] = click_coords
                        if click_coords in white_locations:
                            white_piece = white_locations.index(click_coords)
                            captured_pieces_black.append(white_pieces[white_piece])
                            if white_pieces[white_piece] == 'king':
                                winner = 'black'
                            white_pieces.pop(white_piece)
                            white_locations.pop(white_piece)
                        black_options = check_options(black_pieces, black_locations, 'black')
                        white_options = check_options(white_pieces, white_locations, 'white')
                        turn_step = 0
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
                selection = 100
                valid_moves = []
                black_options = check_options(black_pieces, black_locations, 'black')
                white_options = check_options(white_pieces, white_locations, 'white')

    if winner != '':
        game_over = True
        draw_game_over()

    pygame.display.flip()

pygame.quit()


