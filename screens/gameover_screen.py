import pygame
from config import screen_width, RED, DARK_GRAY, WHITE, GREEN, BLUE


def game_over_screen(screen, surface, snakegame):
    font_big = pygame.font.SysFont("monospace", 60)
    font_small = pygame.font.SysFont("monospace", 30)
    screen.fill(GREEN)
    surface.fill(GREEN)

    game_over_text = font_big.render("GAME OVER", True, WHITE)
    highscore_text = font_small.render(f"Highscore: {snakegame.get_highscore()}", True, WHITE)

    screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, 200))
    screen.blit(highscore_text, (screen_width // 2 - highscore_text.get_width() // 2, 300))
    pygame.display.update()

    pygame.time.wait(5000)  # 5 Sekunden warten