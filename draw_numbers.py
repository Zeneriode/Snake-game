"""
Реализация класса чисел
"""
from pygame import Rect, Surface, draw
from snake_constants import BLOCK_SIZE, SCREEN_LENGTH, SCREEN_WIDTH, SNAKE_COLOR


# pylint: disable=too-few-public-methods
class Number:
    """Прорисовка цифр"""

    def __init__(self, surface: Surface):
        """Базовый конструктор для создания счета очков"""
        self.size = BLOCK_SIZE
        self.color = SNAKE_COLOR
        self.surface = surface

    def __number(self, blocks: list[tuple[float, float]]):
        for block in blocks:
            draw.rect(
                self.surface, self.color, Rect(block[0], block[1], self.size, self.size)
            )

    def __number_1(self, center_x: float, center_y: float):
        """Создание пикселей первого числа"""
        blocks: list[tuple[float, float]] = [
            (center_x - BLOCK_SIZE / 2, center_y - BLOCK_SIZE * 2),
            (center_x - BLOCK_SIZE / 2, center_y - BLOCK_SIZE),
            (center_x - BLOCK_SIZE / 2, center_y),
            (center_x - BLOCK_SIZE / 2, center_y + BLOCK_SIZE),
            (center_x - BLOCK_SIZE / 2, center_y + BLOCK_SIZE * 2),
            (center_x - BLOCK_SIZE / 2 * 3, center_y - BLOCK_SIZE),
        ]
        self.__number(blocks)

    def __number_2(self, center_x: float, center_y: float):
        """Создание пикселей второго числа"""
        blocks: list[tuple[float, float]] = [
            (center_x + BLOCK_SIZE / 2, center_y - BLOCK_SIZE * 2),
            (center_x + BLOCK_SIZE / 2, center_y - BLOCK_SIZE),
            (center_x + BLOCK_SIZE / 2, center_y),
            (center_x + BLOCK_SIZE / 2, center_y + BLOCK_SIZE * 2),
            (center_x - BLOCK_SIZE / 2, center_y - BLOCK_SIZE * 2),
            (center_x - BLOCK_SIZE / 2, center_y),
            (center_x - BLOCK_SIZE / 2, center_y + BLOCK_SIZE * 2),
            (center_x - BLOCK_SIZE / 2 * 3, center_y - BLOCK_SIZE * 2),
            (center_x - BLOCK_SIZE / 2 * 3, center_y),
            (center_x - BLOCK_SIZE / 2 * 3, center_y + BLOCK_SIZE),
            (center_x - BLOCK_SIZE / 2 * 3, center_y + BLOCK_SIZE * 2),
        ]
        self.__number(blocks)

    def __number_3(self, center_x: float, center_y: float):
        """Создание пикселей третьего числа"""
        blocks: list[tuple[float, float]] = [
            (center_x + BLOCK_SIZE / 2, center_y - BLOCK_SIZE * 2),
            (center_x + BLOCK_SIZE / 2, center_y - BLOCK_SIZE),
            (center_x + BLOCK_SIZE / 2, center_y),
            (center_x + BLOCK_SIZE / 2, center_y + BLOCK_SIZE),
            (center_x + BLOCK_SIZE / 2, center_y + BLOCK_SIZE * 2),
            (center_x - BLOCK_SIZE / 2, center_y - BLOCK_SIZE * 2),
            (center_x - BLOCK_SIZE / 2, center_y),
            (center_x - BLOCK_SIZE / 2, center_y + BLOCK_SIZE * 2),
            (center_x - BLOCK_SIZE / 2 * 3, center_y - BLOCK_SIZE * 2),
            (center_x - BLOCK_SIZE / 2 * 3, center_y),
            (center_x - BLOCK_SIZE / 2 * 3, center_y + BLOCK_SIZE * 2),
        ]
        self.__number(blocks)

    def __number_4(self, center_x: float, center_y: float):
        """Создание пикселей четвёртого числа"""
        blocks: list[tuple[float, float]] = [
            (center_x + BLOCK_SIZE / 2, center_y - BLOCK_SIZE * 2),
            (center_x + BLOCK_SIZE / 2, center_y - BLOCK_SIZE),
            (center_x + BLOCK_SIZE / 2, center_y),
            (center_x + BLOCK_SIZE / 2, center_y + BLOCK_SIZE),
            (center_x + BLOCK_SIZE / 2, center_y + BLOCK_SIZE * 2),
            (center_x - BLOCK_SIZE / 2, center_y),
            (center_x - BLOCK_SIZE / 2 * 3, center_y - BLOCK_SIZE * 2),
            (center_x - BLOCK_SIZE / 2 * 3, center_y - BLOCK_SIZE),
            (center_x - BLOCK_SIZE / 2 * 3, center_y),
        ]
        self.__number(blocks)

    def __number_5(self, center_x: float, center_y: float):
        """Создание пикселей пятого числа"""
        blocks: list[tuple[float, float]] = [
            (center_x + BLOCK_SIZE / 2, center_y - BLOCK_SIZE * 2),
            (center_x + BLOCK_SIZE / 2, center_y),
            (center_x + BLOCK_SIZE / 2, center_y + BLOCK_SIZE),
            (center_x + BLOCK_SIZE / 2, center_y + BLOCK_SIZE * 2),
            (center_x - BLOCK_SIZE / 2, center_y - BLOCK_SIZE * 2),
            (center_x - BLOCK_SIZE / 2, center_y),
            (center_x - BLOCK_SIZE / 2, center_y + BLOCK_SIZE * 2),
            (center_x - BLOCK_SIZE / 2 * 3, center_y - BLOCK_SIZE * 2),
            (center_x - BLOCK_SIZE / 2 * 3, center_y - BLOCK_SIZE),
            (center_x - BLOCK_SIZE / 2 * 3, center_y),
            (center_x - BLOCK_SIZE / 2 * 3, center_y + BLOCK_SIZE * 2),
        ]
        self.__number(blocks)

    def __number_6(self, center_x: float, center_y: float):
        """Создание пикселей шестого числа"""
        blocks: list[tuple[float, float]] = [
            (center_x + BLOCK_SIZE / 2, center_y - BLOCK_SIZE * 2),
            (center_x + BLOCK_SIZE / 2, center_y),
            (center_x + BLOCK_SIZE / 2, center_y + BLOCK_SIZE),
            (center_x + BLOCK_SIZE / 2, center_y + BLOCK_SIZE * 2),
            (center_x - BLOCK_SIZE / 2, center_y - BLOCK_SIZE * 2),
            (center_x - BLOCK_SIZE / 2, center_y),
            (center_x - BLOCK_SIZE / 2, center_y + BLOCK_SIZE * 2),
            (center_x - BLOCK_SIZE / 2 * 3, center_y - BLOCK_SIZE * 2),
            (center_x - BLOCK_SIZE / 2 * 3, center_y - BLOCK_SIZE),
            (center_x - BLOCK_SIZE / 2 * 3, center_y),
            (center_x - BLOCK_SIZE / 2 * 3, center_y + BLOCK_SIZE),
            (center_x - BLOCK_SIZE / 2 * 3, center_y + BLOCK_SIZE * 2),
        ]
        self.__number(blocks)

    def __number_7(self, center_x: float, center_y: float):
        """Создание пикселей седьмого числа"""
        blocks: list[tuple[float, float]] = [
            (center_x + BLOCK_SIZE / 2, center_y - BLOCK_SIZE * 2),
            (center_x + BLOCK_SIZE / 2, center_y - BLOCK_SIZE),
            (center_x + BLOCK_SIZE / 2, center_y),
            (center_x + BLOCK_SIZE / 2, center_y + BLOCK_SIZE),
            (center_x + BLOCK_SIZE / 2, center_y + BLOCK_SIZE * 2),
            (center_x - BLOCK_SIZE / 2, center_y - BLOCK_SIZE * 2),
            (center_x - BLOCK_SIZE / 2 * 3, center_y - BLOCK_SIZE * 2),
            (center_x - BLOCK_SIZE / 2 * 3, center_y - BLOCK_SIZE),
        ]
        self.__number(blocks)

    def __number_8(self, center_x: float, center_y: float):
        """Создание пикселей восьмого числа"""
        blocks: list[tuple[float, float]] = [
            (center_x - BLOCK_SIZE / 2 * 3, center_y - BLOCK_SIZE * 2),
            (center_x - BLOCK_SIZE / 2 * 3, center_y - BLOCK_SIZE),
            (center_x - BLOCK_SIZE / 2 * 3, center_y),
            (center_x - BLOCK_SIZE / 2 * 3, center_y + BLOCK_SIZE),
            (center_x - BLOCK_SIZE / 2 * 3, center_y + BLOCK_SIZE * 2),
        ]
        self.__number_3(center_x, center_y)
        self.__number(blocks)

    def __number_9(self, center_x: float, center_y: float):
        """Создание пикселей девятого числа"""
        blocks: list[tuple[float, float]] = [
            (center_x - BLOCK_SIZE / 2 * 3, center_y - BLOCK_SIZE),
        ]
        self.__number_3(center_x, center_y)
        self.__number(blocks)

    def __number_0(self, center_x: float, center_y: float):
        """Создание пикселей нулевого числа"""
        blocks: list[tuple[float, float]] = [
            (center_x + BLOCK_SIZE / 2, center_y - BLOCK_SIZE * 2),
            (center_x + BLOCK_SIZE / 2, center_y - BLOCK_SIZE),
            (center_x + BLOCK_SIZE / 2, center_y),
            (center_x + BLOCK_SIZE / 2, center_y + BLOCK_SIZE),
            (center_x + BLOCK_SIZE / 2, center_y + BLOCK_SIZE * 2),
            (center_x - BLOCK_SIZE / 2, center_y - BLOCK_SIZE * 2),
            (center_x - BLOCK_SIZE / 2, center_y + BLOCK_SIZE * 2),
            (center_x - BLOCK_SIZE / 2 * 3, center_y - BLOCK_SIZE * 2),
            (center_x - BLOCK_SIZE / 2 * 3, center_y - BLOCK_SIZE),
            (center_x - BLOCK_SIZE / 2 * 3, center_y),
            (center_x - BLOCK_SIZE / 2 * 3, center_y + BLOCK_SIZE),
            (center_x - BLOCK_SIZE / 2 * 3, center_y + BLOCK_SIZE * 2),
        ]
        self.__number(blocks)

    # pylint: disable=too-many-return-statements
    def __one_digit(self, points: int, center_x: float, center_y: float):
        """Прорисовка очков одной цифрой"""
        match points:
            case 0:
                return self.__number_0(center_x, center_y)
            case 1:
                return self.__number_1(center_x, center_y)
            case 2:
                return self.__number_2(center_x, center_y)
            case 3:
                return self.__number_3(center_x, center_y)
            case 4:
                return self.__number_4(center_x, center_y)
            case 5:
                return self.__number_5(center_x, center_y)
            case 6:
                return self.__number_6(center_x, center_y)
            case 7:
                return self.__number_7(center_x, center_y)
            case 8:
                return self.__number_8(center_x, center_y)
            case _:
                return self.__number_9(center_x, center_y)

    def __two_digits(self, points: int, center_x: int, center_y: int):
        """Прорисовка очков двумя цифрами"""
        first, second = points // 10, points % 10

        distance_between_digits = BLOCK_SIZE * 10
        first_x = center_x - distance_between_digits / 6
        second_x = center_x + distance_between_digits / 6

        self.__one_digit(first, first_x, center_y)
        self.__one_digit(second, second_x, center_y)

    def __three_digits(self, points: int, center_x: int, center_y: int):
        """Прорисовка очков тремя цифрами"""
        first, second, third = points // 100, points // 10 % 10, points % 10

        # x - y - z
        distance_between_digits = BLOCK_SIZE * 14
        first_x = center_x - distance_between_digits / 2
        third_x = center_x + distance_between_digits / 2

        self.__one_digit(first, first_x, center_y)
        self.__one_digit(second, center_x, center_y)
        self.__one_digit(third, third_x, center_y)

    def draw_in_total(self, points: int):
        """Прорисовка цифр"""
        if points // 100 > 0:
            self.__three_digits(points, SCREEN_LENGTH / 2, SCREEN_WIDTH / 2)
        elif points // 10 > 0:
            self.__two_digits(points, SCREEN_LENGTH / 2, SCREEN_WIDTH / 2)
        else:
            self.__one_digit(points, SCREEN_LENGTH / 2, SCREEN_WIDTH / 2)

    def draw_in_game(self, points: int, snake_x: int, snake_y: int) -> None:
        """Прорисовка цифр во время игры"""
        global BLOCK_SIZE
        reduce_coefficient = 2
        BLOCK_SIZE /= reduce_coefficient
        # Узнаем, в какой четверти змея
        # Запускаем метод прорисовки в конкретной четверти
        BLOCK_SIZE *= reduce_coefficient

    def __draw_in_quarter1(self, points: int):
        """Выбор рисования в 1 четверти экрана"""
        if points // 100 > 0:
            self.__three_digits(points, SCREEN_LENGTH - 2 * BLOCK_SIZE / 2, SCREEN_WIDTH - 23 * BLOCK_SIZE / 2)
        elif points // 10 > 0:
            self.__two_digits(points, points, SCREEN_LENGTH - 2 * BLOCK_SIZE / 2, SCREEN_WIDTH - 23 * BLOCK_SIZE / 2)
        else:
            self.__one_digit(points, points, SCREEN_LENGTH - 2 * BLOCK_SIZE / 2, SCREEN_WIDTH - 23 * BLOCK_SIZE / 2)

    def __draw_in_quarter2(self, points: int):
        """Выбор рисования во 2 четверти экрана"""
        if points // 100 > 0:
            self.__three_digits(points, SCREEN_LENGTH - 42 * BLOCK_SIZE / 2, SCREEN_WIDTH - 23 * BLOCK_SIZE / 2)
        elif points // 10 > 0:
            self.__two_digits(points, SCREEN_LENGTH - 42 * BLOCK_SIZE / 2, SCREEN_WIDTH - 23 * BLOCK_SIZE / 2)
        else:
            self.__one_digit(points, SCREEN_LENGTH - 42 * BLOCK_SIZE / 2, SCREEN_WIDTH - 23 * BLOCK_SIZE / 2)

    def __draw_in_quarter3(self, points: int):
        """Выбор рисования в 3 четверти экрана"""
        if points // 100 > 0:
            self.__three_digits(points, SCREEN_LENGTH - 42 * BLOCK_SIZE / 2, SCREEN_WIDTH - 2 * BLOCK_SIZE / 2)
        elif points // 10 > 0:
            self.__two_digits(points, SCREEN_LENGTH - 42 * BLOCK_SIZE / 2, SCREEN_WIDTH - 2 * BLOCK_SIZE / 2)
        else:
            self.__one_digit(points, SCREEN_LENGTH - 42 * BLOCK_SIZE / 2, SCREEN_WIDTH - 2 * BLOCK_SIZE / 2)

    def __draw_in_quarter4(self, points: int):
        """Выбор рисования в 4 четверти экрана"""
        if points // 100 > 0:
            self.__three_digits(points, SCREEN_LENGTH - 2 * BLOCK_SIZE / 2, SCREEN_WIDTH - 2 * BLOCK_SIZE / 2)
        elif points // 10 > 0:
            self.__two_digits(points, SCREEN_LENGTH - 2 * BLOCK_SIZE / 2, SCREEN_WIDTH - 2 * BLOCK_SIZE / 2)
        else:
            self.__one_digit(points, SCREEN_LENGTH - 2 * BLOCK_SIZE / 2, SCREEN_WIDTH - 2 * BLOCK_SIZE / 2)
    # код будет сильно похож на __draw_in_quarter1, разница только в координатах рисования
