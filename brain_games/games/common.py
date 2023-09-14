import random
import prompt


def get_random_number(max_num=100):
    random.seed()
    result = random.randint(1, max_num)
    return result


def play_game(game, user_name):
    max_wins = 3
    count_wins = 0
    while count_wins < max_wins:
        result_game = game()
        if result_game:
            count_wins += 1
        else:
            count_wins = 0
            print(f'Let\'s try again, {user_name}!')
    print(f'Congratulations, {user_name}!')


def get_user_answer(question):
    print(f'Question: {question}')
    user_answer = prompt.string('Your answer: ')
    return user_answer


def check_answer(user_answer, right_answer):
    result = (user_answer == right_answer)
    if result:
        print('Correct!')
    else:
        print(f'\'{user_answer}\' is wrong answer ;(. '
              f'Correct answer was \'{right_answer}\'.')
    return result
