from python_lab_oop import abstract , color


class rectangle(abstract.figure):
    def __init__(self, height = 0, length = 0, color_= 'Красный'):
        self._length = length
        self.__height = height
        self._color = color.color(color_)
        self._name = 'Прямоугольник'

    def square(self):
        res = self.__height * self._length
        return res

    def get_name(self):
        return self._name

    def get_color(self):
        return self._color

    def repr(self):
        print(f'Название фигуры: {self.get_name()}\n'
              f'Цвет фигуры: {self.get_color()}\n'
              f'Площадь фигуры: {self.square()}\n'
              + '\n'
              )