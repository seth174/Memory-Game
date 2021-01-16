import pygame
import GUI
import random
import time

WIDTH = 600
HEIGHT = 800

USER_BOARD = {}
GAME_BOARD = {}
winning_streak = 0


def initialize_pygame():
    screen.fill((100, 100, 100))
    pygame.display.set_caption('Memory Game')
    pygame.display.update()


def random_board():
    for row in range(0, 3):
        for column in range(0, 3):
            USER_BOARD[(row, column)] = random.randint(0, 4)
            GAME_BOARD[(row, column)] = 0


def start_game():
    random_board()
    GUI.initialize_board(screen)
    GUI.draw_board(USER_BOARD, screen)
    pygame.display.update()
    GUI.write_instructions_01(screen)


def check_boards():
    user_board_elements = list(USER_BOARD.values())
    game_board_elements = list(GAME_BOARD.values())
    trues = []
    correct = True
    for i in range(len(user_board_elements)):
        column = i // 3
        row = i % 3
        right = True
        if user_board_elements[i] == game_board_elements[i]:
            trues.append(True)
        else:
            right = False
            correct = False

        GUI.fill_rectangle(screen, (column, row))
        GUI.draw_shape(screen, user_board_elements[i], (column, row))
        GUI.right_or_wrong(screen, right, (column, row))
    return correct


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
initialize_pygame()

start_game()

pointer = False
game_over = False
running = True
won = False

while running:
    for event in pygame.event.get():
        if game_over:
            GUI.loosing_instructions(screen)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    GUI.clear_instructions(screen)
                    start_game()
                    game_over = False
                elif event.key == pygame.K_q:
                    running = False
        elif won:
            GUI.winning_instructions(screen, winning_streak)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    GUI.clear_instructions(screen)
                    start_game()
                    won = False
                elif event.key == pygame.K_q:
                    running = False
        elif event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pointer:
                board = USER_BOARD
            else:
                board = GAME_BOARD
            x, y = pygame.mouse.get_pos()
            if y > 600:
                continue
            column, row = GUI.get_column_row(x, y)
            tracker = GAME_BOARD[(column, row)]
            if tracker + 1 == 5:
                tracker = 0
            else:
                tracker = tracker + 1
            GAME_BOARD[(column, row)] = tracker
            GUI.fill_rectangle(screen, (column, row))
            GUI.draw_shape(screen, tracker, (column, row))
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                pygame.draw.rect(screen, (255, 0, 0), (50, 50, 50, 50))
                pygame.display.update()
            elif event.key == pygame.K_c:
                GUI.clear_board(screen)
            elif event.key == pygame.K_t:
                GUI.draw_board(GAME_BOARD, screen)
            elif event.key == pygame.K_RETURN:
                GUI.clear_board(screen)
                random_board()
                GUI.draw_board(USER_BOARD, screen)
                pointer = True
                time.sleep(6)
                GUI.clear_board(screen)
                GUI.draw_board(GAME_BOARD, screen)
                GUI.clear_instructions(screen)
                GUI.write_instructions_02(screen)
            elif event.key == pygame.K_f:
                if not check_boards():
                    game_over = True
                    winning_streak = 0
                else:
                    won = True
                    winning_streak = winning_streak + 1
