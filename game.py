import pygame
import sys

from alien import Alien
import function as func
from setting import Setting
from ship import Ship
from pygame.sprite import Group

def main():
    pygame.init()
    clock = pygame.time.Clock()
    game_setting = Setting()

    window = pygame.display.set_mode((game_setting.screen_width, game_setting.screen_height))
    pygame.display.set_caption('Alien invason')


    ship = Ship(window, game_setting)
    bullets = Group()

    # alien = Alien(window, game_setting)
    aliens = Group()

    func.create_fleet(window, game_setting, aliens, ship)

    while True:
        func.check_event(ship, game_setting, window, bullets)
        ship.update()
        bullets.update()

        func.update_bullets(bullets)

        func.update_fleet(aliens, window)

        func.update_screen(game_setting, ship, window, bullets, aliens)
        


        

if __name__ == "__main__":
    main()