from snake_constants import BLOCK_SIZE, SNAKE_COLOR
from pygame import Surface


class Snake:
    def __init__(self, surface: Surface) -> None:
        self.size = BLOCK_SIZE
        self.color = SNAKE_COLOR
        self.surface = surface
        self.coordinates_x: list[int] = []
        self.coordinates_y: list[int] = []
        self.speed = 10
