from snake_constants import SNAKE_COLOR, BLOCK_SIZE
from pygame import Surface

class Snake:
    def __init__(self, surface: Surface) -> None:
        self.size = BLOCK_SIZE
        self.color = SNAKE_COLOR
        self.surface = surface
        self.coordinates_x = []
        self.coordinates_y = []
        self.speed = 10
