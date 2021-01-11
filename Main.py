import pygame
import GUI

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
pygame.init()
screen = pygame.display.set_mode((600, 600))
screen.fill((100, 100, 100))
pygame.display.set_caption('Memory Game')
pygame.display.update()
running = True
GUI.initialize_board(screen)
list_tracker = {}
for i in range(0, 3):
    for j in range(0, 3):
        list_tracker[(i, j)] = 1
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            column, row = GUI.get_column_row(x, y)
            tracker = list_tracker[(row, column)]
            if tracker == 5:
                tracker = 1
            GUI.fill_rectangle(screen, (column, row))
            GUI.draw_shape(screen, tracker, (column, row))
            list_tracker[(row, column)] = tracker + 1
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                pygame.draw.rect(screen, (255, 0, 0), (50, 50, 50, 50))
                pygame.display.update()
