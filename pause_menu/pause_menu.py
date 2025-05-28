import pygame
import sys

from config import BLACK,GRAY, screen_height, screen_width, BLUE, RED, GREEN, WHITE


def pause_screen(screen, surface):

    font = pygame.font.SysFont("monospace", 40)
    small_font = pygame.font.SysFont("monospace", 30)

    surface.fill(GREEN)

    pause_text = font.render("PAUSE", True, WHITE)
    continue_text = small_font.render("Drücke W zum Weiterspielen", True, WHITE)
    exit_text = small_font.render("Drücke E zum Beenden", True, WHITE)

    surface.blit(pause_text, (screen_width // 2 - pause_text.get_width() // 2, screen_height // 2 - 100))
    surface.blit(continue_text, (screen_width // 2 - continue_text.get_width() // 2, screen_height // 2))
    surface.blit(exit_text, (screen_width // 2 - exit_text.get_width() // 2, screen_height // 2 + 50))

    screen.blit(surface, (0, 0))
    pygame.display.update()

    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    paused = False
                elif event.key == pygame.K_e:
                    pygame.quit()
                    sys.exit()
