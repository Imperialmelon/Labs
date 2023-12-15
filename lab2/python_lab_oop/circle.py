from python_lab_oop import abstract , color
from math import pi


class circle(abstract.figure):
    def __init__(self, rad = 10, color_ = 'Красный '):
        self.__name = 'Круг'
        self.__color = color.color(color_)
        self.__rad = rad

    def square(self):
        res = pi * self.__rad ** 2
        return res

    def get_name(self):
        return self.__name

    def get_color(self):
        return self.__color

    def repr(self):
        print(f'Название фигуры: {self.get_name()}\n'
              f'Цвет фигуры: {self.get_color()}\n'
              f'Площадь фигуры: {self.square()}\n'
              + '\n'
              )
