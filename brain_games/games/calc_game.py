from random import randint, choice


def calculation():
    task = 'What is the result of the expression?'
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    char = choice('+-*')
    expression = str(num1) + ' ' + char + ' ' + str(num2)
    global result
    if char == '+':
        result = num1 + num2
    elif char == '-':
        result = num1 - num2
    else:
        result = num1 * num2
    base = (expression, result, task)
    return base
