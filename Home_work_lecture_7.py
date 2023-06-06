from random import choice
                                        # Побудова функцій

def my_choice():
    if user_choice == comp_choice:
        return 'Draw'
    elif user_choice == 'scissors':
        if comp_choice == 'paper':
            return 'Win'
        else:
            return 'Lose'
    elif user_choice == 'paper':
        if comp_choice == 'scissors':
            return 'Lose'
        else:
            return 'Win'
    elif user_choice == 'rock':
        if comp_choice == 'paper':
            return 'Lose'
        else:
            return 'Win'


def my_score():
    if my_choice() == 'Draw':
        score['user'] += 1
        score['computer'] += 1
    elif my_choice() == 'Win':
        score['user'] += 1
    else:
        score['computer'] += 1
    return score


def final_message():
    if my_choice() == 'Draw':
        print(f'Your choice "{user_choice}" == computer choice "{comp_choice}", it`s a draw!')
    elif my_choice() == 'Win':
        print(f'Your choice is "{user_choice}", computer choice is "{comp_choice}", you win!')
    else:
        print(f'Your choice is "{user_choice}", computer choice is "{comp_choice}", you lose!')

                                        # Основний код

score = {
        'user': 0,
        'computer': 0
    }

VALUES = ('rock', 'paper', 'scissors')

while True:
    comp_choice = choice(VALUES)
    user_choice = ''
    while not user_choice:
        user_choice = input('Enter one of three items rock, paper or scissors: ').lower()

    if user_choice not in ('rock', 'paper', 'scissors'):
        print(f'Unexpected data "{user_choice}", check the rules and try again!')
        continue

    final_message()
    score = (my_score())

    print('''\nScore Table:''')
    for name, res in score.items():
        print(f'{name:.<11s}{res}')

    end = input('\nWanna play again? Say "y" or "n": '.lower())
    if end == 'y':
        continue
    else:
        print('Thank you for playing, hope to see you again later!')
        break
