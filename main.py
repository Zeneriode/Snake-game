from time import sleep
from food import Food
from land import Land
from pygame import K_ESCAPE, QUIT, display, draw, event, key, time, font, init
from snake import Snake
from draw_numbers import Number
from snake_constants import BLOCK_SIZE, SCREEN_LENGTH, SCREEN_WIDTH, \
    SNAKE_COLOR, LINE_COLOR

screen = display.set_mode((SCREEN_LENGTH, SCREEN_WIDTH))  # Игровое окно
land = Land(screen)  # Задний фон
snake = Snake(screen)  # Змея
food = Food(screen)  # еда
clock = time.Clock()  # смена кадров
result = Number(screen)
reason_of_death = ""


def check_food():
    """Проверяет, надо ли есть еду"""
    global food
    if snake.coordinates_x[0] == food.x_coordinate and snake.coordinates_y[
        0] == food.y_coordinate:
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
            draw.line(screen, LINE_COLOR, (i, 0), (i, SCREEN_WIDTH))

        for i in range(0, SCREEN_WIDTH, BLOCK_SIZE):
            draw.line(screen, LINE_COLOR, (0, i), (SCREEN_LENGTH, i))

        result.draw_in_game(len(snake), snake.coordinates_x[0],
                            snake.coordinates_y[0])

        display.update()
        clock.tick(200)
        frame += 1

        play, reason_of_death = snake.check_collision()

        # Проверка, что игрок нажал на кнопку "закрыть"
        for e_check in event.get():
            if e_check.type == QUIT:
                play = False
                reason_of_death = "Вы покинули игру!"

        # Проверка, что игрок нажал esc
        if key.get_pressed()[K_ESCAPE]:
            play = False
            reason_of_death = "Вы покинули игру!"


def game_over():
    """Конец игры"""
    land.draw()
    result.draw_in_total(len(snake))
    # Задаём шрифт и размер текста
    text_font = font.Font("C:\\WINDOWS\\Fonts\\candaral.ttf", 50)
    # Задаём контент и цвет текста
    text = text_font.render(reason_of_death, False, SNAKE_COLOR)
    # Задаём форму и местонахождение текста
    text_line = text.get_rect()
    text_line.center = (SCREEN_LENGTH / 2, SCREEN_WIDTH / 2 + 200)
    # рисуем текст
    screen.blit(text, text_line)

    display.update()
    sleep(2.5)


init()
if __name__ == "__main__":
    game()
    game_over()
