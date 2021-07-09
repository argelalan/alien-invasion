import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Class that manages the aliens in Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize an alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load('images/alien.bmp').convert_alpha()
        self.rect = self.image.get_rect()

        self.x = self.rect.width
        self.y = self.rect.height

        self.x = float(self.x)

    def check_edges(self):
        """Check if aliens reach the edges of the screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Update the alien's position."""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
