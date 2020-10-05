import pygame, sys

from engine import *

WINDOW_SIZE = (600,400)

def main():

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

    running = True
    while running:
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

        enemies = []
        enemies.append(enemy)

        for arrow in projectiles:
            if arrow.frames_left <= 0:
                del arrow
                continue
            arrow.draw(display)
            hits = arrow.collides(enemies)
            for hit in hits:
                hit.damage(0.2)

        for e in enemies:
            if e.collides([player.rect]):
                player.damage(0.2)

        for e in enemies:
            if e.life == 0:
                del e
                continue
            e.move(tile_rects)
            e.draw(display)

        if player.life == 0:
            running = False

        player.move(tile_rects)
        player.draw(display)

        for event in pygame.event.get(): # event loop
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.moving_right = True
                if event.key == pygame.K_LEFT:
                    player.moving_left = True
                if event.key == pygame.K_SPACE:
                    if player.air_timer < 6:
                        player.y_momentum = -5
                if event.key == pygame.K_a:
                    projectiles.append(Projectile(player.rect.x,
                                                player.rect.y,
                                                -player.facing_dir))
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    player.moving_right = False
                if event.key == pygame.K_LEFT:
                    player.moving_left = False

        screen.blit(pygame.transform.scale(display,WINDOW_SIZE),(0,0))
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
