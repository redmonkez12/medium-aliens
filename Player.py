import pygame


class Player:
    def __init__(self, game):
        self.screen = game.screen
        self.settings = game.settings  # new
        self.screen_rect = game.screen.get_rect()

        self.image = pygame.image.load("images/player.bmp")
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)  # new

        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.player_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.player_speed

        self.rect.x = self.x
