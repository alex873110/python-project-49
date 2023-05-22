from random import randint

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    d = 2
    while d * d <= number:
        if number % d == 0:
            return False
        else:
            d += 1
    return True


def get_question_data():
    n = randint(2, 1000)
    if is_prime(n):
        result = 'yes'
    if not is_prime(n):
        result = 'no'
    expression = str(n)
    base = (expression, result)
    return (base)
