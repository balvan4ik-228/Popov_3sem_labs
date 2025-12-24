from figure import Figure
from color import Color
import math


class Rectangle(Figure):
    """Класс Прямоугольник"""

    name = "Прямоугольник"

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color_obj = Color(color)

    def area(self):
        """Вычисление площади прямоугольника"""
        return self.width * self.height

    @property
    def name(self):
        return self.__class__.name

    def __repr__(self):
        return "{{фигура}}: {width} {height}, {{цвет}}: {color}, {{площадь}}: {area:.2f}".format(
            width=self.width,
            height=self.height,
            color=self.color_obj.color,
            area=self.area()
        )