import pygame
pygame.init()
pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FPS = 240

WIDTH, HEIGHT = 600, 700

ROWS = COLS = 28

TOOLBAR_HEIGHT = HEIGHT - WIDTH

PIXEL_SIZE = WIDTH // COLS

BG_COLOR = BLACK

DRAW_GRID_LINES = True


def get_font(size):
    return pygame.font.SysFont("comicsans", size)