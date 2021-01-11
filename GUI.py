import pygame

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



