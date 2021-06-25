class Settings:
    """Class that stores all settings for Alien Invasion game."""

    def __init__(self):
        """Initialize the game's settings."""
        self.screen_height = 1200
        self.screen_width = 800
        self.bg_color = (0, 2, 42)
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self. bullet_color = (0, 242, 0)
        self.bullet_limit = 1000

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # 1 represents right; -1 represents left.
        self.fleet_direction = 1
