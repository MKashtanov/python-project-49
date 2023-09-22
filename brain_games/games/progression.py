import random

MAX_STEP = 10
MAX_NUM = 100
MAX_LEN_PROGRESSION = 10
MIN_LEN_PROGRESSION = 5


def get_rules_game():
    return 'What number is missing in the progression?'


def generate_progression():
    step = random.randint(1, MAX_STEP)
    len_progression = random.randint(MIN_LEN_PROGRESSION, MAX_LEN_PROGRESSION)
    first_num = random.randint(1, MAX_NUM)
    progression = []
    for current_num in range(first_num,
                             first_num + (len_progression * step), step):
        progression.append(str(current_num))
    return progression


def get_params_round():
    result = {}
    progression = generate_progression()
    hidden_position = random.randint(0, (len(progression) - 1))

    right_answer = str(progression[hidden_position])
    progression[hidden_position] = '..'

    result['question'] = ' '.join(progression)
    result['right_answer'] = right_answer
    return result
