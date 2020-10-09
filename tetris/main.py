from random import randint

import pygame

from tetromino import Tetromino

WINDOW_SIZE = (600, 600)
BOARD_POS = (0, 0)

COLOR  = [
    (0, 0, 0),
    (44, 135, 245),
    (66, 245, 78),
    (245, 242, 66),
    (245, 66, 66),
    (66, 245, 233),
    (242, 66, 245),
    (255, 255, 255)
]

board = [[7, 7, 7, 7, 7, 7, 7, 7, 7, 7 , 7, 7],
         [7, 0, 0, 0, 0, 0, 0, 0, 0, 0 , 0, 7],
         [7, 0, 0, 0, 0, 0, 0, 0, 0, 0 , 0, 7],
         [7, 0, 0, 0, 0, 0, 0, 0, 0, 0 , 0, 7],
         [7, 0, 0, 0, 0, 0, 0, 0, 0, 0 , 0, 7],
         [7, 0, 0, 0, 0, 0, 0, 0, 0, 0 , 0, 7],
         [7, 0, 0, 0, 0, 0, 0, 0, 0, 0 , 0, 7],
         [7, 0, 0, 0, 0, 0, 0, 0, 0, 0 , 0, 7],
         [7, 0, 0, 0, 0, 0, 0, 0, 0, 0 , 0, 7],
         [7, 0, 0, 0, 0, 0, 0, 0, 0, 0 , 0, 7],
         [7, 0, 0, 0, 0, 0, 0, 0, 0, 0 , 0, 7],
         [7, 0, 0, 0, 0, 0, 0, 0, 0, 0 , 0, 7],
         [7, 0, 0, 0, 0, 0, 0, 0, 0, 0 , 0, 7],
         [7, 0, 0, 0, 0, 0, 0, 0, 0, 0 , 0, 7],
         [7, 0, 0, 0, 0, 0, 0, 0, 0, 0 , 0, 7],
         [7, 0, 0, 0, 0, 0, 0, 0, 0, 0 , 0, 7],
         [7, 0, 0, 0, 0, 0, 0, 0, 0, 0 , 0, 7],
         [7, 0, 0, 0, 0, 0, 0, 0, 0, 0 , 0, 7],
         [7, 0, 0, 0, 0, 0, 0, 0, 0, 0 , 0, 7],
         [7, 0, 0, 0, 0, 0, 0, 0, 0, 0 , 0, 7],
         [7, 0, 0, 0, 0, 0, 0, 0, 0, 0 , 0, 7],
         [7, 0, 0, 0, 0, 0, 0, 0, 0, 0 , 0, 7],
         [7, 0, 0, 0, 0, 0, 0, 0, 0, 0 , 0, 7],
         [7, 0, 0, 0, 0, 0, 0, 0, 0, 0 , 0, 7],
         [7, 0, 0, 0, 0, 0, 0, 0, 0, 0 , 0, 7],
         [7, 0, 0, 0, 0, 0, 0, 0, 0, 0 , 0, 7],
         [7, 7, 7, 7, 7, 7, 7, 7, 7, 7 , 7, 7]]

def draw_board(display):
    for i in range(len(board)):
        for j in range(len(board[i])):
            rect = (j, i, 1, 1)

            for k in range(1, len(COLOR)):
                if(board[i][j] == k):
                    pygame.draw.rect(display, COLOR[k], rect)

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
    display = pygame.Surface((int(WINDOW_SIZE[0] / 20),
                              int(WINDOW_SIZE[1] / 20)))

    tet = Tetromino(tet=randint(0, 5))
    running = True
    while running:
        display.fill(0)

        if not tet.falling:
            tet = Tetromino(tet=randint(0, 5))

        if tet.can_fall(board): tet.fall()

        tet.draw(display)
        draw_board(display)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(pygame.transform.scale(display, WINDOW_SIZE), (25, 25))
        pygame.display.update()
        clock.tick(6)

    pygame.quit()

if __name__ == '__main__':
    main()
