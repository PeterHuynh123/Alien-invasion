from turtle import screensize
from bullet import Bullet
import pygame
import sys
from alien import Alien

"""update pos by k_d/k_u event"""
def check_kd_event(event, ship, setting, window, bullets):
    if event.key == pygame.K_ESCAPE:
            sys.exit() 
    if event.key == pygame.K_RIGHT:
        # ship.rect.centerx += 10
        ship.is_moving_right = True
    elif event.key == pygame.K_LEFT:
        # ship.rect.centerx += 10
        ship.is_moving_left = True
    elif event.key == pygame.K_SPACE:
        if len(bullets) < setting.bullet_max_allowed:
            new_bullet = Bullet(setting, window, ship)
            bullets.add(new_bullet)

def check_ku_event(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.is_moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.is_moving_left = False

"""check for event"""
def check_event(ship, game_setting, window, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            check_kd_event(event, ship, game_setting, window, bullets)
        elif event.type == pygame.KEYUP:
            check_ku_event(event, ship)
        
            

"""update scr"""
def update_screen(game_setting, ship, window, bullets, aliens):
    window.fill(game_setting.bg_color)

    for bullet in bullets.sprites():
        bullet.draw()

    ship.draw_ship()
    aliens.draw(window)
    pygame.display.flip()

    

def update_bullets(bullets):
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0 :
            bullets.remove(bullet)

def get_total_num_of_aliens_on_a_row(game_settings, alien, alien_width, gap):
    available_space = game_settings.screen_width -  alien_width
    total_aliens_on_a_row = int(available_space / (gap * alien.rect.width))

    return total_aliens_on_a_row

def create_new_alien(screen, game_setings, aliens, alien_index, alien_width, row):
    alien = Alien(screen, game_setings)
    alien.x = alien.rect.x + alien_width * alien_index
    alien.rect.x = alien.x
    alien.rect.y = int(alien.rect.height + (alien.rect.height * 2 * row))
    aliens.add(alien)

def get_total_rows(screen, ship, alien):
    available_height = screen.get_height() - ship.rect.height - (alien.rect.height*3)
    total_rows = int(available_height / (alien.rect.height * 2))
    print(f"total row: {total_rows}")

    return total_rows

def create_fleet(screen, game_settings, aliens, ship):
    alien = Alien(screen, game_settings)
    gap = 1.5
    alien_width = alien.rect.width * gap
    total_aliens_on_a_row = get_total_num_of_aliens_on_a_row(game_settings, alien, alien_width, gap)

    total_rows = get_total_rows(screen, ship, alien)

    for row in range(total_rows):
        for alien_index in range(total_aliens_on_a_row):
            create_new_alien(screen, game_settings, aliens, alien_index, alien_width, row)

def update_fleet(aliens, screen):
    aliens.update(screen)
    
    # space = screen width - (gap * width of 1 alien)
    # tt num of aliens that can fits on on line 1 row = tt space/(gap*width of 1 alien)