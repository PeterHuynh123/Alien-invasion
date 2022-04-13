from bullet import Bullet
import pygame
import sys
from alien import Alien
from time import sleep
from constant import *
import json
"""update pos by k_d/k_u event"""
def check_kd_event(event, ship, setting, screen, bullets, game_stats):
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
    elif event.key == pygame.K_RETURN:
        setting.increase_speed()

def check_ku_event(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.is_moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.is_moving_left = False

"""check for event"""
def check_event(ship, game_setting, screen, bullets, btn_play, game_stats, aliens, game_settings, score):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            check_kd_event(event, ship, game_setting, screen, bullets, game_stats)
            if event.key == pygame.K_RETURN and game_stats.game_over == True:
                reset_game(game_settings, screen, game_stats, ship, aliens, bullets, score)
        elif event.type == pygame.KEYUP:
            check_ku_event(event, ship)

        mouse_x, mouse_y = pygame.mouse.get_pos()
        if btn_play.rect.collidepoint(mouse_x, mouse_y):
            if event.type == pygame.MOUSEBUTTONDOWN:
                play_btn_onClick_handler(game_stats, aliens, bullets, screen, game_settings, ship, score)
            else:
                pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
                btn_play.bg_color = (40, 101, 158)
                btn_play.display_message("Play!")
                update_screen(game_setting, ship, screen, bullets, aliens, btn_play, game_stats, score)
                
        else:
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)
            btn_play.bg_color = (50, 111, 168)
            btn_play.display_message("Play!")
            update_screen(game_setting, ship, screen, bullets, aliens, btn_play, game_stats, score)
            

"""update scr"""
def game_start(game_settings, screen, ship, aliens, bullets, score  ):
    bullets.empty()
    aliens.empty()
    score.render_level()
    create_fleet(screen, game_settings, aliens, ship)
    ship.center_ship()

    sleep(1)

def play_btn_onClick_handler(game_stats, aliens, bullets, screen, game_settings, ship, score):
    if game_stats.game_over == True:
        overwrite_highscore(game_stats)
        game_stats.game_over = False
        game_stats.reset_statistic()
        # score.render_score(SCORE_TYPE_NORMAL)

        aliens.empty()
        bullets.empty()

        create_fleet(screen, game_settings, aliens, ship)
        pygame.mouse.set_visible(False)
        ship.center_ship()
        game_settings.init_dynamic_settings()

def update_screen(game_setting, ship, screen, bullets, aliens, btn_play, game_stats, score):
    screen.fill(game_setting.bg_color)
    score.draw()

    for bullet in bullets.sprites():
        bullet.draw()

    ship.draw_ship()
    aliens.draw(screen)

    if game_stats.game_over:
        btn_play.draw()
        
    pygame.display.flip()

def create_fleet(screen, game_settings, aliens, ship):
    alien = Alien(screen, game_settings)
    gap = 1.7
    alien_width = alien.rect.width * gap
    total_aliens_on_a_row = get_total_num_of_aliens_on_a_row(game_settings, alien, alien_width, gap)

    total_rows = get_total_rows(screen, ship, alien)

    for row in range(total_rows):
        for alien_index in range(total_aliens_on_a_row):
            create_new_alien(screen, game_settings, aliens, alien_index, alien_width, row)

def update_bullets(bullets, aliens, game_settings, screen, ship, game_stats, score):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0 :
            bullets.remove(bullet)
    collision = pygame.sprite.groupcollide(aliens, bullets, True, True)
    if collision:
        for aliens in collision.values():  
            game_stats.score += game_settings.alien_points * len(aliens)
            score.render_score(SCORE_TYPE_NORMAL)
        replace_highscore(game_stats, score)

    if (len(aliens)==0):
        bullets.empty()
        create_fleet(screen, game_settings, aliens, ship)
        ship.center_ship()
        game_settings.increase_speed()
        game_stats.level += 1
        score.render_level()
        sys.sleep(1)

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
        
def reset_game(game_settings, screen, game_stats, ship, aliens, bullets, score):
        if game_stats.ship_lives == 1:
            game_stats.game_over = True
            pygame.mouse.set_visible(True)
            game_stats.reset_statistic() 
            game_start(game_settings, screen, ship, aliens, bullets, score)    
            print(game_stats.ship_lives)
        else:
            game_stats.ship_lives -= 1

            bullets.empty()
            aliens.empty()

            create_fleet(screen, game_settings, aliens, ship)
            ship.center_ship()
            sleep(1)

def update_fleet(game_settings, aliens, ship, screen, game_stats, bullets, score):
    check_collision(game_settings, aliens,)
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):
       reset_game(game_settings, screen, game_stats, ship, aliens, bullets, score)

    aliens_hit_bottom(game_settings, screen, game_stats, ship, aliens, bullets, score)

def aliens_hit_bottom(game_settings, screen, game_stats, ship, aliens, bullets, score):
    screen.get_rect()

    for alien in aliens.sprites():
        if alien.rect.bottom > screen.get_rect().bottom:
            reset_game(game_settings, screen, game_stats, ship, aliens, bullets, score)
            break

def replace_highscore(game_stats, score):
    if game_stats.score > game_stats.high_score:
        game_stats.high_score = game_stats.score
        score.render_score(SCORE_TYPE_HIGHSCORE)

def overwrite_highscore(game_stats):
    file_content = ''
    with open ("./data.json", "r") as file_r:
        file_content = json.load(file_r)
        if file_content["high_score"] < game_stats.high_score:
            file_content["high_score"] = game_stats.high_score

        with open ("./data.json", "w") as file_w:
            json.dump(file_content, file_w, indent=4)
            file_w.close()
        file_r.close()