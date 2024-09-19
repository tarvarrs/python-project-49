import prompt

def start_game(name, correct_ans, res):
    ans = prompt.string('Your answer: ')
    if is_answer_correct(ans, correct_ans):
        res += 1
        if is_win(res):
            win_message(name)
            return True
    else:
        loose_message(ans, correct_ans)
        return True


def greet_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    return name


def get_answer():
    ans = prompt.string('Answer: ')
    return ans


def is_answer_correct(user_answer, correct_answer):
    return user_answer == correct_answer


def is_win(correct_count):
    return correct_count == 3


def win_message(user_name):
    print(f'Congratulations, {user_name}!')


def loose_message(user_answer, correct_answer):
    print(f'\'{user_answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'.')
