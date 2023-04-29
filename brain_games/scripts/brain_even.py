
import prompt
from random import randint


def is_even(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


print('Welcome to the Brain Games!')
name = prompt.string('May I have your name? ')
print('Hello, ' + name + '!')
print('Answer "yes" if the number is even, otherwise answer "no".')


def even_question():
    counter = 0
    while counter < 3:
        num = randint(1, 1000)
        str_num = str(num)
        print('Question: ' + str_num)
        answer = prompt.string('Your answer:')
        if answer == is_even(int(str_num)):
            print('Correct!')
            counter += 1
        else:
            print("'" + answer + "' is wrong answer ;(. Correct answer was '"
                  + (is_even(int(str_num))) + "'.")
            print("Let's try again, " + name + '!')
            break
    if counter == 3:
        print('Congratulations, ' + name + '!')


def main():
    even_question()


if __name__ == '__main__':
    main()
