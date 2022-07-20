from land import Land
from pygame import K_ESCAPE, QUIT, display, draw, event, key
from snake_constants import SCREEN_LENGTH, SCREEN_WIDTH, BLOCK_SIZE

screen = display.set_mode((SCREEN_LENGTH, SCREEN_WIDTH))  # Игровое окно
land = Land(screen)  # Задний фон


def game():
    """Игра запускается и работает до выключения пользователем"""
    play = True  # Работает ли игровое окно или нет
    while play:
        land.draw()

        for i in range(0, SCREEN_LENGTH, BLOCK_SIZE):
            draw.line(screen, "black", (i, 0), (i, SCREEN_WIDTH))

        for i in range(0, SCREEN_WIDTH, BLOCK_SIZE):
            draw.line(screen, "black", (0, i), (SCREEN_LENGTH, i))

        display.update()

        # Проверка, что игрок нажал на кнопку "закрыть"
        for e in event.get():
            if e.type == QUIT:
                play = False

        # Проверка, что игрок нажал esc
        if key.get_pressed()[K_ESCAPE]:
            play = False


if __name__ == "__main__":
    game()
