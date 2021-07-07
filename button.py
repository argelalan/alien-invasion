import pygame.font


class Button:

    def __init__(self, ai_game, msg):
        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Set button dimensions, colors, font, and size.
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)

        # Create button's rect object and center it on the screen.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button message is prepped only once.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn the button into a rendered image."""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw the button to the screen."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image.convert(), self.msg_image_rect)
