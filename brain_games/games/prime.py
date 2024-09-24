from random import randint
import brain_games.games.logics as logics


def start():
    name = logics.greet_user()
    res = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    while True:
        number = randint(1, 100)
        correct_ans = 'yes' if is_number_prime(number) else 'no'
        print(f'Question: {number}')
        ans = logics.get_answer()

        if logics.is_answer_correct(ans, correct_ans):
            res += 1
            print('Correct!')
            if logics.is_win(res):
                logics.win_message(name)
                break
        else:
            logics.loose_message(ans, correct_ans, name)
            break
    pass


def is_number_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False

    return True
