from abc import ABC, abstractmethod


class Figure(ABC):
    """Абстрактный класс Геометрическая фигура"""

    @abstractmethod
    def area(self):
        """Абстрактный метод для вычисления площади"""
        pass

    @property
    @abstractmethod
    def name(self):
        """Абстрактное свойство для имени фигуры"""
        pass

    def __repr__(self):
        """Базовый метод repr, который можно переопределить"""
        return f"{self.name}"