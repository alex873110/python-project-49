from random import randint, choice

TASK = 'What is the result of the expression?'


def get_question_data():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    char = choice('+-*')
    expression = f'{num1} {char} {str(num2)}'
    if char == '+':
        result = num1 + num2
    if char == '-':
        result = num1 - num2
    if char == '*':
        result = num1 * num2
    return (expression, str(result))
