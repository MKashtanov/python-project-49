#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.games.calc import print_rules
from brain_games.games.calc import calc_game
from brain_games.games.common import play_game


def main():
    user_name = welcome_user()
    print_rules()
    play_game(calc_game, user_name)


if __name__ == '__main__':
    main()
