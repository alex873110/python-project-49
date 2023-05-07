#!/usr/bin/env python3
from brain_games.common_functions import answer_questions
from brain_games.games import progression_game


def main():
    answer_questions(progression_game.get_question_data)


if __name__ == '__main__':
    main()
