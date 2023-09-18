from brain_games.games.common import get_random_number
from brain_games.games.common import get_user_answer
from brain_games.games.common import check_answer


def print_rules():
    print('What is the result of the expression?')


def run_game(max_num=100):
    list_action = ['+', '-', '*']
    num_action = get_random_number(3)
    current_action = list_action[num_action - 1]
    num1 = get_random_number(max_num)
    num2 = get_random_number(max_num)
    question = ' '.join([str(num1), current_action, str(num2)])

    right_answer = ''
    if current_action == '+':
        right_answer = str(num1 + num2)
    elif current_action == '-':
        right_answer = str(num1 - num2)
    elif current_action == '*':
        right_answer = str(num1 * num2)

    user_answer = get_user_answer(question)
    result = check_answer(user_answer, right_answer)
    return result
