from figure import Figure
from color import Color
import math


class Circle(Figure):
    """Класс Круг"""

    name = "Круг"

    def __init__(self, radius, color):
        self.radius = radius
        self.color_obj = Color(color)

    def area(self):
        """Вычисление площади круга"""
        return math.pi * self.radius ** 2

    @property
    def name(self):
        return self.__class__.name

    def __repr__(self):
        return "{{фигура}}: радиус {radius}, {{цвет}}: {color}, {{площадь}}: {area:.2f}".format(
            radius=self.radius,
            color=self.color_obj.color,
            area=self.area()
        )