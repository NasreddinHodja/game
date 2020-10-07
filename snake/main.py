import pygame

from snake import Snake
from food import Food

def main():
    scale = 10

    pygame.init()

    display = pygame.display.set_mode((400, 400), 0, 32)
    clock = pygame.time.Clock()
    # display = pygame.Suface((400, 400))

    snake = Snake()
    food = Food()

    running = True
    while running:
        display.fill(0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_RIGHT and
                    not (snake.x_speed == -1 * snake.scale)):
                    snake.move(1, 0)
                elif (event.key == pygame.K_LEFT and
                      not (snake.x_speed == 1 * snake.scale)):
                    snake.move(-1, 0)
                elif (event.key == pygame.K_UP and
                      not (snake.y_speed == 1 * snake.scale)):
                    snake.move(0, -1)
                elif (event.key == pygame.K_DOWN and
                      not (snake.y_speed == -1 * snake.scale)):
                    snake.move(0, 1)

        if food.collides(snake.head):
            food = Food()
            snake.grow()

        food.show(display)

        snake.update()
        snake.show(display)

        if snake.cuts_itself():
            running = False

        pygame.display.update()
        clock.tick(10)

    pygame.quit()

if __name__ == '__main__':
    main()
