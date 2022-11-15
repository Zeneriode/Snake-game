from food import Food
from land import Land
from pygame import K_ESCAPE, QUIT, display, draw, event, key, time
from snake import Snake
from snake_constants import BLOCK_SIZE, SCREEN_LENGTH, SCREEN_WIDTH

screen = display.set_mode((SCREEN_LENGTH, SCREEN_WIDTH))  # Игровое окно
land = Land(screen)  # Задний фон
snake = Snake(screen)  # Змея
food = Food(screen)  # еда
clock = time.Clock()  # смена кадров


def check_food():
    """Проверяет, надо ли есть еду"""
    global food, snake
    if snake.coordinates_x[0] == food.x_coordinate and snake.coordinates_y[0] == food.y_coordinate:
        food = Food(screen)
        snake.grow()


def game():
    """Игра запускается и работает до выключения пользователем"""
    global land, snake, food, screen, clock
    play = True  # Работает ли игровое окно или нет
    frame = 0
    while play:
        if frame % 20 == 0:
            land.draw()
            snake.draw()
            food.draw()
            snake.move()
            check_food()

        snake.change_direction()

        for i in range(0, SCREEN_LENGTH, BLOCK_SIZE):
            draw.line(screen, "black", (i, 0), (i, SCREEN_WIDTH))

        for i in range(0, SCREEN_WIDTH, BLOCK_SIZE):
            draw.line(screen, "black", (0, i), (SCREEN_LENGTH, i))

        display.update()
        clock.tick(200)
        frame += 1

        play = snake.check_collision()

        # Проверка, что игрок нажал на кнопку "закрыть"
        for e_check in event.get():
            if e_check.type == QUIT:
                play = False

        # Проверка, что игрок нажал esc
        if key.get_pressed()[K_ESCAPE]:
            play = False


if __name__ == "__main__":
    game()
