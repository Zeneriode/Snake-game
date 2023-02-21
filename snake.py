"""
Реализация класса змеи
"""
from random import randint
from typing import Optional, Tuple

# pylint: disable=no-name-in-module
from pygame import K_a, K_d, K_s, K_w, Rect, Surface, draw, key

# pylint: disable=import-error
from snake_constants import BLOCK_SIZE, SCREEN_LENGTH, SCREEN_WIDTH, SNAKE_COLOR


class Snake:
    """
    Змея, которая ползает по игровому полю\n

    Methods:
        grow растит змею
        get_effect даёт эффект змее
        move двигает змею
        change_direction поворачивает змею
        check_collision проверяет не врезалась ли змея
        draw рисует змею
    """

    def __init__(self, surface: Surface) -> None:
        self.size = BLOCK_SIZE
        self.color = SNAKE_COLOR
        self.surface = surface
        self.direction = ""
        head_x = (
            randint(BLOCK_SIZE, SCREEN_LENGTH - BLOCK_SIZE * 3)
            // BLOCK_SIZE
            * BLOCK_SIZE
        )
        head_y = randint(BLOCK_SIZE, SCREEN_WIDTH) // BLOCK_SIZE * BLOCK_SIZE
        self.coordinates_x: list[int] = [head_x, head_x]
        self.coordinates_y: list[int] = [head_y, head_y]
        self.speed = BLOCK_SIZE

    def __len__(self):
        return len(self.coordinates_x) - 2

    def grow(self) -> None:
        """Змея растёт"""
        self.coordinates_x.append(-BLOCK_SIZE)
        self.coordinates_y.append(-BLOCK_SIZE)

    def get_effect(self, effect: tuple[str, float]):
        if effect[0] == "вырасти":
            self.grow()

    def move(self) -> None:
        """Двигает змею"""
        for i in range(len(self.coordinates_x) - 1, 0, -1):
            self.coordinates_x[i] = self.coordinates_x[i - 1]
            self.coordinates_y[i] = self.coordinates_y[i - 1]

        if self.direction == "r":
            self.coordinates_x[0] += self.speed

        elif self.direction == "l":
            self.coordinates_x[0] -= self.speed

        elif self.direction == "u":
            self.coordinates_y[0] -= self.speed

        elif self.direction == "d":
            self.coordinates_y[0] += self.speed

    def change_direction(self) -> None:
        """Поворачивает змею"""
        if key.get_pressed()[K_w] and self.direction != "d":
            self.direction = "u"

        elif key.get_pressed()[K_a] and self.direction != "r":
            self.direction = "l"

        elif key.get_pressed()[K_s] and self.direction != "u":
            self.direction = "d"

        elif key.get_pressed()[K_d] and self.direction != "l":
            self.direction = "r"

    def check_collision(self) -> Tuple[bool, Optional[str]]:
        """Проверяет не врезалась ли змея"""
        if (
            0 <= self.coordinates_x[0] <= SCREEN_LENGTH
            and 0 <= self.coordinates_y[0] <= SCREEN_WIDTH
        ):
            return True, None
        return False, "Вы врезались в стену!"

    def draw(self) -> None:
        """Прорисовка змеи"""
        number_of_iterations = len(self.coordinates_x)
        for i in range(number_of_iterations):
            draw.rect(
                self.surface,
                self.color,
                Rect(
                    self.coordinates_x[i], self.coordinates_y[i], self.size, self.size
                ),
            )
