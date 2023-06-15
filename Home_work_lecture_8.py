from time import perf_counter

print('Task_1')
#Task1:
# Наришіть декоратор, який вимірює час виконання функції


                                        # декоратор

def func_time(func):

    def inner(*args, **kwargs):
        start = perf_counter()
        func(*args, **kwargs)
        print(f'\nFunction "{func.__name__}" execution time is {(perf_counter() - start):.10f}')

    return inner


                                        # побудова функцій


def my_years(age):
    years = ''
    if 2 <= age % 10 <= 4:
        years = 'роки'
    elif 5 <= age % 10 <= 9 or age % 10 == 0:
        years = 'років'
    else:
        years = 'рік'
    return years


@func_time
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
        age = int(input('Введіть ваш вік: '))
    except ValueError:
        print('Використовуйте тільки цифри!')
        continue
    else:
        my_age(age)
