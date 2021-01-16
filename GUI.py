import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)


def draw_shape(screen, shape, column_row):
    x_position, y_position = column_row
    x_position = x_position * 200
    y_position = y_position * 200
    if shape == 1:
        pygame.draw.rect(screen, (0, 255, 0), (x_position + 25, y_position + 25, 150, 150))
    elif shape == 2:
        pygame.draw.polygon(screen, (0, 0, 255), [(x_position + 25, y_position + 175),
                                                  (x_position + 100, y_position + 25),
                                                  (x_position + 175, y_position + 175)])
    elif shape == 3:
        pygame.draw.circle(screen, (255, 0, 0), (x_position + 100, y_position + 100), 75)
    elif shape == 4:
        pygame.draw.ellipse(screen, (255, 0, 255), (x_position + 30, y_position + 15, 125, 175))
    elif shape == 0:
        fill_rectangle(screen, column_row)
    pygame.display.update()


def initialize_board(screen):
    for i in range(0, 601, 200):
        pygame.draw.line(screen, (0, 0, 0), (i, 0), (i, 600))
        pygame.draw.line(screen, (0, 0, 0), (0, i), (600, i))
    pygame.display.update()


def get_shape(shape_name):
    if shape_name == 'rectangle':
        return 50, 50, 50, 50


def get_color():
    return 255, 0, 0


def get_column_row(x_position, y_position):
    return x_position // 200, y_position // 200


def fill_rectangle(screen, column_row):
    x, y = column_row
    x = x * 200
    y = y * 200
    screen.fill((100, 100, 100), (x + 1, y + 1, 198, 198))
    pygame.display.update()


def clear_board(screen):
    for i in range(0, 3):
        for j in range(0, 3):
            fill_rectangle(screen, (i, j))


def draw_board(board, screen):
    for coordinates, value in board.items():
        fill_rectangle(screen, coordinates)
        draw_shape(screen, value, coordinates)


def write_instructions_01(screen):
    font = pygame.font.Font(None, 50)
    img = font.render('Press enter to start game', True, BLACK)
    screen.blit(img, (25, 675))
    pygame.display.update()


def clear_instructions(screen):
    screen.fill((100, 100, 100), (0, 601, 600, 199))
    pygame.display.update()


def loosing_instructions(screen):
    clear_instructions(screen)
    font = pygame.font.Font(None, 50)
    img = font.render('You loose', True, BLACK)
    screen.blit(img, (25, 675))
    img = font.render('Press r to restart q to quit', True, BLACK)
    screen.blit(img, (25, 725))
    pygame.display.update()

def winning_instructions(screen, winning_streak):
    clear_instructions(screen)
    font = pygame.font.Font(None, 50)
    img = font.render('You win', True, BLACK)
    screen.blit(img, (25, 625))
    img = font.render(f'You have won {str(winning_streak)} games in a row ', True, BLACK)
    screen.blit(img, (25, 675))
    img = font.render('Press r to restart q to quit', True, BLACK)
    screen.blit(img, (25, 725))
    pygame.display.update()

def write_instructions_02(screen):
    font = pygame.font.Font(None, 50)
    img = font.render('Match shapes', True, BLACK)
    screen.blit(img, (25, 675))
    img = font.render('press f when finished', True, BLACK)
    screen.blit(img, (25, 725))
    pygame.display.update()


def right_or_wrong(screen, right, column_row):
    column, row = column_row
    column = column * 200
    row = row * 200
    color = []
    if right:
        color = [0, 100, 0]
    else:
        color = [100, 0, 0]
    pygame.draw.rect(screen, tuple(color), (column + 5, row + 5, 190, 190), 5)
    pygame.display.update()
