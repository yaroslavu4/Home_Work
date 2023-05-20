print('Task 1')
# Task 1: Напишіть программу "Касир в кінотеватрі", яка буде виконувати наступне:
# Попросіть користувача ввести свсвій вік (можно використати константу або input()).
# - якщо користувачу менше 6 - вивести повідомлення "Де твої батьки?"
# - якщо користувачу менше 16 - вивести повідомлення "Це фільм для дорослих!"
# - якщо користувачу більше 65 - вивести повідомлення "Покажіть пенсійне посвідчення!"
# - якщо вік користувача містить цифру 7 - вивести повідомлення "Вам пощастить!"
# - у будь-якому іншому випадку - вивести повідомлення "А білетів вже немає!"
# P.S. На екран має бути виведено лише одне повідомлення, якщо вік користувача містить цифру тільки відповідне
# повідомлення! Також подумайте над варіантами, коли введені невірні або неадекватні (неможливі) дані.


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

