import pygame
from constant import *
from pygame.sprite import Sprite
from pygame.sprite import Group
from ship import Ship
class Score():
    def __init__(self, game_settings, screen, game_stats):
        self.game_settings = game_settings
        self.screen = screen
        self.game_stats = game_stats
        self.screen_rect = screen.get_rect()
        self.gap = 10

        self.text_color = (50, 50, 50)
        self.bg_color = (200, 200, 200)
        self.font = pygame.font.Font(None, 48)
        self.sprite = pygame.image.load('./sprite/ship.png')
        self.sprite = pygame.transform.scale(self.sprite, (self.sprite.get_width()//15, self.sprite.get_height()//15))
        
        self.render_level()   
        self.render_score(SCORE_TYPE_NORMAL)
        self.render_score(SCORE_TYPE_HIGHSCORE)
        self.render_lives()     
                
    
    def render_score(self, score_type):
        # rounded_score = int(round(self.game_stats.score, -1))
        # score = "{:,}".format(rounded_score)
        if score_type == SCORE_TYPE_NORMAL:
            rounded_score = int(self.game_stats.score)
            score = self.format_num(rounded_score)
            self.normal_score = self.font.render(score, True, self.text_color, self.bg_color)
            self.normal_score_rect = self.normal_score.get_rect()
            self.normal_score_rect.top = self.rendered_level_rect.bottom + 10
            self.normal_score_rect.left = self.screen_rect.left + 10

        if score_type == SCORE_TYPE_HIGHSCORE:
            rounded_score = int(self.game_stats.high_score)
            score = f"Highscore: {self.format_num(rounded_score)}"
            self.high_score = self.font.render(score, True, self.text_color, self.bg_color)
            self.high_score_rect = self.high_score.get_rect()
            self.high_score_rect.top = 10
            self.high_score_rect.right = self.screen_rect.right - 10
        # return rendered_score, score_rect

    def draw(self):
        self.screen.blit(self.normal_score, self.normal_score_rect)
        self.screen.blit(self.high_score, self.high_score_rect)
        self.screen.blit(self.rendered_level, self.rendered_level_rect)
        self.render_lives()

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

    def render_level(self):
        self.rendered_level = self.font.render( f"LV: {str(self.game_stats.level)}", True, self.text_color, self.bg_color)
        self.rendered_level_rect = self.rendered_level.get_rect()
        print(self.game_stats.level)
        self.rendered_level_rect.left = 10
        self.rendered_level_rect.top = 10

    def render_lives(self):
        # self.lives = Group()
        live = self.sprite
        for ship_lives in range(1, self.game_stats.ship_lives+1):
            live_rect = live.get_rect()
            live_rect.x = self.screen_rect.right - self.gap - ((self.gap + live_rect.width) * (ship_lives))
            live_rect.y = self.high_score_rect.bottom + self.gap
            self.screen.blit(live, live_rect)
