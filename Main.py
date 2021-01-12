import pygame
import GUI
import random
import time


def random_board(board_dic):
    for row in range(0, 3):
        for column in range(0, 3):
            board_dic[(row, column)] = random.randint(0, 4)


def start_game(screen, board):
    random_board(board)
    GUI.initialize_board(screen)
    GUI.draw_board(board, screen)
    pygame.display.update()
    GUI.write_instructions_01(screen)


def check_boards(user_board_01, board2):
    board2_elements = list(board2.values())
    board1_elements = list(user_board_01.values())
    trues = []
    for i in range(len(user_board_01)):
        column = i // 3
        row = i % 3
        right = True
        if board1_elements[i] == board2_elements[i]:
            trues.append(True)
        else:
            right = False

        GUI.right_or_wrong(screen, right, (column, row))
        GUI.fill_rectangle(screen, (column, row))
        GUI.draw_shape(screen, board2_elements[i], (column, row))
        print(board1_elements)
    return trues


pygame.init()
screen = pygame.display.set_mode((600, 800))
screen.fill((100, 100, 100))
pygame.display.set_caption('Memory Game')
pygame.display.update()

game_board = {}
user_board = {}
for i in range(0, 3):
    for j in range(0, 3):
        game_board[(i, j)] = 0
start_game(screen, user_board)

pointer = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pointer:
                board = game_board
            else:
                board = user_board
            x, y = pygame.mouse.get_pos()
            column, row = GUI.get_column_row(x, y)
            tracker = game_board[(column, row)]
            if tracker + 1 == 5:
                tracker = 0
            else:
                tracker = tracker + 1
            game_board[(column, row)] = tracker
            GUI.fill_rectangle(screen, (column, row))
            GUI.draw_shape(screen, tracker, (column, row))
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                pygame.draw.rect(screen, (255, 0, 0), (50, 50, 50, 50))
                pygame.display.update()
            elif event.key == pygame.K_c:
                GUI.clear_board(screen)
            elif event.key == pygame.K_t:
                GUI.draw_board(user_board, screen)
            elif event.key == pygame.K_RETURN:
                GUI.clear_board(screen)
                random_board(user_board)
                GUI.draw_board(user_board, screen)
                pointer = True
                time.sleep(3)
                GUI.clear_board(screen)
                GUI.draw_board(game_board, screen)
                GUI.clear_instructions(screen)
                GUI.write_instructions_02(screen)
            elif event.key == pygame.K_f:
                check_boards(game_board, user_board)

print(2 % 3)
