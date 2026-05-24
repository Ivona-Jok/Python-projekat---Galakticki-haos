import pygame
import math
from core.projectile import Projectile
from config.settings import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_SPEED

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = self._create_ship()
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.x = float(self.rect.centerx)
        self.y = float(self.rect.centery)
        self.angle = 90
        self.level = 1
        self.last_shot = 0

    def _get_shoot_delay(self):
        return max(80, 300 - (self.level - 1) * 40)

    def _get_bullet_count(self):
        return min(self.level, 5)

    def _create_ship(self):
        surface = pygame.Surface((40, 50), pygame.SRCALPHA)
        pygame.draw.polygon(surface, (0, 200, 255), [
            (20, 0),
            (0, 50),
            (40, 50)
        ])
        pygame.draw.polygon(surface, (0, 100, 180), [
            (20, 8),
            (6, 46),
            (34, 46)
        ])
        return surface

    def update(self):
        # WASD kretanje
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]: self.y -= PLAYER_SPEED
        if keys[pygame.K_s]: self.y += PLAYER_SPEED
        if keys[pygame.K_a]: self.x -= PLAYER_SPEED
        if keys[pygame.K_d]: self.x += PLAYER_SPEED

        self.x = max(20, min(SCREEN_WIDTH - 20, self.x))
        self.y = max(20, min(SCREEN_HEIGHT - 20, self.y))
        self.rect.center = (int(self.x), int(self.y))

        # Rotacija prema mišu
        mouse_x, mouse_y = pygame.mouse.get_pos()
        dx = mouse_x - self.x
        dy = mouse_y - self.y
        self.angle = math.degrees(math.atan2(-dy, dx))

        rotated = pygame.transform.rotate(self.original_image, self.angle - 90)
        old_center = self.rect.center
        self.image = rotated
        self.rect = self.image.get_rect(center=old_center)

        # Pucanje držanjem desnog klika
        if pygame.mouse.get_pressed()[2]:
            self._try_shoot()

    def _try_shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self._get_shoot_delay():
            self.last_shot = now
            self._spawn_bullets()

    def _spawn_bullets(self):
        from ui.screens import GameScreen
        count = self._get_bullet_count()
        spread = 10   # ugao između projektila u stepenima

        if count == 1:
            self.projectiles_group.add(Projectile(self.x, self.y, self.angle))
        else:
            total_spread = (count - 1) * spread
            start_angle = self.angle - total_spread / 2

            for i in range(count):
                bullet_angle = start_angle + i * spread
                self.projectiles_group.add(
                    Projectile(self.x, self.y, bullet_angle)
                )

    def set_projectiles_group(self, group):
        self.projectiles_group = group