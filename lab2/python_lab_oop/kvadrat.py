from python_lab_oop import abstract, color, rectangle


class kvadrat(rectangle.rectangle):
    def __init__(self, length = 10, color_ = 'Красный'):
        rectangle.rectangle.__init__(self, length=length, color_=color_)
        self.__name = 'Квадрат'

    def square(self):
        res = self._length ** 2
        return res

    def get_name(self):
        return self.__name

    def get_color(self):
        return self._color

    def repr(self):
        print(f'Название фигуры: {self.get_name()}\n'
              f'Цвет фигуры: {self.get_color()}\n'
              f'Площадь фигуры: {self.square()}\n'
              + '\n'
              )
