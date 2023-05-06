from random import randint


def is_even(number):
    return number % 2 == 0


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def even_question():
    num = randint(1, 1000)
    expression = str(num)
    if is_even(num):
        result = 'yes'
    else:
        result = 'no'
    base = (expression, result, TASK)
    return base
