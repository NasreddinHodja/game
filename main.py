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

scroll = [0, 0]

while True:
    display.fill(0)

    scroll[0] += (player.rect.x-scroll[0]-150) / 20
    scroll[1] += (player.rect.y-scroll[1]-100) / 20

    tile_rects = []
    y = 0
    for layer in game_map:
        x = 0
        for tile in layer:
            if tile == '1':
                display.blit(dirt_img,(x*16-int(scroll[0]), y*16-int(scroll[1])))
            if tile == '2':
                display.blit(grass_img,(x*16-int(scroll[0]), y*16-int(scroll[1])))
            if tile != '0':
                tile_rects.append(pygame.Rect(x*16,y*16,16,16))
            x += 1
        y += 1

    player.move(tile_rects)
    enemy.move(tile_rects)

    player.draw(display, scroll)
    enemy.draw(display, scroll)

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
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.moving_right = False
            if event.key == pygame.K_LEFT:
                player.moving_left = False

    screen.blit(pygame.transform.scale(display,WINDOW_SIZE),(0,0))
    pygame.display.update()
    clock.tick(60)
