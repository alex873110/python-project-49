#!/usr/bin/env python3
from brain_games.games.prime_game import bg_is_prime
from brain_games.common_functions import answer_questions


def main():
    answer_questions(bg_is_prime)


if __name__ == '__main__':
    main()
