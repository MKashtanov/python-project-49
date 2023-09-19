import random
from math import gcd


def get_rules():
    return 'Find the greatest common divisor of given numbers.'


def get_param_game(max_num=100):
    result = {}
    num1 = random.randint(1, max_num)
    num2 = random.randint(1, max_num)

    result['question'] = ' '.join([str(num1), str(num2)])
    result['right_answer'] = str(gcd(num1, num2))
    return result
