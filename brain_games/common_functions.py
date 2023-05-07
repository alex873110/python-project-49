import prompt


def answer_questions(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    (expression, result, task) = game()
    print(task)
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
        print('Congratulations, ' + name + '!')
