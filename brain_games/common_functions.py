import prompt


def hello(task):
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print(task)


def congratulation():
    print('Congratulations, ' + name + '!')


def answer_questions(game):
    (expression, result, task) = game()
    hello(task)
    counter = 0
    while counter < 3:
        print('Question: ' + expression)
        ans = prompt.string('Your answer:')
        if ans == str(result):
            print('Correct!')
            counter = counter + 1
            (expression, result, task) = game()
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{result}'.")
            print("Let's try again, " + name + '!')
            break
    if counter == 3:
        congratulation()
