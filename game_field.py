import pygame


class GameField:
    def __init__(self, width_screen = 600, height_screen = 400):
        self.game_array = [0, 0, 0,
                           0, 0, 0,
                           0, 0, 0,
                           ]
        self.game_over = False
        self.start_menu = True
        self.screen = pygame.display.set_mode((width_screen, height_screen))

    # ставит крестик или нолик
    def make_a_move(self):
        pass

    def start_menu(self):
        self.screen.fill((0, 0, 0))  # отрисовка экрана черным цветом




