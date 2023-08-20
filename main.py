import pygame
import sys

from Settings import Settings
from Player import Player


class AlienInvasion:

    def __init__(self):
        pygame.init()

        self.settings = Settings()  # use settings class

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        # use constants
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Aliens")
        self.ship = Player(self)

        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                elif event.key == pygame.K_q:
                    sys.exit()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()


if __name__ == "__main__":
    game = AlienInvasion()
    game.run()
