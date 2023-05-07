#!/usr/bin/env python3
from brain_games.games.calc_game import get_question_data
from brain_games.common_functions import answer_questions


def main():
    answer_questions(get_question_data)


if __name__ == '__main__':
    main()
