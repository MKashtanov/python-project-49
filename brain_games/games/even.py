import random


def get_rules():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def get_param_game(max_num=100):
    result = {}
    num = random.randint(1, max_num)

    result['question'] = str(num)
    result['right_answer'] = 'yes' if num % 2 == 0 else 'no'
    return result
