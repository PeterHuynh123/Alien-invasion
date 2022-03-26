class Stats:
    def __init__(self, game_settings):
        self.game_setting = game_settings
        self.game_over = False
        self.score = 0
        self.reset_statistic()
        
    def reset_statistic(self):
        self.ship_lives = self.game_setting.ship_lives
        self.score = 0
    