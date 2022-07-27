from random import randint

from pygame import Rect, Surface, draw
from snake_constants import BLOCK_SIZE, SCREEN_LENGTH, SCREEN_WIDTH, SNAKE_COLOR


class Snake:
    def __init__(self, surface: Surface) -> None:
        self.size = BLOCK_SIZE
        self.color = SNAKE_COLOR
        self.surface = surface
        x = randint(BLOCK_SIZE, SCREEN_LENGTH - BLOCK_SIZE * 3) // BLOCK_SIZE * BLOCK_SIZE
        y = randint(BLOCK_SIZE, SCREEN_WIDTH) // BLOCK_SIZE * BLOCK_SIZE
        self.coordinates_x: list[int] = [x, x - BLOCK_SIZE]
        self.coordinates_y: list[int] = [y, y]
        self.speed = BLOCK_SIZE

    def eat(self) -> bool:
        """Ест яблоки"""
        pass

    def move(self) -> None:
        """Двигает змею"""
        pass

    def change_direction(self) -> None:
        """Поворачивает змею"""
        pass

    def check_collision(self) -> bool:
        """Проверяет не врезалась ли змея"""
        pass

    def draw(self) -> None:
        """Прорисовка цвета змеи"""
        for i in range(len(self.coordinates_x)):
            draw.rect(self.surface,
            self.color,
            Rect(self.coordinates_x[i], self.coordinates_y[i], self.size, self.size))
