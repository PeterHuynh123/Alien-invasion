import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, screen, game_settings):
        super(Alien, self).__init__()
        self.screen = screen
        self.game_settings = game_settings

        self.image = pygame.image.load("./sprite/alien.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width()//5, self.image.get_height()//5))
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def check_collision(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right: #right border
            return True
        elif self.rect.left < 0: #left border
            return True

    def update(self):
       self.x += self.game_settings.alien_speed * self.game_settings.alien_fleet_direction
       self.rect.x = self.x
    def draw(self):
        self.screen.blit(self.sprite, self.rect)

    

        