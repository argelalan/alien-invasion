import pygame


class Ship:
    """Class that manages the ship for the Alien Invasion game."""

    def __init__(self, ai_game):
        """Initialize the ship and get its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/ship_75.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)
