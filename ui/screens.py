import pygame
from config.settings import *
from core.player import Player

class GameScreen:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 36)
        self.font_small = pygame.font.SysFont(None, 26)

        self.all_sprites = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()

        self.player = Player()
        self.player.set_projectiles_group(self.projectiles)
        self.all_sprites.add(self.player)

    def update(self):
        self.all_sprites.update()
        self.projectiles.update()

    def draw(self):
        self.screen.fill(BLACK)

        for i in range(0, SCREEN_WIDTH, 50):
            for j in range(0, SCREEN_HEIGHT, 50):
                pygame.draw.circle(self.screen, (50, 50, 80), (i, j), 1)

        self.projectiles.draw(self.screen)
        self.all_sprites.draw(self.screen)

        nivo_txt = self.font.render(f"Nivo: {self.player.level}", True, YELLOW)
        info_txt = self.font_small.render(
            f"Projektili: {self.player._get_bullet_count()}  |  "
            f"Delay: {self.player._get_shoot_delay()}ms  |  "
            f"[+/-] nivo", True, WHITE)

        self.screen.blit(nivo_txt, (10, 10))
        self.screen.blit(info_txt, (10, 46))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_EQUALS or event.key == pygame.K_PLUS:
                self.player.level = min(self.player.level + 1, 5)
            if event.key == pygame.K_MINUS:
                self.player.level = max(self.player.level - 1, 1)
        return None