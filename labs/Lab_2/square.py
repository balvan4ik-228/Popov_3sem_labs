from rectangle import Rectangle


class Square(Rectangle):
    """Класс Квадрат (наследуется от Прямоугольника)"""

    name = "Квадрат"

    def __init__(self, side, color):
        # Квадрат - это прямоугольник с равными сторонами
        super().__init__(side, side, color)

    @property
    def side(self):
        return self.width

    @side.setter
    def side(self, value):
        self.width = value
        self.height = value

    def __repr__(self):
        return "{{фигура}}: сторона {side}, {{цвет}}: {color}, {{площадь}}: {area:.2f}".format(
            side=self.width,
            color=self.color_obj.color,
            area=self.area()
        )