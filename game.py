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
from Sound import *
from constant import *
from menu import *


from time import sleep
def main():
    sound = Sound()
    pygame.init()
    clock = pygame.time.Clock()
    game_setting = Setting()
    game_stats = Stats(game_setting)

    screen = pygame.display.set_mode((game_setting.screen_width, game_setting.screen_height))
    pygame.display.set_caption('Alien invason')

    menu = Menu("!!!WELCOME!!!", screen)

    ship = Ship(screen, game_setting)
    bullets = Group()

    # alien = Alien(screen, game_setting)
    aliens = Group()

    func.create_fleet(screen, game_setting, aliens, ship)

    btn_play = Button(screen, "Hit ENTER!!") 
    score = Score(game_setting, screen, game_stats)
    
    pygame.mouse.set_visible(False)
    sound.bgm.play(loops=-1)
    while True:
        
        func.check_event(ship, game_setting, screen, bullets, btn_play, game_stats, aliens, game_setting, score, sound, menu)
        
        if game_stats.game_state == GAME_STATE_MENU:
            menu.draw_menu_frame()
            pygame.mouse.set_visible(True)
            for event in pygame.event.get():
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if menu.play_button.rect.collidepoint(mouse_x, mouse_y):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        game_stats.game_state == GAME_STATE_PLAY
                        func.start_a_new_game(game_stats, aliens, bullets, screen, game_setting, ship, score)
                        print("clicked")
        else:
            if game_stats.game_over == False:
                btn_play.draw()
                ship.update()
                bullets.update()

                func.update_bullets(bullets, aliens, game_setting, screen, ship, game_stats, score, sound)

                func.update_fleet(game_setting, aliens, ship, screen, game_stats, bullets, score, sound)

                func.update_screen(game_setting, ship, screen, bullets, aliens, btn_play, game_stats, score)
        clock.tick(60)

if __name__ == "__main__":
    main()