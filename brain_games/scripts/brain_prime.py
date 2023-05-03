from random import randint
from brain_games.games.common_functions import hello, question, congratulation


def is_prime():
    n = randint(2, 1000)
    d = 2
    global expression
    expression = str(n)
    while d * d <= n:
        if n % d == 0:
            return ('no')
            break
        else:
            d += 1
    return ('yes')


def bg_is_prime():
    task = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    hello(task)
    counter = 0
    while counter < 3:
        result = is_prime()
        count = question(expression, result, counter)
        counter = count
    if counter == 3:
        congratulation()


def main():
    bg_is_prime()


if __name__ == '__main__':
    main()
