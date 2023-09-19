import random


def get_rules():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            return False
    return True


def get_param_game(max_num=100):
    result = {}
    num = random.randint(1, max_num)
    result['question'] = str(num)
    result['right_answer'] = 'yes' if is_prime(num) else 'no'
    return result
