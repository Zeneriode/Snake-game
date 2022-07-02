import pygame

from pygame import display, event, key
from pygame import QUIT, K_ESCAPE
from snake_constants import *
from land import Land

screen = display.set_mode((SCREEN_LENGTH, SCREEN_WIDTH))  # Игровое окно
land = Land(screen)  # Задний фон


def game():
    """Игра запускается и работает до выключения пользователем"""
    play = True  # Работает ли игровое окно или нет
    while play:
        land.draw()

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



