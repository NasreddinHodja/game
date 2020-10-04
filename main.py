import pygame

WINDOW_SIZE = (400, 400)

pygame.init()

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    pygame.display.update()
    clock.tick(60)

pygame.quit()
