# Task
# Доопрацюйте класс Point так, щоб в атрибути x та y обʼєктів цього класу можна було записати
# тільки обʼєкти класу int або float
# Доопрацюйте класс Line так, щоб в атрибути begin та end обʼєктів цього класу можна було записати
# тільки обʼєкти класу Point
# Створіть класс Triangle (трикутник), який задається трьома точками (обʼєкти классу Point).
# Реалізуйте перевірку даних, аналогічно до класу Line.
# Визначет метод, що містить площу трикутника. Для обчислень можна використати формулу Герона


class Point:
    x_coord = 0
    y_coord = 0

    def __init__(self, x, y):
        self.x_coord = x
        self.y_coord = y
        if type(self.x_coord) not in (int, float) and type(self.y_coord) not in (int, float):  # перевірка на тип
            print('Use type " int or float " only!!!')  # float, int
            raise TypeError

    def __str__(self):
        return f'Point {self.x_coord}:{self.y_coord}'

    def __getitem__(self, item):
        print(f'__getitem__ {item}')
        if item == 0:
            return self.x_coord
        elif item == 1:
            return self.y_coord
        else:
            raise TypeError

    def __setitem__(self, item, value):
        print(f'__setitem__ {item}, {value}')
        if item == 0:
            self.x_coord = value
        elif item == 1:
            self.y_coord = value
        else:
            raise TypeError

    def __add__(self, other):
        return Line(self, other)


class Line:
    begin_point = None
    end_point = None

    def __init__(self, begin, end):
        self.begin_point = begin
        self.end_point = end
        if not all(isinstance(i, Point) for i in (begin, end)):  # перевірка на тип Point
            print('Wrong type!')
            raise TypeError

    def __str__(self):
        return f'Line from [{self.begin_point}] to [{self.end_point}]'

    def length(self):
        k1 = self.begin_point.x_coord - self.end_point.x_coord
        k2 = self.begin_point.y_coord - self.end_point.y_coord

        return (k1 ** 2 + k2 ** 2) ** 0.5

    def __contains__(self, item):
        """ a in b """
        print('__contains__', item)
        return self.begin_point == item or self.end_point == item


# В умові завдання вы просили щоб в аргументи обєкту класу Трикутник надходили обєкти класу Точка
# але я віришив як аргументи передати обьекти Лінії, не дарма ж Ви їх створювали, та здається так ніби навіть легше
class Triangle:
    a_side = None
    b_side = None
    c_side = None

    def __init__(self, a, b, c):
        self.a_side = a
        self.b_side = b
        self.c_side = c
        if not all(isinstance(i, Line) for i in (a, b, c)):  # перевірка на тип Line
            print('Wrong class!')
            raise TypeError

    def triangle_square(self):
        p = (self.a_side.length() + self.b_side.length() + self.c_side.length()) / 2
        square = pow((p * (p - self.a_side.length()) * (p - self.b_side.length()) * (p - self.c_side.length())), 0.5)
        return square

    def __str__(self):
        return f'Desired perimeter is "{self.triangle_square()}"'


p1 = Point(0, 7)
p2 = Point(5, 0)
p3 = Point(0, 0)
# print(p1[0])
# print(p1[1])

# p1[1] = 100


line1 = Line(p1, p2)
line2 = Line(p2, p3)
line3 = Line(p3, p1)

triangle = Triangle(line1, line2, line3)
print(triangle)
