from random import randint

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def get_question_data():
    num = randint(1, 1000)
    expression = str(num)
    if is_even(num):
        result = 'yes'
    else:
        result = 'no'
    base = (expression, result)
    return base
