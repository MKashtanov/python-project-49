#!/usr/bin/env python3
from brain_games.game_engine import play_game
from brain_games.games.progression import get_rules_game, get_params_round


def main():
    play_game(get_rules_game, get_params_round)


if __name__ == '__main__':
    main()
