import prompt

'''
def start_game(name, correct_ans, res):
    ans = get_answer()
    if is_answer_correct(ans, correct_ans):
        res += 1
        if is_win(res):
            win_message(name)
            return True
    else:
        loose_message(ans, correct_ans)
        return True
'''


def greet_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def get_answer():
    ans = prompt.string('Your answer: ')
    return ans


def is_answer_correct(user_answer, correct_answer):
    return user_answer == correct_answer


def is_win(correct_count):
    RES_TO_WIN = 3
    return correct_count == RES_TO_WIN


def win_message(user_name):
    print(f'Congratulations, {user_name}!')


def loose_message(user_answer, correct_answer, name):
    print(f'\'{user_answer}\' is wrong answer ;(. ',
          f'Correct answer was \'{correct_answer}\'.')
    print(f'Let\'s try again, {name}!')
