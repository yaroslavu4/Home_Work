# Task
# Доопрацюйте класс Triangle зі свого попереднього дз.
# Реалізуйте перевірку даних на те що вершини є Point за допомогою property.
# Реалізуйте ітератор по вершинам трикутника


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
        return f'Point ({self.x_coord}:{self.y_coord})'

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

    @property
    def begin_p(self):
        return self.begin_point

    @begin_p.setter
    def begin_p(self, new_begin_point):
        if not isinstance(new_begin_point, Point):
            print('Wrong type')
            raise TypeError
        else:
            self.begin_point = new_begin_point

    @begin_p.deleter
    def begin_p(self):
        del self.begin_point

    @property
    def end_p(self):
        return self.end_point

    @end_p.setter
    def end_p(self, new_end_point):
        if not isinstance(new_end_point, Point):
            print('Wrong type')
            raise TypeError
        else:
            self.end_point = new_end_point

    @end_p.deleter
    def end_p(self):
        del self.end_point

    def __str__(self):
        return f'Line from [{self.begin_point}] to [{self.end_point}]'

    @property
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
    iter_max = 3
    iter_current = -1

    def __init__(self, a, b, c):
        self.a_side = a
        self.b_side = b
        self.c_side = c
        self.my_tuple = (a, b, c)

        if not all(isinstance(i, Line) for i in (a, b, c)):  # перевірка на тип Line
            print('Wrong class!')
            raise TypeError

    @property
    def triangle_square(self):
        p = (self.a_side.length + self.b_side.length + self.c_side.length) / 2
        square = pow((p * (p - self.a_side.length) * (p - self.b_side.length) * (p - self.c_side.length)), 0.5)
        return square

    def __str__(self):
        return f'Desired perimeter is "{self.triangle_square}"'

    def __iter__(self):
        self.iter_current = self.__class__.iter_current
        return self

    def __next__(self):
        self.iter_current += 1
        if self.iter_current >= self.iter_max:
            raise StopIteration
        else:
            return str(self.my_tuple[self.iter_current].begin_point), str(self.my_tuple[self.iter_current].end_point)
            # повертаю кортеж з 2 точок, бо атрибутами класу Trianle у минулому ДЗ я зробив лінії а не точки :(


p1 = Point(0, 7)
p2 = Point(5, 0)
p3 = Point(0, 0)
# print(p1[0])
# print(p1[1])

# p1[1] = 100


line1 = Line(p1, p2)
print(line1.length)
line2 = Line(p2, p3)
print(line2.length)
line3 = Line(p3, p1)
print(line3.length)

triangle = Triangle(line1, line2, line3)
print(triangle)


print('\nЛекція 12 ДЗ:')
print('Вершини трикутника:')

for i in triangle:
    print(i[0])

#===========================#
# Перевірки
print('\nПеревірки')
line4 = Line(p1, p2)
print(line4.begin_point)
print(line4.end_point)

line4.begin_p = Point(2, 3)
line4.end_p = Point(3, 2)
print(line4.begin_point)
print(line4.end_point)

del line4.end_p
del line4.begin_p
print(line4.begin_point)
print(line4.end_point)
