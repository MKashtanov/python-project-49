import random

MAX_STEP = 10
MAX_LEN_PROGRESSION = 10
MIN_LEN_PROGRESSION = 5


def get_rules():
    return 'What number is missing in the progression?'


def generate_progression(max_num):
    step = random.randint(1, MAX_STEP)
    delta_len = random.randint(0, (MAX_LEN_PROGRESSION - MIN_LEN_PROGRESSION))
    len_progression = MAX_LEN_PROGRESSION - delta_len
    first_num = random.randint(1, max_num)
    progression = []
    for current_num in range(first_num,
                             first_num + (len_progression * step), step):
        progression.append(str(current_num))
    return progression


def get_param_game(max_num=100):
    result = {}
    progression = generate_progression(max_num)
    hidden_position = random.randint(0, (len(progression) - 1))

    right_answer = str(progression[hidden_position])
    progression[hidden_position] = '..'

    result['question'] = ' '.join(progression)
    result['right_answer'] = right_answer
    return result
