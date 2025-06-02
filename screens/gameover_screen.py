import pygame
from config import screen_width, RED


def game_over_screen(screen, surface):
    font_big = pygame.font.SysFont("monospace", 60)
    font_small = pygame.font.SysFont("monospace", 30)
    screen.fill(DARK_GRAY)
    surface.fill(DARK_GRAY)

    game_over_text = font_big.render("GAME OVER", True, RED)

    screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, 100))
    pygame.display.update()

    pygame.time.wait(5000)  # 5 Sekunden warten