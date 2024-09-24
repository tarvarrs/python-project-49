from random import randint
import brain_games.games.logics as logics


def start():
    name = logics.greet_user()
    res = 0
    print('Find the greatest common divisor of given numbers.')

    while True:
        a = randint(0, 50)
        b = randint(0, 50)
        print(f'Question: {a} {b}')
        correct_ans = find_answer(a, b)

        ans = int(logics.get_answer())

        if logics.is_answer_correct(ans, correct_ans):
            res += 1
            print('Correct!')
            if logics.is_win(res):
                logics.win_message(name)
                break
        else:
            logics.loose_message(ans, correct_ans, name)
            break


def find_answer(a, b):
    res = min(a, b)
    while res:
        if a % res == 0 and b % res == 0:
            return res
        else:
            res -= 1
