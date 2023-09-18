from brain_games.games.common import get_random_number
from brain_games.games.common import get_user_answer
from brain_games.games.common import check_answer
from math import gcd


def print_rules():
    print('Find the greatest common divisor of given numbers.')


def run_game(max_num=100):
    num1 = get_random_number(max_num)
    num2 = get_random_number(max_num)
    question = ' '.join([str(num1), str(num2)])

    right_answer = str(gcd(num1, num2))

    user_answer = get_user_answer(question)
    result = check_answer(user_answer, right_answer)
    return result
