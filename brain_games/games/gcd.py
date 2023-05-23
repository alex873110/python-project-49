from random import randint

TASK = 'Find the greatest common divisor of given numbers.'


def gcd(a, b):
    greater = max(a, b)
    smaller = min(a, b)
    while greater % smaller != 0:
        remain = greater % smaller
        greater = smaller
        smaller = remain
    return (smaller)


def get_question_data():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    expression = f'{num1} {num2}'
    result = gcd(num1, num2)
    return (expression, result)
