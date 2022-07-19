from pygame import Surface
from snake_constants import BLOCK_SIZE, SNAKE_COLOR, SCREEN_LENGTH
from random import randint


class Snake:
    def __init__(self, surface: Surface) -> None:
        self.size = BLOCK_SIZE
        self.color = SNAKE_COLOR
        self.surface = surface
        self.x = randint(0, SCREEN_LENGTH)
        self.y = randint(0, SCREEN_LENGTH)
        self.coordinates_x: list[int] = []
        self.coordinates_y: list[int] = []
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
        pass
