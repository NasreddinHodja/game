from random import randint

import pygame

from tetromino import Tetromino

WINDOW_SIZE = (600, 600)

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
    display = pygame.Surface((int(WINDOW_SIZE[0] / 10),
                              int(WINDOW_SIZE[1] / 10)))

    running = True
    while running:
        display.fill(0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(pygame.transform.scale(display, WINDOW_SIZE), (0, 0))
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
