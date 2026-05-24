# import pygame
# import sys

# pygame.init()

# screen = pygame.display.set_mode((800, 600))
# pygame.display.set_caption("Galaktički haos")
# clock = pygame.time.Clock()

# font = pygame.font.SysFont(None, 64)

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     screen.fill((0, 0, 0))
    
#     tekst = font.render("Galaktički haos radi!", True, (255, 255, 0))
#     screen.blit(tekst, (150, 270))
    
#     pygame.display.flip()
#     clock.tick(60)

# pygame.quit()
# sys.exit()