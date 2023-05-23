print('Task 1')
# Task 1
# Напишіть код, який зформує строку, яка містить певну інформацію про символ за його номером у слові.
# Наприклад "The [номер символу] symbol in '[тут слово]' is '[символ з відповідним порядковим номером в слові]'".
# Слово та номер символу отримайте за допомогою input() або скористайтеся константою. Наприклад (слово - "Python" а
# номер символу 3) - "The 3 symbol in 'Python' is 't' ".

string = ''
while not string:
    string = input('Please enter text here: ')
symbol = input('Enter symbol number: ')
if symbol[0] == '-':
    if symbol[1:].isdigit():
        if int(symbol) < -len(string):
            print('Symbol number is out of string, try again!')
        else:
            print(f'The symbol {int(symbol)} in {string} is "{string[int(symbol)]}"')
    else:
        print('Use digits only!')
else:
    if symbol.isdigit():
        if int(symbol) >= len(string):
            print('Symbol number is out of string, try again!')
        else:
            print(f'The symbol {int(symbol)} in {string} is "{string[int(symbol)]}"')
    else:
        print('Use digits only!')


print('Task 2')
# Task 2
# Вести з консолі строку зі слів за допомогою input() (або скористайтеся константою).
# Напишіть код, який визначить кількість слів, в цих даних.

string = input('enter a sentence: ')
my_list = string.split()
print(f'There is {len(my_list)} words in string "{string}" ')
print('\n')


print("Task 3")
# Task 3
# Існує ліст з різними даними, наприклад
# lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який сформує новий list (наприклад lst2), який би містив всі числові змінні (int, float), які є в lst1.
# Майте на увазі, що данні в lst1 не є статичними можуть змінюватись від запуску до запуску.

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']


