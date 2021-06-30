class Settings:
    """Class that stores all settings for Alien Invasion game."""

    def __init__(self):
        """Initialize the game's static settings."""
        self.screen_height = 1200
        self.screen_width = 800
        self.bg_color = (0, 2, 42)

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 242, 0)
        self.bullet_limit = 1000

        # Alien settings
        self.fleet_drop_speed = 10

        # Number of ships in game
        self.ship_limit = 3

        # How quickly the game speeds up.
        self.speedup_scale = 1.4

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize game's dynamic settings."""
        self.ship_speed = 1.5
        self.bullet_speed = 2
        self.alien_speed = 1.0
        # 1 represents right; -1 represents left.
        self.fleet_direction = 1

    def speedup_game(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
