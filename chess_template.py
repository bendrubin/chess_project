import pygame

pygame.init()

# Initial screen size
# Start with any default size
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Resizable Chessboard")

clock = pygame.time.Clock()
running = True

# Piece layout (just pawns and kings for demo)
# 'bP' = black pawn, 'wK' = white king, etc.
board_state = [
    ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
    ['bP'] * 8,
    [''] * 8,
    [''] * 8,
    [''] * 8,
    [''] * 8,
    ['wP'] * 8,
    ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
]

# Piece colors for placeholder rendering
piece_colors = {
    'bP': (30, 30, 30), 'wP': (220, 220, 220),
    'bK': (30, 30, 30), 'wK': (220, 220, 220),
    'bQ': (50, 50, 50), 'wQ': (230, 230, 230),
    'bR': (50, 50, 50), 'wR': (230, 230, 230),
    'bB': (80, 80, 80), 'wB': (240, 240, 240),
    'bN': (80, 80, 80), 'wN': (240, 240, 240),
}

def draw_board(screen, square_size, offset_x, offset_y):
    colors = [(240, 217, 181), (181, 136, 99)]  # Light and dark squares
    for row in range(8):
        for col in range(8):
            color = colors[(row + col) % 2]
            rect = pygame.Rect(offset_x + col * square_size, offset_y + row * square_size, square_size, square_size)
            pygame.draw.rect(screen, color, rect)


def draw_pieces(screen, square_size, offset_x, offset_y):
    for row in range(8):
        for col in range(8):
            piece = board_state[row][col]
            if piece:
                color = piece_colors[piece]
                center_x = offset_x + col * square_size + square_size // 2
                center_y = offset_y + row * square_size + square_size // 2
                radius = square_size // 3
                pygame.draw.circle(screen, color, (center_x, center_y), radius)



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.w, event.h
            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

    screen.fill((0, 0, 0))  # Clear screen

    square_size = min(WIDTH, HEIGHT) // 8
    offset_x = (WIDTH - square_size * 8) // 2
    offset_y = (HEIGHT - square_size * 8) // 2
    draw_board(screen, square_size, offset_x, offset_y)
    draw_pieces(screen, square_size, offset_x, offset_y)


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
