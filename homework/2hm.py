class Figure:
    unit = 'cm'

    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def info(self):
        pass

class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.__side_length = side_length

    def calculate_area(self):
        return self.__side_length ** 2

    def info(self):
        print(f'Фигура: Квадрат')
        print(f'Единица измерения: {Figure.unit}')
        print(f'Длина стороны: {self.__side_length}')
        print(f'Площадь: {self.calculate_area()}')


    def get_side_length(self):
        return self.__side_length


    def set_side_length(self, value):
        if value > 0:
            self.__side_length = value
        else:
            raise ValueError("Длина стороны квадрата должна быть положительным числом.")
class Rectangle(Figure):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calculate_area(self):
        return self.__length * self.__width

    def info(self):
        print(f'Длина: {self.__length}, Ширина: {self.__width}, Всего: {self.__length * self.__width}')

if __name__ == '__main__':
    square1 = Square(4)
    square2 = Square(6)

    rectangle1 = Rectangle(5, 8)
    rectangle2 = Rectangle(7, 4)
    rectangle3 = Rectangle(6, 10)

    shapes = [square1, square2, rectangle1, rectangle2, rectangle3]


    for shape in shapes:
        shape.info()
        print()
# square = Square(5)
# square.info()
#
# print(square.get_side_length())
#
#
# square.set_side_length(6)
# square.info()