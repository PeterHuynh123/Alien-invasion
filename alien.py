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

        self.speed = 1

    def update(self, screen):
        self.rect.x += self.speed
        if self.rect.x > screen.get_width() - self.rect.width or self.rect.x < 0 + self.rect.width:
            for i in range(int(self.rect.height)):
                self.rect.y += 1
            self.speed = -self.speed
    def draw(self):
        self.screen.blit(self.sprite, self.rect)