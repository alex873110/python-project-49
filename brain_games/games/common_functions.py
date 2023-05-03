#!/usr/bin/env python3
import prompt


def hello(task):
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print(task)


def question(expression, result, counter):
    print('Question: ' + expression)
    answer = prompt.string('Your answer:')
    if answer == str(result):
        print('Correct!')
        return (counter + 1)
    else:
        print("'" + answer + "' is wrong answer ;(. Correct answer was '"
              + str(result) + "'.")
        print("Let's try again, " + name + '!')
        return (4)


def congratulation():
    print('Congratulations, ' + name + '!')


def main():
    hello()
    question()
    congratulation()


if __name__ == '__main__':
    main()
