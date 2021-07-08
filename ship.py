import pygame


class Ship:
    """Class that manages the ship for the Alien Invasion game."""

    def __init__(self, ai_game):
        """Initialize the ship and get its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        self.image = pygame.image.load('images/test_ship.bmp').convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        # Store decimal value for ship's horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        self.rect.x = self.x
        self.rect.y = self.y

    def draw_ship(self):
        """Draw ship to screen."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center ships to the mid-bottom of the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
