import prompt
ROUNDS_QUANTITY = 3


def play_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.TASK)
    for _ in range(ROUNDS_QUANTITY):
        expression, result = game.get_question_data()
        print(f'Question: {expression}')
        ans = prompt.string('Your answer:')
        if ans != result:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{result}'.")
            print(f"Let's try again, {name}!")
            break
        print('Correct!')
    else:
        print(f'Congratulations, {name}!')
