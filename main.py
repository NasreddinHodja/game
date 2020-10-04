import pygame

WINDOW_SIZE = (400, 400)

pygame.init()

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
clock = pygame.time.Clock()

running = True

sprite = pygame.image.load('assets/chronomage.png')

moving_right = False
moving_left = False

player_location = [50, 50]
player_y_momentum = 0

player_rect = pygame.Rect(player_location[0], player_location[1],
                          sprite.get_width(), sprite.get_height())
test_rect = pygame.Rect(100, 100, 100, 50)

while running:
    screen.fill(0)

    if player_location[1] > WINDOW_SIZE[1] - sprite.get_height():
        player_y_momentum *= -1
    else:
        player_y_momentum += 0.2

    player_location[1] += player_y_momentum

    if moving_right:
        player_location[0] += 4
    if moving_left:
        player_location[0] -= 4

    player_rect.x = player_location[0]
    player_rect.y = player_location[1]

    if player_rect.colliderect(test_rect):
        pygame.draw.rect(screen, (255, 0, 0), test_rect)
    else:
        pygame.draw.rect(screen, (0, 0, 0), test_rect)

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

    screen.blit(sprite, player_location)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
