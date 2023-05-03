from random import randint
from brain_games.games.common_functions import hello, question, congratulation


def gcd(a, b):
    greater = max(a, b)
    smaller = min(a, b)
    while greater % smaller != 0:
        remain = greater % smaller
        greater = smaller
        smaller = remain
    gcd = smaller
    return (gcd)


def bg_gcd():
    task = 'Find the greatest common divisor of given numbers.'
    hello(task)
    counter = 0
    while counter < 3:
        num1 = randint(1, 100)
        num2 = randint(1, 100)
        expression = str(num1) + ' ' + str(num2)
        result = gcd(num1, num2)
        count = question(expression, result, counter)
        counter = count
    if counter == 3:
        congratulation()


def main():
    bg_gcd()


if __name__ == '__main__':
    main()
