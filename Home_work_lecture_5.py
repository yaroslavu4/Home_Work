from random import choice
from string import ascii_lowercase as available

print('Task 1')
# Task 1: guess the word

WORDS = ('javascript', 'python', 'java', 'kotlin', 'swift', 'pascal', 'limbo')
word = choice(WORDS)
so_far = '?' * len(word)    # guessed string with letters so far
wrong = 0   # mistakes counter
used = []   # already used letters
MAX_WRONG = len(word)   # quantity of mistakes can be made

print('Welcome to the game "Guess the Word". Good luck !\n')

while wrong < MAX_WRONG and so_far != word:
    print(f'Guess the word "{so_far}"')
    guess = input('Enter a letter: ').lower()

    if len(guess) != 1:
        print('\nPlease, enter exactly 1 letter!')
        continue
    elif guess not in available:
        print('\nUse only English letters!')
        continue
    elif guess in used:
        print('\nYou`ve suggested this letter yet')
        continue

    if guess in word:
        print(f'\nBingo, letter "{guess}" is in guessed word!')
        new = ''    # new string so_far with guessed put in letters
        for indx in range(len(word)):
            if guess == word[indx]:
                new += word[indx]
            else:
                new += so_far[indx]
        so_far = new
    else:
        print(f'\nUnfortunately letter "{guess}" isn`t in guessed word')
        wrong += 1
        print(f'You`ve got {MAX_WRONG - wrong} tries left')
    used.append(guess)

if wrong == MAX_WRONG:
    print(f'\nYou`ve spent all {MAX_WRONG} tries, word "{word}" was never guessed \nYou lose')
else:
    print(f'You won, word "{word}" was guessed')


