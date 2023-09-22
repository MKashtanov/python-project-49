import random

MAX_NUM = 100


def get_rules_game():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def get_params_round():
    result = {}
    num = random.randint(1, MAX_NUM)

    result['question'] = str(num)
    result['right_answer'] = 'yes' if num % 2 == 0 else 'no'
    return result
