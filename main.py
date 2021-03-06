import pygame
import sys
from colors import *
from winning_positions import *
import button


# рисует крестик в заданных координатах
def draw_cross_game(screen_local, pos: tuple):
    x, y = pos
    pygame.draw.line(screen_local, RED, [x - 80, y - 60], [x + 80, y + 60], 3)
    pygame.draw.line(screen_local, RED, [x - 80, y + 60], [x + 80, y - 60], 3)


def get_victory(table: list, screen_local):
    line_squares = []
    for i in range(len(table)):
        if table[i] != 0:
            line_squares.append(i)

    line_coordinates = []

    for i in line_squares:
        line_coordinates.append(coordinates_for_draw(i))

    pygame.draw.lines(screen_local, WHITE, True, line_coordinates, 5)

    return


def draw(screen):
    pass


def check_victory(matrix: list, player: int, screen):
    table = [0, 0, 0,
             0, 0, 0,
             0, 0, 0,
             ]

    flag = 1
    for i in range(len(matrix)):
        if matrix[i] == 0:
            flag = 0

    for i in range(len(matrix)):
        table[i] = matrix[i]

    for i in range(len(table)):
        if player != table[i]:
            table[i] = 0
        else:
            table[i] = 1

    print('---cheking table----')
    print_game_array(table)
    print('--------------------')

    for position in WIN_POSITIONS:
        count = 0
        for k in range(len(position)):
            if position[k] == 1 and table[k] == 1:
                count += 1
                if count == 3:
                    get_victory(position, screen)
                    return True

    if flag:
        # matrix = new_game(screen)
        return True

    return False


# рисует нолик в заданных координатах
def draw_circle_game(screen, pos: tuple):
    pygame.draw.circle(screen, BLUE, pos, 60, 3)


# возвращает координаты для отрисовки крестика или нолика в конкретной ячейке
def coordinates_for_draw(cell: int):
    dictionary = {0: (100, 66), 1: (300, 66), 2: (500, 66), 3: (100, 200), 4: (300, 200), 5: (500, 200),
                  6: (100, 333), 7: (300, 333), 8: (500, 333)}

    if cell not in dictionary:
        print(" ERROR coordinates_for_draw")
        exit(1)

    return dictionary[cell]


# проверят по координате, в какую ячейку нажала мышка
def check_square(pos: tuple):
    x, y = pos

    if 0 < x < 200 and 0 < y < 133:
        return 0
    if 200 < x < 400 and 0 < y < 133:
        return 1
    if 400 < x < 600 and 0 < y < 133:
        return 2
    if 0 < x < 200 and 133 < y < 266:
        return 3
    if 200 < x < 400 and 133 < y < 266:
        return 4
    if 400 < x < 600 and 133 < y < 266:
        return 5
    if 0 < x < 200 and 266 < y < 400:
        return 6
    if 200 < x < 400 and 266 < y < 400:
        return 7
    if 400 < x < 600 and 266 < y < 400:
        return 8

    print("ERRROROROROR")
    exit(1)


def print_game_array(matrix: list):
    for i in range(len(matrix)):
        print(matrix[i], end=' ')
        if (i + 1) % 3 == 0:
            print()


def new_game(screen):
    screen.fill((0, 0, 0))  # отрисовка экрана черным цветом

    draw_field(screen)

    matrix = [0, 0, 0,
              0, 0, 0,
              0, 0, 0,
              ]

    pygame.time.delay(1000)

    return matrix


class Manager:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.condition = 0
        self.game_array = [0, 0, 0,
                           0, 0, 0,
                           0, 0, 0,
                           ]
        self.game_over = False

        # чей ход. 0 - не важно, 1 - нолик, 2 - крестик
        self.whose_move = 0
        self.winner = 0

    def next_condition(self):
        '''
        0 - Начальная меню
        1 - Сама игра
        2 - Конец игры, потом опять надо начальное меню запустить

        :return:
        '''

        self.condition = (self.condition + 1) % 3

    def main_cycle(self):
        while 1:
            clock.tick(60)

            events = pygame.event.get()
            # print(events)
            for i in events:
                if self.condition == 0:
                    self.start_menu(i)


                if self.condition == 1:
                    draw_field(self.screen)
                    self.make_a_move(i)

                events = []

                if self.condition == 2:
                    pygame.time.delay(100)
                    self.victory(i)

            pygame.display.update()


    def victory(self, event: pygame.event):


        self.screen.fill((0, 0, 0))
        if self.winner == 1:
            draw_circle_game(self.screen, (300, 66))
        if self.winner == 2:
            draw_cross_game(self.screen, (300, 66))
        end_button = button.Button(self.screen, 250, 200, 20, 20, 'Win', 80)
        if event.type == pygame.QUIT:
            print(pygame.QUIT)
            print(i)
            print(i.type)
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            print('down')
            end_button.is_pressed(event.pos)

        if event.type == pygame.MOUSEBUTTONUP:
            print('up')
            print('Im here')
            end_button.is_not_pressed()
            pygame.time.delay(1000)
            self.next_condition()
            self.screen.fill((0, 0, 0))



    def start_menu(self, i: pygame.event):

        self.winner = 0
        self.screen.fill((0, 0, 0))
        start_button = button.Button(self.screen, 250, 200, 20, 20, 'Start', 80)

        if i.type == pygame.QUIT:
            print(pygame.QUIT)
            print(i)
            print(i.type)
            pygame.quit()
            sys.exit()

        if i.type == pygame.MOUSEBUTTONDOWN:
            print(i.pos)

            print('down')
            start_button.is_pressed(i.pos)

        if i.type == pygame.MOUSEBUTTONUP:
            print('up')
            start_button.is_not_pressed()
            pygame.time.delay(50)
            self.next_condition()
            self.screen.fill((0, 0, 0))
            self.game_array = new_game(self.screen)
            self.whose_move = 0

    # делает ход
    def make_a_move(self, event: pygame.event):

        if event.type == pygame.QUIT:
            print(pygame.QUIT)
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:

            # 1 - это нолик в массиве
            if event.button == 1:
                wich_cell = check_square(event.pos)
                right_pos = coordinates_for_draw(wich_cell)

                if (self.whose_move == 0 or self.whose_move == 1) and self.game_array[wich_cell] == 0:
                    draw_circle_game(screen, right_pos)

                    # передаёт ход крестикам
                    self.whose_move = 2
                    self.game_array[wich_cell] = 1
                    print_game_array(self.game_array)
                    print()

                    if check_victory(self.game_array, 1, screen):
                        pygame.display.update()
                        self.winner = 1
                        self.next_condition()
                        '''
                                                if event.type == pygame.MOUSEBUTTONDOWN:
                            self.game_array = new_game(screen)
                            self.whose_move = 0
                            
                        '''
                        pygame.time.delay(1000)

                pygame.display.update()

            # 2 - это крестик в массиве
            elif event.button == 3:
                # получение координаты, куда рисовать
                wich_cell = check_square(event.pos)
                right_pos = coordinates_for_draw(wich_cell)

                if (self.whose_move == 0 or self.whose_move == 2) and self.game_array[wich_cell] == 0:
                    draw_cross_game(screen, right_pos)

                    # передаёт ход ноликам
                    self.whose_move = 1
                    self.game_array[wich_cell] = 2

                    print_game_array(self.game_array)
                    print()

                    if check_victory(self.game_array, 2, screen):
                        pygame.display.update()
                        self.next_condition()
                        self.winner = 2
                        '''
                                                if event.type == pygame.MOUSEBUTTONDOWN:
                            self.game_array = new_game(screen)
                            self.whose_move = 0
                        '''

                        pygame.time.delay(1000)

                pygame.display.update()
            elif event.button == 2:
                screen.fill(WHITE)
                pygame.display.update()

    def playing_game(self):
        pass

    def end_menu(self):
        pass


width_screen, height_screen = 600, 400

# создание окна
screen = pygame.display.set_mode((width_screen, height_screen))

manager = Manager(screen)

# часики
clock = pygame.time.Clock()

# инициализирую все модули pygame
pygame.init()

FIRST_COLUMN = ((200, 0), (200, 400))
SECOND_COLUMN = ((400, 0), (400, 400))
FIRST_ROW = ((0, 133), (600, 133))
SECOND_ROW = ((0, 266), (600, 266))

r1 = pygame.Rect((150, 20, 100, 75))


# pygame.draw.rect(screen, WHITE, (20, 20, 100, 75))
# pygame.draw.rect(screen, LIGHT_BLUE, r1, 10)


# прорисовка линий игры
def draw_field(sceen_local):
    pygame.draw.line(screen, WHITE, FIRST_ROW[0], FIRST_ROW[1], 4)
    pygame.draw.line(screen, WHITE, SECOND_ROW[0], SECOND_ROW[1], 4)
    pygame.draw.line(screen, WHITE, FIRST_COLUMN[0], FIRST_COLUMN[1], 4)
    pygame.draw.line(screen, WHITE, SECOND_COLUMN[0], SECOND_COLUMN[1], 4)


draw_field(screen)

game_array = [0, 0, 0,
              0, 0, 0,
              0, 0, 0,
              ]

pygame.display.update()

whose_move = 0

text = '3 cunts'

# f1 = pygame.font.Font(None, 36)
# text1 = f1.render(text, True, RED)

# print(text1.get_rect())

# pygame.draw.rect(screen, GREEN, self.bounds)

# screen.blit(text1, (50, 50))
pygame.display.update()

text = '3 cunts'

# button_start = button.Button(screen, 250, 200, 20, 20, text, 80)

manager.main_cycle()

while 1:
    clock.tick(60)

    events = pygame.event.get()
    # print(events)
    for i in events:
        if i.type == pygame.QUIT:
            print(pygame.QUIT)
            print(i)
            print(i.type)
            pygame.quit()
            sys.exit()

        if i.type == pygame.MOUSEBUTTONDOWN:
            print(i.pos)

            print('down')
            # button_start.is_pressed(i.pos)

        if i.type == pygame.MOUSEBUTTONUP:
            print('up')
            # button_start.is_not_pressed()

    pygame.display.update()
