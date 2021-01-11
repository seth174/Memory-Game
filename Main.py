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
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                pygame.draw.rect(screen, (255, 0, 0), (50, 50, 50, 50))
                pygame.display.update()

