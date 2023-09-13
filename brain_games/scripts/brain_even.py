#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.even_game import even_game


def print_rules():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def main():
    max_wins = 3
    count_wins = 0

    print('Welcome to the Brain Games!')
    user_name = welcome_user()
    print_rules()
    while count_wins < max_wins:
        result_game = even_game()
        if result_game:
            count_wins += 1
        else:
            count_wins = 0
            print(f'Let\'s try again, {user_name}!')
    print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    main()
