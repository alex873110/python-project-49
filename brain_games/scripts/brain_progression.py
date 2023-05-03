from random import randint
from brain_games.games.common_functions import hello, question, congratulation


def progression():
    num1 = randint(1, 100)
    num2 = randint(1, 50)
    num3 = randint(0, 9)
    string = ''
    i = 0
    while i < 10:
        if i != num3:
            string += str(num1) + ' '
            num1 += num2
            i += 1
        else:
            string += '.. '
            global result
            result = num1
            num1 += num2
            i += 1
    string = string[:-1]
    return (string)


def bg_progression():
    exercize = 'What number is missing in the progression?'
    hello(exercize)
    count = 0
    while count < 3:
        expression = progression()
        counter = question(expression, result, count)
        count = counter
    if count == 3:
        congratulation()


def main():
    bg_progression()


if __name__ == '__main__':
    main()
