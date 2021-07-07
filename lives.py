import pygame
from pygame.sprite import Sprite


class Lives(Sprite):
    """Class that manages the player's lives"""

    def __init__(self, ai_game):
        """Initialize the life indicator and get its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        self.image = pygame.image.load('images/heart_40.bmp').convert_alpha()
        self.rect = self.image.get_rect()
