from random import choice
print('Task_1\n')
# Task1:
# Напишіть функцію, що приймає один аргумент будь-якого типу та повертає цей аргумент, перетворений на float.
# Якщо перетворити не вдається функція має повернути 0.

VALUES = (1, '2', (3,), 'four', ['fi', 've'], 6, "7", (8,), 'nine', 10, '', 9.0, 3.0, {2, 3, 5}, {'one': 1, 'two': 2})

def float_maker(x):
    print(f'taken value is: {x}')
    if str(x).isdigit() or isinstance(x, float):
        x = float(x)
    else:
        x = 0
    z = f'Converted result is: {x}'
    return z

print(float_maker(choice(VALUES)))
print('='*30)
print('\n')


print('Task_2\n')
# Task2:
# Напишіть функцію, що приймає два аргументи. Функція повинна:
# якщо аргументи відносяться до числових типів (int, float) - повернути перемножене значення цих аргументів,
# якщо обидва аргументи це строки (str) - обʼєднати в одну строку та повернути
# у будь-якому іншому випадку повернути кортеж з цих аргументів

cases = {                   # словарь создал лишь чтобы показать случаи, попадающие в аргументы функции
    'case_1': [5, 5.0],
    'case_2': ['hello', 'world'],
    'case_3': [5, 'days']
}
values = []
for i in cases.values():    # создал список из данных разного типа
    values.append(i)

types = (float, int)
def my_function(x, y):
    if type(x) in types and type(y) in types:
        return x * y
    elif isinstance(x, str) and isinstance(y, str):
        return x + y
    else:
        return (x, y)

print(my_function(*choice(values)))    # и распаковал список в аргументы функции
print('='*30)
print('\n')


print('Task_3')
# Task3:
# Перепишіть за допомогою функцій вашу программу "Касир в кінотеатрі", яка буде виконувати наступне:
# Попросіть користувача ввести свсвій вік.
age = ''
while not age:  # сделал так чтоб пользователь в любом случае что-то вводил в строку ввода, не оставлял ее пустой
    age = input('Please, tell us your age: ')

if not age.isdigit():
    print('Try to use digits only!')
else:
    int_age = int(age)



    if int_age <= 0 or int_age > 105:
        print('Are you even a human ?))')

    elif int_age < 6:
        print('Where are your parents?')

    elif int_age < 16:
        print('This movie for adults only!')
        if '7' in age:  # решил сделать вложенный if с цифрой 7 ибо возраст 7, 17, ..., 67 попадают сразу под 2 условия
            print('And you`re gonna get lucky!')

    elif int_age > 65:
        print('Please show us your pensioner`s ID!')
        if '7' in age:
            print('And you`re gonna get lucky!')

    else:
        print('Unfortunately all tickets have run out!')
        if '7' in age:
            print('But you`re gonna get lucky!')







