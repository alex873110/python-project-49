from random import randint

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number <= 1:
        return False
    for divider in range(2, int(number ** (0.5)) + 1):
        if number % divider == 0:
            return False
    return True


def get_question_data():
    num = randint(0, 1000)
    result = is_prime(num) and 'yes' or 'no'
    expression = str(num)
    return (expression, result)
