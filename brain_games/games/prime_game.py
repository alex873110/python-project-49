from random import randint


def bg_is_prime():
    task = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    n = randint(2, 1000)
    d = 2
    expression = str(n)
    while d * d <= n:
        if n % d == 0:
            result = 'no'
            base = (expression, result, task)
            return base
            break
        else:
            d += 1
    result = 'yes'
    base = (expression, result, task)
    return (base)
