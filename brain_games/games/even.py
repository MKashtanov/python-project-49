from brain_games.games.common import get_random_number
from brain_games.games.common import get_user_answer
from brain_games.games.common import check_answer


def print_rules():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def run_game(max_num=100):
    num = get_random_number(max_num)
    question = str(num)

    user_answer = get_user_answer(question)
    right_answer = 'yes' if num % 2 == 0 else 'no'
    result = check_answer(user_answer, right_answer)
    return result
