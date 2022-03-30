import pygame
from constant import *
class Score():
    def __init__(self, game_settings, screen, game_stats):
        self.game_settings = game_settings
        self.screen = screen
        self.game_stats = game_stats
        self.screen_rect = screen.get_rect()

        self.text_color = (50, 50, 50)
        self.bg_color = (200, 200, 200)
        self.font = pygame.font.Font(None, 48)
        
        self.render_score(SCORE_TYPE_NORMAL)
        self.render_score(SCORE_TYPE_HIGHSCORE)


            
                
    
    def render_score(self, score_type):
        # rounded_score = int(round(self.game_stats.score, -1))
        # score = "{:,}".format(rounded_score)

        if score_type == SCORE_TYPE_NORMAL:
            rounded_score = int(self.game_stats.score)
            score = self.format_num(rounded_score)
            self.normal_score = self.font.render(score, True, self.text_color, self.bg_color)
            self.normal_score_rect = self.normal_score.get_rect()
            self.normal_score_rect.top = 10
            self.normal_score_rect.left = self.screen_rect.left + 10

        if score_type == SCORE_TYPE_HIGHSCORE:
            rounded_score = int(self.game_stats.high_score)
            score = self.format_num(rounded_score)
            self.high_score = self.font.render(score, True, self.text_color, self.bg_color)
            self.high_score_rect = self.high_score.get_rect()
            self.high_score_rect.top = 10
            self.high_score_rect.right = self.screen_rect.right - 10
        # return rendered_score, score_rect

    def draw(self):
        self.screen.blit(self.normal_score, self.normal_score_rect)
        self.screen.blit(self.high_score, self.high_score_rect)



    def format_num(self, num):
        num = str(num)
        if len(num) <= 3:
            return num
        new_num = ''
        skip_num = len(num)%3
        for k in range(skip_num):
            new_num += num[k]
            if k == skip_num-1:
                new_num += ','
        for i in range(len(num)-skip_num):
            if i % 3 == 0 and i != 0:
                new_num += ','
            new_num += num[i+skip_num]
        return new_num