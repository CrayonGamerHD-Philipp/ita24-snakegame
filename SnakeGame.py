import pygame
import sys
import json
import os

from figures.snake import Snake
from figures.food import Food, SpecialFood
from screens.startscreen import start_screen
from config import screen_width, screen_height, grid_height, grid_size, grid_width
from effekte.effekte import background_music, eat_sound, game_over_sound
from pause_menu.pause_menu import pause_screen
from effekte.snake_eyes import draw_eyes
from screens.gameover_screen import game_over_screen

class SnakeGame():

    def __init__(self):
        pygame.init()
        self.__clock = pygame.time.Clock()
        self.__screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
        self.__surface = pygame.Surface(self.__screen.get_size()).convert()
        self.__font = pygame.font.SysFont("monospace", 16)
        self.__snake = Snake(color=(0, 200, 0))
        self.__food = Food(color=(255, 0, 0))
        self.__special_food = SpecialFood(color=(0, 0, 255))
        self.__running = True
        self.__gamespeed = 5
        self.__highscore = 0
        self.load_data()
        


    def reset(self):
        if self.__snake.get_score() > self.__highscore:
            self.__highscore = self.__snake.get_score()
        self.__snake = Snake(color=(0, 200, 0))
        self.__food = Food(color=(255, 0, 0))
        self.__special_food = SpecialFood(color=(0, 0, 255))
        self.__running = True
        background_music.play(-1)

        self.save_data()

    def update(self):
        if self.__snake.is_dead():
            game_over_sound.play()
            background_music.stop()
            game_over_screen(self.__screen, self.__surface)
            self.reset()
            return

        self.__gamespeed = 5 + (self.__snake.get_score() // 10)
        self.__clock.tick(self.__gamespeed)
        self.__snake.move()
        self.__special_food.increase_counter()
        self.__special_food.check_counter()

        if self.__snake.get_head_position() == self.__special_food.get_position():
            self.__special_food.randomize_position()
            self.__special_food.reset_counter()
            self.__snake.increase_length()
            self.__snake.increase_score()
            self.__snake.increase_score()

        if self.__snake.get_head_position() == self.__food.get_position():
            self.__snake.increase_score()
            self.__snake.increase_length()
            self.__food.randomize_position()
            eat_sound.play()

    def run(self):
        start_screen(self.__screen, self.__surface)
        background_music.play(-1)
        while True:
            self.handle_events()
            if self.__running:
                self.update()
                self.draw()

    def draw(self):
        self.draw_grid()
        self.__snake.draw(self.__surface)
        self.__food.draw(self.__surface)
        self.__special_food.draw(self.__surface)

        draw_eyes(self.__surface, self.__snake)

        text = self.__font.render(f"Score: {self.__snake.get_score()} Highscore: {self.__highscore} Gamespeed: {self.__gamespeed}", True, (0, 0, 0))
        self.__surface.blit(text, (5, 10))

        self.__screen.blit(self.__surface, (0, 0))
        pygame.display.update()

    def draw_grid(self):
        for y in range(0, int(grid_height)):
            for x in range(0, int(grid_width)):
                if (x + y) % 2 == 0:
                    r = pygame.Rect((x * grid_size, y * grid_size), (grid_size, grid_size))
                    pygame.draw.rect(self.__surface, (170, 255, 213), r)
                else:
                    rr = pygame.Rect((x * grid_size, y * grid_size), (grid_size, grid_size))
                    pygame.draw.rect(self.__surface, (107, 148, 107), rr)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.__snake.turn((0, -1))
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.__snake.turn((0, 1))
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.__snake.turn((-1, 0))
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.__snake.turn((1, 0))
                elif event.key == pygame.K_p:
                    pause_screen(self.__screen, self.__surface)

    def load_data(self):
        if os.path.exists("data.json"):
            with open("data.json", "r") as file:
                data = json.load(file)
                self.__highscore = data.get("highscore", 0)
        return 0

    def save_data(self):
        with open("data.json", "w") as file:
            json.dump({"highscore": self.__highscore}, file, indent=4)

if __name__ == "__main__":
    snake_game = SnakeGame()
    snake_game.run()
