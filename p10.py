### PART 1 ###
import pygame

pygame.init()
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption('Two-Player Pygame Chess!')

font = pygame.font.Font('freesansbold.ttf', 20)
medium_font = pygame.font.Font('freesansbold.ttf', 40)
big_font = pygame.font.Font('freesansbold.ttf', 50)

timer = pygame.time.Clock()
fps = 60
selected_square = None

# Game variables (same as before)
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
    'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
       (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
    'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
       (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']
captured_pieces_white = []
captured_pieces_black = []

# Turn state (same as before)
turn_step = 0
selection = 100    
valid_moves = []



### PART 2 ###
# Function to resize the images based on the new screen size
def resize_all_images(square_size):
    small_size = square_size // 2

    def ls(name, size):
        return load_and_scale(image_paths[name], (size, size))

    # Resize all pieces
    white_pawn = ls("white_pawn", int(square_size * 0.6))
    white_queen = ls("white_queen", square_size)
    white_king = ls("white_king", square_size)
    white_knight = ls("white_knight", square_size)
    white_rook = ls("white_rook", square_size)
    white_bishop = ls("white_bishop", square_size)

    black_pawn = ls("black_pawn", int(square_size * 0.6))
    black_queen = ls("black_queen", square_size)
    black_king = ls("black_king", square_size)
    black_knight = ls("black_knight", square_size)
    black_rook = ls("black_rook", square_size)
    black_bishop = ls("black_bishop", square_size)

    # Return resized normal images
    white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
    black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
    
    # Now, resize for small images used for captured pieces (just smaller size)
    small_white_images = [pygame.transform.smoothscale(img, (50, 50)) for img in white_images]
    small_black_images = [pygame.transform.smoothscale(img, (50, 50)) for img in black_images]
    
def resize_all_images(square_size):
    scale_factor = 0.85  # Shrink to 85% of square size
    piece_size = int(square_size * scale_factor)

    white_images = [pygame.transform.scale(img, (piece_size, piece_size)) for img in white_images]
    black_images = [pygame.transform.scale(img, (piece_size, piece_size)) for img in black_images]

    small_white_images = [pygame.transform.scale(img, (piece_size // 2, piece_size // 2)) for img in small_white_images]
    small_black_images = [pygame.transform.scale(img, (piece_size // 2, piece_size // 2)) for img in small_black_images]

    return white_images, black_images, small_white_images, small_black_images


# Helper function to load and scale an image
def load_and_scale(path, size):
    return pygame.transform.smoothscale(pygame.image.load(path), size)


### PART 3 ###

# image file paths
image_paths = {
    "black_queen": r'C:\Users\benjy\OneDrive\Desktop\py_pro\black queen.png',
    "black_king": r'C:\Users\benjy\OneDrive\Desktop\py_pro\black king.png',
    "black_bishop": r'C:\Users\benjy\OneDrive\Desktop\py_pro\black bishop.png',
    "black_knight": r'C:\Users\benjy\OneDrive\Desktop\py_pro\black knight.png',
    "black_rook": r'C:\Users\benjy\OneDrive\Desktop\py_pro\black rook.png',
    "black_pawn": r'C:\Users\benjy\OneDrive\Desktop\py_pro\black pawn.png',
    "white_queen": r'C:\Users\benjy\OneDrive\Desktop\py_pro\white queen.png',
    "white_king": r'C:\Users\benjy\OneDrive\Desktop\py_pro\white king.png',
    "white_bishop": r'C:\Users\benjy\OneDrive\Desktop\py_pro\white bishop.png',
    "white_knight": r'C:\Users\benjy\OneDrive\Desktop\py_pro\white knight.png',
    "white_rook": r'C:\Users\benjy\OneDrive\Desktop\py_pro\white rook.png',
    "white_pawn": r'C:\Users\benjy\OneDrive\Desktop\py_pro\white pawn.png',
}

# Define a square size for your images
square_size = 100  # This is where you define the size of each square

# Call resize_all_images to get the resized images
def resize_all_images(square_size):
    small_size = square_size // 2

    def ls(name, size):
        return load_and_scale(image_paths[name], (size, size))

    # Resize all pieces
    white_pawn = ls("white_pawn", int(square_size * 0.7))
    white_queen = ls("white_queen", int(square_size * 0.7))
    white_king = ls("white_king", int(square_size * 0.7))
    white_knight = ls("white_knight", int(square_size * 0.7))
    white_rook = ls("white_rook", int(square_size * 0.7))
    white_bishop = ls("white_bishop", int(square_size * 0.7))

    black_pawn = ls("black_pawn", int(square_size * 0.7))
    black_queen = ls("black_queen", int(square_size * 0.7))
    black_king = ls("black_king", int(square_size * 0.7))
    black_knight = ls("black_knight", int(square_size * 0.7))
    black_rook = ls("black_rook", int(square_size * 0.7))
    black_bishop = ls("black_bishop", int(square_size * 0.7))

    # Return resized normal images
    white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
    black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
    
    # Now, resize for small images used for captured pieces (just smaller size)
    small_white_images = [pygame.transform.smoothscale(img, (50, 50)) for img in white_images]
    small_black_images = [pygame.transform.smoothscale(img, (50, 50)) for img in black_images]
    
    return white_images, black_images, small_white_images, small_black_images

# Now, call this function after defining square_size to initialize images
white_images, black_images, small_white_images, small_black_images = resize_all_images(square_size)

### PART 4 ###
# Drawing the main board with dynamic resizing
def draw_board():
    # Dynamically calculate square size based on the current window width and height
    square_size = min(WIDTH, HEIGHT) // 8  # Ensure the board remains square, fit to the smaller dimension
    board_height = square_size * 8  # The height of the board area
    status_bar_height = HEIGHT - board_height  # Status bar height should adjust based on available height
    sidebar_width = WIDTH - board_height  # Sidebar width adjusts based on available width

    # Make sure the status bar and sidebar do not overlap the board area
    if status_bar_height < 0:  # In case the window is too small, prevent overlap
        status_bar_height = 0
    if sidebar_width < 0:  # Similarly, ensure sidebar doesn't become negative
        sidebar_width = 0

    # Draw the alternating colors of the board
    for row in range(8):
        for col in range(8):
            color = 'light gray' if (row + col) % 2 == 0 else 'dark gray'
            pygame.draw.rect(screen, color, [col * square_size, row * square_size, square_size, square_size])

    # Draw the status bar and sidebar
    pygame.draw.rect(screen, 'gray', [0, board_height, WIDTH, status_bar_height])
    pygame.draw.rect(screen, 'gold', [0, board_height, WIDTH, status_bar_height], 5)
    pygame.draw.rect(screen, 'gold', [board_height, 0, sidebar_width, HEIGHT], 5)

    # Status text - showing which player's turn it is
    status_text = ['White: Select a Piece to Move!', 'White: Select a Destination!',
                   'Black: Select a Piece to Move!', 'Black: Select a Destination!']
    screen.blit(big_font.render(status_text[turn_step], True, 'black'), (20, board_height + 20))

    # Draw grid lines for the board
    for i in range(9):
        pygame.draw.line(screen, 'black', (0, i * square_size), (board_height, i * square_size), 2)
        pygame.draw.line(screen, 'black', (i * square_size, 0), (i * square_size, board_height), 2)

    # FORFEIT button (adjust its position to fit the window size)
    screen.blit(medium_font.render('FORFEIT', True, 'black'), (board_height + 10, board_height + 30))



### PART 5 ###
# Draw pieces
def draw_pieces():
    square_size = WIDTH // 8  # Make everything dynamic
    padding_small = int(square_size * 0.22)
    padding_large = int(square_size * 0.1)
    box_thickness = max(2, square_size // 50)

    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        x = white_locations[i][0] * square_size
        y = white_locations[i][1] * square_size

        if white_pieces[i] == 'pawn':
            screen.blit(white_images[0], (x + padding_small, y + padding_small + 8))  # extra y adjustment for pawns
        else:
            screen.blit(white_images[index], (x + padding_large, y + padding_large))

        if turn_step < 2 and selection == i:
            pygame.draw.rect(screen, 'red', [x + 1, y + 1, square_size, square_size], box_thickness)

    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        x = black_locations[i][0] * square_size
        y = black_locations[i][1] * square_size

        if black_pieces[i] == 'pawn':
            screen.blit(black_images[0], (x + padding_small, y + padding_small + 8))
        else:
            screen.blit(black_images[index], (x + padding_large, y + padding_large))

        if turn_step >= 2 and selection == i:
            pygame.draw.rect(screen, 'blue', [x + 1, y + 1, square_size, square_size], box_thickness)

# === PART 6A ===
# checking all valid pieces on the board
def check_options(pieces, locations, turn):
    moves_list = []
    all_moves_list = []
    for i in range(len(pieces)):  # Iterate through each piece
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


# === Before calling check_valid_moves ===
def update_options():
    global white_options, black_options

    # Check options based on the current turn
    if turn_step < 2:
        white_options = check_options(white_pieces, white_locations, 'white')
    else:
        black_options = check_options(black_pieces, black_locations, 'black')
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

### PART 8

def draw_valid(moves):
    if moves is None:
        moves = []  # Ensure moves is always a list
    if turn_step < 2:
        color = 'red'
    else:
        color = 'blue'
    for move in moves:
        pygame.draw.circle(screen, color, (move[0] * 100 + 50, move[1] * 100 + 50), 5)

        
# PART 9: Draw captured pieces on the side of the screen
def draw_captured():
    for i in range(len(captured_pieces_white)):
        captured_piece = captured_pieces_white[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_black_images[index], (825, 5 + 50 * i))  # Display black captured pieces
    for i in range(len(captured_pieces_black)):
        captured_piece = captured_pieces_black[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_white_images[index], (925, 5 + 50 * i))  # Display white captured pieces

# === GLOBAL VARIABLES NEEDED FOR PART 10 ===
counter = 0           # Used for flickering effect when king is in check
winner = ''           # Stores the name of the winner when game ends

### PART 10: the rules for putting a king in check, and winning the game ###

# Draw a highlight around the king if in check
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

# Display game over screen
def draw_game_over():
    pygame.draw.rect(screen, 'black', [200, 200, 400, 70])
    screen.blit(font.render(f'{winner} won the game!', True, 'white'), (210, 210))
    screen.blit(font.render(f'Press ENTER to Restart!', True, 'white'), (210, 240))


# === Initialize game state variables ===
counter = 0
winner = ''
game_over = False
selection = 100
turn_step = 0

# Captured pieces tracking
captured_pieces_white = []
captured_pieces_black = []

# Initial piece setup
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
selected_piece_index = None
selected_piece_color = None

## PART 11
# Main game loop
running = True
selected_square = None  # <- this can also be set above the loop
while running:
    WIDTH, HEIGHT = pygame.display.get_surface().get_size()
    square_size = WIDTH // 8

    # Resize images every frame (optional: optimize later)
    white_images, black_images, small_white_images, small_black_images = resize_all_images(square_size)

    screen.fill(("dark gray"))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            grid_x = mouse_x // square_size
            grid_y = mouse_y // square_size
            clicked_square = (grid_x, grid_y)

    # Check if you're selecting a piece
            if selected_piece_index is None:
                for i, (x, y) in enumerate(white_locations):
                    if (x, y) == clicked_square:
                        selected_piece_index = i
                        selected_piece_color = 'white'
                        break
                for i, (x, y) in enumerate(black_locations):
                    if (x, y) == clicked_square:
                        selected_piece_index = i
                        selected_piece_color = 'black'
                        break
                selected_square = clicked_square

    # If you've already selected a piece, try to move it
            else:
                if selected_piece_color == 'white':
                    white_locations[selected_piece_index] = clicked_square
                else:
                    black_locations[selected_piece_index] = clicked_square

                selected_piece_index = None
                selected_piece_color = None
                selected_square = None  # remove highlight after moving



            print(f"Mouse clicked on square: ({grid_x}, {grid_y})")

          
        
    # Draw the chessboard
    for row in range(8):
        for col in range(8):
            color = (240, 217, 181) if (row + col) % 2 == 0 else (181, 136, 99)
            pygame.draw.rect(screen, color, (col * square_size, row * square_size, square_size, square_size))
    if selected_square:
        highlight_surface = pygame.Surface((square_size, square_size), pygame.SRCALPHA)
        highlight_surface.fill((0, 255, 0, 100))  # translucent green
        screen.blit(highlight_surface, (selected_square[0] * square_size, selected_square[1] * square_size))
    

    # Draw white pieces
    for idx, (x, y) in enumerate(white_locations):
        piece_name = white_pieces[idx]
        piece_img = white_images[piece_list.index(piece_name)]
        offset = (square_size - piece_img.get_width()) // 2
        screen.blit(piece_img, (x * square_size + offset, y * square_size + offset))


    # Draw black pieces
    for idx, (x, y) in enumerate(black_locations):
        piece_name = black_pieces[idx]
        piece_img = black_images[piece_list.index(piece_name)]
        offset = (square_size - piece_img.get_width()) // 2
        screen.blit(piece_img, (x * square_size + offset, y * square_size + offset))


    pygame.display.update()
    timer.tick(fps)
    pygame.display.flip()

pygame.quit()
