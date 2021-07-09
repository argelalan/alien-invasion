import pygame


class Sounds:
    """Class that manages sound effects for game."""

    def __init__(self):
        """Initialize attributes for the game's sounds"""
        self.start_noise = pygame.mixer.Sound('sounds/start_noise.wav')
        self.game_over_sound = pygame.mixer.Sound('sounds/game_over.wav')
        self.gun_sound = pygame.mixer.Sound('sounds/gun_shot.wav')
        self.damage_sound = pygame.mixer.Sound('sounds/damage.wav')
        self.player_hit_sound = pygame.mixer.Sound('sounds/player_hit.wav')

    def play_start_noise(self):
        """Play and stop the start noise."""
        pygame.mixer.Sound.play(self.start_noise)
        pygame.mixer.music.stop()

    def play_game_over_sound(self):
        """Play and stop the game over sound."""
        pygame.mixer.Sound.play(self.game_over_sound)
        pygame.mixer.music.stop()

    def play_gun_sound(self):
        """Play and stop the gun sound."""
        pygame.mixer.Sound.play(self.gun_sound)
        pygame.mixer.music.stop()

    def play_damage_sound(self):
        """Play and stop the damage sound."""
        pygame.mixer.Sound.play(self.damage_sound)
        pygame.mixer.music.stop()

    def play_player_hit_sound(self):
        """Play and stop the player hit sound."""
        pygame.mixer.Sound.play(self.player_hit_sound)
        pygame.mixer.music.stop()
