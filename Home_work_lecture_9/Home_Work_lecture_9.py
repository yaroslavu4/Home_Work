import lib


# Створіть файл lib.py, помістіть в нього функції вашої гри.
# Імпортуйте гру в основний файл і запустіть гру з основного файлу


age = ''
while not age:
    try:
        age = int(input('Введіть ваш вік: '))
    except ValueError:
        print('Використовуйте тільки цифри!')
        continue
    else:
        lib.my_age(age)
