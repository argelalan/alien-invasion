import json

import pygame.font
from pygame.sprite import Group

from lives import Lives


class Scoreboard:
    """Class that manages game scoreboard."""

    def __init__(self, ai_game):
        """Initialize scoreboard attributes."""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.filename = 'high_score.json'

        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont('default', 30)

        self.read_high_score()
        self.prep_images()

    def prep_images(self):
        """Prepare all the images for the scoreboard."""
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_lives()

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = round(self.stats.score, -1)
        score_str = "Score: " + "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Turn high score into a rendered image."""
        self.high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(self.high_score)
        self.high_score_image = self.font.render(
            high_score_str, True, self.text_color, self.settings.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Turn level into a rendered image"""
        level_str = "Level: " + str(self.stats.level)
        self.level_image = self.font.render(
            level_str, True, self.text_color, self.settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_lives(self):
        """Show how many lives the player has left."""
        self.lives = Group()
        for life_number in range(self.stats.ships_left):
            life = Lives(self.ai_game)
            life.rect.x = 10 + life_number * life.rect.width
            life.rect.y = 10
            self.lives.add(life)

    def show_score(self):
        """Draw scores, level, and lives left to the screen."""
        self.screen.blit(self.score_image.convert(), self.score_rect)
        self.screen.blit(self.high_score_image.convert(), self.high_score_rect)
        self.screen.blit(self.level_image.convert(), self.level_rect)
        self.lives.draw(self.screen)

    def check_high_score(self):
        """Check if current score is greater than the high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def store_high_score(self):
        """Write the current high score to a file to save it."""
        try:
            with open(self.filename, 'w') as f:
                f.write(str(self.high_score))
        except FileNotFoundError:
            pass

    def read_high_score(self):
        """Change the current high score to the last one stored."""
        try:
            with open(self.filename) as f:
                new_high_score = json.load(f)
        except json.decoder.JSONDecodeError:
            pass
        else:
            self.stats.high_score = int(new_high_score)
