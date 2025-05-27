import random
import pygame
import sys
from abc import ABC, abstractmethod

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

class Figure(ABC):
    def __init__(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    @abstractmethod
    def draw(self, surface):
        pass

class Food(Figure):
    def __init__(self, color):

        super().__init__(color)

        self.__position = (0, 0)

        self.randomize_position()

    def randomize_position(self):
        pos_x = random.randint(0, (grid_width - 1)) * grid_size
        pos_y = random.randint(0, (grid_height - 1)) * grid_size
        self.__position = (pos_x, pos_y)

    def draw(self, surface):
        r = pygame.Rect((self.__position[0], self.__position[1]), (grid_size, grid_size))
        pygame.draw.rect(surface, self.get_color(), r, 10)

    def get_position(self):
        return self.__position

    def set_position(self, position):
        self.__position = position


class SpecialFood(Food):
    def __init__(self, color):
        super().__init__(color)
        self.__counter = 0

    def get_counter(self):
        return self.__counter

    def set_counter(self, counter):
        self.__counter = counter

    def increase_counter(self):
        self.__counter += 1

    def reset_counter(self):
        self.__counter = 0

    def check_counter(self):
        if self.__counter >= 15:
            self.reset_counter()
            self.randomize_position()


class Snake(Figure):

    def __init__(self, color):

        super().__init__(color)

        self.__length = 1

        self.__positions = [[screen_width // 2, screen_height // 2]]

        self.__direction = (1, 0)

        self.__score = 0

    def draw(self, surface):

        for p in self.__positions:
            r = pygame.Rect((p[0], p[1]), (grid_size, grid_size))

            pygame.draw.rect(surface, self.get_color(), r)

    def turn(self, new_dir):
        if self.__length > 1 and (new_dir[0] * -1, new_dir[1] * -1) == self.__direction:
            return
        else:
            self.__direction = new_dir

    def move(self):
        cur_head_pos = self.get_head_position()
        x, y = self.__direction
        new_head_pos = (
            ((cur_head_pos[0] + (x * grid_size)) % screen_width), (cur_head_pos[1] + (y * grid_size)) % screen_height)
        if len(self.__positions) > 2 and new_head_pos in self.__positions[2:]:
            self.reset()
        else:
            self.__positions.insert(0, new_head_pos)
            if len(self.__positions) > self.__length:
                self.__positions.pop()

    def get_head_position(self):
        return self.__positions[0]

    def reset(self):
        self.__length = 1
        self.__positions = [((screen_width / 2), (screen_height / 2))]
        self.__direction = (1, 0)
        self.__score = 0

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if score >= 0:
            self.__score = score

    def increase_score(self):
        self.__score += 1

    def reset_score(self):
        self.__score = 0

    def get_length(self):
        return self.__score

    def set_length(self, length):
        if length >= 0:
            self.__length = length

    def increase_length(self):
        self.__length += 1

    def reset_length(self):
        self.__length = 0


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
