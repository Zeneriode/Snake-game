"""
Основной файл игры. Используйте его для запуска самой игры.
В этом файле создаются все предметы, необходимые для игры, а также реализованы
функции, которые запускают игру и экран после игры.
"""
from time import sleep

from draw_numbers import Number
from food import Food, create_food, create_start_foods, DefaultFood, CoolFood
from land import Land

# pylint: disable=no-name-in-module
from pygame import K_ESCAPE, QUIT, display, draw, event, font, init, key, time
from snake import Snake
from snake_constants import (
    BLOCK_SIZE,
    LINE_COLOR,
    SCREEN_LENGTH,
    SCREEN_WIDTH,
    SNAKE_COLOR,
)

screen = display.set_mode((SCREEN_LENGTH, SCREEN_WIDTH))  # Игровое окно
land = Land(screen)  # Задний фон
snake = Snake(screen)  # Змея
foods = []
create_start_foods(foods=foods, snake=snake, surface=screen)
clock = time.Clock()  # смена кадров
result = Number(screen)
# pylint: disable=C0103
reason_of_death = ""


# TODO (пока не трогать) подправить взаимодействие со змеей (пока она всегда растет на 1 блок)
# TODO (если ещё нужно) подготовить 1 задачу по for с уроков по информатике
# TODO (если не получается todo снизу) подготовить вопросы по вещам, которые не ясны (например, что значит "-> Food")
def check_food() -> Food:
    """Проверяет, надо ли есть еду"""
    # TODO сделать всё согласно плану снизу. Если не получается - писать Тиме или придумать новый план
    # Главное - чтобы всё работало
    """
    как работает функция
    0) функция должна работать каждый кадр
    1) проверяем координаты еды и змеи (могу)
    2) Если совпадают:
    2.1) Убираем еду на этих координатах (не могу)
    2.2) Добавляем 1 блок змеи к змейке (могу)
    2.3) Создаём новый блок еды на экране (не могу)
    """
    for food in foods():
    if (
            snake.coordinates_x[0] == food.x_coordinate
            and snake.coordinates_y[0] == food.y_coordinate
    ):
        snake.grow()
        food.creature()


def game():
    """Игра запускается и работает до выключения пользователем"""
    # pylint: disable=[C0103, W0603]
    global reason_of_death, foods
    play = True  # Работает ли игровое окно или нет
    frame = 0
    while play:
        if frame % 35 == 0:
            land.draw()
            snake.draw()
            for food in foods:
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
