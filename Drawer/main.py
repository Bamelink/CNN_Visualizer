from utils import *
import time
import cv2 as cv
import numpy as np

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drawing Program")
SURFACE = pygame.Surface([28*PIXEL_SIZE, 28*PIXEL_SIZE])


def init_grid(rows, cols, color):
    grid = []

    for i in range(rows):
        grid.append([])
        for _ in range(cols):
            grid[i].append(color)

    return grid


def draw_grid(surface, grid):
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            pygame.draw.rect(surface, pixel, (j * PIXEL_SIZE, i *
                                          PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

    if DRAW_GRID_LINES:
        for i in range(ROWS + 1):
            pygame.draw.line(surface, WHITE, (0, i * PIXEL_SIZE),
                             (WIDTH, i * PIXEL_SIZE))

        for i in range(COLS + 1):
            pygame.draw.line(surface, WHITE, (i * PIXEL_SIZE, 0),
                             (i * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))


def draw(win, surface, grid, buttons):
    win.fill(BG_COLOR)
    draw_grid(surface, grid)

    for button in buttons:
        button.draw(win)

    WIN.blit(surface, (0,0))
    pygame.display.update()


def get_row_col_from_pos(pos):
    x, y = pos
    row = y // PIXEL_SIZE
    col = x // PIXEL_SIZE

    if row >= ROWS:
        raise IndexError

    return row, col


run = True
clock = pygame.time.Clock()
grid = init_grid(ROWS, COLS, BG_COLOR)
drawing_color = WHITE

button_y = HEIGHT - TOOLBAR_HEIGHT/2 - 25
buttons = [
    Button(10, button_y, 50, 50, WHITE),
    Button(110, button_y, 50, 50, BLACK, "Erase", WHITE),
    Button(210, button_y, 50, 50, BLACK, "Save", WHITE),
    Button(310, button_y, 50, 50, BLACK, "Clear", WHITE)
]

while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()

            try:
                row, col = get_row_col_from_pos(pos)
                grid[row][col] = drawing_color
            except IndexError:
                for button in buttons:
                    if not button.clicked(pos):
                        continue

                    drawing_color = button.color
                    if button.text == "Clear":
                        grid = init_grid(ROWS, COLS, BG_COLOR)
                        drawing_color = WHITE
                    if button.text == "Save":
                        timestr = time.strftime("%Y%m%d-%H%M%S")
                        view = pygame.surfarray.array3d(SURFACE).transpose([1, 0, 2])
                        img_gray = cv.cvtColor(view, cv.COLOR_BGR2GRAY)
                        img_gray = cv.resize(img_gray, (28,28))
                        cv.imwrite(f"{timestr}.png", img_gray)
    draw(WIN, SURFACE, grid, buttons)

pygame.quit()