from random import randint

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    for d in range(2, int(number ** (0.5)) + 1):
        if number % d == 0:
            return False
    else:
        return number >= 2


def get_question_data():
    n = randint(0, 1000)
    result = is_prime(n) and 'yes' or 'no'
    expression = str(n)
    return (expression, result)
