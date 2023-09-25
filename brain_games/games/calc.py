import random
import operator

MAX_NUM = 100
MAPPING_OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul
}


def get_rules_game():
    return 'What is the result of the expression?'


def get_params_round():
    result = {}
    str_operator = random.choice(list(MAPPING_OPERATORS.keys()))
    func_operator = MAPPING_OPERATORS.get(str_operator)
    num1 = random.randint(1, MAX_NUM)
    num2 = random.randint(1, MAX_NUM)

    result['question'] = ' '.join([str(num1), str_operator, str(num2)])
    result['right_answer'] = str(func_operator(num1, num2))
    return result
