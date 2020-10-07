from random import randint

import pygame

class Food:
    def __init__(self):
        self.scale = 10
        self.x = randint(0, 40 - 1) * self.scale
        self.y = randint(0, 40 - 1) * self.scale
        self.color = (0, 0, 255)
        self.rect = pygame.Rect((self.x, self.y, self.scale, self.scale))

    def show(self, display):
        pygame.draw.rect(display, self.color,
                         (self.x, self.y, self.scale - 2, self.scale - 2))

    def collides(self, snake):
        return self.x == snake.x and self.y == snake.y
