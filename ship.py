import pygame

class Ship():
    def __init__(self, screen, setting):
        self.screen = screen
        self.setting = setting

        self.sprite = pygame.image.load('./sprite/ship.png')
        self.sprite = pygame.transform.scale(self.sprite, (self.sprite.get_width()//8, self.sprite.get_height()//8))
        self.rect = self.sprite.get_rect()
        self.screen_rect = screen.get_rect()

        self.is_moving_right = False
        self.is_moving_left = False
        
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def update(self):
        if self.is_moving_right and (self.rect.right < self.screen_rect.right):
            self.rect.centerx += self.setting.ship_speed
        if self.is_moving_left and (self.rect.left > self.screen_rect.left):
            self.rect.centerx -= self.setting.ship_speed

    def draw_ship(self):
        self.screen.blit(self.sprite, self.rect)