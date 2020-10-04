import pygame, sys

from engine import Player, Enemy

WINDOW_SIZE = (600,400)

def load_map(path):
    f = open(path, 'r')
    data = f.read()
    f.close()

    data = data.split('\n')
    game_map = []
    for row in data:
        game_map.append(list(row))

    return game_map

game_map = load_map('map.txt')

clock = pygame.time.Clock()

pygame.init()

pygame.display.set_caption('Pygame Platformer')

screen = pygame.display.set_mode(WINDOW_SIZE,0,32) # initiate the window

display = pygame.Surface((300,200)) # used as the surface for rendering, which is scaled

grass_img = pygame.image.load('assets/grass.png')
dirt_img = pygame.image.load('assets/dirt.png')

player = Player(10, 10, 'assets/chronomage.png')
enemy = Enemy(150, 20, 'assets/zombie.png')

projectiles = []

while True:
    display.fill(0)

    tile_rects = []
    y = 0
    for layer in game_map:
        x = 0
        for tile in layer:
            if tile == '1':
                display.blit(dirt_img,(x*16, y*16))
            if tile == '2':
                display.blit(grass_img,(x*16, y*16))
            if tile != '0':
                tile_rects.append(pygame.Rect(x*16,y*16,16,16))
            x += 1
        y += 1

    player.move(tile_rects)
    enemy.move(tile_rects)

    player.draw(display)
    enemy.draw(display)

    arrow_img = pygame.image.load('assets/arrow.png')
    for arrow in projectiles:
        if arrow[2] == 0:
            del arrow
            continue

        arrow[2] -= 5
        if arrow[3] == -1:
            display.blit(arrow_img,
                         (arrow[0] - (120 - arrow[2]),
                          arrow[1]))
        else:
            display.blit(pygame.transform.flip(arrow_img, True, False),
                         (arrow[0] + (120 - arrow[2]),
                          arrow[1]))

    for event in pygame.event.get(): # event loop
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.moving_right = True
            if event.key == pygame.K_LEFT:
                player.moving_left = True
            if event.key == pygame.K_SPACE:
                if player.air_timer < 6:
                    player.y_momentum = -5
            if event.key == pygame.K_a:
                projectiles.append([player.rect.x,
                                    player.rect.y,
                                    120,
                                    -player.facing_dir])
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.moving_right = False
            if event.key == pygame.K_LEFT:
                player.moving_left = False

    screen.blit(pygame.transform.scale(display,WINDOW_SIZE),(0,0))
    pygame.display.update()
    clock.tick(60)
