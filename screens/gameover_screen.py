import pygame
import sys
from config import screen_width, screen_height,WHITE, GREEN


def game_over_screen(screen, surface):
    font_big = pygame.font.SysFont("monospace", 60)
    font_small = pygame.font.SysFont("monospace", 30)


    button_rect = pygame.Rect(screen_width // 2 - 100, screen_height // 2 + 50, 200, 50)

    while True:
        surface.fill((GREEN))


        text = font_big.render("Game Over", True, (WHITE))
        surface.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - 50))


        pygame.draw.rect(surface, (0, 0, 0), button_rect)
        button_text = font_small.render("Play Again", True, (WHITE))
        surface.blit(button_text, (button_rect.x + 20, button_rect.y + 10))

        screen.blit(surface, (0, 0))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()


