import random
import pygame

from figures.figure import Figure
from config import grid_size, grid_height, grid_width

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