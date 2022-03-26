from pygame import init


class Setting():
    def __init__(self):
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (200, 200, 200)
        
        self.ship_speed = 10
        self.ship_lives = 1

        self.bullet_width = 5
        self.bullet_height = 10
        self.bullet_speed = 10
        self.bullet_cl = 255, 0, 0
        self.bullet_max_allowed = 3

        self.alien_speed = 3
        self.alien_fleet_direction = 1 #-1 is left
        self.alien_fleet_drop_speed = 5

        self.alien_points = 0

        self.speeed_factor = 1.1

        self.init_dynamic_settings()

    def init_dynamic_settings(self):
        self.ship_speed = 12
        self.bullet_speed = 10
        self.alien_speed = 5
        self.alien_fleet_direction = 1

    def increase_speed(self):
        self.ship_speed = self.ship_speed * self.speeed_factor
        self.bullet_speed = self.bullet_speed * self.speeed_factor
        self.alien_speed = self.alien_speed * self.speeed_factor



