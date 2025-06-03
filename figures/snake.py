import pygame

from figures.figure import Figure
from config import screen_width, screen_height, grid_size

class Snake(Figure):

    def __init__(self, color):

        super().__init__(color)

        self.__length = 1

        self.__positions = [[screen_width // 2, screen_height // 2]]

        self.__direction = (1, 0)

        self.__score = 0

        self.__is_dead = False

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
            self.__is_dead = True
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
        self.__is_dead = False

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

    def is_dead(self):
        return self.__is_dead

    def get_direction(self):
        return self.__direction
