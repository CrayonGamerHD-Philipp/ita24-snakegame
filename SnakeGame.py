import pygame
import sys

from figures.snake import Snake
from figures.food import Food, SpecialFood

grid_size = 20
grid_width = 18
grid_height = 18

screen_width = grid_size * grid_width
screen_height = grid_size * grid_height


def draw_grid(surface):
    for y in range(0, int(grid_height)):
        for x in range(0, int(grid_width)):
            if (x + y) % 2 == 0:
                r = pygame.Rect((x * grid_size, y * grid_size), (grid_size, grid_size))
                pygame.draw.rect(surface, (93, 216, 228), r)
            else:
                rr = pygame.Rect((x * grid_size, y * grid_size), (grid_size, grid_size))
                pygame.draw.rect(surface, (84, 194, 205), rr)


def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()


def handle_keys(snake):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_UP:
                snake.turn((0, -1))
            elif event.key == pygame.K_DOWN:
                snake.turn((0, 1))
            elif event.key == pygame.K_LEFT:
                snake.turn((-1, 0))
            elif event.key == pygame.K_RIGHT:
                snake.turn((1, 0))


def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    myfont = pygame.font.SysFont("monospace", 16)
    snake = Snake(color=(0, 200, 0))

    food = Food(color=(255, 0, 0))
    special_food = SpecialFood(color=(0, 0, 255))

    while (True):
        clock.tick(5)
        handle_keys(snake)
        snake.move()

        special_food.increase_counter()
        special_food.check_counter()

        if snake.get_head_position() == special_food.get_position():
            special_food.randomize_position()
            special_food.reset_counter()
            snake.increase_length()
            snake.increase_score()
            snake.increase_score()

        if snake.get_head_position() == food.get_position():
            snake.increase_score()
            snake.increase_length()
            food.randomize_position()

        draw_grid(surface)
        snake.draw(surface)
        food.draw(surface)
        special_food.draw(surface)
        handle_events()
        screen.blit(surface, (0, 0))
        print(snake.get_score())
        text = myfont.render(f"Score: {snake.get_score()}", bool(1), (0, 0, 0))
        screen.blit(text, (5, 10))
        pygame.display.update()


main()
