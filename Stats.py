from asyncio import constants
import json
from constant import *

class Stats:
    def __init__(self, game_settings):
        self.game_setting = game_settings
        self.game_over = False
        self.score = 0
        self.reset_statistic()
        self.high_score = 0
        self.read_high_score()
        self.level = 1
        self.game_state = GAME_STATE_MENU

    def reset_statistic(self):
        self.ship_lives = self.game_setting.ship_lives
        self.score = 0
        self.level = 1
        print("function called")
    def read_high_score(self):
        with open ("./data.json", 'r') as file:
            data = json.load(file)
            self.high_score = data['high_score']
            file.close()
                