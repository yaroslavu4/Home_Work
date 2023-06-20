# Task_1
# Створіть клас "Транспортний засіб" та підкласи "Автомобіль", "Літак", "Корабель", наслідувані від
# "Транспортний засіб". Наповніть класи атрибутами на свій розсуд.
# Створіть обʼєкти класів "Автомобіль", "Літак", "Корабель".


class Vehicle:
    seats = None
    length = None
    weight = None
    name = "Vehicle"

    def __init__(self, s, l, w):
        self.seats = s
        self.length = l
        self.weight = w

    def vehicle_specifics(self):  # цей метод повертає крапку тільки тому, що він на кінці речення, потім я його змінюю
        return '.'

    def method_func(self):
        res = f'The type of vehicle is "{self.name}", it could take up to "{self.seats}" passengers,' \
              f' it`s also "{self.length}" meters long and "{self.weight}" tone weight{self.vehicle_specifics()}'
        return res


class Car(Vehicle):
    name = 'Car'
    wheels = 4
    engine = 1

    def vehicle_specifics(self):
        res = f'. Your "{self.name.lower()}" also has "{self.wheels}" wheels and "{self.engine}" engine(s)'
        return res


class Plane(Car):
    name = 'Plane'
    engine = 2


class Boat(Car):
    name = 'Boat'
    engine = 1


# my_vehicle = Vehicle(40, 50, 3)
# print(f'\n{my_vehicle.method_func()}')

my_car = Car(4, 3, 1.5)
print(f'\n{my_car.method_func()}')

my_plane = Plane(350, 65, 96)
print(f'\n{my_plane.method_func()}\n')

my_boat = Boat(12, 25, 12)
print(my_boat.method_func())
