#!/usr/bin/env python3
from brain_games.common_functions import answer_questions
from brain_games.games.progression_game import get_question_data


def main():
    answer_questions(get_question_data)


if __name__ == '__main__':
    main()
