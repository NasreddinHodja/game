import pygame

class Snake:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.x_speed = 10
        self.y_speed = 0
        self.color = (255, 0, 0)


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

    def show(self, display):
        pygame.draw.rect(display, self.color,
                         (self.x, self.y, 10, 10))

    def move(self, x, y):
        self.x_speed = x * 10
        self.y_speed = y * 10
