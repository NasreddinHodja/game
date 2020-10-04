import pygame

WINDOW_SIZE = (400, 400)

pygame.init()

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
clock = pygame.time.Clock()

running = True

sprite = pygame.image.load('assets/chronomage.png')

moving_right = False
moving_left = False

player_location = [50, 300]

while running:
    screen.fill(0)
    screen.blit(sprite, player_location)

    if moving_right:
        player_location[0] += 4
    if moving_left:
        player_location[0] -= 4

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moving_right = True
            elif event.key == pygame.K_LEFT:
                moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                moving_right = False
            elif event.key == pygame.K_LEFT:
                moving_left = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()
