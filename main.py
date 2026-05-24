import pygame
import sys
from config.settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, TITLE
from ui.menu import MainMenu
from ui.screens import GameScreen

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    current_screen = "menu"
    menu = MainMenu(screen)
    game = GameScreen(screen)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            if current_screen == "menu":
                result = menu.handle_event(event)
                if result == "game":
                    current_screen = "game"
            elif current_screen == "game":
                game.handle_event(event)

        if current_screen == "menu":
            menu.draw()
        elif current_screen == "game":
            game.update()
            game.draw()

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()