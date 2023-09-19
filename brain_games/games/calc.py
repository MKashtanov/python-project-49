import random
import operator


def get_rules():
    return 'What is the result of the expression?'


def get_right_answer(num1, num2, action):
    result = ''
    if action == '+':
        result = operator.add(num1, num2)
    elif action == '-':
        result = operator.sub(num1, num2)
    elif action == '*':
        result = operator.mul(num1, num2)
    return str(result)


def get_action(str_action):
    result = ''
    if str_action == '+':
        result = operator.add
    elif str_action == '-':
        result = operator.sub
    elif str_action == '*':
        result = operator.mul
    return result


def get_param_game(max_num=100):
    result = {}
    list_action = ['+', '-', '*']
    num_action = random.randint(0, 2)
    str_action = list_action[num_action]
    action = get_action(str_action)
    num1 = random.randint(1, max_num)
    num2 = random.randint(1, max_num)

    result['question'] = ' '.join([str(num1), str_action, str(num2)])
    result['right_answer'] = str(action(num1, num2))
    return result
