from random import randint


TASK = 'What number is missing in the progression?'


def bg_progression():
    num1 = randint(1, 100)
    num2 = randint(1, 50)
    num3 = randint(0, 9)
    progression = ''
    i = 0
    while i < 10:
        if i != num3:
            progression += str(num1) + ' '
            num1 += num2
            i += 1
        else:
            progression += '.. '
            result = num1
            num1 += num2
            i += 1
    progression = progression[:-1]
    base = (progression, result, TASK)
    return (base)
