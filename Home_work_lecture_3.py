print('Task 1')
# Task 1
# Напишіть код, який зформує строку, яка містить певну інформацію про символ за його номером у слові.
# Наприклад "The [номер символу] symbol in '[тут слово]' is '[символ з відповідним порядковим номером в слові]'".
# Слово та номер символу отримайте за допомогою input() або скористайтеся константою. Наприклад (слово - "Python" а
# номер символу 3) - "The 3 symbol in 'Python' is 't' ".

# мучался над этой задачей,ибо метод isdigit() не распознает знак минус, пришлось делить цикл на две части
# мне не нравится как сильно похожи обе части цикла, но по-другому я сделать не смог(
string = input('Please enter text here: ')
symbol = input('Enter symbol number: ')
if symbol[0] == '-':
    if symbol[1:].isdigit():
        int_symbol = int(symbol)
        if int(symbol) < -len(string):
            print('Symbol number is out of string, try again!')
        else:
            print(f'The symbol {int_symbol} in {string} is "{string[int_symbol]}"')
    else:
        print('Use digits only!')
else:
    if symbol.isdigit():
        int_symbol = int(symbol)
        if int(symbol) >= len(string):
            print('Symbol number is out of string, try again!')
        else:
            print(f'The symbol {int_symbol} in {string} is "{string[int_symbol]}"')
    else:
        print('Use digits only!')


print('Task 2')
# Task 2
# Вести з консолі строку зі слів за допомогою input() (або скористайтеся константою).
# Напишіть код, який визначить кількість слів, в цих даних.

string = input('Enter a sentence: ')
my_list = string.split()
print(f'There is {len(my_list)} words in string "{string}" ')
print('\n')


print("Task 3")
# Task 3
# Існує ліст з різними даними, наприклад
# lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який сформує новий list (наприклад lst2), який би містив всі числові змінні (int, float), які є в lst1.
# Майте на увазі, що данні в lst1 не є статичними можуть змінюватись від запуску до запуску.

lst = ['1', '2', 3, 4.0, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
new_lst = [value for value in lst if type(value) == int or type(value) == float]
print(new_lst)


