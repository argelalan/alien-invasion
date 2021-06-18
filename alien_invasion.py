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
            # Checks for user events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen with every pass through the loop.
            self.screen.fill(self.settings.bg_color)

            # Draw ship to screen.
            self.ship.blitme()

            # Show the most recently drawn screen.
            pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
