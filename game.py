import pygame
import sys

from alien import Alien
from button import Button
import function as func
from setting import Setting
from ship import Ship
from Stats import Stats
from pygame.sprite import Group
from score import Score
import json

from time import sleep
def main():
    pygame.init()
    clock = pygame.time.Clock()
    game_setting = Setting()
    game_stats = Stats(game_setting)

    screen = pygame.display.set_mode((game_setting.screen_width, game_setting.screen_height))
    pygame.display.set_caption('Alien invason')


    ship = Ship(screen, game_setting)
    bullets = Group()

    # alien = Alien(screen, game_setting)
    aliens = Group()

    func.create_fleet(screen, game_setting, aliens, ship)

    btn_play = Button(screen, "PLAY!!") 
    score = Score(game_setting, screen, game_stats)
    
    pygame.mouse.set_visible(False)
    while True:
        
        func.check_event(ship, game_setting, screen, bullets, btn_play, game_stats, aliens, game_setting, score)
        if game_stats.game_over == False:
            btn_play.draw()
            ship.update()
            bullets.update()

            func.update_bullets(bullets, aliens, game_setting, screen, ship, game_stats, score)

            func.update_fleet(game_setting, aliens, ship, screen, game_stats, bullets, score)

            func.update_screen(game_setting, ship, screen, bullets, aliens, btn_play, game_stats, score)
        
            clock.tick(60)

if __name__ == "__main__":
    main()