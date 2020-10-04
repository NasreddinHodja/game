import pygame

class Character:
    def __init__(self, x, y, sprite_path):
        self.sprite = pygame.image.load(sprite_path)
        self.y_momentum = 0
        self.x_momentum = 0
        self.x_momentum_rate = 0.5
        self.y_momentum_rate = 0.2
        self.air_timer = 0
        self.moving_right = False
        self.moving_left = False
        self.movement = [0, 0]
        self.rect = pygame.Rect((x, y, self.sprite.get_width(),
                                 self.sprite.get_height()))
        self.life = 1

    def collides(self, tiles):
        hit_list = []
        for tile in tiles:
            if self.rect.colliderect(tile):
                hit_list.append(tile)

        return hit_list

    def move_collide(self, tiles):
        collision_types = {'top': False,
                           'bottom': False,
                           'right': False,
                           'left': False}

        self.rect.x += self.movement[0]
        hit_list = self.collides(tiles)
        for tile in hit_list:
            if self.movement[0] > 0:
                self.rect.right = tile.left
                collision_types['right'] = True
            elif self.movement[0] < 0:
                self.rect.left = tile.right
                collision_types['left'] = True

        self.rect.y += self.movement[1]
        hit_list = self.collides(tiles)
        for tile in hit_list:
            if self.movement[1] > 0:
                self.rect.bottom = tile.top
                collision_types['bottom'] = True
            elif self.movement[1] < 0:
                self.rect.top = tile.bottom
                collision_types['top'] = True

        return collision_types

    def stop(self):
        if self.x_momentum < 0:
            self.x_momentum += self.x_momentum_rate
        elif self.x_momentum > 0:
            self.x_momentum -= self.x_momentum_rate

    def move(self, tiles):
        pass

    def draw_life(self, display, scroll):
        bg_rect = pygame.Rect((self.rect.x - scroll[0], self.rect.y - scroll[1] - 5,
                               self.sprite.get_width(), 1))
        fg_rect = pygame.Rect((self.rect.x - scroll[0], self.rect.y - scroll[1] - 5,
                               self.sprite.get_width() * self.life, 1))
        pygame.draw.rect(display, (255, 0, 0), bg_rect)
        pygame.draw.rect(display, (0, 255, 0), fg_rect)

    def draw(self, display, scroll):
        display.blit(self.sprite, (self.rect.x - scroll[0],
                                   self.rect.y - scroll[1]))
        self.draw_life(display, scroll)

class Player(Character):
    def move(self, tiles):
        self.movement = [0,0]
        if self.moving_right:
            self.x_momentum += self.x_momentum_rate
            self.x_momentum = min(self.x_momentum, 2)
        elif self.moving_left == True:
            self.x_momentum -= self.x_momentum_rate
            self.x_momentum = max(self.x_momentum, -2)
        else:
            self.stop()

        self.movement[0] += self.x_momentum
        self.movement[1] += self.y_momentum
        self.y_momentum += self.y_momentum_rate
        if self.y_momentum > 3:
            self.y_momentum = 3

        collisions = self.move_collide(tiles)

        if collisions['bottom'] or collisions['top']:
            self.air_timer = 0
            self.y_momentum = 0
        else:
            self.air_timer += 1

class Enemy(Character):
    def move(self, tiles):
        # if randint(0, 1) == 1:
        #     self.moving_right = True
        # else:
        #     self.moving_left = True

        self.movement = [0,0]
        if self.moving_right:
            self.x_momentum += self.x_momentum_rate
            self.x_momentum = min(self.x_momentum, 2)
        elif self.moving_left == True:
            self.x_momentum -= self.x_momentum_rate
            self.x_momentum = max(self.x_momentum, -2)
        else:
            self.stop()

        self.movement[0] += self.x_momentum
        self.movement[1] += self.y_momentum
        self.y_momentum += self.y_momentum_rate
        if self.y_momentum > 3:
            self.y_momentum = 3

        collisions = self.move_collide(tiles)

        if collisions['bottom'] or collisions['top']:
            self.air_timer = 0
            self.y_momentum = 0
        else:
            pass
