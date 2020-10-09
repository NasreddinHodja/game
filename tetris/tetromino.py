import pygame

class Tetromino:
    def __init__(self, x = 5, y = 0, tet = 0):
        self.tetrominos = [
            # I
            [[0, 1, 0, 0],
             [0, 1, 0, 0],
             [0, 1, 0, 0],
             [0, 1, 0, 0]],

            # J
            [[0, 0, 2, 0],
             [0, 0, 2, 0],
             [0, 2, 2, 0],
             [0, 0, 0, 0]],

            # L
            [[0, 3, 0, 0],
             [0, 3, 0, 0],
             [0, 3, 3, 0],
             [0, 0, 0, 0]],

            # T
            [[0, 4, 0, 0],
             [0, 4, 4, 0],
             [0, 4, 0, 0],
             [0, 0, 0, 0]],

            # S
            [[0, 0, 0, 0],
             [0, 5, 5, 0],
             [5, 5, 0, 0],
             [0, 0, 0, 0]],

            # Z
            [[0, 0, 0, 0],
             [0, 6, 6, 0],
             [0, 0, 6, 6],
             [0, 0, 0, 0]],
        ]

        self.colors = [
            (0, 0, 0, 0),
            (44, 135, 245),
            (66, 245, 78),
            (245, 242, 66),
            (245, 66, 66),
            (66, 245, 233),
            (242, 66, 245),
            (255, 255, 255)
        ]

        self.tetromino = self.tetrominos[tet]

        self.x = x
        self.y = y

        self.falling = True

    def __str__(self):
        s = ''
        for i in range(len(self.tetromino)):
            s += f'{self.tetromino[i]}'
            if i < len(self.tetromino) - 1:
                s += '\n'
        return s

    def draw(self, display):
        for i in range(len(self.tetromino)):
            for j in range(len(self.tetromino[i])):
                if self.tetromino[i][j] == 0:
                    continue

                rect = (self.x+j, self.y+i, 1, 1)
                pygame.draw.rect(display, self.colors[self.tetromino[i][j]], rect)

    def can_fall(self, board):
        if self.y == 0:
            return True

        for i in range(len(self.tetromino)):
            for j in range(len(self.tetromino[i])):
                if self.tetromino[i][j] == 0:
                    continue

                if board[self.x + i][self.y + j] != 0:
                    return False

        return True

    def fall(self):
        self.y += 1
