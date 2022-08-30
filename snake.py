from random import randint

from pygame import K_w, K_a, K_s, K_d, Rect, Surface, draw, key
from snake_constants import (
    BLOCK_SIZE,
    SCREEN_LENGTH,
    SCREEN_WIDTH,
    SNAKE_COLOR,
)


class Snake:
    def __init__(self, surface: Surface) -> None:
        self.size = BLOCK_SIZE
        self.color = SNAKE_COLOR
        self.surface = surface
        self.direction = None
        x = (
                randint(BLOCK_SIZE, SCREEN_LENGTH - BLOCK_SIZE * 3)
                // BLOCK_SIZE
                * BLOCK_SIZE
        )
        y = randint(BLOCK_SIZE, SCREEN_WIDTH) // BLOCK_SIZE * BLOCK_SIZE
        self.coordinates_x: list[int] = [x, x - BLOCK_SIZE]
        self.coordinates_y: list[int] = [y, y]
        self.speed = BLOCK_SIZE

    def eat(self) -> bool:
        """Ест яблоки"""
        pass

    def move(self) -> None:
        """Двигает змею"""
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
        if key.get_pressed()[K_w]:
            self.direction = "u"

        elif key.get_pressed()[K_a]:
            self.direction = "l"

        elif key.get_pressed()[K_s]:
            self.direction = "d"

        elif key.get_pressed()[K_d]:
            self.direction = "r"

    def check_collision(self) -> bool:
        """Проверяет не врезалась ли змея"""
        pass

    def draw(self) -> None:
        """Прорисовка змеи"""
        for i in range(len(self.coordinates_x)):
            draw.rect(
                self.surface,
                self.color,
                Rect(
                    self.coordinates_x[i], self.coordinates_y[i], self.size, self.size
                ),
            )
