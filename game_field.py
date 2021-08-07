import pygame


class GameField:
    def __init__(self, screen: pygame.Surface):
        self.game_array = [0, 0, 0,
                           0, 0, 0,
                           0, 0, 0,
                           ]
        self.game_over = False
        self.start_menu = True
        self.screen = screen

    # ставит крестик или нолик
    def make_a_move(self):
        pass

    def start_menu(self):
        self.screen.fill((0, 0, 0))  # отрисовка экрана черным цветом




