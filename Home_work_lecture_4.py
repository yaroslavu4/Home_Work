print('Task 1')
# Task 1
# Дана довільна строка. Напишіть код, який знайде в ній і віведе на екран кількість слів,
# які містять дві голосні літери підряд.

lst = ''
while not lst:
    lst = input('Enter a string: ').lower().split()

vowels = ['а', 'е', 'и', 'і', 'о', 'у', 'я', 'ю', 'є', 'ї']
vowels_list = []
count = 0

if not ''.join(lst).isalpha():
    print('Use letters, not digits!')
else:
    for word in lst:
        for letter in word:
            count = count + 1 if letter in vowels else 0
            if count == 2:
                vowels_list.append(word)
                break
    print(f'There are {len(vowels_list)} words with repetitive vowels')
print('\n')


print('Task 2')
# Є два довільних числа які відповідають за мінімальну і максимальну ціну. Є Dict з назвами магазинів і цінами:
# {
#   "cito": 47.999,
#   "BB_studio": 42.999,
#   "momo": 49.999,
#   "main-service": 37.245,
#   "buy.now": 38.324,
#   "x-store": 37.166,
#   "the_partner": 38.988,
#   "store": 37.720,
#   "rozetka": 38.003
# }
# Напишіть код, який знайде і виведе на екран назви
# магазинів, ціни яких попадають в діапазон між мінімальною і максимальною ціною. Наприклад:
# lower_limit = 35.9
# upper_limit = 37.339
# > match: "x-store", "main-service"

market_price = {
    "cito": 47.999,
    "BB_studio": 42.999,
    "momo": 49.999,
    "main-service": 37.245,
    "buy.now": 38.324,
    "x-store": 37.166,
    "the_partner": 38.988,
    "store": 37.720,
    "rozetka": 38.003
}

low_limit, upp_limit = map(float, input('Enter Lower and upper price limits through whitespace: ').split())
match_list = []
for name, price in market_price.items():
    if low_limit <= price <= upp_limit:
        match_list.append(name)

print(f'There are {len(match_list)} shops that meet the range between set up prices:')
# for name in match_list:
#     print(name)
for indx in range(len(match_list)):
    print(f'{indx + 1}.{match_list[indx]:_>25s}')
