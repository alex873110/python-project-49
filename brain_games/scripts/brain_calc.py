#!/usr/bin/env python3
from random import randint, choice
from brain_games.games.common_functions import hello, question, congratulation


def calculation():
    hello()
    global counter
    counter = 0
    print('What is the result of the expression?')
    while counter < 3:
        num1 = randint(1, 100)
        num2 = randint(1, 100)
        char = choice('+-*')
        expression = str(num1) + char + str(num2)
        if char == '+':
            result = num1 + num2
        elif char == '-':
            result = num1 - num2
        else:
            result = num1 * num2
        count = question(expression, result, counter)
        counter = count
    if counter == 3:
        congratulation()


def main():
    calculation()


if __name__ == '__main__':
    main()
