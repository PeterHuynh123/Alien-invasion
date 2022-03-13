from bullet import Bullet
import pygame
import sys
from alien import Alien
from time import sleep

"""update pos by k_d/k_u event"""
def check_kd_event(event, ship, setting, screen, bullets):
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
            new_bullet = Bullet(setting, screen, ship)
            bullets.add(new_bullet)

def check_ku_event(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.is_moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.is_moving_left = False

"""check for event"""
def check_event(ship, game_setting, screen, bullets, btn_play, game_stats, aliens, game_settings):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            check_kd_event(event, ship, game_setting, screen, bullets)
        elif event.type == pygame.KEYUP:
            check_ku_event(event, ship)

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if btn_play.rect.collidepoint(mouse_x, mouse_y):
                play_btn_onClick_handler(game_stats, aliens, bullets, screen, game_settings, ship)
                

        
        
            

"""update scr"""

def play_btn_onClick_handler(game_stats, aliens, bullets, screen, game_settings, ship):
    game_stats.game_over = False
    game_stats.reset_statistic()

    aliens.empty()
    bullets.empty()

    create_fleet(screen, game_settings, aliens, ship)
    ship.center_ship()

def update_screen(game_setting, ship, screen, bullets, aliens, btn_play, game_stats):
    screen.fill(game_setting.bg_color)

    for bullet in bullets.sprites():
        bullet.draw()

    ship.draw_ship()
    aliens.draw(screen)

    if game_stats.game_over:
        btn_play.draw()

    pygame.display.flip()

def create_fleet(screen, game_settings, aliens, ship):
    alien = Alien(screen, game_settings)
    gap = 1.5
    alien_width = alien.rect.width * gap
    total_aliens_on_a_row = get_total_num_of_aliens_on_a_row(game_settings, alien, alien_width, gap)

    total_rows = get_total_rows(screen, ship, alien)

    for row in range(total_rows):
        for alien_index in range(total_aliens_on_a_row):
            create_new_alien(screen, game_settings, aliens, alien_index, alien_width, row)

def update_bullets(bullets, aliens, game_settings, screen, ship):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0 :
            bullets.remove(bullet)


    collision = pygame.sprite.groupcollide(aliens, bullets, True, True)
    print(collision)

    if (len(aliens)==0):
        bullets.empty()
        create_fleet(screen, game_settings, aliens, ship)

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


def change_fleet_direction(game_settings, aliens):
    for each_alien in aliens.sprites():
        each_alien.rect.y += game_settings.alien_fleet_drop_speed
    game_settings.alien_fleet_direction = -game_settings.alien_fleet_direction

def check_collision(game_settings, aliens):
    for each_alien in aliens.sprites():
        if each_alien.check_collision():
            change_fleet_direction(game_settings, aliens)
            break
        
def reset_game(game_settings, screen, game_stats, ship, aliens, bullets):
        if game_stats.ship_lives == 0:
            game_stats.game_over = True
        
        else:
            game_stats.ship_lives -= 1

            bullets.empty()
            aliens.empty()

            create_fleet(screen, game_settings, aliens, ship)
        
            sleep(1)

def update_fleet(game_settings, aliens, ship, screen, game_stats, bullets):
    check_collision(game_settings, aliens,)
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):
       reset_game(game_settings, screen, game_stats, ship, aliens, bullets)

    aliens_hit_bottom(game_settings, screen, game_stats, ship, aliens, bullets)
def aliens_hit_bottom(game_settings, screen, game_stats, ship, aliens, bullets):
    screen.get_rect()

    for alien in aliens.sprites():
        if alien.rect.bottom > screen.get_rect().bottom:
            reset_game(game_settings, screen, game_stats, ship, aliens, bullets)
            break