import pygame

class Button():
    def __init__(self, screen, game_settings, message):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width, self.height = 200, 50
        self.bg_color = (50, 111, 168)
        self.text_color = (50, 168, 81)
        self.font = pygame.font.SysFont(None, 50)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.display_message(message)

    def display_message(self, message):
        self.rendered_msg = self.font.render(
            message,
            True,
            self.text_color,
            self.bg_color
        )
        self.rendered_msg_rect = self.rendered_msg.get_rect()
        self.rendered_msg_rect.center = self.rect.center

    def draw(self):
        self.screen.fill(self.bg_color, self.rect)
        self.screen.blit(self.rendered_msg, self.rendered_msg_rect)