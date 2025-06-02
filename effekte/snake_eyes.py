import pygame

from config import grid_size, BLACK


def draw_eyes(surface, snake):
    head_x, head_y = snake.get_head_position()  # Das sind Pixelkoordinaten!
    center_x = head_x + grid_size // 2  # Mittelpunkt im Grid-Quadrat
    center_y = head_y + grid_size // 2

    dx, dy = snake.get_direction()
    offset = grid_size // 4

    if dx == 1:  # Rechts
        eye1 = (center_x + offset, center_y - offset)
        eye2 = (center_x + offset, center_y + offset)
    elif dx == -1:  # Links
        eye1 = (center_x - offset, center_y - offset)
        eye2 = (center_x - offset, center_y + offset)
    elif dy == 1:  # Runter
        eye1 = (center_x - offset, center_y + offset)
        eye2 = (center_x + offset, center_y + offset)
    elif dy == -1:  # Hoch
        eye1 = (center_x - offset, center_y - offset)
        eye2 = (center_x + offset, center_y - offset)
    else:
        eye1 = eye2 = (center_x, center_y)

    pygame.draw.circle(surface, BLACK, eye1, 3)
    pygame.draw.circle(surface, BLACK, eye2, 3)