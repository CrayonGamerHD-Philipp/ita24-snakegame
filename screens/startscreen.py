import pygame
import sys
from config import WHITE, screen_height, screen_width, RED, BLUE, GREEN, YELLOW



def draw_button(surface, text, x, y, width, height, color, hover_color, font, mouse_pos, click):
    button_rect = pygame.Rect(x, y, width, height)
    if button_rect.collidepoint(mouse_pos):
        pygame.draw.rect(surface, hover_color, button_rect)
        if click[0]:
            return True
    else:
        pygame.draw.rect(surface, color, button_rect)

    text_surf = font.render(text, True, WHITE)
    text_rect = text_surf.get_rect(center=button_rect.center)
    surface.blit(text_surf, text_rect)
    return False


def start_screen(screen, surface):
    font = pygame.font.SysFont("monospace", 50)
    button_font = pygame.font.SysFont("monospace", 30)

    # Bild laden ("start_background.png")
    background_img = pygame.image.load("images/start_background.png").convert()

    #Bild auf Bildschirmgröße skalieren
    background_img = pygame.transform.scale(background_img, (screen_width, screen_height))

    while True:
        screen.blit(background_img, (0, 0))  # Bild als Hintergrund zeichnen
        surface.fill((0, 0, 0, 0))  # Oberfläche transparent oder andere Farbe


        mouse_pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        start_clicked = draw_button(screen, "Start", 300, 240, 200, 60, GREEN, BLUE, button_font, mouse_pos, click)
        Settings_clicked = draw_button(screen, "Settings", 300, 320, 200, 60,GREEN , BLUE, button_font, mouse_pos, click)
        exit_clicked = draw_button(screen, "Exit", 300, 400, 200, 60, RED, BLUE, button_font, mouse_pos, click)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

        if start_clicked:
            return
        elif exit_clicked:
            pygame.quit()
            sys.exit()