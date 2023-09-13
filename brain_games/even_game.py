import random
import prompt


def get_random_number(max_num):
    random.seed()
    result = random.randint(1, max_num)
    return result


def even_game(max_num=100):
    num = get_random_number(max_num)

    print(f'Question: {num}')
    user_answer = prompt.string('Your answer: ')
    right_answer = 'yes' if num % 2 == 0 else 'no'
    result = (user_answer == right_answer)
    if result:
        print('Correct!')
    else:
        print(f'\'{user_answer}\' is wrong answer ;(. '
              f'Correct answer was \'{right_answer}\'.')
    return result
