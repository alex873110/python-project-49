from random import randint


def is_even(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def even_question():
    num = randint(1, 1000)
    expression = str(num)
    result = is_even(num)
    base = (expression, result, TASK)
    return base
