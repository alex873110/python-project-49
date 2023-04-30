
import prompt
from random import randint
from brain_games.games.common_functions import hello, question, congratulation

def is_even(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


hello()
print('Answer "yes" if the number is even, otherwise answer "no".')


def even_question():
    counter = 0
    while counter < 3:
        num = randint(1, 1000)
        expression = str(num)
        result = is_even(num)
        count = question(expression, result, counter)
        counter = count

    if counter == 3:
        congratulation()


def main():
    even_question()


if __name__ == '__main__':
    main()
