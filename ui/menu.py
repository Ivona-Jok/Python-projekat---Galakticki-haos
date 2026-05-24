import pygame
from config.settings import *

class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.font_title  = pygame.font.SysFont(None, 80)
        self.font_button = pygame.font.SysFont(None, 48)

        # Dugme START — centriran na ekranu
        self.button_rect = pygame.Rect(0, 0, 200, 60)
        self.button_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)

    def draw(self):
        # Pozadina
        self.screen.fill(DARK_GREY)

        # Naslov igrice
        title = self.font_title.render("Galaktički haos", True, YELLOW)
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 80))
        self.screen.blit(title, title_rect)

        # Hover efekat na dugmetu
        mouse_pos = pygame.mouse.get_pos()
        if self.button_rect.collidepoint(mouse_pos):
            color = BUTTON_HOVER_COLOR
        else:
            color = BUTTON_COLOR

        # Crtanje dugmeta
        pygame.draw.rect(self.screen, color, self.button_rect, border_radius=10)
        button_text = self.font_button.render("START", True, BUTTON_TEXT_COLOR)
        text_rect = button_text.get_rect(center=self.button_rect.center)
        self.screen.blit(button_text, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(event.pos):
                return "game"   # signal da prelazimo na igricu
        return None