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
    hello()
    global counter
    counter = 0
    print('What number is missing in the progression?')
    while counter < 3:
        expression = progression()
        count = question(expression, result, counter)
        counter = count
    if counter == 3:
        congratulation()


def main():
    bg_progression()


if __name__ == '__main__':
    main()
