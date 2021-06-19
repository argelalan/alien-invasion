import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Class that manages overall game behaviors and features."""

    def __init__(self):
        """Initialize game and create game resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.height, self.settings.width))
        pygame.display.set_caption('Alien Invasion')

        self.ship = Ship(self)

    def run_game(self):
        """Start main loop of game."""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Monitor mouse and keyboard events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Update the images on the screen and flip the screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
