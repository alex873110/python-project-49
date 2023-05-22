from random import randint


def gcd(a, b):
    greater = max(a, b)
    smaller = min(a, b)
    while greater % smaller != 0:
        remain = greater % smaller
        greater = smaller
        smaller = remain
    gcd = smaller
    return (gcd)


TASK = 'Find the greatest common divisor of given numbers.'


def get_question_data():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    expression = f'{num1} {num2}'
    result = gcd(num1, num2)
    base = (expression, result, TASK)
    return base
