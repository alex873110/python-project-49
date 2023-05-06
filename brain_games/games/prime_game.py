from random import randint


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def bg_is_prime():
    n = randint(2, 1000)
    d = 2
    expression = str(n)
    while d * d <= n:
        if n % d == 0:
            result = 'no'
            base = (expression, result, TASK)
            return base
            break
        else:
            d += 1
    result = 'yes'
    base = (expression, result, TASK)
    return (base)
