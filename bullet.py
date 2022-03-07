import pygame
from setting import *

from pygame.sprite import Sprite

"""inherited class from pygame"""
class Bullet(Sprite):
    def __init__(self, setting, screen, ship):
        super(Bullet, self).__init__() 

        self.screen = screen

        self.rect = pygame.Rect(0,0, setting.bullet_width, setting.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = (self.rect.y)
        self.speed = setting.bullet_speed
        self.color = setting.bullet_speed

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y


    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)