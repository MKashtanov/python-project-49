from brain_games.games.common import get_random_number
from brain_games.games.common import get_user_answer
from brain_games.games.common import check_answer


def print_rules():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def is_prime(num):
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            return False
    return True


def run_game(max_num=100):
    num = get_random_number(max_num)
    question = str(num)

    user_answer = get_user_answer(question)
    right_answer = 'yes' if is_prime(num) else 'no'
    result = check_answer(user_answer, right_answer)
    return result
