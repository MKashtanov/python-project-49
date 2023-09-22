import random

MAX_NUM = 100


def get_rules_game():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            return False
    return True


def get_params_round():
    result = {}
    num = random.randint(1, MAX_NUM)
    result['question'] = str(num)
    result['right_answer'] = 'yes' if is_prime(num) else 'no'
    return result
