from random import randint

from pygame import Rect, Surface, draw
from snake_constants import BLOCK_SIZE, FOOD_COLOR, SCREEN_LENGTH, SCREEN_WIDTH


class Food:
    def __init__(self, surface: Surface):
        self.size = BLOCK_SIZE
        self.color = FOOD_COLOR
        self.surface = surface
        self.x = (
            randint(BLOCK_SIZE, SCREEN_LENGTH - BLOCK_SIZE * 3)
            // BLOCK_SIZE
            * BLOCK_SIZE
        )
        self.y = randint(BLOCK_SIZE, SCREEN_WIDTH) // BLOCK_SIZE * BLOCK_SIZE

    def draw(self) -> None:
        """Прорисовка еды"""
        draw.rect(
            self.surface,
            self.color,
            Rect(self.x, self.y, self.size, self.size),
        )
