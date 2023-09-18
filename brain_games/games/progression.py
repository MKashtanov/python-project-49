from brain_games.games.common import get_random_number
from brain_games.games.common import get_user_answer
from brain_games.games.common import check_answer

MAX_STEP = 10
MAX_LEN_PROGRESSION = 10
MIN_LEN_PROGRESSION = 5


def print_rules():
    print('What number is missing in the progression?')


def generate_progression(max_num):
    step = get_random_number(MAX_STEP)
    len_progression = (MIN_LEN_PROGRESSION - 1
                       + get_random_number(MAX_LEN_PROGRESSION
                                           - MIN_LEN_PROGRESSION + 1))
    first_num = get_random_number(max_num)
    progression = []
    for current_num in range(first_num,
                             first_num + (len_progression * step), step):
        progression.append(str(current_num))
    return progression


def run_game(max_num=100):
    progression = generate_progression(max_num)
    hidden_position = get_random_number(len(progression)) - 1

    right_answer = str(progression[hidden_position])
    progression[hidden_position] = '..'

    question = ' '.join(progression)
    user_answer = get_user_answer(question)
    result = check_answer(user_answer, right_answer)
    return result
