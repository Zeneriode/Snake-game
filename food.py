"""
Реализация класса еды
"""
from random import randint
from snake import Snake
from numpy.random import choice
from abc import ABC, abstractmethod

from pygame import Rect, Surface, draw
from snake_constants import (
    BLOCK_SIZE,
    DEFAULT_FOOD_COLOR,
    COOL_FOOD_COLOR,
    SUPER_FOOD_COLOR,
    SCREEN_LENGTH,
    SCREEN_WIDTH,
)


class Food(ABC):
    """
    Еда, которую ест змея.

    Attributes
    ----------
    surface: окно на котором происходит вся игра
    size: размер еды
    color: цвет еды

    Methods
    -------
    draw():
        рисует еду
    give_effect():
        возвращает эффект от еды
    """

    # TODO узнать, как сохранить список объектов класса, в котором используются эти объекты
    def __init__(self, surface: Surface, foods: list, snake: Snake):
        """
        Стандартный конструктор для еды. Фиксирует размер, цвет, координаты еды.

        :param surface: окно на котором происходит вся игра
        """
        self.size = BLOCK_SIZE
        self.color: tuple[int, int, int] = ...
        self.surface = surface
        self.__generate_coordinates(foods, snake)

    def __generate_coordinates(self, foods: list, snake: Snake):
        """Создаёт координаты"""
        while True:
            self.x_coordinate = (
                    randint(BLOCK_SIZE, SCREEN_LENGTH - BLOCK_SIZE * 3)
                    // BLOCK_SIZE
                    * BLOCK_SIZE
            )
            self.y_coordinate = randint(BLOCK_SIZE, SCREEN_WIDTH) // BLOCK_SIZE * BLOCK_SIZE

            for food in foods:
                if food.x_coordinate == self.x_coordinate \
                        and food.y_coordinate == self.y_coordinate:
                    continue

            for body_x, body_y in zip(snake.coordinates_x, snake.coordinates_y):
                if body_x == self.x_coordinate and body_y == self.y_coordinate:
                    continue

            break

    def draw(self) -> None:
        """Прорисовка еды"""
        draw.rect(
            self.surface,
            self.color,
            Rect(self.x_coordinate, self.y_coordinate, self.size, self.size),
        )

    @abstractmethod
    def give_effect(self) -> tuple[str, float]:
        """
        Даёт эффект.

        :return: Команду "Вырасти", а также количество блоков, на которое змейка должна вырасти
        """


class DefaultFood(Food):
    """Обычная еда - при поедании прибавляет 1 блок змейке"""

    def __init__(self, surface: Surface, foods: list, snake: Snake):
        """
        Конструктор для создания обычной еды\n
        :param surface: окно, в котором будет рисоваться еда
        """
        super().__init__(surface, foods, snake)
        self.color = DEFAULT_FOOD_COLOR

    def give_effect(self) -> tuple[str, float]:
        return "вырасти", 1


class CoolFood(Food):
    """Крутая еда - при поедании прибавляет 2 блока змейке"""

    def __init__(self, surface: Surface, foods: list, snake: Snake):
        """
        Конструктор для создания крутой еды\n
        :param: CoolFood обозначает то что это крутая еда
        """
        super().__init__(surface, foods, snake)
        self.color = COOL_FOOD_COLOR

    def give_effect(self) -> tuple[str, float]:
        return "вырасти", 2


class SuperFood(Food):
    """Супер еда - при поедании прибавляет 3 блока змейке"""

    def __init__(self, surface: Surface, foods: list, snake: Snake):
        """Конструктор для создания еды"""
        super().__init__(surface, foods, snake)
        self.color = SUPER_FOOD_COLOR

    def give_effect(self) -> tuple[str, float]:
        return "вырасти", 3


class TerribleFood(Food):
    """Ужасная еда - при поедании забирает 3 блока змейке"""

    def __init__(self, surface: Surface, foods: list, snake: Snake):
        """Конструктор для создания еды"""
        super().__init__(surface, foods, snake)
        self.color = SUPER_FOOD_COLOR

    def give_effect(self) -> tuple[str, float]:
        """
        Даёт эффект.

        :return: Команду "убавиться", а также количество блоков, на которое змейка должна убавиться
        """
        return "убавиться", 3


__types_of_food = [DefaultFood, CoolFood, SuperFood, TerribleFood]
__types_probability = [0.5, 0.4, 0.05, 0.05]


def create_food(surface: Surface, foods: list[Food], snake: Snake):
    """Создаёт еду во время игры"""
    type_of_food = choice(__types_of_food, p=__types_probability)
    foods.append(type_of_food(surface, foods, snake))


def create_start_foods(surface: Surface, foods: list[Food], snake: Snake):
    """Создаёт еду в начале игры"""
    for _ in range(3):
        create_food(surface, foods, snake)


if __name__ == "__main__":
    help(Food)
