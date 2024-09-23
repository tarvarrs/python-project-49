#!/usr/bin/env python3
from random import randint
import brain_games.games.logics as logics


def main():
    name = logics.greet_user()
    res = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')

    while True:
        number = randint(0, 100)
        correct_ans = 'yes' if number % 2 == 0 else 'no'
        print(f'Question: {number}')
        ans = logics.get_answer()

        if logics.is_answer_correct(ans, correct_ans):
            res += 1
            if logics.is_win(res):
                logics.win_message(name)
                break
        else:
            logics.loose_message(ans, correct_ans, name)
            break


if __name__ == '__main__':
    main()
