from brain_games.scripts.brain_games import main as welcome
import prompt
import importlib
import importlib.util

MAX_WINS = 3


def play_game(game_name):
    path_module = 'brain_games.games.' + game_name
    if importlib.util.find_spec(path_module):
        game = importlib.import_module(path_module)
    else:
        print(f'Unknown game "{game_name}"')
        return

    user_name = welcome()
    print(game.get_rules())

    count_wins = 0
    while count_wins < MAX_WINS:
        params = game.get_param_game()
        result_game = run_game(params)
        if result_game:
            count_wins += 1
        else:
            print(f'Let\'s try again, {user_name}!')
            return
    print(f'Congratulations, {user_name}!')


def run_game(params):
    user_answer = get_user_answer(params['question'])
    return check_answer(user_answer, params['right_answer'])


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
