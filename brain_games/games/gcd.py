import random
from math import gcd

MAX_NUM = 100


def get_rules_game():
    return 'Find the greatest common divisor of given numbers.'


def get_params_round():
    result = {}
    num1 = random.randint(1, MAX_NUM)
    num2 = random.randint(1, MAX_NUM)

    result['question'] = ' '.join([str(num1), str(num2)])
    result['right_answer'] = str(gcd(num1, num2))
    return result
