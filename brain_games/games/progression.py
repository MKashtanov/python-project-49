from brain_games.games.common import get_random_number
from brain_games.games.common import get_user_answer
from brain_games.games.common import check_answer


def print_rules():
    print('What number is missing in the progression?')


def run_game(max_num=100):
    max_step = 10
    step = get_random_number(max_step)
    len_progression = 4 + get_random_number(6)  # длина 5-10 чисел
    hidden_position = get_random_number(len_progression)
    first_num = get_random_number(max_num)
    progression = []
    current_num = first_num

    while len(progression) < len_progression:
        progression.append(str(current_num))
        current_num += step
    right_answer = str(progression[hidden_position - 1])
    progression[hidden_position - 1] = '..'

    question = ' '.join(progression)
    user_answer = get_user_answer(question)
    result = check_answer(user_answer, right_answer)
    return result
