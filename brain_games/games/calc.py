import random
import operator

MAX_NUM = 100


def get_rules_game():
    return 'What is the result of the expression?'


def get_operator(str_operator):
    result = ''
    if str_operator == '+':
        result = operator.add
    elif str_operator == '-':
        result = operator.sub
    elif str_operator == '*':
        result = operator.mul
    return result


def get_params_round():
    result = {}
    list_operator = ['+', '-', '*']
    str_operator = list_operator[random.randint(0, len(list_operator) - 1)]
    func_operator = get_operator(str_operator)
    num1 = random.randint(1, MAX_NUM)
    num2 = random.randint(1, MAX_NUM)

    result['question'] = ' '.join([str(num1), str_operator, str(num2)])
    result['right_answer'] = str(func_operator(num1, num2))
    return result
