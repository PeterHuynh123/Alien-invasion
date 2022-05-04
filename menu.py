import pygame

class Menu():
    def __init__(self, msg, screen):
        self.msg = msg
        self.screen = screen
        self.font = pygame.font.Font(None, 40)
        self.font_img = self.font.render(msg, True, (50, 50, 50), (200, 200 ,200))
        self.font_img_rect = self.font_img.get_rect()
    def draw_menu_frame(self):
        self.screen.fill((200, 200 ,200))
        self.screen.blit(self.font_img, (self.font_img_rect.centerx+self.font_img.get_width(), 200))
        pygame.display.flip()
