import prompt

MAX_WINS = 3


def play_game(get_rules_game, get_params_round):
    user_name = get_user_name()
    print(get_rules_game())

    count_wins = 0
    while count_wins < MAX_WINS:
        params_round = get_params_round()
        user_answer = get_user_answer(params_round['question'])
        result_round = check_answer(user_answer, params_round['right_answer'])
        if result_round:
            count_wins += 1
        else:
            print(f'Let\'s try again, {user_name}!')
            return
    print(f'Congratulations, {user_name}!')


def get_user_name():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


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
