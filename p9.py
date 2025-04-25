import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the screen (default size, will resize later)
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Chess")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
light_square = (240, 217, 181)
dark_square = (181, 136, 99)

# Define the board setup with full names
board = [
    ['black_rook', 'black_knight', 'black_bishop', 'black_queen', 'black_king', 'black_bishop', 'black_knight', 'black_rook'],
    ['black_pawn', 'black_pawn', 'black_pawn', 'black_pawn', 'black_pawn', 'black_pawn', 'black_pawn', 'black_pawn'],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    ['white_pawn', 'white_pawn', 'white_pawn', 'white_pawn', 'white_pawn', 'white_pawn', 'white_pawn', 'white_pawn'],
    ['white_rook', 'white_knight', 'white_bishop', 'white_queen', 'white_king', 'white_bishop', 'white_knight', 'white_rook']
]

# Load images for pieces (ensure you have the correct image files)
piece_images = {
    'black_rook': pygame.image.load('black_rook.png'),
    'black_knight': pygame.image.load('black_knight.png'),
    'black_bishop': pygame.image.load('black_bishop.png'),
    'black_queen': pygame.image.load('black_queen.png'),
    'black_king': pygame.image.load('black_king.png'),
    'black_pawn': pygame.image.load('black_pawn.png'),
    'white_rook': pygame.image.load('white_rook.png'),
    'white_knight': pygame.image.load('white_knight.png'),
    'white_bishop': pygame.image.load('white_bishop.png'),
    'white_queen': pygame.image.load('white_queen.png'),
    'white_king': pygame.image.load('white_king.png'),
    'white_pawn': pygame.image.load('white_pawn.png')
}

# Function to resize the pieces based on the board's size
def resize_pieces():
    square_size = screen_width // 8  # Calculate the size of each square dynamically based on the screen width
    for piece in piece_images:
        piece_images[piece] = pygame.transform.scale(piece_images[piece], (square_size, square_size))
    return square_size

# Function to draw the chessboard
def draw_board():
    for row in range(8):
        for col in range(8):
            color = light_square if (row + col) % 2 == 0 else dark_square
            pygame.draw.rect(screen, color, pygame.Rect(col * square_size, row * square_size, square_size, square_size))

# Function to draw the pieces
def draw_pieces():
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece is not None:
                screen.blit(piece_images[piece], pygame.Rect(col * square_size, row * square_size, square_size, square_size))

# Resize pieces initially
square_size = resize_pieces()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check for resizing the window
    if pygame.display.get_surface().get_width() != screen_width or pygame.display.get_surface().get_height() != screen_height:
        screen_width, screen_height = pygame.display.get_surface().get_size()
        square_size = resize_pieces()  # Resize the pieces when window size changes
    
    draw_board()
    draw_pieces()

    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()
