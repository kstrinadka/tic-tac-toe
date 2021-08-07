from game_object import GameObject
from colors import *
import pygame


def make_a_button():
    pass


class Button(GameObject):
    def __init__(self, screen: pygame.Surface, x, y, w=0, h=0, text: str = '', size_text=36):
        super(Button, self).__init__(x, y, w, h)

        self.pressed = False  # нажата ли клавиша
        self.color = BLUE
        self.text = text
        self.size_text = size_text
        self.screen = screen
        self.draw(screen)

        f1 = pygame.font.Font(None, self.size_text)
        text_surface = f1.render(self.text, True, RED)
        coord = text_surface.get_rect()
        coord[0], coord[1] = self.coordinate

        self.bounds = coord
        self.text_surface = text_surface

    def is_pressed(self, coordinates):
        x_pos, y_pos = coordinates

        # проверка попадания в кнопку
        if self.bounds.left <= x_pos <= self.bounds.right and self.bounds.top <= y_pos <= self.bounds.bottom:
            self.color = GREEN
            self.draw(self.screen)

        self.draw(self.screen)

    def is_not_pressed(self):
        self.color = BLUE
        self.draw(self.screen)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.bounds)
        if self.text:
            f1 = pygame.font.Font(None, self.size_text)
            text1 = f1.render(self.text, True, RED)
            coord = text1.get_rect()
            coord[0], coord[1] = self.coordinate
            pygame.draw.rect(surface, self.color, coord)
            surface.blit(text1, self.coordinate)
        pygame.display.update()
