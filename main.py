from food import Food
from land import Land
from time import sleep
from pygame import K_ESCAPE, QUIT, display, draw, event, key, time
from snake import Snake
from draw_numbers import Number
from snake_constants import BLOCK_SIZE, SCREEN_LENGTH, SCREEN_WIDTH

screen = display.set_mode((SCREEN_LENGTH, SCREEN_WIDTH))  # Игровое окно
land = Land(screen)  # Задний фон
snake = Snake(screen)  # Змея
food = Food(screen)  # еда
clock = time.Clock()  # смена кадров
result = Number(screen)
reason_of_death = None


def check_food():
    """Проверяет, надо ли есть еду"""
    global food
    if snake.coordinates_x[0] == food.x_coordinate and snake.coordinates_y[0] == food.y_coordinate:
        food = Food(screen)
        snake.grow()


def game():
    """Игра запускается и работает до выключения пользователем"""
    global reason_of_death
    play = True  # Работает ли игровое окно или нет
    frame = 0
    while play:
        if frame % 35 == 0:
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

        play, reason_of_death = snake.check_collision()

        # Проверка, что игрок нажал на кнопку "закрыть"
        for e_check in event.get():
            if e_check.type == QUIT:
                play = False

        # Проверка, что игрок нажал esc
        if key.get_pressed()[K_ESCAPE]:
            play = False


def game_over():
    """Конец игры"""
    # причины смерти:
    # 1) столкновение со стенкой
    # 2) выход из игры
    land.draw()
    result.draw(len(snake))
    display.update()
    sleep(1.5)


if __name__ == "__main__":
    game()
    game_over()
