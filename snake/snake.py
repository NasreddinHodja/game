import pygame

class Snake:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.x_speed = 10
        self.y_speed = 0
        self.color = (255, 0, 0)
        self.scale = 10
        self.head = pygame.Rect((self.x, self.y, self.scale, self.scale))
        self.tail = []

    def update(self):
        self.x += self.x_speed
        if self.x < 0:
            self.x = 400
        if self.x > 400:
            self.x = 0

        self.y += self.y_speed
        if self.y < 0:
            self.y = 400
        if self.y > 400:
            self.y = 0

        self.head = pygame.Rect((self.x, self.y, self.scale, self.scale))

    def show(self, display):
        pygame.draw.rect(display, self.color,
                         (self.x, self.y, self.scale, self.scale))

    def move(self, x, y):
        self.x_speed = x * self.scale
        self.y_speed = y * self.scale

    def grow(self):
        pass
