import pygame
from config import screen_width

WHITE = (255, 255, 255)
DARK_GRAY = (40, 40, 40)
GREEN = (17, 24, 47)
BLUE = (93, 216, 228)
RED = (139, 0, 0)
EYE_COLOR = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)





def game_over_screen(screen, surface):
    font_big = pygame.font.SysFont("monospace", 60)
    font_small = pygame.font.SysFont("monospace", 30)
    screen.fill(DARK_GRAY)
    surface.fill(DARK_GRAY)

    game_over_text = font_big.render("GAME OVER", True, RED)

    screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, 100))
    pygame.display.update()

    pygame.time.wait(5000)  # 5 Sekunden warten