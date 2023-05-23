import prompt


def answer_questions(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    (expression, result) = game.get_question_data()
    print(game.TASK)
    for i in range(3):
        print(f'Question: {expression}')
        ans = prompt.string('Your answer:')
        if ans != str(result):
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{result}'.")
            print(f"Let's try again, {name}!")
            break
        print('Correct!')
        (expression, result) = game.get_question_data()
    else:
        print(f'Congratulations, {name}!')
