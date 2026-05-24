import pygame
import math

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init__()
        self.speed = 10
        self.angle = angle
        self.x = float(x)
        self.y = float(y)
        self.vx = math.cos(math.radians(angle)) * self.speed
        self.vy = -math.sin(math.radians(angle)) * self.speed

        # Tanka duga linija rotirana u smjeru pucanja
        self.original_image = pygame.Surface((4, 20), pygame.SRCALPHA)
        pygame.draw.rect(self.original_image, (255, 255, 80), (0, 0, 4, 20))

        self.image = pygame.transform.rotate(self.original_image, angle - 90)
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.rect.center = (int(self.x), int(self.y))

        if (self.rect.right < 0 or self.rect.left > 800 or
                self.rect.bottom < 0 or self.rect.top > 600):
            self.kill()