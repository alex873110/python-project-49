#!/usr/bin/env python3
from brain_games.games import calc_game
from brain_games.common_functions import answer_questions


def main():
    answer_questions(calc_game.get_question_data)


if __name__ == '__main__':
    main()
