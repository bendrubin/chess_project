import pygame

# Initialize pygame before setting display
pygame.init()

# Screen setup
WIDTH, HEIGHT = 1000, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption('Two-Player Pygame Chess!')

# Fonts and clock
font = pygame.font.Font('freesansbold.ttf', 20)
medium_font = pygame.font.Font('freesansbold.ttf', 40)
big_font = pygame.font.Font('freesansbold.ttf', 50)
timer = pygame.time.Clock()
fps = 60

# Board layout ratios
BOARD_WIDTH_RATIO = 0.8   # 80% of the window's width
BOARD_HEIGHT_RATIO = 0.9  # 90% of the window's height
BOARD_TOP_MARGIN_RATIO = 0.05  # 5% of the window height as top margin

# Function to calculate board layout dynamically
def calculate_board_layout(width, height):
    board_width = width * BOARD_WIDTH_RATIO
    board_height = height * BOARD_HEIGHT_RATIO
    top_margin = height * BOARD_TOP_MARGIN_RATIO
    tile_size = min(board_width, board_height) / 8
    board_left = (width - tile_size * 8) // 2
    board_top = top_margin
    return tile_size, board_left, board_top

# Initial calculation
tile_size, board_left, board_top = calculate_board_layout(WIDTH, HEIGHT)
running = True
while running:
    timer.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.w, event.h
            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
            tile_size, board_left, board_top = calculate_board_layout(WIDTH, HEIGHT)

    # Clear screen
    screen.fill((255, 255, 255))

    # Draw the chess board
    colors = [(235, 235, 208), (119, 148, 85)]  # Light and dark squares
    for row in range(8):
        for col in range(8):
            color = colors[(row + col) % 2]
            rect = pygame.Rect(
                board_left + col * tile_size,
                board_top + row * tile_size,
                tile_size,
                tile_size
            )
            pygame.draw.rect(screen, color, rect)

    pygame.display.flip()
