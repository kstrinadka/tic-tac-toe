import pygame
import sys
from colors import *
from winning_positions import *


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


width_screen, height_screen = 600, 400

# создание окна
screen = pygame.display.set_mode((width_screen, height_screen))



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
    pygame.draw.line(screen, WHITE, FIRST_COLUMN[0], FIRST_COLUMN[1],4)
    pygame.draw.line(screen, WHITE, SECOND_COLUMN[0], SECOND_COLUMN[1], 4)

draw_field(screen)


game_array = [0, 0, 0,
              0, 0, 0,
              0, 0, 0,
              ]

pygame.display.update()

whose_move = 0

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

            # 1 - это нолик в массиве
            if i.button == 1:

                wich_cell = check_square(i.pos)
                right_pos = coordinates_for_draw(wich_cell)

                if (whose_move == 0 or whose_move == 1) and game_array[wich_cell] == 0:
                    draw_circle_game(screen, right_pos)

                    # передаёт ход крестикам
                    whose_move = 2
                    game_array[wich_cell] = 1

                    print_game_array(game_array)
                    print()

                    if check_victory(game_array, 1, screen):
                        pygame.display.update()
                        for i in events:
                            if i.type == pygame.MOUSEBUTTONDOWN:
                                game_array = new_game(screen)
                                whose_move = 0
                                break
                        pygame.time.delay(1000)

                pygame.display.update()

            # 2 - это крестик в массиве
            elif i.button == 3:
                # print(i.pos)
                # print(type(i.pos))

                # получение координаты, куда рисовать
                wich_cell = check_square(i.pos)
                right_pos = coordinates_for_draw(wich_cell)

                if (whose_move == 0 or whose_move == 2) and game_array[wich_cell] == 0:
                    draw_cross_game(screen, right_pos)

                    # передаёт ход ноликам
                    whose_move = 1
                    game_array[wich_cell] = 2

                    print_game_array(game_array)
                    print()

                    if check_victory(game_array, 2, screen):
                        pygame.display.update()
                        for i in events:
                            if i.type == pygame.MOUSEBUTTONDOWN:
                                game_array = new_game(screen)
                                whose_move = 0
                                break
                        pygame.time.delay(1000)

                pygame.display.update()
            elif i.button == 2:
                screen.fill(WHITE)
                pygame.display.update()

    pygame.display.update()
