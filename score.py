import pygame

class Score():
    def __init__(self, game_settings, screen, game_stats):
        self.game_settings = game_settings
        self.screen = screen
        self.game_stats = game_stats
        self.screen_rect = screen.get_rect()

        self.text_color = (50, 50, 50)
        self.bg_color = (200, 200, 200)
        self.font = pygame.font.Font(None, 48)
        self.render_score()
            
                
    
    def render_score(self):
        # rounded_score = int(round(self.game_stats.score, -1))
        # score = "{:,}".format(rounded_score)
        # rounded_score = int(self.game_stats.score)
        score = self.format_num(self.game_stats.score)
        print("Score:", self.game_stats.score)
        self.rendered_score = self.font.render(score, True, self.text_color, self.bg_color)

        self.score_rect = self.rendered_score.get_rect()
        self.score_rect.left = self.screen_rect.left = 10
        self.score_rect.top = 20

    def draw(self):
        self.screen.blit(self.rendered_score, self.score_rect)

    def format_num(self, num):
        num = str(num)
        if len(num) <= 3:
            return num
        new_num = ''
        skip_num = len(num)%3
        for k in range(skip_num):
            new_num += num[k]
            if skip_num == 0:
                new_num += ','
        for i in range(len(num)-skip_num):
            if i % 3 == 0 and i != 0:
                new_num += ','
            new_num += num[i+skip_num]
        print(new_num)
        return new_num
