from random import randint
import brain_games.games.logics as logics


def main():
    name = logics.greet_user()
    res = 0
    print('Find the greatest common divisor of given numbers.')

    while True:
        a = randint(0, 50)
        b = randint(0, 50)
        print(f'Question: {a} {b}')
        correct_ans = find_answer(a, b)

        ans = logics.make_decimal(logics.get_answer())

        if isinstance(ans, int) and logics.is_answer_correct(ans, correct_ans):
            res += 1

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


if __name__ == '__main__':
    main()
