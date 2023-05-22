from random import randint


TASK = 'What number is missing in the progression?'


def get_question_data():
    random_index = randint(0, 9)
    step = randint(1, 50)
    start = randint(0, 50)
    stop = start + 10 * step
    progression = list(range(start, stop, step))
    result = progression[random_index]
    progression[random_index] = '..'
    expression = ' '.join(map(str,progression))
    base = (expression , result, TASK)
    return (base)
