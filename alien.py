import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Class that manages the aliens in Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize an alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen

        self.image = pygame.image.load('images/alien_2.bmp').convert_alpha()
        self.rect = self.image.get_rect()

        self.x = self.rect.width
        self.y = self.rect.height

        self.x = float(self.x)
