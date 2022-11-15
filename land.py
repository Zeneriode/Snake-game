"""
Реализация класса земли
"""
from pygame import Rect, Surface, draw
from snake_constants import LAND_COLOR, SCREEN_LENGTH, SCREEN_WIDTH


# pylint: disable=too-few-public-methods
class Land:
    """Задний фон игры"""

    def __init__(self, surface: Surface) -> None:
        """Базовый конструктор для создания фона игры"""
        self.color = LAND_COLOR
        self.length = SCREEN_LENGTH
        self.width = SCREEN_WIDTH
        self.surface = surface

    def draw(self) -> None:
        """Прорисовка заднего фона"""
        draw.rect(self.surface, self.color, Rect(0, 0, self.length, self.width))
