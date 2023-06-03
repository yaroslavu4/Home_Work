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

                                # Побудова функцій

def my_years(age):
    years = ''
    if 2 <= age % 10 <= 4:
        years = 'роки'
    elif 5 <= age % 10 <= 9 or age % 10 == 0:
        years = 'років'
    else:
        years = 'рік'
    return years


def my_age(age):
    if age <= 0 or age > 105:
        print(f'Вам {age} {my_years(age)}, ви взагалі людина?')
    elif age < 7:
        print(f'Тобі ж {age} {my_years(age)}! Де твої батьки?')
    elif age < 16:
        print(f'Тобі лише {age} {my_years(age)}, а це е фільм для дорослих!')
        if '7' in str(age):
            print(f'А також у твоєму віці є "7", вам пощастить')
    elif age > 65:
        print(f'Вам {age} {my_years(age)}? Покажіть пенсійне посвідчення!')
        if '7' in str(age):
            print(f'А також у вашому віці є "7", вам пощастить')
    else:
        print(f'Незважаючи на те, що вам {age} {my_years(age)}, білетів всеодно нема!')
        if '7' in str(age):
            print(f'Але у вашому віці є "7", вам пощастить')


                                    # Основний код
age = ''
while not age:
    try:
        age = int(input('Please, tell us your age: '))
    except ValueError:
        print('Try to use digits only!')
        continue
    else:
        my_age(age)







