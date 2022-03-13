class Stats:
    def __init__(self, game_settings):
        self.game_setting = game_settings
        self.reset_statistic()
        self.game_over = False

    def reset_statistic(self):
        self.ship_lives = self.game_setting.ship_lives
